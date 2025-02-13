import sys  
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit  

class MainWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.setMouseTracking(True)  
        self.label = QLabel("Click in this window")  
        self.label.setMouseTracking(True)  
        self.setCentralWidget(self.label)  

    def mouseMoveEvent(self, e):  
        self.label.setText("mouseMoveEvent")  

    def mousePressEvent(self, e):  
        self.label.setText("mousePressEvent")  

    def mouseReleaseEvent(self, e):  
        self.label.setText("mouseReleaseEvent") 
 
    def mouseDoubleClickEvent(self, e):  
        self.label.setText("mouseDoubleClickEvent")  

app = QApplication(sys.argv)  
window = MainWindow()  
window.show()  
app.exec()