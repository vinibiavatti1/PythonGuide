"""
Calendar
"""
import datetime
from calendar import monthrange, weekday, month_name


###############################################################################
# Classes
###############################################################################


# Calendar
class Calendar:
    """
    Calendar that can be rendered as string
    """

    LINE = '+----+----+----+----+----+----+----+\n'
    FULL_LINE = '+----------------------------------+\n'

    def __init__(self, year, month):
        """
        Creates a new calendar with year and month
        """
        self.year = year
        self.month = month
        self.week_days = ('S', 'M', 'T', 'W', 'T', 'F', 'S')

    @classmethod
    def current_month(cls):
        """
        Creates a new calendar with current year and month
        """
        today = datetime.date.today()
        return cls(today.year, today.month)

    def __repr__(self):
        """
        Generates calendar as string
        """
        display = ''
        start_week_day = weekday(self.year, self.month, 1)
        days_count = monthrange(self.year, self.month)[1]

        display += Calendar.FULL_LINE
        display += self._description_block()
        display += Calendar.LINE
        display += self._week_block()
        display += Calendar.LINE
        display += self._days_block(start_week_day, days_count)
        return display

    def _description_block(self):
        """
        Creates a description block for calendar
        """
        display = f'{month_name[self.month]} of {self.year}'.center(34)
        return '|' + display + '|\n'

    def _week_block(self):
        """
        Creates a week block for calendar
        """
        return '|' + (
            '|'.join(str(wd).rjust(3) + ' ' for wd in self.week_days)
            ) + '|\n'

    def _days_block(self, start_week_day, days_count):
        """
        Creates a days block for calendar
        """
        today = datetime.date.today()
        show_today = False
        if self.year == today.year and self.month == today.month:
            show_today = True
        start_week_day += 2
        display = ''
        day = None
        for block in range(1, 43):
            if block == start_week_day:
                day = 1
            if day:
                if show_today and day == today.day:
                    display += '|(' + str(day).rjust(2) + ')'
                else:
                    display += '|' + str(day).rjust(3) + ' '
                day += 1
                if day > days_count:
                    day = None
            else:
                display += '|    '
            if block % 7 == 0:
                display += '|\n'
                display += Calendar.LINE
        return display


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    calendar = Calendar.current_month()
    print(repr(calendar))


# Init
if __name__ == '__main__':
    main()
