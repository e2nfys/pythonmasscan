#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def exec(parms):
    os.system(parms)

if __name__ == '__main__':
    port = sys.argv[1]
    rate = sys.argv[2]
    dir = sys.argv[3]
    if os.path.exists(dir) == False:
        os.mkdir(dir)
    with open("ips.txt","r") as f:
        for line in f.readlines():
            line = line.strip()
            parms = "./masscan -p{port} {ip} -oL {filename} --max-rate {rate}".format(port=port,ip=line,filename=dir + "/" + line.replace("/","") + ".txt",rate=rate)
            print(parms)
            exec(parms)
