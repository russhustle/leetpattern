// 1. Create a new HashMap
let hashMap = new Map();
console.log(hashMap);

// 2. Add key-value pairs
hashMap.set("apple", 1); // Adds key 'apple' with value 1
hashMap.set("banana", 2);
hashMap.set("cherry", 3);

console.log(hashMap);

// 3. Get a value by its key
console.log(hashMap.get("apple"));
// Output: 1

// 4. Check if a key exists
console.log(hashMap.has("banana"));
// Output: true

console.log(hashMap.has("grape"));
// Output: false

// 5. Delete a key-value pair
hashMap.delete("banana");
console.log(hashMap);

// 6. Get the size of the HashMap
console.log(hashMap.size);
// Output: 2

// 7. Loop through the HashMap
hashMap.forEach((value, key) => {
  console.log(key, ":", value);
});

// 8. Check if HashMap is empty
console.log(hashMap.size === 0);
// Output: false

// 9. Clear the HashMap (remove all key-value pairs)
hashMap.clear();
console.log(hashMap);
console.log(hashMap.size);
// Output: 0
