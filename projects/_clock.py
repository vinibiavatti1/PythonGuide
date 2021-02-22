"""
Clock
"""
import time


delay = 1
seconds = 0
minutes = 0
hour = 0

while True:
    time.sleep(delay)
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
            if hour == 24:
                hour = 0

    sfill = str(seconds).zfill(2)
    mfill = str(minutes).zfill(2)
    hfill = str(hour).zfill(2)
    print(f'{hfill}:{mfill}:{sfill}')
