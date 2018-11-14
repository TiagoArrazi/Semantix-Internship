#!/usr/bin/env python3

#Use it by -> ./GitPusher.py (file_1) (file_2) (file_3) (file_4) ...
#Only works with SSH

import os
import sys
import time

def getArgvSize(argv):

    return len(argv)


if __name__ == "__main__":

    for i in range(1, getArgvSize(sys.argv)):

        os.system(f"git add {sys.argv[i]}")
        os.system("git status")
        os.system("git commit -m \"Commit through GitPusher\"")
        os.system("git push -u origin master")
