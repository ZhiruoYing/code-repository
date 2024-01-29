"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""
#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone)


def date_passed(todays_date, scheduled_date):
    from datetime import datetime #必须是有from和import才能使用strptime
    t=todays_date.replace("th"," ").replace("rd"," ").replace("st"," ").replace("nd"," ")#把日期中不能识别的曲调
    t=datetime.strptime(t,"%d %B")#转化成系统能识别的样子（“%d %B %Y)
    s=scheduled_date.replace("th"," ").replace("rd"," ").replace("st"," ").replace("nd"," ")#把日期中不能识别的曲调
    s=datetime.strptime(s,"%d %B")

    if t>s:#转化成系统能识别的时间之后就是可以比较的
        return "Scheduled date has passed"
    elif t==s:
        return "Scheduled date is today"
    else:
        return "Scheduled date is yet to pass"

    




    # Implement the logic to compare the dates and print the appropriate message
    pass  # Delete this after implementing some code inside this function


# Test cases
print(date_passed("26th March", "25th March"))  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
