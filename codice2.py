import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

admin_list = [2102404147]

def start(update, context):
    if update.message.from_user.id in admin_list:
        update.message.reply_text("Inserisci il link Mixdrop da scaricare: ")
    else:
        update.message.reply_text("Non hai i permessi per utilizzare questo comando")

def download_file(update, context):
    if update.message.from_user.id in admin_list:
        link = update.message.text
        nome_file = link.split("/")[-1]
        r = requests.get(link, allow_redirects=True)
        context.bot.send_document(chat_id=update.message.chat_id, document=r.content, filename=nome_file)
        update.message.reply_text("Il file è stato inviato con successo in chat!")
        os.remove(nome_file)
    else:
        update.message.reply_text("Non hai i permessi per utilizzare questo comando")

def add_admin(update, context):
    if update.message.from_user.id in admin_list:
        new_admin = update.message.text.split()[1]
        admin_list.append(new_admin)
        update.message.reply_text(f"L'utente {new_admin} è stato aggiunto come amministratore")
    else:
        update.message.reply_text("Non hai i permessi per utilizzare questo comando")

# Inserisci il tuo token del bot qui
updater = Updater("5849475631:AAFx9r-_fqZvax38VC4IMRQu5bO8H8zcO-w", use_context=True)

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("add_admin", add_admin))
updater.dispatcher.add_handler(MessageHandler(filters.text, download_file))

updater.start_polling()
updater.idle()
