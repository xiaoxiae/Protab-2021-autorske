from subprocess import *

for i in range(2, 1001):
    Popen(["tar", "xf", "heslo.tar.gz"]).communicate()
