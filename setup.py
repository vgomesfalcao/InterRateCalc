import sys
from cx_Freeze import setup, Executable
import yaml


executables = [
        Executable("main.py", base=None)
]

buildOptions = dict(
        packages = [],
        includes = ['yaml'],
        include_files = ['./db/dados.bin','setup.py'],
        excludes = ['desktop.ini']
)

setup(
    name = "Taxas Cartões",
    version = "1.0",
    description = "Descrição do programa",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
