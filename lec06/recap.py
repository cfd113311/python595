#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 6a: Recap from OH
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# In[2]:


# What is the output of the following function calls?

def addifbig(a,b):
    if a>10 and b>15:
        return a+b
    
addifbig(20,30)
addifbig(10,30)
addifbig(1,1)


# In[3]:


# custom exception class

class OutOfOfficeError(Exception):
    pass


# In[4]:


def askquestion(to, msg):
    if to=="Colleague on Holiday":
        raise OutOfOfficeError
    # else send message


# In[5]:


# custom errors allow applications to have custom behavior
# It also makes code very readable!

try:
    askquestion("Colleague on Holiday", 
                "Hi! Do you have the hw for 595?")
except OutOfOfficeError:
    askquestion("Colleague NOT on Holiday", 
                "Hi! Do you have the hw for 595?")


# In[6]:


#Python filesystem demonstration


# # HW
# 
# Before starting lecture 6b modules, please read PEP 3141: A Type Hierarchy for Numbers
# 
# https://www.python.org/dev/peps/pep-3141/
# 
