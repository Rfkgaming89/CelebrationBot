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

2.Step 1: Set the Environment Variable
On Windows

Open Command Prompt and set the environment variable:
```
set DISCORD_BOT_TOKEN=your_discord_bot_token
```
On macOS/Linux

Open Terminal and set the environment variable:

``` 
export DISCORD_BOT_TOKEN=your_discord_bot_token
```


3. Install the required dependencies:

```
pip install -r requirements.txt
```
4. Create a config.ini file in the project directory with the following content:
```
[DISCORD]
TOKEN=your_discord_bot_token
GUILD_ID=your_guild_id
BIRTHDAY_CHANNEL_ID=your_channel_id
```
Replace your_discord_bot_token, your_guild_id, and your_channel_id with the appropriate values.

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














