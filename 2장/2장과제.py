#!/usr/bin/env python
# coding: utf-8

# ## 주피터 테스트

# In[1]:


class Dog():
    #속성
    age = 0
    name = ""
    weight = 0
    #메서드
    def bark(self):
        print("%s -> 멍멍" % self.name)


# In[2]:


myDog = Dog()
myDog.name = "Merry"
myDog.weight = 20
myDog.age = 5
myDog.bark()


# In[3]:


yourDog = Dog()
yourDog.name = "Happy"
yourDog.weight = 30
yourDog.age = 5
yourDog.bark()


# In[ ]:




