#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author: Nitish Vijai
# <nitishv@umich.edu>
# https://www.github.com/nitishvijai/Markdown2HTML
# md2html.py


"""Convert Markdown to HTML with this simple Python script.

Usage:
  md2html.py --src=<path> --dest=<name> [--quiet]
  md2html.py (-h | --help)
  md2html.py (-c | --credits)
  
Options:
  -h --help      Shows this help screen
  -c --credits   Shows credits, copyrights, and other licensing info
  --src=<path>   Path to the source Markdown file you want to convert to HTML
  --dest=<name>  Destination HTML file name - to be located in the same directory
  --quiet        Silent conversion (optional, default is verbose)

"""
from docopt import docopt
import os
from os import path
import re
import sys

verbose = True

"""
TODO:
1. Ship a working implementation
2. Implement alt. syntax for h1/h2
"""

def convert(source, dest, args, verbosity):
    dest = open(args['--dest'], 'w')
    prevLine = ''
    nested = ''

    # write HTML header markup
    dest.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Converted with Md2Html</title>\n</head>\n<body>\n')

    for line in source:
        newLine = ''

        # ------------------------- Headings (h1 - h6) -------------------------
        if line.startswith('# '): # heading level 1
            content = line[2:len(line) - 1]
            nested = 'h1'
            newLine = '<h1>' + content + '</h1>\n'
            dest.write(newLine)
        elif line.startswith('## '): # heading level 2
            content = line[3:len(line) - 1]
            nested = 'h2'
            newLine = '<h2>' + content + '</h2>\n'
            dest.write(newLine)
        elif line.startswith('### '): # heading level 3
            content = line[4:len(line) - 1]
            nested = 'h3'
            newLine = '<h3>' + content + '</h3>\n'
            dest.write(newLine)
        elif line.startswith('#### '): # heading level 4
            content = line[5:len(line) - 1]
            nested = 'h4'
            newLine = '<h4>' + content + '</h4>\n'
            dest.write(newLine) 
        elif line.startswith('##### '): # heading level 5
            content = line[6:len(line) - 1]
            nested = 'h5'
            newLine = '<h5>' + content + '</h5>\n'
            dest.write(newLine)   
        elif line.startswith('###### '): # heading level 6
            content = line[7:len(line) - 1]
            nested = 'h6'
            newLine = '<h6>' + content + '</h6>\n'
            dest.write(newLine)   
        elif line == '\n': # blank lines
            continue
        elif line.startswith('') and (line.endswith('  \n') or line.endswith('<br>\n')): # paragraph n line break
            nested = 'p'
            if nested is not None:
                line.replace('  \n', '<br>\n')
                newLine = '<p>' + line + '</p>\n'
                dest.write(newLine)
            

        if verbosity:
            print("Source: " + line)
            print("Destination: " + newLine)

        prevLine = line
        

    dest.write('</body>\n</html>')


def create_files(args, verbosity):
    source = open(args['--src'], 'rt') # read the file
    os.chdir(os.path.dirname(args['--src']))
    dest = open(args['--dest'], 'a') # initialize destination file
    dest.close()
    if verbosity:
        print("Destination file successfully created at: " + os.getcwd())
        print("Beginning conversion process...")
    
    # convert!
    convert(source, dest, args, verbosity)
    

def display_credits():
    # display credits if user asks to
    print('Markdown 2 HTML v1.0')
    print('Written by Nitish Vijai <nitishv@umich.edu>')
    print('Licensed under Apache License 2.0')
    print('Copyright (c) 2020 Nitish Vijai.')

if __name__ == "__main__":
    args = docopt(__doc__, help=True)
    verbose = not args['--quiet']

    # check to make sure file exists
    filesPresent = path.isfile(args['--src'])
    if filesPresent != True:
        print("Error: invalid source file path")
        exit

    create_files(args, verbose)
    
    if args['--credits'] == True:
        display_credits()
    
