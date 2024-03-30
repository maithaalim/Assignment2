#!/usr/bin/env python
# coding: utf-8

# In[11]:


from LouvreMuseum import LouvreMuseum
from exhibition import Exhibition

def test_exhibition():
    # Create a LouvreMuseum instance
    museum = LouvreMuseum()

    # Add an exhibition
    exhibition = Exhibition("Ancient Civilization Exhibition", "Exhibition Hall A", 7)
    museum.add_exhibition(exhibition)
    assert exhibition in museum.exhibitions

    # Display exhibition information before removal
    print("Exhibition information before removal:")
    museum.display_exhibitions()

    # Remove the exhibition
    museum.remove_exhibition(exhibition)
    assert exhibition not in museum.exhibitions

    # Display exhibition information after removal
    print("Exhibition information after removal:")
    museum.display_exhibitions()
    

# Run the test case
test_exhibition()


# In[ ]:





# In[ ]:




