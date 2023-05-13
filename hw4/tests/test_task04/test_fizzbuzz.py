import doctest

import os, sys
sys.path.append(os.path.abspath('../../'))
import task_4_doctest

"""
Example of usage doctest
- Write func that will be tested (im my case this is fizzbuzz)
- Write documentation under your func (doctest demends special documentation formatting, you need to use >>> and call func with args in doc string,
  then in string below you need to write expected output from your func)
- Then create file for running doctest for your func (right now you are reading this comment in this file for running doctest)
- Import doctest library
- Import your module with func (in case of any ModuleNotFoundError you can use sys.path.append(os.path.abspath('../')), some kind of thing
- Write doctest.testmod(m=your_module, verbose=True)
    arg 'm' is for name of module where doctest will be runned, arg 'verbose' for displaying output in terminal
- Execute test_module for doctest
"""

if __name__ == "__main__":
    doctest.testmod(m=task_4_doctest, verbose=True)