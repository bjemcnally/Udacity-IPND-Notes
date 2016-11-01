import time
import webbrowser

"""
MY ANSWER:

break_number = 1


def take_a_break(break_number):
    while break_number <= 3:
        time.sleep(10)
        webbrowser.open("https://youtu.be/lENWOLce59s?list=LLbekQlDyAdlvcFcLh2dwucA")
        break_number += 1

take_a_break(break_number)

REMEMBER TO AVOID 'magic numbers'! This is the main difference
between my answer and the video answer!

Also: creating a function is unneccesary!
"""

"""Video answer"""

total_breaks = 3
break_count = 0

print ("This program started on " + time.ctime())
while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("https://youtu.be/lENWOLce59s?list=LLbekQlDyAdlvcFcLh2dwucA")
    break_count += 1

