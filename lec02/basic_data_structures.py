#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 2: Basic Data Structures
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# # Homework
# 
# You were asked to read PEP 372: Adding an ordered dictionary to collections.
# 
# It is an advanced reading.
# 
# If you waited on the homework, watch today's video
# and read today's slides and go back.
# 
# https://www.python.org/dev/peps/pep-0372/

# # Overview
# 
# Python has four basic built-in container types.
# 
# 1. list
# 2. dictionary
# 3. set
# 4. tuple
# 
# The reading explains an additional container type, *OrderedDict* in the collections module.
# 
# We will explore these additional objects at the end of the lecture.

# # list

# In[1]:


a = []

type(a)


# In[2]:


help(a)


# In[3]:


# mutable means it is editable

a = [1,2,3]

a.append(4)

print(a)


# In[4]:


a.clear()

a


# In[5]:


a = [1,2,4,3]

a.sort()

a


# In[10]:


for x in a:
    print(x+10)


# In[6]:


# list comprehensions are in-line lists

b = [x+10 for x in a]

b


# In[16]:


list_of_names = ['Janet', 'Mike','Charlie','Henry', 'Jane']

# String concatenation also works.
list_of_fullnames = [x+" Doe" for x in list_of_names]

list_of_fullnames


# # dictionary

# In[12]:


d = {}

type(d)


# In[13]:


help(d)


# In[26]:


# There are two key ways to initialize a dictionary.

x = {'one': 1, 'two': 2, 'three': 3}
print(x)
x = dict(one=1,two=2,three=3)
x


# In[17]:


x['one']
x['two']


# In[18]:


x.get('one')


# In[19]:


x['four']


# In[23]:


four = x.get('four')
type(four)


# In[24]:


if four is None:
    print("four is not in dictionary x")


# In[27]:


dictionary = {'listitems': [1,2,3], 'string': "hello!!"}


# In[29]:


for key, items in dictionary.items():
    print(key, items)


# # set

# In[33]:


empty_set = set()
numbers = set([1,2,3,4])
help(set)


# In[34]:


a = set([1,2,3])
b = set([4,5,6])
a.union(b)


# In[37]:


for x in a:
    print(x)


# In[41]:


new_set = set("HiwidiTheOrder")
[x for x in new_set] # in general order is not preserved!


# # tuple

# In[43]:


x = (1,)
type(x)


# In[44]:


help(tuple)


# In[50]:


x = (1,2,3,4,)
x[0]


# In[52]:


# tuples are immutable

x[0] = 3


# # special containers
# 
# ### OrderdDict

# In[55]:


import collections

special_collections = [ x for x in dir(collections) if x[0]!='_']
print(special_collections)


# In[56]:


help(collections.OrderedDict)


# In[73]:


regular_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
ordered_dict = collections.OrderedDict(one=1, two=2, three=3, four=4)

[x for x in ordered_dict]
[x for x in regular_dict]


# In[75]:


ordered_dict.popitem()


# In[76]:


ordered_dict

