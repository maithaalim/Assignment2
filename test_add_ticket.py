#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Ticketing import TicketingSystem
from Ticket import Ticket

def test_add_ticket():
    # Create a TicketingSystem instance
    ticketing_system = TicketingSystem()

    # Create a ticket
    ticket = Ticket(50, "Adult", 5)

    # Add the ticket to the ticketing system
    ticketing_system.add_ticket(ticket)

    # Check if the ticket is in the ticket list
    assert ticket in ticketing_system.ticket_list

    # Display ticket information
    print("Ticket information:")
    print(f"Price: {ticket.price}, Category: {ticket.category}, VAT: {ticket.VAT}")

# Run the test case
test_add_ticket()


# In[ ]:




