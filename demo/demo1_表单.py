import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLineEdit, QLabel, \
    QHBoxLayout, QComboBox
from PyQt5.QtGui import QFont


class AddDataDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.input_boxes = []  # 用于存储输入框对
        self.add_combo_box()  # 初始化时添加下拉框
        self.add_input_boxes()  # 初始化时添加一对输入框

        self.add_button = QPushButton("添加输入框对")
        self.add_button.clicked.connect(self.add_input_boxes)

        # 设置按钮字体大小
        font = QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)

        self.save_button = QPushButton("保存")
        self.save_button.setFont(font)  # 设置保存按钮的字体大小
        self.save_button.clicked.connect(self.save_inputs)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

    def add_combo_box(self):
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["选项1", "选项2", "选项3"])  # 添加选项

        # 创建水平布局，将下拉框放在第一行
        h_layout = QHBoxLayout()

        # 设置标签和下拉框的字体大小
        label = QLabel("选择一个选项:")
        font = QFont()
        font.setPointSize(12)
        label.setFont(font)
        self.combo_box.setFont(font)

        # 设置间距
        h_layout.setSpacing(5)  # 减少 QLabel 和 QComboBox 之间的间距

        h_layout.addWidget(label)
        h_layout.addWidget(self.combo_box)

        self.layout.addLayout(h_layout)  # 将下拉框布局添加到主布局

    def add_input_boxes(self):
        input_box1 = QLineEdit(self)
        input_box2 = QLineEdit(self)
        label1 = QLabel(f"输入框 {len(self.input_boxes) + 1}a:")
        label2 = QLabel(f"输入框 {len(self.input_boxes) + 1}b:")

        # 设置字体大小
        font = QFont()
        font.setPointSize(12)
        input_box1.setFont(font)
        input_box2.setFont(font)
        label1.setFont(font)
        label2.setFont(font)

        # 创建水平布局，将两个输入框和标签放在同一行
        h_layout = QHBoxLayout()
        h_layout.addWidget(label1)
        h_layout.addWidget(input_box1)
        h_layout.addWidget(label2)
        h_layout.addWidget(input_box2)

        # 将新行插入到下拉框和最后一个输入框之间
        if self.input_boxes:
            self.layout.insertLayout(len(self.input_boxes) + 1, h_layout)  # 在最后一个输入框后插入新行
        else:
            self.layout.addLayout(h_layout)  # 如果没有输入框，直接添加
        self.input_boxes.append((input_box1, input_box2))  # 添加输入框对到列表中

    def save_inputs(self):
        inputs = [(input_box1.text(), input_box2.text()) for input_box1, input_box2 in self.input_boxes]
        selected_option = self.combo_box.currentText()  # 获取选中的选项
        print("选择的选项:", selected_option)
        print("输入内容:", inputs)  # 输出所有输入的内容
        self.close()  # 关闭对话框


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")

        self.button = QPushButton("打开弹窗", self)
        self.button.clicked.connect(self.open_dialog)
        self.setCentralWidget(self.button)

    def open_dialog(self):
        dialog = AddDataDialog()
        dialog.exec_()  # 显示对话框并阻塞，直到关闭


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
