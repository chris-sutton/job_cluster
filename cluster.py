#!/usr/bin/python3
import subprocess
import shlex

f = open("HOSTS", "r")
HOSTS = f.read().split('\n')

f = open("CMDS", "r")
CMDS = f.read().split('\n')

# while len(CMDS) != 0:

# for cmd in CMDS:
#     output.append(subprocess.run(cmd, shell=True))
p = subprocess.Popen(args=CMDS[0], shell=True, stdout=subprocess.PIPE)
# stout = None
# op = None
# while stout is not None and op is not None:
stout, sterr = p.communicate()
print(stout.decode('utf-8'), end="")
p.kill()
