"""
Clock
"""
import time
import datetime


###############################################################################
# Classes
###############################################################################


# Clock class
class Clock:
    """
    Clock class to process a clock by hours, minutes and seconds
    """
    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Creates a new clock
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @classmethod
    def now(cls):
        """
        Creates a new clock with current time
        """
        current_date = datetime.datetime.now()
        return cls(
            current_date.hour,
            current_date.minute,
            current_date.second
        )

    def __repr__(self):
        """
        Generates a clock string
        """
        return (
            f'{str(self.hours).zfill(2)}:'
            f'{str(self.minutes).zfill(2)}:'
            f'{str(self.seconds).zfill(2)}'
        )

    def update(self):
        """
        Updates the clock adding one second
        """
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    """
    Main method
    """
    clock = Clock.now()
    while True:
        print(repr(clock))
        clock.update()
        time.sleep(1)


# Init
if __name__ == '__main__':
    main()
