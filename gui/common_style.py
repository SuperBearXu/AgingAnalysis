from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

from utils.my_utils import get_icon

font_15_family = QtGui.QFont()
font_15_family.setFamily("等线")
font_15_family.setPixelSize(15)

font_16_family = QtGui.QFont()
font_16_family.setFamily("等线")
font_16_family.setPixelSize(16)


def set_window_icon(ui_object):
    ui_object.setWindowIcon(QIcon(get_icon()))
