#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Ticket import Ticket

def test_calculate_price():
    # Create a ticket
    ticket = Ticket(50, "Adult", 5)

    # Calculate the ticket price
    total_price = ticket.calculate_price()

    # Check if the calculated price is correct
    assert total_price == 52.5  # Expected total price: 50 + (50 * 5 / 100) = 52.5

    # Display ticket information
    print("Ticket information:")
    print(f"Price: {ticket.price} AED, Category: {ticket.category}, Total Price (including VAT): {total_price} AED")

# Run the test case
test_calculate_price()


# In[ ]:




