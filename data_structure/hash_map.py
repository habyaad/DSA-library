import re
class HashMap:
    def __init__(self) -> None:
        self.MAX = 100
        self.hashTable = [[] for i in range(self.MAX) ]
    def getHash(self, data) -> int:
        dataAggregate = 0
        for i in data:
            dataAggregate += ord(i)
        return dataAggregate % self.MAX

    def exists(self, key):
        hashkey = self.getHash(key)
        for element in self.hashTable[hashkey]:
            if element[0] == key:
                return True
        return False

    def __setitem__(self, key, value) -> None:
        hashkey = self.getHash(key)
        if self.exists(key):
            for index, element in enumerate(self.hashTable[hashkey]):
                if element[0] == key:
                    self.hashTable[hashkey][index] = (key, value)
                    break
        else:
            self.hashTable[hashkey].append((key, value))

    def __getitem__(self, key):
        hashkey = self.getHash(key)
        for element in self.hashTable[hashkey]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        hashkey = self.getHash(key)
        if self.exists(key):
            for index, element in enumerate(self.hashTable[hashkey]):
                if element[0] == key:
                    del self.hashTable[hashkey][index]
                    break
        else:
            raise Exception(f"{key} does not exist in the hash map")

def sort_words():
    with open("src/poem.txt", "r") as f:
        for line in f:
            for word in re.split(" |,|;|:|\\.|\\n", line):
                word.replace("\n", "")
                if len(word)>=1:
                    if hashmap.exists(word):
                        hashmap[word] += 1
                    else:
                        hashmap[word] = 1
def print_result():
    for element in hashmap.hashTable:
        if len(element)>=1:
            for words in element:
                if len(words[0])>=1:
                    print(f"{words[0]} : {words[1]}")
        
if __name__ == "__main__":
    hashmap = HashMap()
    sort_words()
    print_result()