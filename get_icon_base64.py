import base64

from global_setting import GS

img_path = f'{GS.current_path}\\my_icon.ico'

with open(img_path, 'rb') as icon:
    icon_str = base64.b64encode(icon.read())
    icon_bytes = 'icon_bytes = ' + str(icon_str)
with open('my_icon.py', 'w+') as my_icon_py:
    my_icon_py.write(icon_bytes)
