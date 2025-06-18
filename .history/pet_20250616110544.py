import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class VirtualPet(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        # Set pet image (PNG with transparency or animated GIF)
        self.setPixmap(QtGui.QPixmap("Dog.gif"))  # Replace with your image file

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

def main():
    app = QtWidgets.QApplication(sys.argv)
    pet = VirtualPet()
    pet.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
