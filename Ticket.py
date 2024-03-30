#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Ticket:
    def __init__(self, price, category, VAT):
        # Initialize ticket object with price, category, and VAT
        self.price = price
        self.category = category
        self.VAT = VAT

    def calculate_price(self):
        # Calculate the total price including VAT
        return self.price + (self.price * self.VAT / 100)

    def display_info(self):
        # Display ticket information including price and category
        print(f"Ticket: Price: {self.price} AED, Category: {self.category}.")


# In[ ]:




