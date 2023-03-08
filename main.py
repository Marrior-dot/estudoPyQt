from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QtWidge
import sys


#primeira aula(dimensões e titulo)
def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(0,0,300,300)
    window.setWindowTitle("titulo")
    window.show()
    sys.exit(app.exec())
    #pass

#main()
#print(sys.argv)

#segunda aula: label, botão, funções para o botão
def on_click():
    print("Pressionado")

def main2():
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    window.setGeometry(0,0,300,300)
    window.setWindowTitle("titulo")
    
    text = QLabel(window)
    text.setText("Primeiro texto")
    text.move(100,50)
    
    btn = QPushButton(window)
    btn.setText("Clique-me")
    btn.move(50,50)
    btn.clicked.connect(on_click)
    
    window.show()
    sys.exit(app.exec())
    #pass

#main2()

#aula3: orientação a objetos

class Ui_mainWindow(QMainWindow):
    def __init__(self):
        super(Ui_mainWindow, self).__init__()
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Janela de orientação a objeto")
        
        self.setUpUi()
    
    def setUpUi(self):
        text = QLabel(self)
        self.text.setText("Primeiro código")
        self.text.move(100,100)
        
        self.btn2 = QPushButton(self)
        self.btn2.setText("me cliqueeeeeee")
        self.btn2.clicked.connect(self.onClick)
    
    def onClick(self):
        print("Pressionado")
        self.text.setText("Primeiro código")

        

        
        
    

def on_click():
    print("Pressionado")

def main2():
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    window.setGeometry(0,0,300,300)
    window.setWindowTitle("titulo")
    
    text = QLabel(window)
    text.setText("Primeiro texto")
    text.move(100,50)
    
    btn = QPushButton(window)
    btn.setText("Clique-me")
    btn.move(50,50)
    btn.clicked.connect(on_click)
    
    window.show()
    sys.exit(app.exec())
    #pass
    
    