import sys
import os
import zipfile
import shutil

from cx_Freeze import setup, Executable

sys.argv = ["build.py", "build"]

build_exe_options = {"packages":["pygame", "keyshift"],
                     #"include_files":includefiles,
                     "excludes":["tkinter", "ctypes", "distutils", "email", "html", "http", "json", "logging", "multiprocessing", "test", "unittest", "urllib", "xml", "xmlrpc"],
                     "icon":"keyshift.ico",
                     "optimize":2,
                     "init_script":os.path.abspath("Console.py"),
                     "silent":True,}

base = "console"

setup(  name = "Keyshift",
        version = "0.1",
        description = "KEYSHIFT",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py",
                                  base=base,
                                  targetName="keyshift.exe")])

os.mkdir("./build/exe.win-amd64-3.4/lib")

for file in os.listdir("bundle"):
    shutil.copy(os.path.join("bundle", file), './build/exe.win-amd64-3.4')

keep_with_exe = ["python34.dll", "libvorbis.dll", "libvorbisfile.dll", "libogg.dll"]

for file in os.listdir("./build/exe.win-amd64-3.4/"):
    if ".pyd" in file:
        shutil.move(os.path.join("./build/exe.win-amd64-3.4/", file), os.path.join("./build/exe.win-amd64-3.4/lib/", file))

    if ".dll" in file and not file in keep_with_exe:
        shutil.move(os.path.join("./build/exe.win-amd64-3.4/", file), os.path.join("./build/exe.win-amd64-3.4/lib/", file))

shutil.copy("./resource.zip", "./build/exe.win-amd64-3.4/resource.zip")
