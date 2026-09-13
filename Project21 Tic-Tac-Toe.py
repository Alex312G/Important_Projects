import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

#Forms = (" ", "X", "O")
Table = [[" " for _ in range(3)] for _ in range(3)]
class X_and_O(QMainWindow):
    def __init__(self):
        super().__init__()
        self.moves = 0
        self.setGeometry(0,0,1920,1080)
        self.text = QLabel("Chose your move: ", self)
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)
        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.button7 = QPushButton(self)
        self.button8 = QPushButton(self)
        self.button9 = QPushButton(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("X AND O")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QGridLayout()
        vboxfin = QVBoxLayout()

        vbox.addWidget(self.button1,0,0)
        vbox.addWidget(self.button2,0,1)
        vbox.addWidget(self.button3,0,2)
        vbox.addWidget(self.button4,1,0)
        vbox.addWidget(self.button5,1,1)
        vbox.addWidget(self.button6,1,2)
        vbox.addWidget(self.button7,2,0)
        vbox.addWidget(self.button8,2,1)
        vbox.addWidget(self.button9,2,2)

        self.text.setAlignment(Qt.AlignCenter)  
        vboxfin.addStretch(1) 
        vboxfin.addWidget(self.text)
        vboxfin.addLayout(vbox)
        vboxfin.addStretch(1) 
        vboxfin.setAlignment(vbox, Qt.AlignCenter)
        central_widget.setLayout(vboxfin)
        #central_widget.setStyleSheet("background-color: blue;")
        central_widget.setObjectName("central")
        for button in self.findChildren(QPushButton):
            button.setFixedSize(500, 150)
        self.setStyleSheet("""
        QWidget#central{
            background-color: black; 
        }
        QPushButton{
            font-size: 50px;
            background-color: white;
            color: black;
        }
        QLabel{
            font-size: 50px;
            font-family: calibri;
            font-weight: bold;
            color: white;
        }
        """)
        self.button1.setObjectName("1")
        self.button2.setObjectName("2")
        self.button3.setObjectName("3")
        self.button4.setObjectName("4")
        self.button5.setObjectName("5")
        self.button6.setObjectName("6")
        self.button7.setObjectName("7")
        self.button8.setObjectName("8")
        self.button9.setObjectName("9")

        self.button1.clicked.connect(self.chose_position_P1)
        self.button2.clicked.connect(self.chose_position_P1)
        self.button3.clicked.connect(self.chose_position_P1)
        self.button4.clicked.connect(self.chose_position_P1)
        self.button5.clicked.connect(self.chose_position_P1)
        self.button6.clicked.connect(self.chose_position_P1)
        self.button7.clicked.connect(self.chose_position_P1)
        self.button8.clicked.connect(self.chose_position_P1)
        self.button9.clicked.connect(self.chose_position_P1)
    def lose_screen(self):
        for button in self.findChildren(QPushButton):
            button.hide()
        self.text.setStyleSheet("font-size: 150px;"
                    "font-family: calibri;"
                    "font-weight: bold;")
        self.text.setText("You lost!")
    def win_screen(self):
        for button in self.findChildren(QPushButton):
            button.hide()
        self.text.setStyleSheet("font-size: 150px;"
                            "font-family: calibri;"
                            "font-weight: bold;")
        self.text.setText("You won!")
    def draw_screen(self):
        for button in self.findChildren(QPushButton):
            button.hide()
        self.text.setStyleSheet("font-size: 150px;"
                            "font-family: calibri;"
                            "font-weight: bold;")
        self.text.setText("Draw!")
    def chose_position_P1(self):
        sender = self.sender()
        sender.setText("X")
        sender.setDisabled(True)
        number = int(sender.objectName())
        used_space(number, 0)
        self.update_moves()
        win_condition = verify_win()
        if win_condition == 1 or win_condition == 2 or self.moves == 9:
            if win_condition == 1:
                self.win_screen()
            elif win_condition == 2:
                self.lose_screen()
            else:
               self.draw_screen()
        else:
            p1, p2 = chose_position(self.moves)
            position_by_Ai = int(p1)*3 + int(p2) + 1
            position_by_Ai = str(position_by_Ai)
            button = self.findChild(QPushButton, f"{position_by_Ai}")
            if button is None:
                print("Did not find the button")
            else:
                button.setText("O")
                button.setDisabled(True)
            win_condition = verify_win()
            if win_condition == 1 or win_condition == 2:
                if win_condition == 1:
                    self.win_screen()
                else:
                    self.lose_screen()
                self.is_running = False
            else:
                self.update_moves()
        

    def update_moves(self):
        self.moves += 1
def used_space(position, AI):
    position-=1
    line = position // 3
    column = position % 3
    if Table[line][column] != " ":
        return True
    else:
        if AI == 0:
           Table[line][column] = "X"
        else: 
           Table[line][column] = "O"
        return False
def show_table():
    for line in Table:
        print(end = "| ")
        for column in line:
            print(column, end = " | ")
        print()
def verify_win():
    for line in Table:
        if line[0] == line[1] == line[2] and line[0] != " ":
            if line[0] == "X":
                #print("You won!")
                return 1
            else:
                #print("You lost!")
                return 2
    for i in range(3):
            if Table[0][i] == Table[1][i] == Table[2][i] and Table[0][i] != " ":
                if Table[0][i] == "X":
                    #print("You won!")
                    return 1
                else:
                    #print("You lost!")
                    return 2
    if Table[0][0] == Table[1][1] == Table[2][2] and Table[0][0] != " ":
        if Table[0][0] == "X":
          #print("You won!")
          return 1
        else:
          #print("You lost!")
          return 2
    if Table[0][2] == Table[1][1] == Table[2][0] and Table[0][2] != " ":
            if Table[0][2] == "X":
              #print("You won!")
              return 1
            else:
              #print("You lost!")
              return 2
    return 0
def score_cnt():
    win = verify_win()
    if win == 2:
        return 10
    elif win == 1:
        return -10
    else:
        return 0
def Find_Best_Move(line, column, moves):
    score = [] 
    if moves % 2 == 1:
        Table[line][column] = "O"
    else:
        Table[line][column] = "X"
    ended = int(score_cnt())
    if ended != 0 or moves == 8:
        Table[line][column] = " "
        return ended
    elif moves % 2 == 1:
        for i in range(3):
            for j in range(3):
                if Table[i][j] == " ":
                    score.append(Find_Best_Move(i,j,moves+1))
        Table[line][column] = " "
        return min(score)
    else:
        for i in range(3):
            for j in range(3):
                if Table[i][j] == " ":
                    score.append(Find_Best_Move(i,j,moves+1))
        Table[line][column] = " "
        return max(score)
    
def chose_position(moves):
    best_pos = -11
    ip = 0
    jp = 0
    for line in range(3):
        for column in range(3):
            if Table[line][column] == " ":
                result = Find_Best_Move(line, column, moves)
                if(best_pos < result):
                    best_pos = result
                    ip = line
                    jp = column
    Table[ip][jp] = "O"
    return ip, jp
    
def main():
    app = QApplication(sys.argv)
    window = X_and_O()
    window.show()
    sys.exit(app.exec_())
#    is_running = True
#    moves = 0
#    while is_running and moves < 9:
#        placed = input("Vhose where you place(1-9):")
#        if not placed.isdigit():
#           print("Your input is invalid")
#            continue
#        placed = int(placed)
#        if placed > 9 or placed < 1 or used_space(placed, 0):
#            print("Invalid number")
#            continue
#        show_table()
#        win_condition = verify_win()
#       moves+=1
#        if win_condition == 1 or win_condition == 2 or moves == 9:
#            if win_condition == 1:
#                print("You Won!")
#           elif win_condition == 2:
#                print("You Lose!")
#            else:
#                print("Draw!")
#            is_running = False
#        else:
#            chose_position(moves)
#            print()
#            show_table()
#            win_condition = verify_win()
#            if win_condition == 1 or win_condition == 2:
#                if win_condition == 1:
#                    print("You Won!")
#                else:
#                    print("You Lose!")
#                is_running = False
#            else:
#                moves+=1


if __name__ == "__main__":
    main()