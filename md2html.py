#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author: Nitish Vijai
# <nitishv@umich.edu>
# https://www.github.com/nitishvijai/Markdown2HTML
# md2html.py


"""Convert Markdown to HTML with this simple Python script.

Usage:
  md2html.py --src=<path> --dest=<path> [--quiet | --verbose]
  md2html.py (-h | --help)
  md2html.py (-c | --credits)
  
Options:
  -h --help      Shows this help screen
  -c --credits   Shows credits, copyrights, and other licensing info
  --src=<path>   Path to the source Markdown file you want to convert to HTML
  --dest=<path>  Destination HTML file path
  --quiet        Silent conversion (cannot enable verbose at the same time)
  --verbose      Print active conversion status (cannot enable quiet at the same time)

"""
from docopt import docopt
import os
import sys

def display_credits():
    # display credits if user asks to
    print('Markdown 2 HTML v1.0')
    print('Written by Nitish Vijai <nitishv@umich.edu>')
    print('Licensed under Apache License 2.0')
    print('Copyright (c) 2020 Nitish Vijai.')
    

if __name__ == "__main__":
    args = docopt(__doc__, help=True)
    if args['--credits'] == True:
        display_credits()
    
