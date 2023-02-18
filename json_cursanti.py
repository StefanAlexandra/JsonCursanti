import json
import datetime
import logging
import asyncio
import telegram
from time import perf_counter

time_start = perf_counter()


json_data = {"Cursanti":[
    {"nume": "Ion",
     "prenume": "Ionel",
     "hobby": ["calatoritul", "muzica"],
     "tel": [{"cod_tara": "+40", "nr": "75*******"}, {"cod_tara": "+33", "nr": "58*******"}]
     },
    {"nume": "Vasilescu",
     "prenume": "Vasile",
     "hobby": ["calatoritul", "sportul"],
     "tel": [{"cod_tara": "+40", "nr": "74*******"}, {"cod_tara": "+32", "nr": "59*******"}]
     },
    {"nume": "Mihaescu",
     "prenume": "Mihai",
     "hobby": ["cititul", "jocuri video"],
     "tel": [{"cod_tara": "+40", "nr": "72*******"}, {"cod_tara": "+31", "nr": "60*******"}]
     }
]}

#a
path = "C:/Users/Andreea/PycharmProjects/SDA/Intermediate/2023_02_18/JsonCursanti"
hour_now = datetime.datetime.now().hour
logging.basicConfig(filename="json_cursanti.log", format="%(asctime)s %(message)s", filemode='w')

obj_log = logging.getLogger()

obj_log.setLevel(logging.DEBUG)
obj_log.debug(("Just an info"))

# a, b = 1,2
# print(a+b)
# obj_log.info("Printul de a+b a fost cu succes")

try:
    with open(f"{path}/json_cursanti.json", "w") as f:
        f.write(json.dumps(json_data, indent=4))
    obj_log.info("operatiunea de scriere 1 a fost cu succes")
except Exception as e:
    obj_log.error(f"Operatiunea de scriere 1 a esuat cu eroarea {e}")

try:
    with open(f"{path}/json_cursanti.json", "r") as f:
        data = json.loads(f.read())
        json_formatted_str = json.dumps(data, indent=4)
except FileNotFoundError:
    print("Fisierul nu a fost gasit.")
    obj_log.error("Fisierul nu a fost gasit.")

def course_hours(func):
    def wrapper(*args):
        if 9 <= hour_now <= 16:
            return func(*args)
        else:
            return "Nu se poate adauga in afara orelor de curs"
    return wrapper


@course_hours
def add_person(new_data, filename='json_cursanti.json'):
    with open(filename, 'r+') as f:
        file_data = json.loads(f.read())
        file_data["Cursanti"].append(new_data)
        f.seek(0)
        json.dump(file_data, f, indent=4)


new_person = {"nume": "Ionescu",
     "prenume": "Ionut",
     "hobby": ["statul la plaja", "cititul"],
     "tel": [{"cod_tara": "+40", "nr": "77*******"}, {"cod_tara": "+36", "nr": "80*******"}]
     }

try:
    add_person(new_person)
    obj_log.info("Cursant adaugat cu succes!")
except Exception as e:
    obj_log.critical(f"Cursantul nu a putut fi adaugat. Actiunea a esuat cu eroarea {e}")


# #pip install python-telegram-bot
# #bot link = http://t.me/sda_17xy_robot
# # !!! pentru a putea trimite mesaje, trebuie mai intai sa intrati pe pagina bot-ului si sa apasati /start.
# #Acesta e un fel de acord ca robotul sa poata interactiona cu voi
# #pentru a va afla id-ul contului, scrieti aici> https://t.me/raw_info_bot
#
# tg_api = '6227517925:AAEG62y40j_iGJqvXdTSceUlejR1OdRagTQ'
# #pentru a seta un bot, interactionati cu https://t.me/BotFather
# #dar acum puteti folosi acest token pentru bot-ul creat https://t.me/sda_17xy_robot
# id_Constantin = 1307289323
# text_to_send = json_formatted_str
#
# async def send_mes(id,text):
#     bot = telegram.Bot(tg_api)
#     async with bot:
#         await bot.sendMessage(id,text)
#
# asyncio.run(send_mes(id_Constantin, text_to_send))

print(f"Timp de executie = {perf_counter() - time_start} seconds")
