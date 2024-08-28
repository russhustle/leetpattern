# Graph

## Concepts

- Graph
- Vertex (Node)
- Edge
- Weight

### Types

Undirected graph: A graph in which edges have no direction.

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
1 --- 3
1 --- 2
3 --- 4
2 --- 3
2 --- 4
```

Directed graph: A graph in which edges have direction.

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
5((5))
1 --> 3
1 --> 2
3 --> 4
2 --> 3
4 --> 5
```

Cyclic graph: A graph in which there is a cycle.

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
1 --> 3
1 --> 2
3 --> 4
2 --> 3
4 --> 1
```

Acyclic graph

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
1 --> 3
1 --> 2
3 --> 4
2 --> 3
```

Directed Acyclic Graph (DAG)

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
1 --> 3
1 --> 2
3 --> 4
2 --> 3
```

Weighted graph

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
5((5))
1 -->|1| 3
1 -->|2| 2
3 -->|3| 4
2 -->|4| 3
4 -->|5| 5
```

Connected Graph

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
5((5))

1 --- 2
2 --- 3
3 --- 1
1 --- 4
4 --- 5
3 --- 5
```

Sto

### Representation

1. Adjacency Matrix
2. Adjacency List

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
1 --> 3
1 --> 2
3 --> 4
2 --> 3
```

Adjacency Matrix

|            | Node 1 | Node 2 | Node 3 | Node 4 |
| :--------: | :----: | :----: | :----: | :----: |
| **Node 1** |   0    |   1    |   1    |   0    |
| **Node 2** |   0    |   0    |   1    |   0    |
| **Node 3** |   0    |   0    |   0    |   1    |
| **Node 4** |   0    |   0    |   0    |   0    |

```python
grid = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
```

Adjacency List

```mermaid
classDiagram
direction LR
class 1{2, 3}
class 2{3}
class 3{4}
class 4{-}
1 -- 2
2 -- 3
3 -- 4
```

```python
graph = {
    1: [2, 3],
    2: [3],
    3: [4],
    4: []
}
```

### Degree

1. Degree: Number of edges connected to a node
2. In-degree: Number of edges coming into a node
3. Out-degree: Number of edges going out of a node

```mermaid
flowchart LR
1((1))
2((2))
3((3))
4((4))
1 --> 3
1 --> 2
3 --> 4
2 --> 3
```

- In-degree of Node 1: 0
- Out-degree of Node 1: 2
- In-degree of Node 2: 1
- Out-degree of Node 2: 1

```python
# List
in_degree = [0, 1, 2, 1]
out_degree = [2, 1, 1, 0]

# Dict
in_degree = {1: 0, 2: 1, 3: 2, 4: 1}
out_degree = {1: 2, 2: 1, 3: 1, 4: 0}
```
