import os
import shutil

from PyInstaller.__main__ import run

from main import VERSION

script_name = 'main.py'
output_name = VERSION
icon_name = "my_icon.ico"

options = [
    '--onefile',  # Create a single executable file
    '--noconsole',  # Do not open a console window
    f'--icon={icon_name}',
    r'--add-data=D:\scrapy\project\py_study\AgingAnalysis\my_icon.ico;.',
    f'--name={output_name}',  # Specify the output file name
]

run([script_name] + options)
