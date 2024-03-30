#!/usr/bin/env python
# coding: utf-8

# In[1]:


class SpecialEvent:
    def __init__(self, id, title, location, duration):
        # Initialize special event object with id, title, location, and duration
        self.id = id
        self.title = title
        self.location = location
        self.duration = duration

    def display_info(self):
        # Display special event information including title, location, and duration
        print(f"Special Event: {self.title}, Location: {self.location}, Duration: {self.duration} hours.")


# In[ ]:




