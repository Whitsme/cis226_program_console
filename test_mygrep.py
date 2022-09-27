""""
Aaron Whitaker
9/18/2022
CRN: 10235
CIS 226: Advanced Python Programming
Est. Time: 6 hours
"""

"""
Design: Search txt file for string provided by user input. Planned to use 'in' to search for lines of string in .txt

Develop: I used 'in' to search the .txt file provided per user input based on the text also input from user.

Test: I tested valid and invalid user input. I also tried to modify the test to print pass for expected errors but got stuck. 

Documentation: This program searches a .txt file for user input. Navigate to mygrep.py parent directory and run "python3 mygrep.py <string> <filename.txt>" to search for string in filename.txt. 
Expected format of .txt is string sentence, line return, string sentence, line return, etc.. 
"""

import sys
import pytest

search_text = ''
filename = ''

def main(search_text, filename):
    # TODO: Check len(sys.argv) and warn if missing arguments
    try:
        # len(sys.argv) == 2
        search_text = sys.argv[1]
        filename = sys.argv[2]
    except:
        try:
            search_text != None or '' or ' '
            filename != None or '' or ' '
        except:
            try:
                arg = (f'only one argument:({sys.argv[1]})')
            except:
                arg = 'no arguments'
            print(f"\nTwo arguments expected, but {arg} provided. Please try again.\n")
            quit()

    if '.' in search_text:
        print(f"\nFirst argument should be a string, not a file. Please try again.\n")
        quit()
    
    if '.' not in filename:
        print(f"\nSecond argument should be a file, not a string. Please try again.\n")
        quit()

    try:
        f = open(filename, 'r')
        f.close()
    except:
        print(f"\nFile '{filename}' not found. Please try again.\n")
        quit()

    txt_check(search_text, filename)

def txt_check(search_text, filename):
    # print (f"\nSearching for '{search_text}' in file '{filename}'\n")
    with open(filename, 'r') as f:
        for line in f:
            if search_text in line:
                print(line, end='\n')
                return (line)

if __name__ == '__main__':
    main(search_text, filename)

animals = {
    'dog': 'bark',
    'cat': 'meow',
    'duck': 'quack',
    'chicken': 'cluck',
}

def test_grep_pos(capsys):
    for animal, sound in animals.items():
        main(animal, 'animals.txt')
        captured = capsys.readouterr()
        assert (f'The {animal} goes {sound}') in captured.out
