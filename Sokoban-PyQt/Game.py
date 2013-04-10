import sys, pickle, random
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

CONST_PIC_PXL = 32
SCENE_DELAY_TIME = 100

UP = Qt.Key_Up
DOWN = Qt.Key_Down
RIGHT = Qt.Key_Right
LEFT = Qt.Key_Left

class SokoScene(QtGui.QGraphicsScene):
    def __init__(self,view,moveLabel,leftLabel):
        super(SokoScene, self).__init__()
        self.lvl_is_loaded = False
        self.auto_play = False
        self.view = view
        self.moves = []
        self.moveLabel = moveLabel
        self.leftLabel = leftLabel

    def LoadLevel(self,level): ## load the selected level
        self.clear()
        self.moveLabel.setNum(0)
        self.lvl_on_scene = level
        self.moves = []
        lrows = level.split("\n")
        lrows.remove("")
        self.boxes = []
        self.humanPos = []
        self.boxesPos = []
        self.key_pressed = False
        self.dude = QGraphicsPixmapItem(QPixmap("Sprites/guy.png"))
        for rowind,row in enumerate(lrows):
            for boxind,box in enumerate(row):
                if box in ("#"):
                    this = QGraphicsPixmapItem(QPixmap("Sprites/wall.png"))
                    this.moveBy(boxind*CONST_PIC_PXL,rowind*CONST_PIC_PXL)
                    this.setData(0,"wall")
                    self.addItem(this)
                elif box in ("B","$"):
                    this = QGraphicsPixmapItem(QPixmap("Sprites/block.png"))
                    this.moveBy(boxind*CONST_PIC_PXL,rowind*CONST_PIC_PXL)
                    this.setData(0,"box")
                    self.boxes.append(this)
                    self.addItem(this)
                    self.boxesPos.append([boxind, rowind])
                elif box in ("H","@","+"):
                    self.dude.moveBy(boxind*CONST_PIC_PXL,rowind*CONST_PIC_PXL)
                    self.dude.setData(0,"human")
                    self.addItem(self.dude)
                    self.humanPos.append([boxind, rowind])
                elif box in ("P","."):
                    this = QGraphicsPixmapItem(QPixmap("Sprites/place.png"))
                    this.moveBy(boxind*CONST_PIC_PXL,rowind*CONST_PIC_PXL)
                    this.setData(0,"place")
                    this.setZValue(-1)
                    self.addItem(this)
        self.lvl_is_loaded = True
        self.leftLabel.setNum(len(self.boxes))
        self.setSceneRect(0,0,max(list(map(len,lrows)))*CONST_PIC_PXL,len(lrows)*CONST_PIC_PXL)
        self.update()

    def walk(self,obj,keycode,flashback=False): ## move the human
        if keycode == LEFT:
            obj.moveBy(-32,0)

        elif keycode == RIGHT:
            obj.moveBy(32,0)

        elif keycode == DOWN:
            obj.moveBy(0,32)

        elif keycode == UP:
            obj.moveBy(0,-32)

        if flashback:
            self.moves.pop(-1)
        else:
            if obj.data(0) == "human":
                self.moves.append(keycode)
            else:
                self.moves.append("B")

    def keyPressEvent(self,key): ## when a key is pressed
        if (not self.auto_play) and self.lvl_is_loaded:
            self.key_pressed = True
            if key.key() == Qt.Key_F5:
                self.resetLevel()
            elif self.moves and key.key() == Qt.Key_Z:
                self.undoMove()
            elif key.key() in (UP, DOWN, RIGHT, LEFT):
                self.moveHuman(key.key())

    def moveHuman(self, key):
        self.walk(self.dude, key)
        if self.checkGuy(key):
            self.moveLabel.setNum(int(self.moveLabel.text())+1)
        self.update

    def autoMove(self):
        if self.autoMoveMode == "Static":
            if self.autoMoveList != []:
                self.moveHuman(self.autoMoveList[0])
                del self.autoMoveList[0]
                QTimer.singleShot(SCENE_DELAY_TIME, self.autoMove)
            else:
                self.auto_play = False
        elif self.autoMoveMode == "Random":
            if int(self.moveLabel.text()) < 1000:
                self.moveHuman(random.choice([UP, DOWN, RIGHT, LEFT]))
                QTimer.singleShot(SCENE_DELAY_TIME, self.autoMove)
            else:
                self.auto_play = False
        elif self.autoMoveMode == "DFS":
            pass

    def resetLevel(self):
        self.LoadLevel(self.lvl_on_scene)

    def checkGuy(self,key): ## check and move the human
        colly = self.dude.collidingItems()
        plus = -2 if key>=RIGHT else 2
        if colly:
            if colly[0].data(0) == "wall":
                self.walk(self.dude, key+plus,True)
                return False
            elif colly[0].data(0) == "box":
                self.walk(colly[0], key)
                if colly[0].collidingItems():
                    if colly[0].collidingItems()[0].data(0) in ("wall","box"):

                        self.walk(self.dude, key+plus,True)

                        self.walk(colly[0], key+plus,True)
                        return False
                self.checkBoxes()
        return True

    def undoMove(self):
        if self.lvl_is_loaded and self.moves:
            box = False
            last_move = self.moves[-1]
            if last_move=="B":
                box = True
                last_move = self.moves[-2]
            plus = -2 if last_move>=RIGHT else 2
            self.walk(self.dude, last_move)

            if self.dude.collidingItems() and box:
                if self.dude.collidingItems()[0].data(0)=="box":
                    self.walk(self.dude.collidingItems()[0],last_move+plus,True)

            for _ in range(2):
                self.walk(self.dude,last_move+plus,True)
            self.moveLabel.setNum(int(self.moveLabel.text())-1)
            self.checkBoxes()
            self.update()

    def checkBoxes(self): ## ending game check
        left = 0
        check = True
        for box in self.boxes:
            collybox = box.collidingItems()
            if not collybox:
                check = False
                left+=1
        self.leftLabel.setNum(left)
        if check:
            self.clear()
            winrar = QGraphicsPixmapItem(QPixmap("Sprites/winrar.png"))
            self.lvl_is_loaded = False
            self.addItem(winrar)
            self.setSceneRect(0,0,0,0)
            self.update()

    def autoPlay(self, algorithm, level):
        if self.lvl_is_loaded and not self.key_pressed:
            self.auto_play = True
            self.autoMoveMode = algorithm
            if algorithm == "Static":
                self.autoMoveList = { \
                        "1": [],
                        "2": \
                    [ UP, UP, RIGHT, RIGHT, RIGHT, DOWN, DOWN,\
                      UP, UP, RIGHT, RIGHT, DOWN,\
                      RIGHT, RIGHT, UP, LEFT, LEFT, LEFT, LEFT,
                      DOWN, DOWN, RIGHT, RIGHT, UP, RIGHT, DOWN],
                        "3": []
                    }[level]
                if self.autoMoveList != []:
                    QTimer.singleShot(SCENE_DELAY_TIME, self.autoMove)
            else:
                QTimer.singleShot(SCENE_DELAY_TIME, self.autoMove)

