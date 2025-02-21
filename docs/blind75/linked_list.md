---
comments: True
---

# Linked List

## 206. Reverse Linked List

-   Reverse a singly linked list.

```mermaid
graph LR
A[1] --> B[2]
B --> C[3]
C --> D[4]
D --> E[5]
```

```mermaid
graph RL
E[5] --> D[4]
D --> C[3]
C --> B[2]
B --> A[1]
```

=== "Python"

    ```python
    --8<-- "0206_reverse_linked_list.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0206_reverse_linked_list.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0206_reverse_linked_list.ts"
    ```

## 21. Merge Two Sorted Lists

=== "Python"

    ```python
    --8<-- "0021_merge_two_sorted_lists.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0021_merge_two_sorted_lists.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0021_merge_two_sorted_lists.ts"
    ```

## 143. Reorder List

=== "Python"

    ```python
    --8<-- "0143_reorder_list.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0143_reorder_list.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0143_reorder_list.ts"
    ```

## 19. Remove Nth Node From End of List

-   Given the `head` of a linked list, remove the `n-th` node from the end of the list and return its head.

=== "Python"

    ```python
    --8<-- "0019_remove_nth_node_from_end_of_list.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0019_remove_nth_node_from_end_of_list.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0019_remove_nth_node_from_end_of_list.ts"
    ```

## 141. Linked List Cycle

-   Determine if a linked list has a cycle in it.

```mermaid
graph LR
A[3] --> B[2]
B --> C[0]
C --> D[-4]
```

```mermaid
graph LR
A[3] --> B[2]
B --> C[0]
C --> D[-4]
D --> B
```

=== "Python"

    ```python
    --8<-- "0141_linked_list_cycle.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0141_linked_list_cycle.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0141_linked_list_cycle.ts"
    ```

## 23. Merge k Sorted Lists

=== "Python"

    ```python
    --8<-- "0023_merge_k_sorted_lists.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0023_merge_k_sorted_lists.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0023_merge_k_sorted_lists.ts"
    ```
