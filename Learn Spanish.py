import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QMovie, QPixmap
import json
import random
from datetime import datetime
from PyQt5.QtCore import Qt
dictionary = {}
streak = {}
class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.indx = 0
        self.days_streak = 0
        self.words = []
        self.setWindowTitle("Spanish Words")
        self.setGeometry(500,300,700,700)
        self.text_learn = QLabel(self)
        self.centralwidget_words = QWidget()
        self.next_button = QPushButton(self)
        self.next_button.hide()
        self.flag = QLabel(self)
        self.text_start = QLabel(self)
        self.gif_flag = QMovie("spain.gif")
        self.centralwidget = QWidget()
        self.flag.setScaledContents(True) 
        #self.flag.setGeometry(0,0,100,100)
        self.start_button = QPushButton(self)
        self.initBack()
        self.initUI_start()
    def initBack(self):
        #Show 5 Spanish Words
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
                        self.text_start.setText(f"Yay!! You completed a new day: {updated_key} days streak")
                        self.text_start.setText(f"You are on: {last_key} day/s streak")
                        self.days_streak = updated_key
                    else:
                        streak.update({1 : str(datetime.today().date())})
                        json.dump({1 : str(datetime.today().date())},file)
                        self.text_start.setText("Sadly you start again, day streak: 1")
                        #Bug on day 1
                        self.days_streak = 1
            else:
                self.days_streak = last_key
                self.text_start.setText(f"You are on: {last_key} day/s streak")
        #print("Have fun learning")
                #add calendar with all dates done
    def initUI_start(self):
        self.text_start.setMinimumWidth(300)
        self.text_start.setWordWrap(True)
        self.centralwidget.setObjectName("central")
        self.centralwidget_words.setObjectName("central2")
        self.centralwidget.setStyleSheet("""QWidget#central {
                                                background: qlineargradient(
                                                x1:0, y1:0, x2:1, y2:1,
                                                stop:0 #f7f5f2, stop:1 #ece7e1
                                                );
                                            }
                                            QWidget#central {
                                                background: qlineargradient(
                                                x1:0, y1:0, x2:1, y2:1,
                                                stop:0 #f7f5f2, stop:1 #ece7e1
                                                );
                                            }
                                        """)
        self.setStyleSheet("""       QLabel{
                                        font-size: 20px;
                                        font-weight: bold;
                                        font-family: Consolas;
                                    }
                                    QPushButton {
                                        background-color: #1e1e1e;
                                        color: #f0f0f0;
                                        font-size: 15px;
                                        font-family: Consolas;
                                        border: 2px solid #3d3d3d;
                                        border-radius: 8px;
                                        padding: 10px 24px;
                                    }
                                    QPushButton:hover {
                                        background-color: #2a2a2a;
                                        border: 2px solid #555;
                                    }
                                    QPushButton:pressed {
                                        background-color: #111;
                                    }
                                    """)
        self.start_button.setText("Start")
        self.flag.setFixedSize(300,200)
        self.start_button.setFixedSize(300,100)
        #self.text_start.setText(f"You are currently on a {self.days_streak} day/s streak")
        self.flag.setMovie(self.gif_flag)
        self.gif_flag.start()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_start)
        vbox.addWidget(self.flag)
        vbox.addWidget(self.start_button)
        self.sagrada_background = QLabel(self.centralwidget)
        sagrada_pixmap = QPixmap("sagrada_familia.png")
        self.sagrada_background.setPixmap(sagrada_pixmap)
        self.sagrada_background.setScaledContents(True)
        self.sagrada_background.setGeometry(0, 0, self.width(), self.height())
        self.sagrada_background.lower()
        #self.text_start.setAlignment(Qt.AlignCenter)
        #self.flag.setAlignment(Qt.AlignCenter)

        vbox.setAlignment(Qt.AlignCenter)
        
        self.centralwidget.setLayout(vbox)
        self.setCentralWidget(self.centralwidget)

        self.start_button.clicked.connect(self.initUI_Words)
    def initUI_Words(self):
        self.centralwidget.hide()
        self.chose_words()
        self.text_learn.setText(self.words[self.indx])

        self.text_learn.setWordWrap(True)
        self.text_learn.setMinimumWidth(300)
        
        #self.next_button.setFixedSize(300, 100)
        self.next_button.setStyleSheet("""
            QPushButton {
                border: none;
                background: transparent;
                background-image: url(bull.png);
                background-repeat: no-repeat;
                background-position: center;
                color: black;
            }
            QPushButton:hover {
                background-image: url(bull_hover.png);
                color: white;
            }
        """)
        self.next_button.setFixedSize(150, 150) 
        self.next_button.setText("")
        self.next_button.setText("Next")
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.text_learn)
        vbox.addSpacing(20) 
        vbox.addWidget(self.next_button)
        vbox.addStretch(1)
        vbox.setContentsMargins(40, 20, 40, 20)
        vbox.setAlignment(Qt.AlignCenter)
        self.centralwidget_words.setLayout(vbox)
        self.setCentralWidget(self.centralwidget_words)
        
        self.centralwidget.show()
        self.next_button.show()
            
        self.next_button.clicked.connect(self.next_words)
    def next_words(self):
        if self.indx == 4:
            self.text_learn.setText(f"FELICIDAD!!!\nYou finished another lesson: {self.days_streak}.")
            self.text_learn.setStyleSheet("font-size: 70px;")
            self.next_button.hide()
            self.indx = -1000
        else:
            self.indx +=1
            self.text_learn.setText(self.words[self.indx])
    def chose_words(self):
        file_path = "ParsedWords.json"
        with open(file_path, "r", encoding="utf-8") as file:
            
            dictionary = json.load(file)
            chosen_words = random.sample(list(dictionary.items()), 5)
            #print("Your spanish words:")
            for key, value in chosen_words:
                #while not str(number) in dictionary:
                #    number = random.randint(1,len(dictionary))
                self.words.append(f"Your spanish word: {dictionary[key][0]}, means: {dictionary[key][1]}")
                dictionary.pop(f"{key}")
                #print(len(dictionary))
        with open(file_path, "w", encoding = "utf-8") as file:
            json.dump(dictionary, file, indent = 4)

def main():
    app = QApplication(sys.argv)
    main_window = mainwindow()
    main_window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
