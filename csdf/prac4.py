import logging
import time
from datetime import datetime
import re

# Initialize the logging system
logging.basicConfig(filename="app.log", level=logging.INFO)

# Log some events
logging.info("Event 1: Something happened.")
time.sleep(1)
logging.info("Event 2: Another event occurred.")
time.sleep(1)
logging.info("Event 3: A third event took place.")
time.sleep(1)
logging.info("Event 4: Yet another event.")


# Event correlation function
def correlate_events(event1, event2):
    time_threshold = 2  # Time window in seconds for event correlation

    # Extract timestamps from log messages
    timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}"
    match1 = re.search(timestamp_pattern, event1)
    match2 = re.search(timestamp_pattern, event2)

    timestamp1 = None
    timestamp2 = None
    if match1:
        timestamp1 = match1.group(0)
    if match2:
        timestamp2 = match2.group(0)

    # Convert timestamps to datetime objects
    if timestamp1 is not None:
        timestamp1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S,%f")

    if timestamp2 is not None:
        timestamp2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S,%f")

    # Calculate the time difference between events
    if timestamp1 is not None and timestamp2 is not None:
        time_difference = abs((timestamp1 - timestamp2).total_seconds())
        if time_difference <= time_threshold:
            return True
        else:
            return False


# Read the log file and correlate events
with open("app.log", "r") as log_file:
    lines = log_file.readlines()
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            if correlate_events(lines[i], lines[j]):
                print(f"Correlated events: {lines[i].strip()} and {lines[j].strip()}")
