"""Test k file
"""
from k import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-11-29"

def test():
	"""Tests the k function in the k class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert k.k() == "k", "test failed"
	#assert k.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
