import re
import sys
import os

fh_ver = open("ver1.txt",'r')
fh_test = open("test.txt",'r')

wirePat1 = re.compile("wire\s(.*)(;)")
wirePat2 = re.compile("wire\s(\[.*\]\s)(.*)(;)")
wirePat3 = re.compile("wire\s(\[.*\])(.*)(\[.*\]*)(;)")
wirePat4 = re.compile("(.*),(.*)")
wires =[]
wire=""
for line in fh_ver.readlines():
    if wirePat1.search(line):
        m=wirePat1.search(line)
        wire = m.group(1)
        if (wirePat3.search(line)):
            m=wirePat3.search(line)
            wire = m.group(2)
        elif (wirePat2.search(line)):
            m=wirePat2.search(line)
            wire = m.group(2)
        if wirePat4.search(wire):
            m=wirePat4.search(wire)
            wires.append(m.group(1))
            wires.append(m.group(2))
            continue
        wires.append(wire)
print (wires)        
    
fh_ver.close()

for line in fh_test.readlines():
    if wirePat.search(line):
        print (line)
fh_test.close()


