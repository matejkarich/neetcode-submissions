class User:
    def __init__(self):
        self.feed = []
        self.following = []
        self.followers = []

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User()
        userPosting = self.users[userId]
        heapq.heappush_max(userPosting.feed, (self.time, (tweetId, userId)))
        for follower in userPosting.followers:
            heapq.heappush_max(follower.feed, (self.time, (tweetId, userId)))
        self.time += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return

        user = self.users[userId]
        newsFeed = []
        for _ in range(10):

            if not user.feed:
                for feedItem in newsFeed:
                    heapq.heappush_max(user.feed, feedItem)
                return [tweet[0] for time, tweet in newsFeed]

            newsFeed.append(heapq.heappop_max(user.feed))

        for feedItem in newsFeed:
            heapq.heappush_max(user.feed, feedItem)
        return [tweet[0] for time, tweet in newsFeed]

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.users[followerId] or not self.users[followeeId]:
            return None

        follower = self.users[followerId]
        follower.following.append(followeeId)
        followee = self.users[followeeId]
        followee.followers.append(followerId)

        for post in followee.feed:
            if post[1][1] == followeeId:
                heapq.heappush_max(follower.feed, post)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not self.users[followerId] or not self.users[followeeId]:
            return None

        follower = self.users[followerId]
        follower.following.remove(followeeId)
        followee = self.users[followeeId]
        followee.followers.remove(followerId)

        for post in follower.feed:
            if post[1][1] == followeeId:
                follower.feed.remove(post)
