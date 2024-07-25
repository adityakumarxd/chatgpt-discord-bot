# ChatGPT Discord Bot

A Discord bot that integrates with OpenAI's GPT-3.5-turbo to answer questions via slash commands and text commands.

## Features

- Slash command `/ask` to get answers from GPT-3.5-turbo.
- Text command `.ask` for the same functionality.
- Configuration via a `config.json` file.

## Prerequisites

1. Python 3.8 or higher
2. `pip` (Python package installer)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/adityakumarxd/chatgpt-discord-bot.git
cd chatgpt-discord-bot
```

### 2. Install Dependencies
Create a virtual environment (recommended) and install the required packages:

For Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure the Bot
Create a config.json file in the project directory with the following structure:
```json
{
    "bot_token": "YOUR_BOT_TOKEN_HERE",
    "openai_api_key": "YOUR_OPENAI_API_KEY_HERE"
}
```
Replace "YOUR_BOT_TOKEN_HERE" with your Discord bot token and "YOUR_OPENAI_API_KEY_HERE" with your OpenAI API key.

### 4. Run the Bot
For Windows:
```bash
python main.py
```
For macOS/Linux:
```bash
python3 main.py
```
## Usage
Once the bot is running, you can use the following commands in your Discord server:

Slash Command: /ask <question> - Use this command to ask a question and get an answer from GPT-3.5-turbo.
Text Command: .ask <question> - Same as the slash command, but uses the text command format.

Contact
For any questions or feedback, please contact me on Discord `akxd`.








