"""
Test Module for String Calculator
----------------------------------
    @author: [student's name] - [student's email]
    @date: [date of creation]
    @description: This test module is designed to test the functionality of the string calculator
             defined in the calculator.py module. Using pytest for testing allows for more
             concise and powerful test capabilities, which is integrated into the GitHub
             workflow for continuous integration and testing.
"""

import pytest
from calculator import add



def test_basic_add():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("5,2") == "7"
    assert add("10,10") == "20"
    assert add("100,222") == "322"
    assert add("") == "0"
    assert add(",1") == "1"
    assert add("1000000,1111") == "1001111"
    assert add("1.1,1") == "2.1"
    assert add("3.5,100.5") == "104.0"
    assert add("0,10.5") == "10.5"
    assert add("105.11,2.11") == "107.22"

def test_many_add():


def test_float_add():


def test_negative_add():