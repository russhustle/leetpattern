## 2390. Removing Stars From a String

-   Remove all `*` characters and their adjacent characters from the string.

-   Steps for the string `leet**cod*e`:

| char | action | stack   |
| ---- | ------ | ------- |
| l    | push   | "l"     |
| e    | push   | "le"    |
| e    | push   | "lee"   |
| t    | push   | "leet"  |
| \*   | pop    | "lee"   |
| \*   | pop    | "le"    |
| c    | push   | "lec"   |
| o    | push   | "leco"  |
| d    | push   | "lecod" |
| \*   | pop    | "leco"  |
| e    | push   | "lecoe" |
