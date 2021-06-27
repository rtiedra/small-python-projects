# Script for 'binary_search' program in Python
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
The program takes as input a string of integers ordered in a strictly increasing way
and does an iterative binary search to find the position of a given integer in the list
"""

import re

# The function 'test_list' verifies that the list 'lst' has length >=2
# and that its elements are ordered in a strictly increasing way
def test_list(lst):
  var = True
  if len(lst) < 2:
    var = False
  else:
    i = 0
    last = len(lst) - 1
    while i < last and var == True:
      if lst[i] < lst[i+1]:
        i += 1
      else:
        var = False
  return var

# The 'binary_search' function does an iterative binary search to find the position
# of the integer 'number' in the sorted list 'lst'
def binary_search(lst, number):
  var = False
  first = 0
  last = len(lst) - 1
  
  while first <= last and var == False:
    i = (first + last) // 2
    if lst[i] == number:
      var = True
      return 'The integer {} was found at position {} of the list'.format(number, i)
    elif lst[i] > number:
      last = i - 1
    elif lst[i] < number:
      first = i + 1
  if var == False:
    return 'The integer {} was not found in the list'.format(number)

# The 'main' function takes as input a string containing integers and a given integer,
# and returns the position of the given integer in the list
def main():
  var = False
  while var == False:
    input_string = input("Enter a list of strictly increasing integers (at least two integers): ")

    # Finds the integers in the input string and puts them in a list
    input_list = [int(s) for s in re.findall(r'\d+', input_string)]

    # Checks with 'test_list' that the list is suitable
    var = test_list(input_list)

  # Finds with 'binary_search' the position of the given number in the list,
  # and prints the result
  number = int(input("Enter the number to be found in the list: "))
  print('')
  print(binary_search(input_list, number),'\n')
  
if __name__ == '__main__':
  main()  
