import discord
from discord.ext import commands
from discord import Option
from discord.ui import View, Button
import os
import zipfile
import sqlite3
import uuid
import time
from io import BytesIO
from wand.image import Image as WandImage
import shutil  

BASE_DIR = "storage/users"
DB_PATH = "data.db"
SIZES = [440, 260, 128, 64]

os.makedirs(BASE_DIR, exist_ok=True)

def db_connection():
    return sqlite3.connect(DB_PATH)

with db_connection() as conn:
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS jobs ( 
            id TEXT PRIMARY KEY, 
            user_id INTEGER, 
            activated INTEGER, 
            created_at REAL 
        ) 
    """)

def user_job_dir(user_id: int, job_id: str):
    path = os.path.join(BASE_DIR, str(user_id), job_id)
    os.makedirs(path, exist_ok=True)
    return path

def zip_folder(folder_path: str) -> bytes:
    buf = BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in os.listdir(folder_path):
            z.write(os.path.join(folder_path, f), f)
    buf.seek(0)
    return buf.read()

def process_image(image_bytes: bytes, out_dir: str, activated: bool):
    unique_id = str(uuid.uuid4())  
    with WandImage(blob=image_bytes) as img:
        img.format = "png"
        img.resize(440, 440)
        img.save(filename=f"{out_dir}/picture_{unique_id}.png")  
        img.compression = "dxt5"
        for s in SIZES:
            img.resize(s, s)
            img.save(filename=f"{out_dir}/picture{unique_id}_{s}.dds")  
    with open(f"{out_dir}/online_{unique_id}.json", "w") as f:
        f.write(f'{{"avatarUrl":"...","isOfficiallyVerified":{str(activated).lower()}}}')

def save_job(user_id: int, activated: bool) -> str:
    job_id = str(uuid.uuid4())
    with db_connection() as conn:
        conn.execute("""
            INSERT INTO jobs (id, user_id, activated, created_at) 
            VALUES (?, ?, ?, ?)
        """, (job_id, user_id, int(activated), time.time()))
    return job_id

intents = discord.Intents.default()
bot = commands.Bot(intents=intents)

class ActivateView(View):
    def __init__(self, user_id: int, image_bytes: bytes):
        super().__init__(timeout=180)
        self.user_id = user_id
        self.image_bytes = image_bytes

    async def handle(self, interaction: discord.Interaction, activated: bool):
        await interaction.response.edit_message(content="⏳ Processing...", embed=None, view=None)
        job_id = save_job(self.user_id, activated)
        job_dir = user_job_dir(self.user_id, job_id)
        process_image(self.image_bytes, job_dir, activated)
        archive = zip_folder(job_dir)
        await interaction.followup.send(
            content="✅ XAvatar has been created",
            file=discord.File(BytesIO(archive), filename="avatar.xavatar")
        )
        
        shutil.rmtree(job_dir)

    @discord.ui.button(label="Activated", style=discord.ButtonStyle.green)
    async def yes(self, button: Button, interaction: discord.Interaction):
        await self.handle(interaction, True)

    @discord.ui.button(label="Not Activated", style=discord.ButtonStyle.red)
    async def no(self, button: Button, interaction: discord.Interaction):
        await self.handle(interaction, False)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(name="avatar", description="Convert an image to XAvatar")
async def avatar(ctx: discord.ApplicationContext, file: Option(discord.Attachment, "Choose an image")):
    if not file.content_type or not file.content_type.startswith("image"):
        return await ctx.respond("❌ The file is not an image", ephemeral=True)
    
    image_bytes = await file.read()
    embed = discord.Embed(title="Convert Image", description="Is the account activated?")
    embed.set_image(url=file.url)
    await ctx.respond(embed=embed, view=ActivateView(ctx.author.id, image_bytes))

bot.run("PUT YOUR TOKEN")
