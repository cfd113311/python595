#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 3: I/O, System-Level, and Plotting
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# # Overview
# 
# ## Inputs are:
# 
# 1. command-line input.
# 2. direct user input.
# 3. file read input.
# 
# ## Outputs are:
# 
# 1. print output.
# 2. file output.
# 3. "pickled" objects.
# 
# ## Systems-level mechanics are:
# 
# 1. interacting with the filesystem.
# 2. manipulating filenames.
# 
# ## Plotting:

# # Part 1
# 
# 1. Command-line input.
# 2. interacting with the filesystem.
# 3. manipulating filenames.
# 
# 

# # ls.py
# 
# python ls.py filename
# 
# This script will check the current directory for a file named "filename."
# 
# If it is there, it will print, "found it!"
# 
# Otherwise, it will print, "not found."
# 

# In[ ]:


# test.py

import sys

if __name__ == "__main__":
    print(sys.argv)
    


# In[ ]:


# python test.py 2313 312 123

# ['test.py', '2313', '312', '123']


# In[ ]:


type(sys.argv)


# In[ ]:


# test2.py

import sys

if __name__ == "__main__":
    print([type(x) for x in sys.argv])
    


# In[ ]:


# test2.py 231 23123 1

# [<class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>]


# In[ ]:


import os
help(os)


# In[ ]:


os.listdir()


# In[ ]:


3 in [1,2,3]


# In[ ]:


# ls.py

import sys
import os

def search_filesystem(filename):
    if filename in os.listdir():
        print("found!")
    else:
        print("not found.")


if __name__ == "__main__":
    search_filesystem(sys.argv[-1])


# # find_ext.py
# 
# python find_ext.py file_extension
# 
# This script will check the current directory for any files that end with extension "file_extension"
# 
# If one is there, print the first one.
# 
# Otherwise, it will print, "none found."

# In[ ]:


# find_ext.py

import sys
import os

def search_filesystem(file_ext):
    for filename in os.listdir():
        if file_ext == os.path.splitext(filename)[-1]:
            print("found:", filename)
            break
    else:
        print("none found.")


if __name__ == "__main__":
    search_filesystem(sys.argv[-1])


# In[ ]:


# python find_ext.py .ipynb

# found: iosystemplotting.ipynb


# # Part 2
# 
# 1. direct user input.

# In[ ]:


# user_input.py

txt = input("Type something to test this out: ")
print("Did you say:",txt,"?")


# # Part 3
# 
# 1. pickled objects.
# 2. reading and writing to standard files. 

# # To Pickle (verb)
# 
# definition: to preserve or steep in brine or other liquid.
# 
# We will not use brine.
# 
# Python has a way to save objects so that they can be read back as *Python objects*.

# In[14]:


import pickle
from datetime import datetime

data_dict = dict(greeting="Hello, UserName", 
                 last_login=datetime.fromisoformat("2018-02-01"), 
                 number_posts=231)

data_dict


# In[20]:


with open("data_dict.pickle",'wb') as f:
    pickle.dump(data_dict, f)


# In[21]:


with open("data_dict.pickle",'rb') as f:
    object_from_filesystem = pickle.load(f)
object_from_filesystem


# # Reading and writing to the filesystem
# 
# We saw two examples.
# 
# The key will be the *with* clause and *open* funtion.
# 
# With clauses manage the context of open and closing.

# In[33]:


with open("new.csv", "w") as f:
    f.write("1,1,1,1\n")
    f.write("2,1,1,1\n")
    
with open("new.csv", "r") as f:
    for line in f:
        print(line)


# # Part 4
# 
# 1. Make a plot.
# 2. Save a plot as a file.

# In[35]:


import matplotlib.pyplot as plt


# In[37]:


plt.plot([0.1,0.2,0.3],[4,5,6])


# In[38]:


plt.clf() # clears plot


# In[39]:


plt.plot([0.1,0.2,0.3],[4,5,6])
plt.savefig("line_graph.png")


# In[ ]:




