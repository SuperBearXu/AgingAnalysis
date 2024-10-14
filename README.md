accounts receivable aging schedule 应收账款账龄分析表

有借必有贷，借贷必相等

借方英文简写为“Dr”（Debit），贷方英文简写为“Cr”（Credit）

##### **台式机与笔记本打包后pyqt界面显示差距大：**

1、调整笔记本电脑缩放，一般笔记本的显示缩放都大于100%，可以调整到100%<br>
2、pytq程序中将设置字体的函数 setPointSize 改成 setPixelSize <br>
**注：setPixelSize(x)设置的字体会比setPointSize(x)小一些, 一般将原来的大小+4即可。如原来是setPointSize(10),可以设置为setPixelSize(14)**<br>
[参考链接](https://blog.csdn.net/jay2014dy/article/details/103525310)

##### **打包成exe文件添加图标：**
1、准备一个图片，无论是什么格式<br>
2、demo6_jpg_to_ico.py 下将第一步准备的图片生成我们需要的.ico格式的图片<br>
3、get_icon_base64.py 下将第二步生成的图片转换成base64格式的字符串放入my_icon.py文件中<br>
4、get_icon() 把.ico图标生成的base64格式的字符串转成pixmap格式<br>
5、在pyqt界面中添加pixmap格式的数据，MainWindow.setWindowIcon(QIcon(get_icon())) <br>
6、build.py 添加相关代码
````
f'--icon={icon_name}',
'--add-data=D:\xxx\xxx\xxx\xxx\my_icon.ico;.',
````