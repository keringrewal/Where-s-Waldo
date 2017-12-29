#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:20:20 2017

@author: keringrewal
"""

import threading
import re
import sys

class Waldo(object):

    def __init__(self, waldo, N):
        with open(waldo, 'r') as text:
            self.text = text.read()
        self.N = int(N)

    def search(self):
        section = len(self.text) / self.N
    
        for i in range(self.N):
            
            s = threading.Thread(target=self.find_waldo, args=(self.text[int(i * section):int((i+1) * section)], section * i,))
            s.start()           

    
    def find_waldo(self, waldo, section):
    
        for i in re.finditer('waldo', waldo):
            print("Found Waldo @ {} (Proc. {})".format(int(section + i.start()), threading.current_thread().name))


if __name__ == "__main__":
    Waldo(sys.argv[1], int(sys.argv[2])).search()

    
