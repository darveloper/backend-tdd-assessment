#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import sys
import echo


# Your test case class goes here
class TestEcho(unittest.TestCase):
    
    def setUp(self):
        ''' This function is called only once for all tests '''
        self.parser = echo.create_parser()
        self.pystring = 'python2'
        if sys.version_info[0] == 3:
            self.pystring = 'python3'

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("./USAGE") as f:
            usage = f.read()

        self.assertEquals(stdout, usage)


    def test_no_options(self):
        args = ["HeLlo wOrLd"]
        ns = self.parser.parse_args(args)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.lower)
        self.assertFalse(ns.title)
        actual = echo.main(args)
        expected = args[0]
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)
    def test_all_options(self):
        args = ["-tul", "HeLlo wOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)

    def test_upper_short(self):
        args = ["-u", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)
    def test_lower_short(self):
        args = ["-l", "HeLlo wOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ["-t", "HeLlo wOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ["--upper", "hello world"]
        actual = echo.main(args)
        expected = "HELLO WORLD"
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)
        
    def test_lower_long(self):
        args = ["--lower", "HeLlo wOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)

    def test_title_long(self):
        args = ["--title", "HeLlo wOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        # assert means: "Make sure that..."
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
