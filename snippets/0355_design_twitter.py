import heapq
from collections import defaultdict
from typing import List


# Design
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        news_feed.extend(self.tweets[userId])
        for followee in self.followees[userId]:
            news_feed.extend(self.tweets[followee])

        return [tweet for _, tweet in heapq.nlargest(10, news_feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].discard(followeeId)


twitter = Twitter()
print(twitter.postTweet(1, 5))  # None
print(twitter.getNewsFeed(1))  # [5]
print(twitter.follow(1, 2))  # None
print(twitter.postTweet(2, 6))  # None
print(twitter.getNewsFeed(1))  # [6, 5]
print(twitter.unfollow(1, 2))  # None
print(twitter.getNewsFeed(1))  # [5]
