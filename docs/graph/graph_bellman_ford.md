# Graph - Bellman-Ford Algorithm

- The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph.
- It is slower than Dijkstra's algorithm, but it is more versatile, as it is able to handle graphs with negative edge weights.
- Time Complexity: O(V \* E), where V is the number of vertices and E is the number of edges in the graph.
- Space Complexity: O(V), where V is the number of vertices in the graph.

## LeetCode Problems

1. 0743 - [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium)
2. 0787 - [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium)
3. 0207 - [Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium)
4. 1109 - [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) (Medium)

## 743. Network Delay Time

- Return the minimum time taken to reach all nodes starting from the source node.

![743](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

```python
--8<-- "0743_network_delay_time.py"
```

## 787. Cheapest Flights Within K Stops

- Return the cheapest price to reach the destination within K stops.

![787](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)

```python
--8<-- "0787_cheapest_flights_within_k_stops.py"
```

## 207. Course Schedule

- Return whether it is possible to finish all courses.

```python
--8<-- "0207_course_schedule.py"
```

## 1109. Corporate Flight Bookings

- Return the number of seats booked on each flight.

```python
--8<-- "1109_corporate_flight_bookings.py"
```
