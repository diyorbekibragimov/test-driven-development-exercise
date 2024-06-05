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

def test_newline_as_separator():
    """
        Tests newline as a separator.
    """
    assert add("1\n2,3") == "6", "Failed on 1+2+3==6"
    assert add("1\n2\n3") == "6", "Failed on 1+2+3==6"
    assert add("1\n2\n3\n4") == "10", "Failed on 1+2+3+4==10"
    assert add("1\n2\n3\n4\n5") == "15", "Failed on 1+2+3+4+5==15"
    assert add("1\n2\n3\n4\n5\n6") == "21", "Failed on 1+2+3+4+5+6==21"
    assert add("1\n2\n3\n4\n5\n6\n7") == "28", "Failed on 1+2+3+4+5+6+7==28"
    assert add("1.5,2.5") == "4.0", "Failed on 1.5+2.5==4.0"
    assert add("3.14,2.71") == "5.85", "Failed on 3.14+2.71==5.85"
    assert add("0.5,0.5,0.5") == "1.5", "Failed on 0.5+0.5+0.5==1.5"
    assert add("1.23,4.56,7.89") == "13.68", "Failed on 1.23+4.56+7.89==13.68"
    assert add("1.23\n4.56\n7.89") == "13.68", "Failed on 1.23+4.56+7.89==13.68"
        

def test_basic_add():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("5,2") == "7", "Failed on 5+2==7"
