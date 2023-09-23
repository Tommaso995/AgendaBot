import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "6363096240:AAHGOXpfVMB5FQi018ieUFF-ZbuGtdCFAK0"
datiDaSalvare = []

def start(update, context):
    scelta = update.message.reply_text("Ciao benvenuto nel bot, inizia ad aggiungere le tue note o appuntamenti\n\
                              Aggiungi per aggiungere\
                              Per eliminare digitare cancella più nome della nota\
                              Visualizza per stampare la lista")


def rispondi(update, context):
    testo_ricevuto = update.message.text.lower()
    if "aggiungi" in testo_ricevuto:
        update.message.reply_text("Digita la nota o appuntamento che vuoi aggiungere")
        # Attendere la risposta dell'utente
        context.user_data['action'] = 'aggiungi'  # Memorizza l'azione in corso
        return
    elif "visualizza" in testo_ricevuto:
        update.message.reply_text("Ecco la lista dei dati salvati")
        for i in datiDaSalvare:
            update.message.reply_text(i)
            print(i)
    elif "cancella" in testo_ricevuto:
        update.message.reply_text("Quale dato vuoi eliminare?")
        # Attendere la risposta dell'utente
        context.user_data['action'] = 'cancella'  # Memorizza l'azione in corso
        return
    else:
        # Se il testo ricevuto non corrisponde a nessuna delle opzioni sopra, potrebbe essere una nota da aggiungere o cancellare
        if 'action' in context.user_data:
            if context.user_data['action'] == 'aggiungi':
                datiDaSalvare.append(testo_ricevuto)
                update.message.reply_text("Nota aggiunta con successo!")
            elif context.user_data['action'] == 'cancella':
                for i in datiDaSalvare:
                    if testo_ricevuto in i:
                        datiDaSalvare.remove(i)
                        update.message.reply_text(f"Nota '{i}' eliminata con successo!")
                        break
                else:
                    update.message.reply_text("Dato non presente")
            del context.user_data['action']  # Pulisci l'azione in corso




updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start)) #allo start del bot fa partire la funzione start
updater.dispatcher.add_handler(MessageHandler(Filters.text, rispondi)) #estrae con la classi filter il testo del messaggio
print("Bot in ascolto...")
updater.start_polling() #fa rimanere in ascolto il bot così che sarà sempre pronto a rispondere