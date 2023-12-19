import os

from tasks import task1, task2, task3, task4
import time


def reverse_report():
    text = "Seconds before ending: "
    for i in range(3, -1, -1):
        print(text, i, end='\r')
        time.sleep(1)


def clear():
    os.system('cls')
    print('', end='\b \b')


if __name__ == "__main__":
    task1.run()
    task2.run()
    task3.run()
    task4.run()
