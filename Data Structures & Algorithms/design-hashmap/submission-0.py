class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if key == stored_key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if key == stored_key:
                return stored_value
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if key == stored_key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)