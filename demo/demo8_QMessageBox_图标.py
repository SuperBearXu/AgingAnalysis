import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt


class ColorBlinkingLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('Hello, World!', self)
        self.label.setAlignment(Qt.AlignCenter)

        # 初始化颜色列表
        self.colors = ['red', 'blue', 'green', 'yellow']
        self.color_index = 0

        # 设置定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.changeColor)
        self.timer.start(500)  # 每500毫秒改变一次颜色

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def changeColor(self):
        # 更改 QLabel 的样式表来改变颜色
        self.label.setStyleSheet(f"QLabel {{ color: {self.colors[self.color_index % len(self.colors)]}; }}")
        self.color_index += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorBlinkingLabel()
    ex.show()
    sys.exit(app.exec_())
