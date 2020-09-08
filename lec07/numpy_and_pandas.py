#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 7: SciPy, NumPy, and Pandas
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# # Goals for Today
# 
#  Introduction to the three key Python packages for scientific computing
#  
# 1. NumPy has the array object and efficient low-level matrix operation
# 3. SciPy adds specialized functions for signal processing+linear algebra
# 1. Pandas builds data methods and functions
# 

# # FAQ
# 
# Where can I learn more?

# # Use Good References, instead of Google
# 
# Three book references from PACKT publishing are:
# 1. "NumPy Cookbook" by Idris
# 1. "Learning SciPy for Numerical Computing" by Blanco-Silva
# 3. "Mastering Pandas" by Anthony

# # Part 1: NumPy
# 
# 1. array indexing
# 2. common functions
# 3. ways to practice

# In[11]:


import numpy as np

data = np.array([
                [2, 8, 7, 1, 6,],
                [9, 5, 4, 7, 3,],
                [6, 1, 3, 8, 4,],
                [8, 7, 9, 6, 5,],
                [4, 2, 1, 3, 9,],
                [3, 6, 5, 4, 2,],
                [1, 9, 8, 5, 7,],
                [5, 4, 2, 9, 1,],
                [7, 3, 6, 2, 8,]])

data


# In[22]:


# Indexing is the most important idea in arrays

# indices start at 0 in Python

print(data[0,1]) # first is row, second is column

print(data[:,1]) # get the second column

print(data[0,:]) # first row


# In[25]:


# fancy indexing

print(data)

print(data[range(5),range(5)]) # select diagonal elements


# In[34]:


# find shape

print(data.shape)

data2 = data.copy()


# In[37]:


data2.flat = 0

print(data2)

print(data2.flat) # flat is a mutable sequence of array elements.


# In[43]:


data3 = data[data>3] # select all indices that have value
                     # greater than 3

print(data3) # very handy!


# # Useful NumPy functions
# 
# np.sqrt(), np.log(), np.arange(), np.astype(), and np.sum()
# 
# np.ceil(), np.modf(), np.where(), np.ravel(), and np.take()
# 
# np.sort() and np.outer()
# 
# np.diff(), np.sign(), and np.eig()
# 
# np.histogram() and np.polyfit()
# 
# np.compress() and np.randint()

# In[69]:


print(np.sum([1,2,3]))

print(np.array([1,2,3]).astype(float))

print(np.array(
    ["2018-01-01","2020-01-01","2019-03-04"]
    ).astype(np.datetime64))

print(np.arange(0,10))

np.modf(np.sqrt(2)) # separate fractional and integer parts of numbers


# In[75]:


a = np.array([10,1,2])
print(np.outer(a,a)) # outer product

np.ravel(np.outer(a,a)) # read values from 
                        # top left corner to 
                        # bottom right


# # So many great example problems!
# 
# ## What is the 10,001st prime number?
# 
# Implement Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
# 
# Images are also arrays. A matrix location has value corresponding to the color of the pixel.
# 
# ## How would you implement a *blur* function?
# 
# ## Could you write an *edge detection algorithm*?
# 
# At this point - you have an extremely versatile object, the NumPy array, at your fingertips and can accomplish quite a bit.
# 
# Before moving on, select three of the functions above that were not detailed and write a clear description of what it does and when it would be useful.  This is super helpful practice.
# 

# # Part 2: SciPy
# 
# 1. Linear algebra
# 2. Special functions
# 3. Interpolation

# In[83]:


import scipy.linalg

mu=1/np.sqrt(2)
print(mu)

A=np.matrix([[mu,0,mu],[0,1,0],[mu,0,-mu]])
print(A)

B=scipy.linalg.kron(A,A) # use SciPy for Kroenecker product

B.shape


# In[96]:


square = np.outer(a,a)

A = np.exp(square) # numpy has element-wise exponential

print(A)

# useful in ODE methods
B = scipy.linalg.expm(square) #scipy has the matrix exponential

print(B) 


# In[101]:


scipy.linalg.eigvals(A)

scipy.linalg.lu(A) # LU decomposition in Matrix Theory

# linear solvers...

help(scipy.linalg.solve)


# In[112]:


# special functions

scipy.special.zeta(0,1)
scipy.special.airy(0)
scipy.special.jn(0,3) # Bessel function


# In[119]:


# interpolation functions

import scipy.interpolate

x = np.arange(0,10)

scipy.interpolate.lagrange(x, np.sin(x))

# root finding
# integration
# ODE methods

pass # we are passing, 
     # but please know SciPy has everything you will ever need.


# # Part 3: Pandas
# 
# We did this last because it is some people's first foray into Python.
# 
# The idea is that there are tons of other methods out there besides what is included in Pandas.
# 
# Pandas adds three nice abstractions:
# 1. Series
# 2. DataFrame
# 3. Panel

# In[141]:


import pandas as pd

ser = pd.Series(data.ravel())

temp = ser[0:10] # index is automatically created

print(temp)


# In[139]:


import calendar as cal

monthNames=[cal.month_name[i] for i in np.arange(1,6)]

print(monthNames)

months=pd.Series(data.ravel()[0:5],index=monthNames)

print(months) # labeled univariate data


# In[153]:


# DataFrame from dictionary of series

datadict = dict(data1=months, temp=temp)

dataframe = pd.DataFrame(datadict)

print(dataframe) # automatic merging!

# Panel is 3D object similar to Series to DataFrame


# In[158]:


dataframe.temp # access by dot operator

dataframe.iloc[0,1] # array-like retrieval


# In[165]:


dataframe.to_csv("save.csv")

dataframe_read = pd.read_csv("save.csv")

print(dataframe_read)

print(dataframe_read.set_index("Unnamed: 0")) # now has right index


# # Practice, practice, practice
# 
# This covered ~1% of Pandas, 1% of SciPy and 5% of NumPy.
# 
# The point is there is a lot of great software and clever patterns.
# 
# Take your time to practice solving problems in different ways.
# 
# As an exercise, you may use everything here in the Python module assesment.
# 
# If you completed it, try the assignment again and see how short you can make each task.
