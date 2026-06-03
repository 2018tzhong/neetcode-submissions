from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.ts_counter = 0
        self.tweet_map = defaultdict(str)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.ts_counter, tweetId))
        self.tweet_map[tweetId] = userId
        self.ts_counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following_people = self.following[userId]
        ptrs = {}
        ptrs[userId] = len(self.tweets[userId]) - 1
        
        h = []
        if self.tweets[userId]:
            heapq.heappush(h, self.tweets[userId][ptrs[userId]])
        for i in following_people:
            if i == userId:
                continue
            if self.tweets[i]:
                ptrs[i] = len(self.tweets[i]) - 1
                heapq.heappush(h, self.tweets[i][ptrs[i]])
        
        results = []
        while len(results) < 10 and h:
            curr = heapq.heappop(h)
            results.append(curr[1])
            user = self.tweet_map[curr[1]]
            ptrs[user] -= 1
            if ptrs[user] >= 0:
                heapq.heappush(h, self.tweets[user][ptrs[user]])
        
        return results

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
