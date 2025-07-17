import requests

for i in range (10):
    r = int(input("pick a number"))
    if r== 3:
        l=2
        print("yes")
        print(i)

    elif r==6:
        if v == 7:
            print("fff")
    elif r==4 and l==2 :
        print("no")
    elif r==5 and l==4 :
        print("nes")
    else:
        v=0
        for n in range (7):
            v+=1
        l=4
        print('ddd')

response = requests.get(
    url="https://api.reachcinema.io/api/v1/Cinemas/ListAllByCircuit?circuitId=c7525c4a-d2b6-46e3-83cd-646402c62326",
    headers={'Content-type': 'application/json',
             'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
data = response.json()
o = data['data']
id_ = []
for i in o:
    id_.append(i['id'])
from datetime import datetime, timezone, timedelta

current_time = datetime.now()
response = requests.get(
    url=f"https://max-api.fusionintel.io/api/v1/Showtimes/get-whatsapp-showtimes?DateFrom={current_time.month}%2F{current_time.day}%2F{current_time.year}&DateTo={current_time.month}%2F{current_time.day + 1}%2F{current_time.year}",
    headers={'Content-type': 'application/json',
             'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
data = response.json()
x = data['data']
movie_info_dict = {}
for movie in x:
    movie_name = movie["film"]
    if movie_name not in movie_info_dict:
        movie_info_dict[movie_name] = []

all_movie_info = []
films = 0
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
for movie_name, info_list in movie_info_dict.items():
    movie_info = [f"{keys[films]}) Movie: " + movie_name]
    films += 1
    movie_info.extend(info_list)
    movie_string = '\n'.join(movie_info)
    all_movie_info.append(movie_string)
final_movie_info2 = '\n'.join(all_movie_info)
# ans = f'{id_[1]}\nPlease{retrieved_data["cinemaId"]} Input a letter to view the movies screentimes\n\n' + final_movie_info2
ans = '\nPlease Input a letter to view the movies screentimes\n\n' + final_movie_info2
from datetime import datetime


current_datetime = datetime.utcnow()
formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
retrieved_data["order"]["dateTimeReserved"] = formatted_datetime
retrieved_data["cinemaId"] = id_[1]
connection = sqlite3.connect('my_dictionary_db.db')
cursor = connection.cursor()
cursor.execute("UPDATE dictionaries SET data=? WHERE name=?",
               (json.dumps(retrieved_data), 'example_dict'))
connection.commit()
connection.close()
