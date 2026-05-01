import logging
from telegram.ext import Application, CommandHandler
from bots.telegram import commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    from backend.config import get_settings
    settings = get_settings()

    if not settings.telegram_bot_token:
        logger.error("TELEGRAM_BOT_TOKEN not set in .env")
        return

    app = Application.builder().token(settings.telegram_bot_token).build()

    app.add_handler(CommandHandler("start", commands.start))
    app.add_handler(CommandHandler("health", commands.health))
    app.add_handler(CommandHandler("crisis", commands.crisis))
    app.add_handler(CommandHandler("compare", commands.compare))
    app.add_handler(CommandHandler("top5", commands.top5))
    app.add_handler(CommandHandler("bottom5", commands.bottom5))
    app.add_handler(CommandHandler("briefing", commands.briefing))
    app.add_handler(CommandHandler("query", commands.query))

    logger.info("SOVEREIGN Telegram Bot starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
