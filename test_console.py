#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import unittest
import pycodestyle
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):

    def test_console_docstring(self):
        """module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py no docstring")

    def test_class_docstring(self):
        """function docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNB no docstring")
        
    def test_pep8_test_style(self):
        """Pep8 style test"""
        pep8_codstyle = pycodestyle.StyleGuide(quiet=True)
        res = pep8_codstyle.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")
