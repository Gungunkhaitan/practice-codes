class HashTable:

    def __init__(self, size):

        self.size = size

        self.keys = [None] * size

    def hash(self, key):

        return hash(key) % self.size

    def put(self, key):

        index = self.hash(key)

        initial_index = index  # Save the initial index for wrapping around if necessary

        # Linear probing to find an empty slot

        while self.keys[index] is not None:

            if self.keys[index] == key:

                return  # Key already exists

            index = (index + 1) % self.size

            # If we've wrapped around, break to avoid infinite loop

            if index == initial_index:

                break

        self.keys[index] = key

    def find(self, key):

        index = self.hash(key)

        initial_index = index  # Save the initial index for wrapping around if necessary

        # Linear probing to find the key

        while self.keys[index] is not None:

            if self.keys[index] == key:

                return "Key found at index " + str(index)

            index = (index + 1) % self.size

            # If we've wrapped around, break to avoid infinite loop

            if index == initial_index:

                break

        # Key not found

        return "Key not found"


# Create a hash table with a size of 5

hash_table = HashTable(5)


# Insert keys

hash_table.put(5)
hash_table.put(2)
hash_table.put(8)
hash_table.put(13)
hash_table.put(6)
print(hash_table.find(4))
print(hash_table.find(8))
print(hash_table.find(13))
print(hash_table.find(5))
print(hash_table.find(2))
