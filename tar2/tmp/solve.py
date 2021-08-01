from random import *
from string import *
from subprocess import *
import os

while [file for file in os.listdir() if file.endswith(".tar.gz")]:
    for file in os.listdir():
        if file.endswith(".tar.gz"):
            Popen(["tar", "xf", file]).communicate()
            Popen(["rm", file]).communicate()
