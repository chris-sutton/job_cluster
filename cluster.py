#!/usr/bin/python3
import subprocess
import shlex

f = open("HOSTS", "r")
HOSTS = f.read().split('\n')

f = open("CMDS", "r")
CMDS = f.read().split('\n')
output = []
for cmd in CMDS:
    output.append(subprocess.run(cmd, shell=True, capture_output=True))

print(output)
