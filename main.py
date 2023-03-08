from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
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

main2()
    
    