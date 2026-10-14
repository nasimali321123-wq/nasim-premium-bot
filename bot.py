import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]

# এখানে নিজের অনুমোদিত অ্যাপের তথ্য যোগ করবে
APPS = {
    "app1": {
        "name": "Example App",
        "version": "1.0",
        "url": "https://play.google.com/store",
        "description": "App information"
    }
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 Browse Apps", callback_data="apps")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]

    await update.message.reply_text(
        "👋 Welcome to Nasim Premium Apps Bot!\n\n"
        "Choose an option below.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "apps":
        for app_id, app in APPS.items():
            keyboard = [[
                InlineKeyboardButton(
                    "⬇️ Download / Open",
                    url=app["url"]
                )
            ]]

            await query.message.reply_text(
                f"📱 {app['name']}\n"
                f"Version: {app['version']}\n"
                f"{app['description']}",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    elif query.data == "about":
        await query.message.reply_text(
            "Nasim Premium Apps Bot\n"
            "Official and authorized app links."
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()


if __name__ == "__main__":
    main()
