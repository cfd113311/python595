#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 0: Getting Started
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# # What exactly is a computer?
# 
# # How can one machine perform so many tasks?

# 
# ## ``A Computer is a machine that stores and manipulates information under the control of a changeable program." 
# -John Zelle
# 
# A gas pump is a machine that manipulates information (price of gas, quantity needed), but it only performs one task.
# 
# Computers by definition run many tasks.  Software is the key.

# # What can't a computer do?
# 
# Some problems are *intractable* or *impossible*.
# 
# *Intractable* means the problem solution requires too much memory or too much time to run.
# 
# *Impossible* means no algorithm can exist to solve the task.
# 
# ref: https://en.wikipedia.org/wiki/Computational_complexity_theory

# # An operating system is software that runs other software. 
# 
# > *python* hello_world.py
# 
# This command "python" runs the file "hello_world.py"
# 
# All the details of this operation are *operating-system specific*.
# 
# The results are the same: 
# 
# > "hello world!"
# 

# # Python is a programming language.
# 
# ## Why do we need programming languages?
# 
# Consider the sentence "I saw the man in the park with a telescope."
# 
# Who has the telescope?
# 
# Meaning comes from context and different languages resolve conflicts in different ways.

# # Python is a *high-level* programming language.
# 
# ## There are few memory directives.
# 
# Python is based on an educational-only language called *ABC*.
# 
# There is a reason it is easy to use.
# 
# *The goal of the Python module is to not just learn how to use Python, but to learn how to write production code in Python*
# 
# This is a way higher hurdle.  "Knowing Python" means different things to every employer.

# # Misconception: Python is ``easy."
# 
# ## It is easy to get started, but professional Python programmers have an amazing breadth.
# 
# 

# # Python==Breadth
# 
#     sqlite3 – interacting with SQLite databases
#     xml – creating and processing XML files
#     csv – CSV file reading and writing
#     logging – basics logging facility for Python
#     configparser – configuration file parser
#     os – interacting with the operating system,
#     datetime – manipulating with dates and time
#     io – working with streams,
#     time – time access and conversions
#     math – a basic tool for elementary evaluations
#     NumPy – fundamental package for scientific computing
#     SciPy – an ecosystem for mathematics, science, and engineering
#     Matplotlib – 2D plotting library producing publication quality figures
#     Pandas – a library providing high-performance and data analysis tools
#     SciKit-image – a collection of algorithms for image processing
#     tkinter — Python interface to Tcl/Tk
#         tkinter’s application life cycle
#         Widgets, windows and events
#         Sample applications
#     pygame – a simple way of developing multimedia applications
#     PEP 20 – The Zen of Python: a collection of principles that influences the design of Python code
#     PEP 8 – Style Guide for Python Code: coding conventions for code comprising the standard library in the main Python distribution
#     PEP 257 – Docstring Conventions: what is docstring and some semantics as well as conventions associated with them
#     **Object-Oriented** 
# 

# # There are different versions of Python
# 
# ## The syntax varies.
# 
# Python 2.7.18 reads Python version 2.7 release 18.
# 
# Python 2.7 and Python 3.5 are not compatiable.  There was a break, and the syntax changed.
# 
# We will use *Python 3.8*
# 
# It is the newest version as of August 2020.
# 
# history ref: https://en.wikipedia.org/wiki/Python_%28programming_language%29

# # Are there any questions?
# 
# These materials are available on github at github.com/cfd113311/python595.
# 
# Please log on to the Python help session Wednesdays 12pm - 1pm EST or use picktime to schedule a one-on-one session 1pm - 2:20pm.
# 
# Let's get started!

# # Python has a shell
# 
# > typing *python* opens an interpretated session ("interpretator")
# 
# The shell is a stand-alone interpretator.
# 
# Python commands executed in the interpretator display their result.
# 
# When it starts:
# 
# > Python 3.7.3 (default, Oct  7 2019, 12:56:13) 
# [GCC 8.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# 
# :>>> help(print)
# 
# This is the help screen for the print function.  *help()* is always a friend.

# # Interpretator experiments

# # Shell and interpretator versus scripts
# 
# The function *sum* and *greet* disappear after closing the interpreator.
# 
# The same happens in the shell.
# 
# Scripts are *reusable* portions of code that execute an algorithm.
# 
# The importance is they contain all the instructions for the Python program.
# 
# "Interpreter and shell are good for *testing*"
# https://www.youtube.com/watch?v=50XxuscFy1I

# # ``run" a Python script on your own computer before continuing.
# 
# There are files available next to the slides.
# 

# # Extra 1: Clone the repository from github.
# 
# ## Standard collaboration tools are essential in big projects.
# 
# Cloning a repository means creating a local version.  We are using github as a dropbox.  In reality *git* is a version control software.
# 
# Repository hosted at https://github.com/cfd113311/python595
# 
# Instructions: https://www.wikihow.com/Clone-a-Repository-on-Github
# 
# (The Git GUI = Grahical User Interface is a nice tool.)

# # Extra 2: Setup Jupyter Notebook
# 
# ## The slides are jupyter notebooks. 
# 
# It is a nice combination of *shell* and *script*.
# 
# https://jupyter.org/install

# # Extra 3: How does ``running'' differ on different operating systems.
# 
# ## 500 of the world's 500 fastest computers use *Linux*
# 
# ## Why?
# 
# ref: https://en.wikipedia.org/wiki/Operating_system
# 
# ref: https://en.wikipedia.org/wiki/Computational_science
# 
# extra ref: https://www.quora.com/Why-does-Linux-seem-so-much-faster-than-Windows?share=1

# # Recap
# 
# The tools learned today were:
# 1. Big picture computer science
# 2. Python interpretator
# 3. Python scripting
# 
# The next session is Lecture 1: Python Syntax 
# 
# HW: read PEP 8 https://www.python.org/dev/peps/pep-0008/
