import os
import asyncio

from dotenv import load_dotenv
from google import genai
from google.genai import types

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)


# =========================
# Load environment variables
# =========================

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# =========================
# Gemini client
# =========================

client = genai.Client(api_key=GEMINI_API_KEY)


# =========================
# Content Copilot Personality
# =========================

SYSTEM_INSTRUCTION = """
You are Content Copilot, an intelligent personal content creation assistant.

Your job is NOT to behave like a generic chatbot.

Your main purpose is to help the user turn quick, messy, incomplete ideas
into polished, publish-ready social media content.

You should understand short messages, rough ideas, incomplete thoughts,
and casual language.

Always respond in the same language the user uses unless they ask otherwise.

When the user gives you a content idea, help turn it into useful content.

For a normal content idea, provide:

1. Hook
2. Main content
3. CTA
4. Suggested content format

Possible formats include:
- LinkedIn post
- Instagram caption
- Carousel
- Reel script
- Short video idea

Keep the writing natural and human.
Avoid generic AI-sounding language.
Do not unnecessarily explain what you are doing.

If information is missing, make reasonable creative assumptions when possible.
Only ask a question when the missing information is important.

Remember the conversation and use previous messages as context.

You are a creative partner, not just a text generator.
"""


# =========================
# Create a Gemini chat
# =========================

def create_chat():

    return client.aio.chats.create(

        model="gemini-3.6-flash",

        config=types.GenerateContentConfig(

            system_instruction=SYSTEM_INSTRUCTION,

            thinking_config=types.ThinkingConfig(
                thinking_level="low"
            ),
        ),
    )


# =========================
# Handle Telegram messages
# =========================

async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.message or not update.message.text:
        return

    user_message = update.message.text

    print("User:", user_message)


    # Show "typing..." on Telegram
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )


    # Each Telegram user gets their own Gemini conversation
    chat = context.user_data.get("gemini_chat")

    if chat is None:

        chat = create_chat()

        context.user_data["gemini_chat"] = chat


    # Retry if Gemini temporarily gives 503
    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = await chat.send_message(
                user_message
            )

            ai_reply = response.text

            print("Content Copilot:", ai_reply)

            await update.message.reply_text(
                ai_reply
            )

            return


        except Exception as e:

            print(
                f"Attempt {attempt + 1} ERROR:",
                e
            )

            if (
                "503" in str(e)
                and attempt < max_retries - 1
            ):

                wait_time = 2 ** attempt

                await asyncio.sleep(wait_time)

            else:

                await update.message.reply_text(
                    "في ضغط مؤقت على خدمة الذكاء الاصطناعي. جرّب مرة ثانية بعد شوي."
                )

                return


# =========================
# Reset conversation memory
# =========================

async def reset_chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data.pop(
        "gemini_chat",
        None
    )

    await update.message.reply_text(
        "تم مسح ذاكرة المحادثة ✅"
    )


# =========================
# Start the bot
# =========================

def main():

    if not TELEGRAM_TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN was not found in .env"
        )

    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY was not found in .env"
        )


    app = (
        ApplicationBuilder()
        .token(TELEGRAM_TOKEN)
        .build()
    )


    app.add_handler(
        CommandHandler(
            "reset",
            reset_chat
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )


    print(
        "Content Copilot V2 is running..."
    )


    app.run_polling()


if __name__ == "__main__":
    main()