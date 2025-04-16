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

###

today_str_heading_found = False
first_table_row_found = False
new_table_row_index = None

for text_line_index, text_line in enumerate(text_lines):
    if not today_str_heading_found:
        if text_line == today_str_heading:
            today_str_heading_found = True
    elif not first_table_row_found:
        if text_line.startswith("|"):
            first_table_row_found = True
    elif not text_line.startswith("|"):
        new_table_row_index = text_line_index
        break
