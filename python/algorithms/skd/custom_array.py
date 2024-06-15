class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        # get an item at an index
        # pass
        return self.data[index]

    def push(self, item):
        # add an item to the end of teh array
        # pass
        self.data[self.length] = item
        self.length += 1

        return self.length

    def pop(self):
        # remove the last item in the array
        # pass
        if not self.length:
            return None

        popped_item = self.data[self.length-1]
        self.data[self.length-1] = None
        self.length -= 1

        return popped_item

    def insert(self, index, item):
        # add an item at any index
        # pass

        # Ensure we're inserting inside a valid array length
        # if index > self.length - 1 or index < 0:
        if (self.length-1) > index < 0:
            return None

        # Create our new length
        self.length += 1

        # Shift items up one spot from teh insertion index to the new final spot in the array.
        # We iterate from the back since this is our new empty item
        for i in range(self.length-1, index-1, -1):
            self.data[i] = self.data[i-1]

        self.data[index] = item

        return self.data


    def remove(self, index):
        # remove an item at any index
        # pass

        # Ensure teh array has item
        if index > self.length-1:
            return None

        # Ensure we're removing an item inside the array
        if self.length-1 < index < 0:
            return None

        item_to_be_removed = self.data[index]

        # Shift items inward one index towards the one we remove
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

        # The item we want to delete is just overwritten to the value of the index that comes after it.

        # Since all items were shifted inward one spot, we need to remove the last index/item since our array size shrinks by 1
        self.data[self.length-1] = None
        self.length -= 1

        return item_to_be_removed

