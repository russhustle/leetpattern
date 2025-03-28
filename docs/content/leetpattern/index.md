---
comments: True
---

# LeetPattern

## Resources

-   [滑动窗口题单](https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/solutions/879777/hua-dong-chuang-kou-zhen-di-jian-dan-yi-73bii)

### Sheet

-   In order to visualize and practice the algorithm, I use google sheets to make drafts. You also can have access to it [here](https://drive.google.com/drive/folders/1yxoqn6ra6Th5a_KHJRx3drcy950JPRVg?usp=drive_link).

![sheet-example](../../assets/google-sheet-example.jpg)

## Prerequisites

-   Python Basics: [Python Distilled](https://www.dabeaz.com/python-distilled/)

<img src="https://www.dabeaz.com/python-distilled/cover.jpg" alt="python distilled" width="200">

## Resources

-   [算法竞赛模板库 by 灵茶山艾府](https://github.com/EndlessCheng/codeforces-go)
-   [[Leetcode Discuss] Solved all two pointers problems in 100 days](https://leetcode.com/discuss/study-guide/1688903/solved-all-two-pointers-problems-in-100-days)
-   [[Leetcode Discuss] Solved all dynamic programming (dp) problems in 7 months](https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months)
-   [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems)
-   [如何更加优雅地使用 LeetCode 刷题 ？](https://leetcode.cn/circle/discuss/jPBij8/)

## Dynamic Programming

Steps to Solve DP Problems

1. Define the `dp` array and its meaning.
2. Define the `dp` formula.
3. Initialize the `dp` array.
4. Determine the traversal direction.
5. Derive the `dp` array.

## C++ Containers

-   Array (`std::vector`)

| Operation          | Method                            |
| ------------------ | --------------------------------- |
| Append             | `v.push_back(x);`                 |
| Pop last element   | `v.pop_back();`                   |
| Insert at position | `v.insert(v.begin() + index, x);` |
| Remove at position | `v.erase(v.begin() + index);`     |
| Clear all elements | `v.clear();`                      |
| Get size           | `v.size();`                       |
| Access element     | `v[i]` or `v.at(i);`              |
| Sort               | `sort(v.begin(), v.end());`       |

-   Deque (`std::deque`)

| Operation      | Method             |
| -------------- | ------------------ |
| Append (back)  | `d.push_back(x);`  |
| Append (front) | `d.push_front(x);` |
| Pop last       | `d.pop_back();`    |
| Pop front      | `d.pop_front();`   |
| Access front   | `d.front();`       |
| Access back    | `d.back();`        |

-   Queue (`std::queue`)

| Operation         | Method       |
| ----------------- | ------------ |
| Enqueue (push)    | `q.push(x);` |
| Dequeue (pop)     | `q.pop();`   |
| Get front element | `q.front();` |
| Get back element  | `q.back();`  |
| Check if empty    | `q.empty();` |
| Get size          | `q.size();`  |

-   Priority Queue (`std::priority_queue`)
    -   Default is max heap

| Operation       | Method                                               |
| --------------- | ---------------------------------------------------- |
| Insert          | `pq.push(x);`                                        |
| Remove top      | `pq.pop();`                                          |
| Get top element | `pq.top();`                                          |
| Check if empty  | `pq.empty();`                                        |
| Get size        | `pq.size();`                                         |
| Min heap        | `priority_queue<int, vector<int>, greater<int>> pq;` |

-   Stack (`std::stack`)

| Operation       | Method       |
| --------------- | ------------ |
| Push            | `s.push(x);` |
| Pop             | `s.pop();`   |
| Get top element | `s.top();`   |
| Check if empty  | `s.empty();` |
| Get size        | `s.size();`  |

-   Set (`std::set`)

| Operation         | Method         |
| ----------------- | -------------- |
| Insert            | `s.insert(x);` |
| Remove            | `s.erase(x);`  |
| Check existence   | `s.count(x);`  |
| Get size          | `s.size();`    |
| Find element      | `s.find(x);`   |
| Get first element | `*s.begin();`  |
| Get last element  | `*s.rbegin();` |

-   Unordered Set (`std::unordered_set`)
    -   Similar to `std::set`, but uses hashing for faster lookups

| Operation       | Method          |
| --------------- | --------------- |
| Insert          | `us.insert(x);` |
| Remove          | `us.erase(x);`  |
| Check existence | `us.count(x);`  |
| Find element    | `us.find(x);`   |

-   Map (`std::map`)

| Operation       | Method                           |
| --------------- | -------------------------------- |
| Insert/update   | `mp[key] = value;`               |
| Get value       | `mp[key];`                       |
| Remove key      | `mp.erase(key);`                 |
| Check existence | `mp.count(key);`                 |
| Get size        | `mp.size();`                     |
| Iterate         | `for (auto [k, v] : mp) { ... }` |

-   Unordered Map (`std::unordered_map`)
    -   Similar to `std::map`, but uses hashing for faster lookups

| Operation       | Method              |
| --------------- | ------------------- |
| Insert/update   | `ump[key] = value;` |
| Get value       | `ump[key];`         |
| Remove key      | `ump.erase(key);`   |
| Check existence | `ump.count(key);`   |

-   List (`std::list`)
    -   Doubly linked list

| Operation          | Method               |
| ------------------ | -------------------- |
| Push front         | `lst.push_front(x);` |
| Push back          | `lst.push_back(x);`  |
| Pop front          | `lst.pop_front();`   |
| Pop back           | `lst.pop_back();`    |
| Insert at position | `lst.insert(it, x);` |
| Remove element     | `lst.remove(x);`     |
