import telebot
import os
from Doc_Bot import Doc_Reader
from telebot import types



def main():

    
    TOKEN = 'Bot_token'
    bot = telebot.TeleBot(TOKEN)
    readers = {}
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Hi! Send me a PDF file so that I can extract information from it.")
        show_help_button(message.chat.id)  

    def show_help_button(chat_id):
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        help_button = types.KeyboardButton('/help')
        markup.add(help_button)
        bot.send_message(chat_id, "You can also use the help button below.", reply_markup=markup)

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(message, "To analyze another document, just upload it and the system will track it. "
                            "After adding it, you can ask questions about the document.")



    @bot.message_handler(content_types=['document'])
    def handle_document(message):
        try:
            if message.document.mime_type == 'application/pdf':
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)


                
                file_path = 'temp.pdf'
                
                with open(file_path, 'wb') as new_file:
                    new_file.write(downloaded_file)


                reader = Doc_Reader(file_path)
                chat_id = message.chat.id
                readers[chat_id] = reader

                os.remove(file_path)

                bot.reply_to(message, "The file has been uploaded successfully. Now write a request for analysis.")
            else:
                bot.reply_to(message, "Please send the PDF file.")
        except Exception as e:
            bot.reply_to(message, "An error has occurred: " + str(e))

    @bot.message_handler(func=lambda message: True)
    def handle_text(message):
        try:
            chat_id = message.chat.id
            reader = readers.get(chat_id)

            if reader:
            
                answer = reader.get_answer(message.text)

                bot.reply_to(message, answer)
            
            else:
                bot.reply_to(message, "Please download the PDF file first.")
        except Exception as e:
            bot.reply_to(message, "An error has occurred: " + str(e))


    bot.polling()


if __name__ == "__main__":
    main()
    
