import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'

# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

with open(shoplistfile, 'wb') as f:
    # Dump the object to a file
    pickle.dump(shoplist, f)
# Destroy the shoplist variable
del shoplist

with open(shoplistfile, 'rb') as f:
    # Load the object from the file
    storedlist = pickle.load(f)
    print(storedlist)
