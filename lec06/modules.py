#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 6b: Object-Oriented Programming
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# # HWx2
# 
# Read PEP 3141:A Type Hierarchy for Numbers
# https://www.python.org/dev/peps/pep-3141/
# 
# and 
# https://pypi.org/
# 
# There are Python libraries in all states of development.
# 
# As a homework, please find 3 packages *with changes in the last week*:
# 1. Find one that is solid and seems to have a broad development team.
# 2. Find one that is pre-alpha or in the planning stages.
# 3. Find one relevant to scientific computing.

# # Today's Goal
# 
# ## How can objects simplify thinking
# 
# 1. hierarchy
# 1. types
# 2. modularity

# # FAQ
# 
# Are objects and `classes' the same thing?

# In[9]:


# I use them interchangably.
# Every language has object-oriented patterns.
# Python's objects are called classes.

class Object():
    pass

new_object = Object()


# # FAQ
# 
# Why does Python have abstract classes?

# "[In Python] almost any aspect of an object can be reflected and directly accessed by external code, there are many different ways to test whether an object conforms to a particular protocol or not." - Tulin, PEP 3119
# 
# Abstract classes is one *explicit pattern* for organizing a class hierarchy.
# 
# It reflects the opinions of its designers more than any objective idea on design philosophy.

# In[26]:


# Example

# Determine if an object is a mutable sequence, like a list.

def is_mutable_sequence(obj):
    if type(obj)==list:
        return True
    else:
        return False


# In[27]:


import collections
is_mutable_sequence(collections.UserList) # false negative


# In[46]:


# Answer: This is actually a hard problem to solve ad hoc.
# Formal ideas behind Object hierarchy allow someone to
# specify the answers to questions of hierarchy.

from collections.abc import MutableSequence

issubclass(collections.UserList, MutableSequence)


# # Part 1: A Type Hierarchy for Numbers
# 
# Goals:
# 1. Codify the set inclusions of standard number sets.
# 2. I.e. real numbers contain the rational numbers.
# 3. I.e. Complex numbers contin the reals.

# # "X is a Y" test
# 
# An integer IS A rational number.
# 
# A real number IS A complex number.
# 
# This is the *perfect example* of type hierarchy.

# In[39]:


# Numbers
from abc import ABCMeta #abc means abstract base class

class Number(metaclass=ABCMeta): # the bottom of the hierarcy
    pass

class Complex(Number): # slighlty specific
    pass

class Real(Complex): # slighlty specific
    pass

class Rational(Real): # slighlty specific
    pass

class Integer(Rational): # more specific
    pass

class PositiveInteger(Integer): # and so on...
    pass


# # @abstractmethod and @abstractproperty wrappers
# 
# 

# In[59]:


from abc import abstractmethod, abstractproperty

class Complex(Number):
    """Complex number. """

    @abstractproperty
    def real(self):
        """Retrieve the real component of this number.

        This should subclass Real.
        """
        raise NotImplementedError

    @abstractproperty
    def imag(self):
        """Retrieve the real component of this number.

        This should subclass Real.
        """
        raise NotImplementedError

    @abstractmethod
    def conjugate(self):
        """(x+y*i).conjugate() returns (x-y*i)."""
        raise NotImplementedError

# This is a pattern.
# abstractmethods needs to be implemented.
# The declaration tells the user what it is that defines
# the Complex object as a complex object.

# d = Complex() is a typeerror
# because my definition overrides Complex object :/

c = complex() 

# property
print(c.imag)

# method
print(c.conjugate())


# # Further Reading
# 
# PEP 3119: Introducing Abstract Base Classes
# 
# https://www.python.org/dev/peps/pep-3119/

# # Part 2: Modules
# 
# Modules are packaged collections of objects and functions.
# 
# A number *module* might contains the hierarchy in Part 1.
# 
# *Modules* utilize a consistent design pattern.

# # statsmodels 
# 
# statsmodels is my favorite Python package.
# 
# There is a subpackage called tsa for timeseries analysis.
# 
# We will look very briefly at the hiearchies they use to fit 
# 
# an Autoregressive Moving-average Model.

# In[78]:


from statsmodels import tsa

from statsmodels.tsa import statespace

# MLEModel is a SARIMAX is a ARIMA

class ARIMA(statespace.sarimax.SARIMAX): #class for ARIMA model
    pass

class SARIMAX(statespace.mlemodel.MLEModel):
    pass

class MLEModel(tsa.base.tsa_model.TimeSeriesModel):
    pass


# In[79]:


dir(tsa.base.tsa_model) #base.tsa_model has the following


# # HW
# 
# Now you should complete the three Python module assessments.
# 
# Note the files on github have changed since the class started.