class SokoGame(QtGui.QWidget): ##load GUI file from Forms/GameWindow.ui
    def __init__(self):
        super(SokoGame, self).__init__()
        uic.loadUi("Forms/GameWindow.ui", self)
        self.SokoScene = SokoScene(self.SokoView,self.moveCount,self.leftCount)
        self.SokoScene.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap('Sprites/floor.png')))
        self.SokoView.setScene(self.SokoScene)
        self.SokoView.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform | QtGui.QPainter.HighQualityAntialiasing)
        self.ExitButton.clicked.connect(sys.exit)
        self.APButton.clicked.connect(lambda: self.SokoScene.autoPlay(self.APBox.currentText(), self.ChooseBox.currentText()))
        self.undoButton.clicked.connect(self.SokoScene.undoMove)
        self.LoadButton.clicked.connect(lambda: self.SokoScene.LoadLevel(self.levels[self.ChooseBox.currentText()]))
        self.resetButton.clicked.connect(self.SokoScene.resetLevel)
        self.levels = pickle.load(open("level.dat","rb"))
        self.level_no = list(self.levels.keys())
        self.LoadBasics()


    def LoadBasics(self): ##load ComboBoxes
        self.ChooseBox.clear()
        self.level_no.sort()
        self.ChooseBox.addItems(self.level_no)
        self.APBox.addItems(["Static", "Random", "DFS"])

def main():
    app = QtGui.QApplication(sys.argv)
    ui = SokoGame()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    main()
