#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author: Nitish Vijai
# <nitishv@umich.edu>
# https://www.github.com/nitishvijai/Markdown2HTML
# test-1a.py - Unit Test #1a

import unittest
import filecmp

class ParagraphBreaksTestCase(unittest.TestCase):

    def test_p_br(self):
        # Run: python3 md2html.py --src="./tests/test-2a.md" --dest="test-2a.html"

        identical = filecmp.cmp('test-2a.html', 'model-2a.html')
        self.assertEqual(identical, True)
    

if __name__ == '__main__':
    unittest.main()