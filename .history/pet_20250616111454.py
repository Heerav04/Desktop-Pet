import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class VirtualPet(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        # Set pet image (PNG with transparency or animated GIF)
        self.movie = QtGui.QMovie("Dog.gif")
        self.setMovie(self.movie)
        self.movie.start()
  # Replace with your image file

        # Remove window borders
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | 
                            QtCore.Qt.WindowStaysOnTopHint | 
                            QtCore.Qt.Tool)

        # Make background transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Enable click + drag to move pet
        self.offset = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None:
            self.move(self.pos() + event.pos() - self.offset)

    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu(self)

        feed_action = menu.addAction("🐾 Feed")
        pet_action = menu.addAction("❤️ Pet")
        quit_action = menu.addAction("❌ Quit")

        action = menu.exec_(event.globalPos())

        if action == feed_action:
            print("You fed the pet!")
        elif action == pet_action:
            print("You pet the doggo!")
        elif action == quit_action:
            QtWidgets.qApp.quit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    pet = VirtualPet()
    pet.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
