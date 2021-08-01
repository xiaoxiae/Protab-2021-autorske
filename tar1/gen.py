from subprocess import *

for i in range(2, 1000):
    Popen(["tar", "cfz", "tmp.tar.gz", "heslo.tar.gz"]).communicate()
    Popen(["rm", "heslo.tar.gz"]).communicate()
    Popen(["mv", "tmp.tar.gz", "heslo.tar.gz"]).communicate()
