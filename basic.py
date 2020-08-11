#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv('C:\\Users\\Mojtaba\\Projects\\parkinsons\\parkinsons.data')
df.head()


# In[14]:


claim = "Pluto is a planet!"
claim.lower()
# claim.startswith(planet)


# In[22]:


claim.index('plan')


# In[10]:


claim.startswith('Pluto')


# In[8]:


claim.endswith('dwarf planet')


# In[35]:


print("hello", end='')
print("pluto", end='')
len(planet)
# Yes, we can even loop over them
[char+'! ' for char in planet]


# In[18]:


words = claim.split()
words


# In[15]:


datestr = '1956-01-31'
year, month, day = datestr.split('-')


# In[16]:


year


# In[17]:


'/'.join([month, day, year])


# In[19]:


' 👏 '.join([word.upper() for word in words])


# In[21]:


planet='Pluto'
planet + ', we miss you.'


# In[23]:


position = 9
planet + ", you'll always be the " + str(position) + "th planet to me."


# In[24]:


"{}, you'll always be the {}th planet to me.".format(planet, position)


# In[33]:


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)


# In[34]:


# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


# In[38]:


# Dictionary
numbers = {'one':1, 'two':2, 'three':3}
# add
numbers['eleven'] = 11
# change
numbers['one'] = 'Pluto'

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial


# In[39]:


'Saturn' in planet_to_initial


# In[40]:


for k in numbers:
    print("{} = {}".format(k, numbers[k]))


# In[43]:


# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))


# In[49]:


for i, o in planet_to_initial.items():
    print("{} begins with \"{}\"".format(i.rjust(50), o))


# In[ ]:




