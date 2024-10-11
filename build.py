import os
import shutil

from PyInstaller.__main__ import run

from main import VERSION

script_name = 'main.py'
output_name = VERSION

options = [
    '--onefile',  # Create a single executable file
    '--noconsole',  # Do not open a console window
    f'--name={output_name}',  # Specify the output file name
]

run([script_name] + options)
