from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            strLen = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + strLen])
            i = j + 1 + strLen

        return decoded


# |-------------|-------------|--------------|
# |   Approach  |    Time     |    Space     |
# |-------------|-------------|--------------|
# | Two pointers|    O(n)     |     O(n)     |
# |-------------|-------------|--------------|


codec = Codec()
encoded = codec.encode(["hello", "world"])
print(encoded)  # "5#hello5#world"
decoded = codec.decode(encoded)
print(decoded)  # ["hello", "world"]
