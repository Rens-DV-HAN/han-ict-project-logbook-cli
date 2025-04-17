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

columns = [
    "Spent hours",
    "Description",
    "Those involved",
    "Result",
    "Emoji",
    "Link",
]

new_row_values = [input(f"{column}: ") for column in columns]
new_row = "| " + " | ".join(new_row_values) + " |\n"

text_lines.insert(new_row_index, new_row)
