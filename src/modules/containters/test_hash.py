import unittest
from hash import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_put_and_get(self):
        self.ht.put("key1", "value1")
        self.ht.put("key2", "value2")
        self.assertEqual(self.ht.get("key1"), "value1")
        self.assertEqual(self.ht.get("key2"), "value2")
        self.assertIsNone(self.ht.get("key3"))

    def test_update_value(self):
        self.ht.put("key1", "value1")
        self.ht.put("key1", "value2")
        self.assertEqual(self.ht.get("key1"), "value2")

    def test_remove(self):
        self.ht.put("key1", "value1")
        self.assertTrue(self.ht.remove("key1"))
        self.assertFalse(self.ht.remove("key1"))
        self.assertIsNone(self.ht.get("key1"))

    def test_contains_key(self):
        self.ht.put("key1", "value1")
        self.assertTrue(self.ht.contains_key("key1"))
        self.assertFalse(self.ht.contains_key("key2"))

    def test_resize(self):
        # Insert enough items to trigger resize
        for i in range(20):
            self.ht.put(f"key{i}", f"value{i}")
        for i in range(20):
            self.assertEqual(self.ht.get(f"key{i}"), f"value{i}")

if __name__ == "__main__":
    unittest.main()
