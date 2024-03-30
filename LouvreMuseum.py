#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Ticketing import TicketingSystem

class LouvreMuseum:
    def __init__(self):
        # Initialize Louvre Museum with empty lists for artworks, exhibitions, special events, visitors,
        # and activities, and create a TicketingSystem object
        self.artworks = []
        self.exhibitions = []
        self.special_events = []
        self.visitors = []
        self.ticketing_system = TicketingSystem()
        self.activities = []  
 
    def add_artwork(self, artwork):
        # Add artwork to the museum's collection
        self.artworks.append(artwork)
 
    def remove_artwork(self, artwork):
        # Remove artwork from the museum's collection
        self.artworks.remove(artwork)
 
    def add_exhibition(self, exhibition):
        # Add exhibition to the museum
        self.exhibitions.append(exhibition)
 
    def remove_exhibition(self, exhibition):
        # Remove exhibition from the museum
        self.exhibitions.remove(exhibition)
 
    def add_special_event(self, event):
        # Add special event to the museum's schedule
        self.special_events.append(event)
 
    def remove_special_event(self, event):
        # Remove special event from the museum's schedule
        self.special_events.remove(event)
 
    def add_visitor(self, visitor):
        # Add visitor to the museum's visitor list
        self.visitors.append(visitor)
 
    def remove_visitor(self, visitor):
        # Remove visitor from the museum's visitor list
        self.visitors.remove(visitor)
 
    def generate_ticket(self, visitor, ticket):
        # Generate ticket for a visitor and add it to the ticketing system
        self.ticketing_system.add_ticket(ticket)
        # Record the ticket purchase for the visitor
        visitor.purchase_ticket(ticket)
 
    def display_artworks(self):
        # Display information about artworks in the museum's collection
        for artwork in self.artworks:
            artwork.display_info()
 
    def display_exhibitions(self):
        # Display information about exhibitions in the museum
        for exhibition in self.exhibitions:
            exhibition.display_info()
 
    def display_special_events(self):
        # Display information about special events happening in the museum
        for event in self.special_events:
            event.display_info()
 
    def display_visitors(self):
        # Display information about visitors in the museum
        for visitor in self.visitors:
            visitor.display_info()
            
    def add_activity(self, activity):  # Method to add activity
        # Add activity to the museum's schedule
        self.activities.append(activity)
 
    def remove_activity(self, activity):  # Method to remove activity
        # Remove activity from the museum's schedule
        self.activities.remove(activity)
 
    def display_activities(self):  # Method to display activities
        # Display information about activities happening in the museum
        for activity in self.activities:
            activity.display_info()


# In[ ]:




