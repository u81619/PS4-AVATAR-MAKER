# ✨ **XAvatar Converter Discord Bot** 🚀

## 🌟 **Overview**
This is a powerful **Discord bot** written in Python using the `discord.py` library. It allows users to upload an image and automatically convert it into a high-quality custom **.xavatar** file!

The resulting `.xavatar` file is a **ZIP archive** containing:
- A main PNG image resized to 440x440 (`picture.png` / `avatar.png`) 📸
- Compressed DDS textures using DXT5 compression in multiple sizes (440, 260, 128, 64) for optimal performance (`picture{size}.dds`) ⚡
- An `online.json` file with an official verification badge flag (activated or not) ✅

This format is specifically designed for platforms that support avatars with mipmaps and verification badges (similar to VRChat and others).

⚠️ **Important Warning**: The bot token in the code is exposed! Never share it with anyone. If it's a real token, regenerate it immediately from the Discord Developer Portal.

## 👨‍💻 **Developer**
- **Name**: Haider Ahmed
- **Contact the Developer**: Telegram [@C2_9H](https://t.me/C2_9H) ✈️

## 🔥 **Awesome Features**
- Slash command: `/avatar` ⚔️
- Easy image upload as an attachment
- Beautiful embed with image preview 🖼️
- Interactive buttons: **Activated (Yes)** or **Not Activated (No)** to set verification status
- Professional image processing using Wand (ImageMagick bindings):
  - High-quality resize to 440x440
  - Super-fast generation of compressed DDS files
- Packs everything into a ZIP archive named `avatar.xavatar` and sends it directly 📦

## 🛠️ **Requirements**
- Python 3.8 or higher
- ImageMagick installed and configured (the code sets the path automatically)
- Libraries:
  - `pip install Wand`
  - `pip install discord.py`

## 🚀 **How to Run**
1. Install the required libraries:
   ```bash
   pip install discord.py Wand

Make sure ImageMagick is properly installed.
Replace the token in the code with your own bot token (from Discord Developer Portal).
Invite the bot to your server with application.commands scope.
Run the script:Bashpython bot.py

⚙️ How It Works (Technical Breakdown)

Image Processing:
Loads the image from bytes using wand.image.Image
Saves a 440x440 PNG version
Sets DXT5 compression and generates DDS files for each size

File Copying:
Duplicates files as picture.png and picture{size}.dds
Creates online.json with the isOfficiallyVerified value

Packaging:
Creates a temporary folder → processes files → zips in memory → cleans up

Interaction:
Interactive buttons with a 5-minute timeout ⏱️


🔒 Security Notes

Never share your bot token!
Ensure your environment is secure when running ImageMagick.
Consider adding rate limiting for public use.

⚠️ Current Limitations

Only supports formats readable by ImageMagick/Wand
Fixed sizes and compression (tailored for a specific system)
No comprehensive error handling yet

If you're planning to improve it, add logging, queuing, and rate limiting! 💪
📬 Contact the Developer
For questions, suggestions, or improvements:
Telegram → [@C2_9H](https://t.me/C2_9H) 🌟
Enjoy the bot and make your avatar shine! ✨🔥
