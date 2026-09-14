import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout
import json
import random
from datetime import datetime
dictionary = {}
streak = {}
def main():
    #Show 5 Spanish Words
    file_path = "ParsedWords.json"
    with open(file_path, "r", encoding="utf-8") as file:
        dictionary = json.load(file)
        chosen_words = random.sample(list(dictionary.items()), 5)
        print("Your spanish words:")
        for key, value in chosen_words:
            #while not str(number) in dictionary:
            #    number = random.randint(1,len(dictionary))
            print(f"Your spanish word: {dictionary[key][0]}, means: {dictionary[key][1]}")
            dictionary.pop(f"{key}")
                
            #print(len(dictionary))
    with open(file_path, "w", encoding = "utf-8") as file:
        json.dump(dictionary, file, indent = 4)
        file_path_streak = "streak.json"
        if not os.path.exists(file_path_streak):
            with open(file_path_streak, "w") as file:
                json.dump({1 : str(datetime.today().date())},file)
        update_type = 0
        with open(file_path_streak, "r") as file:
            streak = json.load(file)
            last_key, last_date = next(reversed(streak.items()))
            new_last_date = datetime.strptime(last_date, "%Y-%m-%d").date()
            if (datetime.today().date() - new_last_date).days == 1:
                update_type = 1
            elif (datetime.today().date() - new_last_date).days >= 1:
                update_type = 2
        if update_type:
            with open(file_path_streak, "w") as file:
                if update_type == 1:
                    updated_key = int(last_key) + 1
                    streak.update({updated_key : str(datetime.today().date())})
                    json.dump(streak,file)
                    print(f"Yay!! You completed a new day: {updated_key} days streak")
                else:
                    streak.update({1 : str(datetime.today().date())})
                    json.dump(streak,file)
                    print("Sadly you start again, day streak: 1")
        else:
            print(f"You are on: {last_key} day/s streak")
    print("Have fun learning")
            #add calendar with all dates done
if __name__ == "__main__":
    main()
