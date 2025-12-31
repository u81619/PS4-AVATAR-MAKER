# XAvatar Discord Bot

**Developer:** Haidar Ahmed
**Telegram:** [t.me/C2_9h](https://t.me/C2_9h )

---

## 📜 Project Overview

The XAvatar Bot is a specialized Discord bot developed in Python to automate the creation of "XAvatars." The bot processes images uploaded by users and converts them into a compatible file package. This package includes multiple resized versions of the image in both `PNG` and `DDS` formats, along with a `JSON` metadata file.

The bot features a simple, interactive interface using Slash Commands and Buttons, making the user experience fast and straightforward.

---

## ✨ Key Features

- **🤖 Easy Interaction:** Uses a clear and direct slash command (`/avatar`) to initiate the conversion process.
- **🖼️ Advanced Image Processing:** Automatically resizes the source image into multiple dimensions (`440x440`, `260x260`, `128x128`, `64x64`) and saves them in different formats.
- **⚙️ DDS Format Support:** Utilizes `DXT5` compression to generate `.dds` files, a common format in gaming and graphics applications.
- **👆 Interactive Button UI:** Asks the user whether the account is "activated" or not via simple buttons, making it easy to configure the output.
- **🗃️ Organized Data Management:** Uses an `SQLite` database to log every conversion job, allowing for usage tracking and future analysis.
- **📦 Instant Delivery:** After processing, all resulting files are compressed into a single `.xavatar` file and delivered directly to the user in the same channel.
- **🗑️ Automatic Cleanup:** The bot automatically deletes temporary files after each operation to ensure no unnecessary storage space is consumed.

---

## 📚 Required Libraries

To run this bot, you will need to install the following libraries:

| Library | Command | Usage in Project |
| :--- | :--- | :--- |
| **discord.py** | `pip install py-cord` | The core library for interacting with the Discord API, creating commands, and managing events. |
| **Wand** | `pip install Wand` | A powerful image processing library used here for resizing, format conversion, and applying compression. |
| **Pillow** | `pip install Pillow` | A helper library for image processing, often required by `Wand` on some systems. |

**Additional Requirements:**
- **ImageMagick:** The `Wand` library is a wrapper for ImageMagick, so ImageMagick must be installed on the system where the bot will run.

---

## 🚀 How the Code Works

1.  **Command Invocation:** The user starts the process by typing the `/avatar` command and attaching an image.
2.  **File Validation:** The bot verifies that the attached file is a valid image.
3.  **UI Display:** The bot displays a message containing the uploaded image and two buttons: "Activated" and "Not Activated."
4.  **User Input:** When the user clicks a button, the processing logic begins in the background.
5.  **Job Logging:** The job details (user ID, activation status) are saved to the database.
6.  **Image Processing:** Multiple versions of the image are created in the required sizes and formats (`.png`, `.dds`).
7.  **JSON File Creation:** An `online.json` file is generated to specify the activation status.
8.  **Compression & Delivery:** All resulting files are bundled into a single `.xavatar` archive and sent as a reply to the user.
9.  **Cleanup:** The temporary directory containing the processed files is deleted.
