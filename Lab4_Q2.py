import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound

class Aniumation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.frame_no = 0
        self.images = [
            QPixmap("images/frame-"+str(i+1)+".png")
            #print("images/frame-"+str(i+1)+".png")
            for i in range(20)
        ]
        self.play_pause = 0
        timer = QTimer(self)
        timer.timeout.connect(self.update_value)
        timer.start(50)

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0,0,320,320),self.images[self.frame_no])
        p.end()

    def update_value(self):
        self.frame_no += self.play_pause
        if self.frame_no >= 20:
            self.frame_no = 0
            QSound.play("sounds/rabbit_jump.wav")

        #self.update()
    
    def toggle(self):
        if(self.play_pause == 0):
            self.play_pause = 1
        else :
            self.play_pause = 0

class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.anim_area = Aniumation_area()
        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        self.button = QPushButton("Pause")
        self.button.clicked.connect(self.play_pause)
        layout.addWidget(self.button)
        #print(self.button.text())
        #if(self.button.text() ==)

        self.setLayout(layout)
        self.setMinimumSize(330,400)            

    def play_pause(self):
        if(self.button.text() == "pause"):
            self.button.setText("play")
            self.anim_area.toggle()
        else:
            self.button.setText("pause")
            self.anim_area.toggle()

def main():
    app = QApplication(sys.argv)
    w= Simple_animation_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
#should have this 