# main.py - Punto de entrada del software de control MikroPrinter
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class MikroPrinterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MikroPrinter Control")
        self.setGeometry(200, 200, 400, 300)  # Tamaño de la ventana
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Estado: Desconectado", self)
        layout.addWidget(self.label)
        
        self.connect_btn = QPushButton("Conectar a la impresora", self)
        self.connect_btn.clicked.connect(self.connect_printer)
        layout.addWidget(self.connect_btn)
        
        self.setLayout(layout)

    def connect_printer(self):
        self.label.setText("Estado: Conectado ✅")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MikroPrinterApp()
    ventana.show()
    sys.exit(app.exec())
