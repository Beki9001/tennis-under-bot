"""
Main module for the Tennis Under Bot.
Handles Telegram message processing and coordinates data analysis.
"""
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from data_scraper import get_player_stats
from ai_evaluator import evaluate_match
from utils import parse_message, format_response

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    welcome_message = (
        "Welcome to Tennis Under Bot!\n\n"
        "Send me a message in this format:\n"
        "Player1 vs Player2, surface, odds1 - odds2\n\n"
        "Example:\n"
        "Berrettini vs Giron, clay, 1.22 - 4.20"
    )
    await update.message.reply_text(welcome_message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process incoming messages and return match analysis."""
    try:
        # Parse the message
        player1, player2, surface, odds = parse_message(update.message.text)
        
        # Get player statistics
        stats = get_player_stats(player1, player2, surface)
        
        # Evaluate the match
        evaluation = evaluate_match(stats, odds)
        
        # Format and send the response
        response = format_response(evaluation)
        await update.message.reply_text(response)
        
    except Exception as e:
        error_message = f"Error: {str(e)}"
        logger.error(error_message)
        await update.message.reply_text(error_message)

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()