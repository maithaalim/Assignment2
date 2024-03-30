#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Exhibition:
    def __init__(self, title, location, duration):
        # Initialize exhibition object with title, location, and duration
        self.title = title
        self.location = location
        self.duration = duration

    def display_info(self):
        # Display exhibition information including title, location, and duration
        print(f"Exhibition: {self.title}, Location: {self.location}, Duration: {self.duration} days.")


# In[ ]:




