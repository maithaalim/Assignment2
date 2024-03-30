#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Visitor:
    def __init__(self, name, age, id_card):
        # Initialize visitor object with name, age, and ID card
        self.name = name
        self.age = age
        self.id_card = id_card
        self.ticket_purchased = []

    def purchase_ticket(self, ticket):
        # Add purchased ticket to the visitor's list
        self.ticket_purchased.append(ticket)

    def display_info(self):
        # Display visitor information including name, age, and ID card
        print(f"Visitor: {self.name}, Age: {self.age}, ID Card: {self.id_card}.")


# In[ ]:




