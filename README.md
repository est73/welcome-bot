## WelcomeBot

A simple discord bot for Pokebattler Raid Party raid invites.

## Discord Bot Requirements

- Scope: Bot
- Bot Permissions: Manage Server

## Setup

- `git clone --depth 1 -b master git@github.com:est73/welcome-bot.git`
- `python3 -m venv ~/welcome-bot/venv`
- `. ~/welcome-bot/venv/bin/activate`
- `pip install -U -r ~/welcome-bot/requirements.txt`
- `cp ~/welcome-bot/config-example.py ~/welcome-bot/config.py`
- `nano ~/welcome-bot/config.py`
- `deactivate`
- `nohup ~/welcome-bot/venv/bin/python3 ~/welcome-bot/welcome-bot.py &`

## Requirements

- Python 3.8+
- discord.py