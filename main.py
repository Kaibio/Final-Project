import sys
from PyQt6 import QtWidgets
from scores import ScoresAll

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ScoresAll()
    window.show()
    sys.exit(app.exec())
