#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Activity:
    def __init__(self, title, description, location, duration):
        # Initialize activity object with title, description, location, and duration
        self.title = title
        self.description = description
        self.location = location
        self.duration = duration

    def display_info(self):
        # Display information about the activity including title, description, location, and duration
        print(f"Activity: {self.title}, Description: {self.description}, Location: {self.location}, Duration: {self.duration} hours.")

