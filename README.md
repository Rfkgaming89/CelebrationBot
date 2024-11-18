**CelebrationBot** is a Discord bot designed to manage and celebrate birthdays within your Discord server. It assigns a special birthday role to users on their birthday, sends a customized birthday message, and allows users to add their birthdays using a slash command.

## Features

- Assigns a "Birthday" role to users on their birthday.
- Sends a customized birthday message to a designated channel.
- Allows users to add their birthdays using a slash command in the format "Month Day Year".
- Administrators can add birthdays for other users.

## Setup and Configuration

### Prerequisites

- `Python 3.8` or higher
- `discord.py` library
- `sqlite3` library (comes with Python)
- `configparser` library

### Installation

1. **Clone the Repository:**

   ``` git clone https://github.com/rfkgaming89/CelebrationBot.git ```

   ``` cd CelebrationBot``` 
   

3. **Create and Activate a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install the Required Dependencies:**

   Create a `requirements.txt` file in the root directory with the following content:

   ```
   discord.py
   ```

   Then, install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `config.ini` File:**

   Create a file named `config.ini` in the root directory with the following content:

   ```ini
   [DISCORD]
   TOKEN=your_discord_bot_token
   GUILD_ID=your_guild_id
   BIRTHDAY_CHANNEL_ID=your_channel_id
   ```

   Replace `your_discord_bot_token`, `your_guild_id`, and `your_channel_id` with the appropriate values.

### Running the Bot

1. **Ensure the `config.ini` File is Correctly Configured:**

   Make sure the `config.ini` file is in the same directory as your script and contains the correct values.

2. **Run the Bot:**

   ```bash
   python birthday_bot.py
   ```

### Commands

- **`/add_birthday`**: Add a birthday for a user in "Month Day Year" format.

  Example:
  ```
  /add_birthday @john_doe January 1 2000
  ```

### Customizing Birthday Messages

The bot includes a list of predefined birthday messages. You can customize these messages by modifying the `birthday_messages` list in the script:

```python
birthday_messages = [
    "Happy Birthday, {user}!",
    "🎉🎂 Happy Birthday, {user}! 🎂🎉",
    "Wishing you a fantastic birthday, {user}!",
    "It's your special day, {user}! Happy Birthday!",
    "Cheers to you on your birthday, {user}!"
]
```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py) - An API wrapper for Discord written in Python.
