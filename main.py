import locale
import math
import os.path
from datetime import datetime

import questionary

locale.setlocale(locale.LC_TIME, "nl_NL.utf8")

###

FILE_PATH = "./logboek-projectweek-1.md"

with open(FILE_PATH, encoding="utf-8") as file:
    text_lines = file.readlines()

###

now = datetime.now()
today_str = now.strftime("%A %-d %B").capitalize()
today_str_heading = f"## {today_str}\n"

###

today_str_heading_found = False
first_row_found = False
new_row_index = None

for text_line_index, text_line in enumerate(text_lines):
    if not today_str_heading_found:
        if text_line == today_str_heading:
            today_str_heading_found = True
    elif not first_row_found:
        if text_line.startswith("|"):
            first_row_found = True
    elif not text_line.startswith("|"):
        new_row_index = text_line_index
        break

if new_row_index is None:
    raise ValueError(
        "New table row index not found\n"
        f"{today_str_heading_found = }\n"
        f"{first_row_found = }"
    )

###

last_file_modification_timestamp = os.path.getmtime(FILE_PATH)
last_file_modification_datetime = datetime.fromtimestamp(
    last_file_modification_timestamp
)

hours_since_last_file_modification = (
    now - last_file_modification_datetime
).total_seconds() / 3600
hours_since_last_file_modification_rounded = (
    math.ceil(hours_since_last_file_modification * 2) / 2
)
hours_since_last_file_modification_rounded_str = str(
    hours_since_last_file_modification_rounded
).replace(".", ",")

new_row_data = {
    "Tijd": hours_since_last_file_modification_rounded_str,
    "Beschrijving": "",
    "Met wie": "N.v.t.",
    "Resultaat": "",
    "Emoji": "",
    "Link": "N.v.t.",
}

EMOJIS = ["😐", "😒", "😮‍💨", "🙂", "😀"]

for column, value in new_row_data.items():
    message = f"{column}: "
    new_row_data[column] = (
        questionary.text(message, default=value)
        if column != "Emoji"
        else questionary.select(message, choices=EMOJIS)
    ).ask()

new_row = "| " + " | ".join(new_row_data.values()) + " |\n"

text_lines.insert(new_row_index, new_row)

###

with open(FILE_PATH, "w", encoding="utf-8") as file:
    file.writelines(text_lines)
