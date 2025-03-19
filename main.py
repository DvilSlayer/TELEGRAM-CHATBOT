from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes
from telegram import Update
from typing import Final
import requests
import telebot
TOKEN: Final = "6684821735:AAEn9UbS7Wxnpz_6E_Qg5V7y8DMivXc6l8c"
Bot_username: Final = '@Tele_fuse_chat_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi 😊,\nWelcome to Fusion cinemas. Thank you for contacting us. \nPlease select a location to continue")

# response
def handle_response(text: str) -> str:
    if text == "1":
        from datetime import datetime, timezone, timedelta
        current_time = datetime.now()
        response = requests.get(url=f"https://max-api.fusionintel.io/api/v1/Showtimes/get-whatsapp-showtimes?DateFrom={current_time.month}%2F17%2F{current_time.year}&DateTo={current_time.month}%2F18%2F{current_time.year}", headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
        data = response.json()
        x = data['data']
        movie_info_dict = {}
        for movie in x:
            movie_name = movie["film"]
            if movie_name not in movie_info_dict:
                movie_info_dict[movie_name] = []
            start_time_utc = datetime.strptime(movie["startTime"], "%Y-%m-%dT%H:%M:%SZ")
            end_time_utc = datetime.strptime(movie["endTime"], "%Y-%m-%dT%H:%M:%SZ")
            local_timezone = timezone.utc
            start_time_local = start_time_utc.replace(tzinfo=local_timezone).astimezone(
                timezone(timedelta(hours=5)))  # Adjust the hours according to your timezone
            end_time_local = end_time_utc.replace(tzinfo=local_timezone).astimezone(
                timezone(timedelta(hours=5)))  # Adjust the hours according to your timezone
            movie_info_dict[movie_name].append("Screen: " + movie["screen"])
            movie_info_dict[movie_name].append("Start Time : " + start_time_local.strftime("%I:%M %p"))
            # movie_info_dict[movie_name].append("End Time : " + end_time_local.strftime("%I:%M %p"))
            movie_info_dict[movie_name].append("Total seats: " + str(movie["totalSeats"]))
            movie_info_dict[movie_name].append("Available seats: " + str(movie["totalSeats"] - movie["seatsSold"]))
            movie_info_dict[movie_name].append("=" * 34)
        for i in movie_info_dict.values():
            if len(i) > 6:
                for t in i[:-1]:
                    dd = i.index(t)
                    if t == ('=================================='):
                        i[dd] = ('__________________________________')
        all_movie_in = []
        for movie_name, info_list in movie_info_dict.items():
            movie_info = ["Movie: " + movie_name]
            movie_info.extend(info_list)
            movie_string = '\n'.join(movie_info)
            all_movie_in.append(movie_string)
        final_movie_info = '\n'.join(all_movie_in)
        ans = final_movie_info
        return ans
    elif text == "2":
        from datetime import datetime, timezone, timedelta
        current_time = datetime.now()
        response = requests.get(url=f"https://max-api.fusionintel.io/api/v1/Showtimes/get-whatsapp-showtimes?DateFrom={current_time.month}%2F17%2F{current_time.year}&DateTo={current_time.month}%2F18%2F{current_time.year}", headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
        data = response.json()
        x = data['data']
        movie_info_dict = {}
        for movie in x:
            movie_name = movie["film"]
            if movie_name not in movie_info_dict:
                movie_info_dict[movie_name] = []

        all_movie_info = []
        for movie_name, info_list in movie_info_dict.items():
            movie_info = ["Movie: " + movie_name]
            movie_info.extend(info_list)
            movie_string = '\n'.join(movie_info)
            all_movie_info.append(movie_string)
        final_movie_info2 = '\n'.join(all_movie_info)
        ans = final_movie_info2
        return ans
    elif text == "3":
        from datetime import datetime, timezone, timedelta
        current_time = datetime.now()
        respons = requests.get(url=f"https://max-api.fusionintel.io/api/v1/Showtimes/get-showtimes?DateFrom={current_time.month}%2F17%2F{current_time.year}&DateTo={current_time.month}%2F18%2F{current_time.year}", headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
        dat = respons.json()
        y = dat['data']
        movie_info = []
        for movie in y:
            movie_ = []
            price_card = movie["priceCard"]
            movie_info.append("Price Card Name:" + price_card["name"])

            for ticket in price_card["tickets"]:
                movie_.append("Ticket Name:" + ticket["ticketName"])
                movie_.append("Price:" + str(ticket["price"]))
            movie_info_str = '\n'.join(movie_)
        ans = movie_info_str
        return ans
    elif text == "4":
        ans = "Thank you for contacting us\n One our agents will be with you shortly"
        return ans
    elif "fusion" in text or "Fusion" in text:
        ans = "For showtimes send 1\nFor films send 2\nFor ticket prices send 3\nTo speak to one of our agents send 4"
        return ans
    else:
        response = requests.get(
            url="https://api.reachcinema.io/api/v1/Cinemas/ListAllByCircuit?circuitId=c7525c4a-d2b6-46e3-83cd-646402c62326",
            headers={'Content-type': 'application/json',
                     'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
        data = response.json()
        x = data['data']
        cinema_info = {}
        for cinema in x:
            cinema_name = cinema["name"]
            if cinema_name not in cinema_info:
                cinema_info[cinema_name] = []
            cinema_info[cinema_name].append("Address: " + cinema["address"])
            cinema_info[cinema_name].append("_" * 34)
        all_cinema_in = []
        for cinema_name, info_list in cinema_info.items():
            cinem_info = ["Cinema Name: " + cinema_name]
            cinem_info.extend(info_list)
            cinema_string = '\n'.join(cinem_info)
            # create a movie list
            all_cinema_in.append(cinema_string)
        final_cinema_info = '\n'.join(all_cinema_in)

        ans = f"Hi 😊,\nWelcome to Fusion cinemas. Thank you for contacting us. \nPlease select a location to continue\n\n{final_cinema_info}"
        return ans


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':
        if Bot_username in text:
            new_text: str = text.replace(Bot_username, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)







