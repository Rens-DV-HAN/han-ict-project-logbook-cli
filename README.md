# HAN ICT project logbook CLI

A simple CLI tool to easily add rows to a HAN ICT project logbook

## Prerequisites

- Python 3
- nl_NL.utf8 locale

## Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - Unix: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. Install `questionary`: `pip install questionary`

## Configuration

The following constants can be changed in the `main.py` file:

- `FILE_PATH`, to specify a different path for the logbook markdown file
  - Changing this one is not recommended, because it would make the script specific for a certain project.
    Consider changing into the directory of your logbook file before running the script (see [Usage](#usage))
- `EMOJIS`, to specify a different set of emojis to choose from

## Usage

Run the following in the venv:

`cd <LOGBOOK_PATH>; python <THIS_PROJECT_PATH>/main.py`

### Parameters

#### `--last-file-modification-datetime`

To define a custom last logbook file modification datetime, this parameter can be used. This is useful if the file is in a git stash for example. It should be in the format `%Y-%m-%d %H:%M:%S` (`yyyy-mm-dd hh:mm:ss`).

Example: `cd <LOGBOOK_PATH>; python <THIS_PROJECT_PATH>/main.py --last-file-modification-datetime="2025-05-08 14:26:39"`
