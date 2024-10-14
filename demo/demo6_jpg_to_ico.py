from PIL import Image


def png_to_ico(png_path, ico_path, sizes=[(64, 64), (128, 128), (256, 256)]):
    """
    将PNG图片转换为ICO格式
    :param png_path: 图片路径
    :param ico_path: 输出ICO图片路径
    :param sizes: ICO文件中包含的图标尺寸列表
    """
    # 打开PNG图片
    img = Image.open(png_path)

    # 保存为ICO文件
    img.save(ico_path, format='ICO', sizes=sizes)


png_path = 'D:\scrapy\project\py_study\AgingAnalysis\icon.jpg'  # 图片路径
ico_path = '../my_icon.ico'  # 保存的ICO图片路径

png_to_ico(png_path, ico_path)
