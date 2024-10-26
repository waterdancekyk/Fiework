import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QPoint
from PyQt5.QtGui import QColor, QPainter, QBrush, QFont

class Fireworks(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Салют')
        self.setGeometry(100, 100, 800, 600)
        self.color = []
        self.size = []
        self.fireworks_positions = []
        
        # Настройка текста
        self.text_label = QLabel('Я иду на практику! Долой пары с Меренковым', self)
        self.text_label.setFont(QFont('Arial', 14))
        
        # Настройка кнопки
        self.button = QPushButton('Нажми меня!', self)
        self.button.setGeometry(350, 500, 100, 50)
        self.button.setEnabled(False)  # Изначально кнопка выключена

        # Запускаем таймеры
        self.fireworks_timer = QTimer(self)
        self.fireworks_timer.timeout.connect(self.add_firework)
        self.fireworks_timer.start(1000) 
        
        self.text_timer = QTimer(self)
        self.text_timer.timeout.connect(self.move_text)
        self.text_timer.start(50)  # перемещение текста каждые 50 мс

        # Включаем кнопку через 5 секунд
        QTimer.singleShot(5000, self.enable_button)

    def enable_button(self):
        self.button.setEnabled(True)

    def add_firework(self):
        # Генерация случайного цвета и размера фейерверка
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        size = random.randint(10, 50)
        x = random.randint(0, self.width() - size)
        y = random.randint(0, self.height() - size)
        self.color.append(color)
        self.size.append(size)
        self.fireworks_positions.append((x, y))
        self.update()  # Обновляем окно для перерисовки

    def move_text(self):
        x = random.randint(0, self.width() - self.text_label.width())
        y = random.randint(0, self.height() - self.text_label.height())
        self.text_label.move(x, y)

    def paintEvent(self, event):
        painter = QPainter(self)
        for i in range(len(self.fireworks_positions)):
            painter.setBrush(QBrush(self.color[i]))
            painter.drawEllipse(QPoint(*self.fireworks_positions[i]), self.size[i], self.size[i])

    def mousePressEvent(self, event):
        # Эффект BSOD при нажатии кнопки
        if self.button.rect().contains(event.pos()):
            self.show_bsod()

    def show_bsod(self):
        self.setStyleSheet("background-color: blue;")
        self.button.setEnabled(False)  # Отключаем кнопку
        self.text_label.hide()  # Скрываем текст
        bsod_label = QLabel(self)
        bsod_label.setText('Синяя заставка смерти (BSOD)')
        bsod_label.setFont(QFont('Arial', 24))
        bsod_label.setStyleSheet("color: white;")
        bsod_label.setGeometry(200, 250, 400, 100)
        bsod_label.setAlignment(Qt.AlignCenter)
        bsod_label.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fireworks = Fireworks()
    fireworks.show()
    sys.exit(app.exec_())