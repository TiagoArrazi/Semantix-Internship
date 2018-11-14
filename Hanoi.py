#!/usr/bin/env python3

import sys
import os

def hanoi(d, src, dest, aux):

    if d == 1: #base case, 1 disc

        print(f"Disc {d} goes from {src} to {dest}") #if there's only 1 disc is moved directly to the final tower

    else: #not base case, more than 1 disc

        hanoi(d-1, src, aux, dest) #moves the next disc to the auxiliar tower
        print(f"Disc {d} goes from {src} to {dest}")

        hanoi(d-1, aux, dest, src) #moves the current disc from the auxiliar tower to the final tower
        
if __name__ == "__main__":

    hanoi(int(sys.argv[1]), "A", "C", "B") #plays the game with wished number of discs
    steps = (2 ** int(sys.argv[1])) - 1
    print(f"{steps} steps")
