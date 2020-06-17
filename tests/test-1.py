#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author: Nitish Vijai
# <nitishv@umich.edu>
# https://www.github.com/nitishvijai/Markdown2HTML
# test-1a.py - Unit Test #1a

import unittest
import filecmp

class HeadingsTestCase(unittest.TestCase):

    def test_h1_h6(self):
        # Run: python3 md2html.py --src="./tests/test-1a.md" --dest="test-1a.html"

        identical = filecmp.cmp('test-1a.html', 'model-1a.html')
        self.assertEqual(identical, True)
    

if __name__ == '__main__':
    unittest.main()