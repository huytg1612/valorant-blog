import datetime
import math


class DateTimeProccessing():
    seconds_in_month = 60 * 60 * 24 * 30
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    def calculateDateTime(self, date):
        result = ""

        date = date.replace(tzinfo=None)
        delta = datetime.datetime.utcnow() - date
        total_second = delta.total_seconds()

        temp = total_second
        if total_second < self.seconds_in_minute:
            temp = math.floor(temp)
            result = str(temp) + " second"
        elif total_second < self.seconds_in_hour:
            temp = total_second / self.seconds_in_minute
            temp = math.floor(temp)
            result = str(temp) + " minute"
        elif total_second < self.seconds_in_day:
            temp = total_second / self.seconds_in_hour
            temp = math.floor(temp)
            result = str(temp) + " hour"
            print(temp)
        elif total_second < self.seconds_in_month:
            temp = total_second / self.seconds_in_day
            temp = math.floor(temp)
            result = str(temp) + " day"

        if(temp > 1):
            result += "s"

        result += " ago"
        return result
