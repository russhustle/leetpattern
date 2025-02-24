from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # key -> [val, freq]
        self.key_to_val_freq = {}
        # freq -> OrderedDict of keys
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def remove_least_frequent(self):

        lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        del self.key_to_val_freq[lfu_key]

        # If the frequency list is empty after removal, delete it
        if not self.freq_to_keys[self.min_freq]:
            del self.freq_to_keys[self.min_freq]

    def update_freq(self, key):
        """Updates the frequency of an existing key."""
        value, freq = self.key_to_val_freq[key]

        # Remove key from current frequency group
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Update key frequency
        new_freq = freq + 1
        self.key_to_val_freq[key] = [value, new_freq]
        self.freq_to_keys[new_freq][key] = None

    def add_new_key(self, key, value):
        if len(self.key_to_val_freq) >= self.cap:
            self.remove_least_frequent()

        # Insert the new key with frequency 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self.update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self.update_freq(key)
        else:
            self.add_new_key(key, value)


lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # 1
lfu.put(3, 3)
print(lfu.get(2))  # -1
print(lfu.get(3))  # 3
lfu.put(4, 4)
print(lfu.get(1))  # -1
print(lfu.get(3))  # 3
