class HashTable:
    def __init__(self, initial_capacity=16):
        """
        Initialize the hash table with a given initial capacity.
        Uses separate chaining to handle collisions.
        """
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        """
        Compute the hash value for a given key.
        """
        return hash(key) % self.capacity

    def put(self, key, value):
        """
        Insert or update the key with the given value.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

        # Optional: Resize if load factor exceeds threshold
        if self.size / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        """
        Retrieve the value associated with the key.
        Returns None if the key is not found.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """
        Remove the key and its associated value from the hash table.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def contains_key(self, key):
        """
        Check if the key exists in the hash table.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, _ in bucket:
            if k == key:
                return True
        return False

    def _resize(self):
        """
        Resize the hash table when load factor exceeds threshold.
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)


