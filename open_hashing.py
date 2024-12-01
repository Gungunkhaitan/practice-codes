def display_hash(hashTable): 

    for i in range(len(hashTable)): 
        print(i, end=" ") 

        for j in hashTable[i]: 

            print("-->", end=" ") 

            print(j, end=" ") 

        print() 

HashTable = [[] for _ in range(10)] 

def Hashing(keyvalue): 

    return keyvalue % len(HashTable) 

def insert(Hashtable, keyvalue): 

    hash_key = Hashing(keyvalue) 

    Hashtable[hash_key].append(keyvalue) 

def find(Hashtable, keyvalue): 

    hash_key = Hashing(keyvalue) 

    bucket = Hashtable[hash_key] 

    for item in bucket: 

        if item == keyvalue: 

            return hash_key  # Key found, return the index where it was found 

    return None  # Key not found 

insert(HashTable, 10) 
insert(HashTable, 25) 
insert(HashTable, 20) 
insert(HashTable, 9) 
insert(HashTable, 21) 
insert(HashTable, 21) 
display_hash(HashTable) 
print("Finding 20:", find(HashTable, 20)) 
print("Finding 21:", find(HashTable, 21)) 
print("Finding 22:", find(HashTable, 22)) 