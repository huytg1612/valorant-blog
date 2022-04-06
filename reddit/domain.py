from django.core.files.storage import default_storage
from pyrebase import pyrebase
from rest_framework_simplejwt.tokens import AccessToken
from urllib3.util import url

from ValorantReddit.viewmodels.constant import firebaseConfig
from blog.models import Post, Viewer
from reddit.models import User


class UserDomain():
    def LoadTopUser(self, top):
        users = User.objects.all()
        topUsers = {}
        for user in users:
            posts = Post.objects.filter(author=user)
            numOfViews = 0
            for post in posts:
                viewers = Viewer.objects.filter(post=post)
                numOfViews += len(viewers)
            if (len(topUsers) < top):
                topUsers[user] = numOfViews
            else:
                pass
                # top5Users = sorted(top5Users.items(), key=lambda x: x[1], reverse=True)
                # leastViewUser = top5Users.pop()
                # if(leastViewUser.v)
        return topUsers

    def UploadAvatar(self, user, avatar):
        firebase = pyrebase.initialize_app(firebaseConfig)
        storage = firebase.storage()
        file_save = default_storage.save(avatar.name, avatar)
        storage.child("user_avatar/" + user.email + "_" + avatar.name).put("media/" + avatar.name)
        delete = default_storage.delete(avatar.name)
        url = storage.child("user_avatar/" + user.email + "_" + avatar.name).get_url(None)
        user.avatar = str(url)
        user.save()

    def getUserFromToken(self, token):
        access_token = AccessToken(token)
        user = User.objects.get(id=access_token['user_id'])

        return user
