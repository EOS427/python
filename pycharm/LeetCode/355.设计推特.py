# class Twitter(object):
#
#     user_map={}
#
#     def __init__(self):
#         self.feed_list=[]
#         self.follow_map={}
#         self.followed_map={}
#
#     def insert_and_adjust(self,tweetId):
#         self.feed_list.append(tweetId)
#         if len(self.feed_list)>10:
#             del self.feed_list[0]
#
#     @staticmethod
#     def check_and_establish(userId):
#         if userId not in Twitter.user_map:
#             new_user = Twitter()
#             Twitter.user_map[userId] = new_user
#
#     def postTweet(self, userId, tweetId):
#         Twitter.check_and_establish(userId)
#         id_map=Twitter.user_map[userId].followed_map
#         if len(id_map)>0:
#             for id in id_map:
#                 Twitter.user_map[id].insert_and_adjust(tweetId)
#         Twitter.user_map[userId].insert_and_adjust(tweetId)
#
#     def getNewsFeed(self, userId):
#         if userId not in Twitter.user_map:
#             return []
#         return Twitter.user_map[userId].feed_list
#
#     def follow(self, followerId, followeeId):
#         Twitter.check_and_establish(followerId)
#         Twitter.check_and_establish(followeeId)
#         Twitter.user_map[followeeId].followed_map[followerId]=followerId
#         Twitter.user_map[followerId].follow_map[followeeId]=followeeId
#
#     def unfollow(self, followerId, followeeId):
#         Twitter.check_and_establish(followerId)
#         if followeeId in Twitter.user_map[followerId].follow_map:
#             del Twitter.user_map[followerId].follow_map[followeeId]
#         if followerId in Twitter.user_map[followeeId].followed_map:
#             del Twitter.user_map[followeeId].followed_map
#
class Twitter(object):
    def __init__(self):
         self.relative_time = 0
         self.users_map = {}

    class User:

        def __init__(self):
            self.own_work_list=[]
            self.follow_map= {}


    def postTweet(self, userId, tweetId):
        self.relative_time+=1
        self.establish_if_not_exist(userId)
        user=self.users_map[userId]
        user.own_work_list.append([tweetId,self.relative_time])

    def getNewsFeed(self, userId):
        if userId in self.users_map:
            check_user=self.users_map[userId]
            feed_list=[]
            for followee in check_user.follow_map.values():
                feed_list+=followee.own_work_list
            feed_list+=check_user.own_work_list
            feed_list.sort(key=lambda x:x[1],reverse=True)
            if len(feed_list)>10:
                del feed_list[10:]
            feed_list=list(map(lambda x:x[0],feed_list))
            return feed_list
        return []

    def follow(self, followerId, followeeId):
        if followerId!=followeeId:
            self.establish_if_not_exist(followerId)
            self.establish_if_not_exist(followeeId)
            follower_map=self.users_map[followerId].follow_map
            follower_map[followeeId]=self.users_map[followeeId]

    def unfollow(self, followerId, followeeId):
        self.establish_if_not_exist(followerId)
        self.establish_if_not_exist(followeeId)
        if followeeId in self.users_map[followerId].follow_map:
            del self.users_map[followerId].follow_map[followeeId]


    def establish_if_not_exist(self,userId):
        if userId not in self.users_map:
            new_user=Twitter.User()
            self.users_map[userId]=new_user
