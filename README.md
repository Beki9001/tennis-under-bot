# Tennis Under Bot

A Telegram bot that analyzes tennis matches and provides betting recommendations for Under 22.5 games.

## Features
- Analyzes player statistics and form
- Considers surface performance
- Evaluates injury status
- Provides confidence percentage for Under 22.5 games

## Setup
1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Unix/macOS
   # or
   .\venv\Scripts\activate    # On Windows
   ```
2. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
3. Create `.env` file with your Telegram Bot Token
4. Run the bot:
   ```bash
   python3 src/main.py
   ```

## Usage
Send a message in the format:
`Player1 vs Player2, surface, odds1 - odds2`

Example:
`Berrettini vs Giron, clay, 1.22 - 4.20`