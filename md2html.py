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
import markdown
import os
from os import path
import re
import sys

verbose = True

def convert(source, dest, args, verbosity):
    dest = open(args['--dest'], 'w')
    prevLine = ''

    source = open(args['--src'], "r", encoding="utf-8")

    # write HTML header markup
    dest.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Converted with Md2Html</title>\n</head>\n<body>\n')

    sourceTxt = source.read()
    destTxt = markdown.markdown(sourceTxt)
    dest.write(destTxt)
    dest.write('\n</body>\n</html>')
    dest.close()

    print("Conversion Complete")


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
    
