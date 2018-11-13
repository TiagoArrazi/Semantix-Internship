#!/usr/bin/env python3

import sys

def hanoi(d, src, dest, aux):

    if d == 1:

        print(f"Disc {d} goes from {src} to {dest}")

    else:

        hanoi(d-1, src, aux, dest)
        print(f"Disc {d} goes from {src} to {dest}")

        hanoi(d-1, aux, dest, src)
        
if __name__ == "__main__":

    hanoi(int(sys.argv[1]), "A", "C", "B")
