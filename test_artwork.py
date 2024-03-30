#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LouvreMuseum import LouvreMuseum
from Artwork import Artwork

def test_add_remove_artwork():
    # Create a LouvreMuseum instance
    museum = LouvreMuseum()

    # Test add_artwork method
    artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Iconic portrait", "Permanent Gallery")
    museum.add_artwork(artwork)
    assert artwork in museum.artworks

    # Display artwork information before removal
    print("Artwork information before removal:")
    museum.display_artworks()

    # Test remove_artwork method
    museum.remove_artwork(artwork)
    assert artwork not in museum.artworks

    # Display artwork information after removal
    print("Artwork information after removal:")
    museum.display_artworks()

# Run the test case
test_add_remove_artwork()


# In[ ]:




