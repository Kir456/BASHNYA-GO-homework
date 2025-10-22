from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = '8073665944:AAEq-2eJupeZcOXzZmEn9ocW9wLzu3-xObI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start и приветствия после отсутствия"""
    user = update.effective_user
    await update.message.reply_text(
        f'Привет, {user.first_name}! Я телеграм-бот, работающий с экосистемой BMSTU.\n'
        'Чем могу помочь?'
    )
    context.user_data['last_seen'] = datetime.now()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Проверяем время отсутствия и приветствуем, если нужно"""
    last_seen = context.user_data.get('last_seen')
    now = datetime.now()
    
    if not last_seen or (now - last_seen) > timedelta(hours=1):
        await start(update, context)
    else:
        context.user_data['last_seen'] = now

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🟢 Бот запущен и отслеживает возвращения пользователей...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()