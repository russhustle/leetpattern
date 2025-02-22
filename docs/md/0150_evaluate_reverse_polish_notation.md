## 150. Evaluate Reverse Polish Notation

-   Steps for the list `["2", "1", "+", "3", "*"]`:

| token | action | stack    |
| ----- | ------ | -------- |
| `2`   | push   | `[2]`    |
| `1`   | push   | `[2, 1]` |
| `+`   | pop    | `[3]`    |
| `3`   | push   | `[3, 3]` |
| `*`   | pop    | `[9]`    |
