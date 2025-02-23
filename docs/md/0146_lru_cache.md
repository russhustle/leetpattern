-   Design and implement a data structure for **Least Recently Used (LRU) cache**. It should support the following operations: get and put.

![146](https://miro.medium.com/v2/resize:fit:650/0*fOwBd3z0XtHh7WN1.png)

| Data structure     | Description                   |
| ------------------ | ----------------------------- |
| Doubly Linked List | To store the key-value pairs. |
| Hash Map           | To store the key-node pairs.  |

<iframe width="560" height="315" src="https://www.youtube.com/embed/7ABFKPK2hD4?si=Ys47opcHraHHWtOI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| Approach | Time Complexity | Space Complexity |
| -------- | --------------- | ---------------- |
| LRU      | O(1)            | O(n)             |
