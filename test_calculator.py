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



# def test_basic_add():
#     """
#         Tests addition. This test is written for you, extend it and add others! 
#     """
#     assert add("5,2") == "7", "Failed on 5+2==7"
#     assert add("3,4") == "7", "failed on 3+4==7"
#     assert add("0,0") == "0", "failed on 0+0==0"

def test_a_lot_add():
    assert add("3,4,5,6") == "18", "failed on 3+4+5+6 == 18"
    assert add("0,0,0") == "0", "failed on 0+0+0 == 0"
    assert add("1.9,2.1,1") == "5.0", "failed on 1.9,2.1,1 == 5"
    assert add("3500,2,3,4")  == "3509", "failed on 3500+2+3+4 == 3509"
    assert add("1,0,2,3,4") == "10", "failed on 1+0+2+3+4 == 10"
    assert add("3,4,6,7") == "20","failed"
def test_basic_add():
    """
        Tests addition. This test is written for you, extend it and add others! 
    """
    assert add("5,2") == "7"
    assert add("10,10") == "20"
    assert add("100,222") == "322"
    assert add("") == "0"
    assert add("1000000,1111") == "1001111"
    assert add("1.1,1") == "2.1"
    assert add("3.5,100.5") == "104.0"
    assert add("0,10.5") == "10.5"
    assert add("105.11,2.11") == "107.22"
