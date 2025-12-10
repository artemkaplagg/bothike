import telebot
import os

# --- ВНИМАНИЕ: Токен и ID вставлены ---
TOKEN = "8164185446:AAGfiX1AhS0p4QzzsCaGttJRiv3clrq_9E4"
CHAT_ID_TO_SEND_LOG = 6185367393 # Ваш Telegram ID для логов
# --- --------------------------- ---

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        # Отправляем приветственное сообщение
        bot.reply_to(message, "Привет! Я твой тестовый бот. Отправь мне что-нибудь!")
        
        # Логирование: отправляем сообщение вам, когда бот видит нового пользователя
        log_message = f"Новый пользователь: @{message.from_user.username or 'N/A'} (ID: {message.from_user.id})"
        # Проверяем, что ID отправителя не совпадает с ID для логов, чтобы не спамить самого себя
        if CHAT_ID_TO_SEND_LOG != 0 and message.from_user.id != CHAT_ID_TO_SEND_LOG: 
             bot.send_message(CHAT_ID_TO_SEND_LOG, log_message)
             
    except Exception as e:
        print(f"Ошибка в /start: {e}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        response_text = f"Ты сказал: **{message.text}**\n\nЯ - простой Python-бот, запущенный, возможно, в iSH!"
        bot.reply_to(message, response_text, parse_mode='Markdown')
        
    except Exception as e:
        print(f"Ошибка в echo_all: {e}")


print("Бот запущен. Ожидание сообщений...")
bot.infinity_polling()
