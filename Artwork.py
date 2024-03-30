#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        # Initialize artwork object with title, artist, date of creation, historical significance, and location
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location

    def display_info(self):
        # Display artwork information including title, artist, and date of creation
        print(f"Artwork: {self.title} by {self.artist}, created on {self.date_of_creation}.")


# In[ ]:




