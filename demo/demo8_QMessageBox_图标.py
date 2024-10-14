#面向对象方法
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox   #窗口组件
from PyQt5.QtWidgets import QDesktopWidget              #提供桌面窗口信息
from PyQt5.QtGui import QIcon, QFont                    #图标组件，提示框
from PyQt5.QtCore import QCoreApplication

class Example(QWidget): #创建一个新类叫做Example，Example类继承自QWidget类。QWidget组件(类)是PyQt5中所有用户界面类的基础类。

    def __init__(self):
        super().__init__()  #super()使得Example可以使用其父类QWidget的方法
        self.initUI()

    '''界面主体'''
    def initUI(self):#initUI()中的下述方法(如'.setblabla')都继承自QWidgets类。

        QToolTip.setFont(QFont('SansSerif',8))#这句管理了所有的提示框。静态方法设置了提示框字体的格式，8px大小的SansSerif字体
        self.setToolTip('This is a <b>QWidget</b> widget')#调用setToolTip方法创建提示框，提交给了self对象。提示框中可以使用富文本格式

        #self.setGeometry(300,300,800,540)#在屏幕上显示窗口，并设置其尺寸。前两个参数设定位置，后两个设定宽高。相当于是'.resize()'+'.move()'。
        '''
        这里的'.setGeometry()'方法,不能让窗口居中显示，因为它需要具体的数值。
        我们可以使用下面的'.resize()'与'.center()'方法来实现修改窗口尺寸和居中显示。
        '''
        self.resize(800,540)
        self.center()

        self.setWindowTitle('Ubuntu')#标题
        self.setWindowIcon(QIcon('linuxcartoon.jpg'))#QIcon对象接收图片。

        btn = QPushButton(QIcon('linuxcartoon.jpg'),'A Linux',self)#创建一个按钮组件btn，可以指定图标、文本和父对象
        btn.setToolTip('This is a <b>QPushButton</b> widget')#给btn设置一个提示框，富文本<b>指加粗。
        btn.resize(btn.sizeHint())#改变btn的大小，'.sizeHint()'返回了一个系统推荐值
        btn.move(50,50)
        btn.clicked.connect(self.msg)#链接按钮触发事件msg

        qbtn = QPushButton('Quit',self)#第二个参数是父组件。父组件是Example组件，它继承了QWiget类。
        qbtn.setToolTip('It\'s a button that means <b>quitting</b> this Ubuntu window')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200,50)

        self.show()


    '''窗口位置方法'''
    def center(self):
        qr = self.frameGeometry()#这里我们获得一个主窗口轮廓的几何图形。
        '''
        一些补充:
        geometry.width()：客户区的宽度，客户区：不包括标题栏、边框
        geometry.height()：客户区的高度
        frameGeometry.x()：窗口轮廓整个框架左上角的坐标x，整个框架：包括边框和标题栏
        frameGeometry.y()：窗口轮廓整个框架左上角的坐标y
        frameGeometry.width()：窗口全框架宽度
        frameGeometry.height()：窗口全框架高度

        '''
        cp = QDesktopWidget().availableGeometry().center()
        #QDesktopWidget()获取桌面框架，'.availableGeometry()'获得相对于显示器的绝对值，'.center()'获取屏幕中心点。
        qr.moveCenter(cp)#把qr轮廓框架的中心点移动到cp点(桌面屏幕中心点)
        self.move(qr.topLeft())#把self窗口(左上角)移动到qr的topLeft左上角，实现重合。'.move()'方法默认以左上角为基点移动。
        #self.move(qr.x(),qr.y())这一句和上一句相同效果，'x(),y()'指左上角的坐标。


    '''按键方法'''
    def msg(self):
        reply = QMessageBox.information(self,'Linux',"An operating system. ", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)

    def about(self):#QMessageBox.about消息框只有一个按键'OK'，'.about'所需参数是(QWidget, str, str)，图标是本身这个btn按键的图标。
        reply = QMessageBox.about(self,'About Linux',"Something about Linux. ")

    def closeEvent(self, event):    #当我们关闭一个QWidget，QCloseEvent类事件将会生成。如果要实现关闭前的动作，我们需要修改closeEvent()方法。
        reply = QMessageBox.question(self,'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#最后一个参数QMessageBox.No指跳出qusetion框后默认选择No
        #QMessageBox::Information、Warning、Critical、Question四种消息框自带图标。若想它们中自定义Icon，只能重写QMessageBox方法，见文末。
        if reply == QMessageBox.Yes:
            event.accept()      #这里是值，点下右上角的X之后，"关闭Widget"就成了方法参数中的event。
        else:                   #在这里进行一次question的选择，并把选择结果赋值给reply。如果reply为Yes则event.accept()运行，反之就ignore这个event。
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)#所有的PyQt5应用必须创建一个应用(Application)对象。sys.argv参数是一个来自命令行的参数列表。

    ex = Example()#需要ex来实例化，使用上面的函数
    sys.exit(app.exec_())
    '''
    app.exec_()使得程序可以一直循环运行，直到主窗口被关闭或被终止进程（如果没有这句话，程序运行时会一闪而过）
    主循环将在下面两种情况下退出:(1)调用exit()方法,(2)主widget组件被销毁。
    sys.exit()可以做到退出时系统不留垃圾，且系统环境将会被通知应用是怎样被结束的。
    exec_()方法有一个下划线，是因为exec是Python保留的关键字，所以用exec_()来代替。
    '''



    #未完成
    '''@@@尝试写一个继承了QMessageBox的方法，使它能自定义图标
    class QMessageBox_question(QMessageBox):
        def __init__(self):
            super().__init__()
            self.AddIcon()
        def AddIcon():

    当QMessageBox中的元素不能够满足需求时，可以有两种方法。
    1）声明一个类，从QMessageBox继承而来。然后在其中添加绘制等操作。详见网上另一篇博客:https://www.xuebuyuan.com/896335.html
    2）自定义一个类，其中包含对QMessageBox的更丰富操作:https://blog.csdn.net/liang19890820/article/details/50586031
    '''