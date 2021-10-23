from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

@Client.on_message(filters.private & filters.command("start"))
async def start_main(main, update):
    await update.reply_text(
        text = Translation.START_MSG.format(update.from_user.first_name),
        parse_mode = "markdown",
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text = "Support Developer",
                        url="https://instagram.com/mirshad_kvr?utm_medium=copy_link"
                    ),
                    InlineKeyboardButton(
                        text = "Open Source",
                        url = "https://instagram.com/mirshad_kvr?utm_medium=copy_link"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text = "📢 Developer 📢" ,
                        url="t.me/dev_mirshad"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.private & filters.command("about"))
async def about_main(main, update):
    await update.reply_text(
        text = Translation.ABOUT_MSG,
        parse_mode = "markdown",
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text = "📢 Developer 📢" ,
                        url="t.me/dev_mirshad"
                    )
                ]
            ]
        )
    )
