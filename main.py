from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


print("START")


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    name = update.effective_user.full_name

    keyboard = [
        [
            InlineKeyboardButton("Pherk", callback_data="pherk"),
            InlineKeyboardButton("Ot", callback_data="ot"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo( photo="https://www.s-liquor.com.kh/wp-content/uploads/2021/10/8847108066666.jpg"),

    await update.message.reply_text(
        f"Hello {name}! Pherk ot!",
        reply_markup=reply_markup
    )


# When user clicks a button
async def button_click(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    query = update.callback_query

    # Tell Telegram that we received the button click
    await query.answer()
    name = query.from_user.full_name

    if query.data == "pherk":

        await query.message.reply_text(
            "banh luy mk !!"
        )

        with open("img/qr.jpg", "rb") as photo:
            await query.message.reply_photo(
                photo=photo,
                caption="Nis Qr banh mk"
            )

    elif query.data == "ot":

        await query.message.reply_text(
            "mk tver ey ber ot pherk"
        )


# /clear
async def clear(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    chat_id = update.effective_chat.id

    await update.message.delete()

    message_ids = context.user_data.get("messages", [])

    for message_id in message_ids:
        try:
            await context.bot.delete_message(
                chat_id=chat_id,
                message_id=message_id
            )
        except Exception:
            pass

    context.user_data["messages"] = []


app = ApplicationBuilder().token(
    "8721533513:AAHmbdZ4rTR5UjWzRUAZjsdIscs6u5gEy_g"
).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("clear", clear))

# Handle button clicks
app.add_handler(CallbackQueryHandler(button_click))

app.run_polling()