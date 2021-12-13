#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# In[8]:


#Do lists need to have all the same data types?


# In[9]:


list1 = ["abc", 34, True, 40, "male"]


# In[10]:


print(list1)


# In[11]:


#Print second item


# In[13]:


print(mylist[1])


# In[14]:


#Print last item


# In[16]:


print(mylist[-1])


# In[9]:


#Print 3rd, 4th, 5th item (note that index [5] is not included)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# In[10]:


#This prints from beginning until orange, excluding [4] which is kiwi
print(thislist[:4])


# In[11]:


#This prints from cherry to the end
print(thislist[2:])


# In[23]:


#Changing items in a list
thislist[1] = "blackcurrant"
print(thislist)


# In[24]:


#Change a range of item values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# In[25]:


#Insert a new list item
thislist.insert(2, "dragon fruit")
print(thislist)


# In[27]:


#Remove items
thislist.remove("orange")
print(thislist)


# In[28]:


#Remove a specific indexed item
thislist.pop(1)
print(thislist)


# In[29]:


#If you don't specify for pop() then the last item is removed
thislist.pop()
print(thislist)


# In[33]:


#Sort lists alphabetically
thislist.sort()
print(thislist)


# In[34]:


#Join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[ ]:


#Insert items

thislist.insert(1, "orange")


# In[ ]:


#1. Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print()

#2. Change the value from "apple" to "kiwi", in the fruits list.

fruits[0] = 'kiwi'

#3.  add "lemon" as the second item in the fruits list.
fruits.insert(1, "Lemon")

#4. remove "banana" from the fruits list.

fruits.remove("banana")

#5. print the last item in the list.
print(fruits[-1])

#6. print the third, fourth, and fifth item in the list.
print(fruits[3:])


# In[ ]:




