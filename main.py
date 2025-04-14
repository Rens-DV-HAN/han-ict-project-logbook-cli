import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "nl_NL.utf8")

###

FILE_PATH = "./logboek-projectweek-1.md"

with open(FILE_PATH) as file:
    text_lines = file.readlines()

###

today = datetime.today()
today_str = today.strftime("%A %-d %B").capitalize()
today_str_heading = f"## {today_str}\n"
