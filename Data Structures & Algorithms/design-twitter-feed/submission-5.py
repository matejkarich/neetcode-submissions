class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)
        self.userFollowing = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None: # O(log(10)) -> O(1)
        userTweetHeap = self.userTweets[userId]
        if len(userTweetHeap) < 10:
            heapq.heappush_max(userTweetHeap, (self.time, tweetId))
        else:
            heapq.heappush_max(userTweetHeap, (self.time, tweetId))
            oldestTweetIndex = userTweetHeap.index(min(userTweetHeap))
            userTweetHeap[oldestTweetIndex] = userTweetHeap[-1]
            userTweetHeap.pop()
            heapq.heapify_max(userTweetHeap)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        restore = []
        userTweets = self.userTweets[userId]
        while len(feed) < 10: # O(10 * (f + 1) + 10 * log(10)) -> O(f) where f is # of people user is following
            if userTweets:
                mostRecentTweetHeap = userTweets
            else:
                mostRecentTweetHeap = None
            for f in self.userFollowing[userId]:
                if not mostRecentTweetHeap or (self.userTweets[f] and self.userTweets[f][0][0] > mostRecentTweetHeap[0][0]):
                    mostRecentTweetHeap = self.userTweets[f]
            if not mostRecentTweetHeap:
                break
            mostRecentTweet = heapq.heappop_max(mostRecentTweetHeap)
            feed.append(mostRecentTweet[1])
            restore.append((mostRecentTweetHeap, mostRecentTweet))
        for tweet in restore:
            heapq.heappush_max(tweet[0], tweet[1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None: # O(1)
        self.userFollowing[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: # O(f) where f is # of people user is following
        self.userFollowing[followerId].remove(followeeId)

        
