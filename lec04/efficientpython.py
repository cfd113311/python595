#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 4: Algorithms and Efficienct code
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# "Premature optimization is the root of all evil."
# 
# "Optimization can reduce readability and add code that is used only to improve the performance."
# 
# "In established engineering disciplines a 12% improvement, easily obtained, is never considered marginal and I believe the same viewpoint should prevail in software engineering"
# 
# https://en.wikipedia.org/wiki/Program_optimization#When_to_optimize

# # Simple suggestions
# 
# 1. Move calculations outside a loop.
# 1. Use the right object.
# 2. "timeit"
# 3. cProfiler

# # 1. Move static calculations outside a for loop.
# 

# In[ ]:


# Correct

fixed_adjustment = calculate_fixed_adjustment()
for x in range(1000):
    x + fixed_adjustment
    
# Incorrect
for x in range(1000):
    x + calculate_fixed_adjustment()


# # 2. Use new classes when they are relevant.

# In[55]:


# text parsing option

words = ["the", "new", "new", "new"]
count_the = 0
count_new = 0
for word in words:
    if word == "the":
        count_the += 1
    if word == "new":
        count_new += 1
        
print(count_the, count_new)


# In[58]:


from collections import Counter

words = ["the", "new", "new", "new"]
Counter(words)


# # 3. Timeit
# 
# ## Test simple statements with timeit.

# In[31]:


UserName = "Johnny22222"
greeting = "Hello, " + UserName + "!"
print(greeting)

greeting = "Hello, {}!".format(UserName)
print(greeting)


# In[34]:


from timeit import timeit

timeit('"Hello, {}!".format("Johnny22222")', number=10000)


# In[35]:


timeit('"Hello, "+"Johnny22222"+"!"', number=10000)


# # 4. cProfile

# python -m cProfile hello_world.py 
# 
# hello world!
#          4 function calls in 0.000 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 hello_world.py:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 

# # HW
# 
# Please read PEP 218: Adding a Built-In Set Object Type.
# 
# https://www.python.org/dev/peps/pep-0218/
# 
# We know Python has the set object.
# 
# The reading is the original proposal.
# 
# Set is an object.  Next session will begin a discussion of objects in Python.
