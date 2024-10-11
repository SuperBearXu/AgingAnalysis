from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLineEdit, QLabel, \
    QHBoxLayout, QComboBox, QMessageBox
from PyQt5.QtGui import QFont

from global_setting import GS
from utils.my_logger import my_logger as logger

global_temp_data = []


class AddDataDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("添加借贷数据")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.layout = QVBoxLayout()

        self.input_boxes = []  # 用于存储输入框对
        self.add_combo_box()  # 初始化时添加下拉框
        self.add_origin_input()
        self.add_input_boxes()  # 初始化时添加一对输入框

        self.add_button = QPushButton("新增借贷")
        self.add_button.clicked.connect(self.add_input_boxes)

        # 设置按钮字体大小
        font = QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)

        self.save_button = QPushButton("保存")
        self.save_button.setFont(font)  # 设置保存按钮的字体大小
        self.save_button.clicked.connect(self.save_inputs)

        self.clear_button = QPushButton("清空输入")
        self.clear_button.setFont(font)  # 设置清空按钮的字体大小
        self.clear_button.clicked.connect(self.clear_inputs)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.clear_button)
        self.setLayout(self.layout)

    def add_combo_box(self):
        self.combo_box = QComboBox(self)
        list_enterprise = GS.config.get_config_options("企业列表")
        self.combo_box.addItems(list_enterprise)  # 添加选项

        # 创建水平布局，将下拉框放在第一行
        h_layout = QHBoxLayout()

        # 设置标签和下拉框的字体大小
        label = QLabel("选择企业:")
        font = QFont()
        font.setPointSize(12)
        label.setFont(font)
        self.combo_box.setFont(font)

        h_layout.addWidget(label)
        h_layout.addWidget(self.combo_box)

        self.layout.addLayout(h_layout)  # 将下拉框布局添加到主布局

    def add_origin_input(self):
        label_origin = QLabel("输入初始值:")
        font = QFont()
        font.setPointSize(12)
        label_origin.setFont(font)  # 设置标签字体大小

        self.input_origin = QLineEdit(self)
        self.input_origin.setFont(font)  # 设置字体大小

        # 创建水平布局，将标签和输入框放在同一行
        h_layout = QHBoxLayout()
        h_layout.addWidget(label_origin)
        h_layout.addWidget(self.input_origin)

        self.layout.addLayout(h_layout)  # 将 QLineEdit 和标签的布局添加到主布局

    def add_input_boxes(self):
        input_debit = QLineEdit(self)
        input_credit = QLineEdit(self)
        label_debit = QLabel(f"第{len(self.input_boxes) + 1}年 借方:")
        label_credit = QLabel(f" 贷方:")

        # 设置字体大小
        font = QFont()
        font.setPointSize(12)
        input_debit.setFont(font)
        input_credit.setFont(font)
        label_debit.setFont(font)
        label_credit.setFont(font)

        # 创建水平布局，将两个输入框和标签放在同一行
        h_layout = QHBoxLayout()
        h_layout.addWidget(label_debit)
        h_layout.addWidget(input_debit)
        h_layout.addWidget(label_credit)
        h_layout.addWidget(input_credit)

        # 将新行插入到下拉框和最后一个输入框之间
        if self.input_boxes:
            self.layout.insertLayout(len(self.input_boxes) + 2, h_layout)  # 在最后一个输入框后插入新行
        else:
            self.layout.addLayout(h_layout)  # 如果没有输入框，直接添加
        self.input_boxes.append((input_debit, input_credit))  # 添加输入框对到列表中

    def save_inputs(self):
        inputs = []
        for input_debit, input_credit in self.input_boxes:
            debit = input_debit.text().strip() or "0"  # 若为空，则默认赋值为 "0"
            credit = input_credit.text().strip() or "0"
            # 如果借方和贷方都为空或为 "0"，则跳过这对输入
            if debit == "0" and credit == "0":
                continue
            inputs.append((debit, credit))
        selected_enterprise = self.combo_box.currentText()  # 获取选中的企业
        if selected_enterprise == "":
            QMessageBox.warning(self, "警告", "请选择企业")
            return
        origin_value = self.input_origin.text()
        if origin_value == "":
            QMessageBox.warning(self, "警告", "请输入初始值")
            return
        if all(debit == "" and credit == "" for debit, credit in inputs):
            QMessageBox.warning(self, "警告", "请至少输入一对有效的借贷数据。")
            return
        # 将数据存储到全局临时数据中
        temp_data = {"企业": selected_enterprise, "初始值": origin_value, "借贷": inputs}
        global_temp_data.append(temp_data)
        # 日志记录，包含添加的企业名称和其输入的数据
        logger.info(f"{selected_enterprise} 借贷数据添加完成！ 初始值: {origin_value} 数据: {inputs}")
        self.close()  # 关闭对话框

    def clear_inputs(self):
        for input_box1, input_box2 in self.input_boxes:
            input_box1.clear()
            input_box2.clear()
        self.input_origin.clear()  # 清空额外信息输入框
        self.combo_box.setCurrentIndex(0)  # 选择第一个选项
