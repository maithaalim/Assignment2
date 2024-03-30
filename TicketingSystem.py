#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TicketingSystem:
    def __init__(self):
        # Initialize ticketing system with an empty ticket list
        self.ticket_list = []

    def add_ticket(self, ticket):
        # Add a ticket to the ticket list
        self.ticket_list.append(ticket)

    def remove_ticket(self, ticket):
        # Remove a ticket from the ticket list
        self.ticket_list.remove(ticket)

    def generate_ticket(self, price, category, VAT):
        # Create a new ticket object with the provided details
        new_ticket = Ticket(price, category, VAT)
        # Add the new ticket to the ticket list
        self.add_ticket(new_ticket)
        # Optionally, you can return the newly generated ticket
        return new_ticket

