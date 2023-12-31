# Test generated by RoostGPT for test roost-test using AI Model vertex

"""
This file contains unit tests for the loadFile function.
"""

from __future__ import print_function
import sys


def loadFile(fileName):
    """
    loadFile: This function loads the file and reads its lines.
    """
    global lines
    fo = open(fileName)
    for line in fo:
        lines.append(line)
    fo.close()


def TestLoadFile():
    """
    TestLoadFile: This function tests the loadFile function.
    """

    # Test 1: File exists
    lines = []
    loadFile("test.txt")
    assert len(lines) == 3

    # Test 2: File does not exist
    lines = []
    loadFile("does_not_exist.txt")
    assert len(lines) == 0

    # Test 3: File is empty
    lines = []
    loadFile("empty.txt")
    assert len(lines) == 0


if __name__ == "__main__":
    TestLoadFile()