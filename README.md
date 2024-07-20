# CelebrationBot

CelebrationBot is a Discord bot designed to help manage and celebrate birthdays within your Discord server. The bot assigns a special birthday role to users on their birthday and sends a customized birthday message in a designated channel. Users can add their birthdays using a slash command.

## Features

- Assigns a "Birthday" role to users on their birthday.
- Sends a customized birthday message to a designated channel.
- Allows users to add their birthdays using a slash command in the format "Month Day Year".
- Administrators can add birthdays for other users.

## Setup and Configuration

### Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `sqlite3` library (comes with Python)
- `configparser` library

### Installation 

1. Clone the repository:

```bash
git clone https://github.com/yourusername/CelebrationBot.git
cd CelebrationBot
```

Instructions for Setting Up the .config File

On Windows

Open Notepad or another text editor.
Paste the following content:
```
[DISCORD]
TOKEN=your_discord_bot_token
GUILD_ID=your_guild_id
BIRTHDAY_CHANNEL_ID=your_channel_id
```

On MacOS/Linux

Create a config.ini File:

Open Terminal.
Use a text editor such as nano to create the config.ini file:

``` 
nano config.ini
```
```
[DISCORD]
TOKEN=your_discord_bot_token
GUILD_ID=your_guild_id
BIRTHDAY_CHANNEL_ID=your_channel_id
```
Save the file (for nano, press CTRL+X, then Y, then Enter).


3. Install the required dependencies:

```
pip install -r requirements.txt
```

Running the Bot

1. Ensure the config.ini file is in the same directory as your script and contains the correct values.
Run the bot:
2. Run the bot:
```
python birthday_bot.py
```
Usage

Adding a Birthday

Users can add their own birthday using the /add_birthday command. The command format is:

```
/add_birthday @user Month Day Year
```
For example:

```
/add_birthday @john_doe January 1 2000
```

Birthday Role and Messages

The bot will automatically assign the "Birthday" role to users on their birthday and send a birthday message to the designated channel. The role will be removed at the end of the user's birthday.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License.

Acknowledgements
[discord.py](https://github.com/Rapptz/discord.py) - An API wrapper for Discord written in Python.














