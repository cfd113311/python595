#!/usr/bin/env python
# coding: utf-8

# # Python Lecture 5: Object-Oriented Programming
# ## Jarret Petrillo copyright 2020
# ## AMS 595

# # Today's Goal
# 
# ## How can objects simplify code?
# 
# 1. data encapsulation
# 2. custom methods
# 2. modularity

# # Part 1: Data Encapsulation

# In[1]:


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
origin = Point()
print(origin.x, origin.y)


# # Part 2: Custom Methods

# In[2]:


# let's add points with a new add method.
# Point1.add(Point2) should add x,y elements.


# In[3]:


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def add(self, point):
        new_x = self.x + point.x
        new_y = self.y + point.y
        return Point(new_x, new_y)


# In[4]:


point1 = Point(1,2)
point2 = Point(3,4)
p = point1.add(point2)
print(p.x, p.y)


# In[5]:


# print( point )


# In[6]:


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def add(self, point):
        new_x = self.x + point.x
        new_y = self.y + point.y
        return Point(new_x, new_y)
    
    def __repr__(self):
        return "({},{})".format(self.x, self.y)


# In[7]:


point1 = Point(1,2)
print(point1)


# ### Coordinate data is encapsulated in the Point object.
# 
# ### Object has custom display and a custom method: add.

# # Examples - Good Design is Everywhere
# 
# Do not reinvent a programming style.  Good examples are easy to find.
# 
# Homework will ask you to find three Python packages.

# In[15]:


from sklearn import linear_model #sklearn is machine learning module.

standard_model = linear_model.LinearRegression()

type(standard_model)


# In[30]:


standard_model.fit([[1],[2],[3],[4]],[[1],[2],[3],[4]]) # takes array objects.

standard_model.coef_ # perfect. standard_model holds data of regression.


# In[37]:


from numpy import array

data = array([1,2,3,4,5]) # a mutable container.  *An array with added methods.

# The array object hides functionality.
# Under-the-hood there are C-objects that make this object *fast*.

type(data)


# # Part 3: Modularity

#  mod•u•lar
# 
#  adj. Of, relating to, or based on a module or modulus.
#  
#  adj. Designed with standardized units or dimensions, as for easy assembly and repair or flexible arrangement and use.
# 
# Modular design assembles complex code in small pieces.

# In[38]:


# montecarlo_test.py

# from montecarlo import Engine, 2DNumericalIntegration

# implementing these objects is the assessment for the Python module.


# # Examples of Modularity

# In[41]:


from statsmodels.tsa import arima #Extremely well-made module.
help(arima) # package of time series models
# Package has 3 submodules.


# # HW
# 
# There is a huge community of Python developers who share their home-made modules.
# 
# The repository for user-generated libraries is Python Package Index.
# 
# https://pypi.org/
# 
# There are Python libraries in all states of development.
# 
# As a homework, please find 3 packages *with changes in the last week*:
# 1. Find one that is solid and seems to have a broad development team.
# 2. Find one that is pre-alpha or in the planning stages.
# 3. Find one relevant to scientific computing.
