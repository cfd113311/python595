#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 1: Syntax
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# # Homework
# 
# You were asked to read PEP 8: The Python Style Guide.
# 
# Today's lecture will recap the reading.

# # "Readability counts".
# 
# Let us start coding by learning the elements of clean code.
# 
# Whhere does syntax end and *style* start?

# # Key Ideas
# 
# 1. Indentation
# 1. Whitespace
# 1. Import statements
# 1. Naming conventions
# 1. Exception catching
# 

# # Python Requires Indentation
# 

# In[14]:


def generic_function(var_one, var_two,
                     var_three, var_four):
    '''
    This is the docstring.
    It comments will appear in the help text.
    generic_function takes four inputs.
    Comments should be complete sentences.
    There should be no additional line spaces.
    Notice the function variables are aligned.
    This aids readibility.
    '''
    if var_one == var_two:
        return "The first two inputs are equal."
    elif var_one == var_three:
        # This is an in-line comment.
        # Use these sparingly.
        # Notice the line below was too long,
        # and we broke the link and continued below
        # with the '\'
        return "The first two inputs are not equal,                 but the first and second are equal."
    
    if var_three is not None:
        if var_four is None:
            # Notice the indentation matches the depth.
            return None
        else:
            return var_four


# # Whitespace

# In[ ]:


# Correct:
spam(ham[1], {eggs: 2})

# Wrong:
spam( ham[ 1 ], { eggs: 2 } )

# Correct:
foo = (0,)

# Wrong:
bar = (0, )


# In[23]:


x = 3; y = 2;

# Correct:
if x == 4: print(x)

# Wrong:
if x == 4 : print(x) , y


# In[ ]:


# Correct:
spam(1)

# Wrong:
spam (1)


# In[ ]:


# Correct:
x = 1
y = 2
long_variable = 3

# Wrong:
x             = 1
y             = 2
long_variable = 3


# In[ ]:


# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag) # too many spaces.


# # Import Statements

# In[25]:


# Correct:
import os
import sys

# Wrong:
import sys, os


# In[27]:


# Correct:
from subprocess import Popen, PIPE


# In[ ]:


# The modules below are custom modules.
# It is very helpful to structure your own code
# into pieces.  Modules do that and ...

import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# make it possible to share your code.
from yourpkg import brother, sister


# # Naming Conventions

# lowercase
# 
# lower_case_with_underscores
# 
# UPPERCASE
# 
# UPPER_CASE_WITH_UNDERSCORES
# 
# CapitalizedWords (or CapWords, or CamelCase)
# 
# mixedCase (initial is lowercase)

# *Package and Module Names*: Modules should have short, all-lowercase names.
# 
# *Class Names*: Class names should normally use the CapWords convention.
# 
# *Function and Variable Names*: Function names should be lowercase, with words separated by underscores.
# 
# *Constants*: Constants are usually defined on a module level and written in all capital letters with underscores separating words.

# # Exception Catching

# In[36]:



collection = {}
key = "key_name"
value = collection[key]


# In[39]:


collection = {}
key = "key_name"
try:
    value = collection[key]
except KeyError:
    value = None

print(value)


# In[40]:


try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None


# In[52]:


try:
    do_something(with_input)
except:
    pass
    # this excepts any possible error!
    # way too broad!


# # Next Lecture
# 
# We will cover "Basic Data Structures."
# 
# If you have some familiarity with Python, please read
# PEP 372 -
# 
# https://www.python.org/dev/peps/pep-0372/
