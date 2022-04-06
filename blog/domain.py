import datetime
import operator
from functools import reduce

from django.db.models import Q

from blog.models import Post, Viewer, Comment
from blog.viewmodel.constant import DateTimeProccessing
from reddit.models import User

class PostDomain():
    def GetPostsByAuthor(self, user):
        posts = Post.objects.filter(author=user)
        posts = list(posts)
        posts.sort(key=lambda k: k.post_date, reverse=True)

        result = []
        for post in posts:
            viewers = Viewer.objects.filter(post=post)

            numOfComments = 0
            for viewer in viewers:
                comments = Comment.objects.filter(viewer=viewer)
                numOfComments += len(comments)

            model = {
                'id': post.id,
                'title': post.title,
                'body': post.body,
                'post_date': post.post_date,
                'rate': post.rate,
                'author': post.author,
                'topic': post.topic.all(),
                'numOfViews': len(viewers),
                'numOfComments': numOfComments,
                'time_display': DateTimeProccessing().calculateDateTime(post.post_date)
            }

            result.insert(1, model)

        return result

    def GetPostById(self, id):
        post = Post.objects.get(id=id)
        return post

    def GetAuthorInfor(self, author):
        user = User.objects.get(id=author.id)
        posts = Post.objects.filter(author=author)

        numOfPosts = len(posts)
        numOfViews = 0
        for post in posts:
            viewers = Viewer.objects.filter(post=post)
            numOfViews += len(viewers)

        model = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
            'numOfPosts': numOfPosts,
            'numOfViews': numOfViews,
            'avatar': user.avatar
        }

        return model

    def ReplyComment(self, user, txt_comment, comment_id, post_id):
        comment = Comment.objects.get(id=comment_id)
        post = Post.objects.get(id=post_id)
        viewer = Viewer.objects.filter(post=post).get(user=user)

        if comment.reply_comment == None:
            reply = Comment(viewer=viewer, content=txt_comment, reply_comment=comment)
        if comment.reply_comment != None:
            reply = Comment(viewer=viewer, content=txt_comment, reply_comment=comment.reply_comment)

        if (reply.viewer != comment.viewer):
            reply.reply_to = comment.viewer
        reply.save()

    def CommentPost(self, post_id, user, txt_comment):
        post = Post.objects.get(id=post_id)
        print(post_id)
        viewer = Viewer.objects.filter(post=post).get(user=user)

        if viewer:
            comment = Comment(viewer=viewer, content=txt_comment)
            comment.save()

    def GetListPost(self):
        posts = Post.objects.all()
        posts = list(posts)
        posts.sort(key=lambda k: k.post_date, reverse=True)

        result = []
        for post in posts:
            viewers = Viewer.objects.filter(post=post)

            numOfComments = 0
            for viewer in viewers:
                comments = Comment.objects.filter(viewer=viewer)
                numOfComments += len(comments)

            model = {
                'id': post.id,
                'title': post.title,
                'body': post.body,
                'post_date': post.post_date,
                'rate': post.rate,
                'author': post.author,
                'topic': post.topic.all(),
                'numOfViews': len(viewers),
                'numOfComments': numOfComments,
                'time_display': DateTimeProccessing().calculateDateTime(post.post_date)
            }

            result.insert(1, model)

        return result

    def ProccessNewViewer(self, id, user):
        post = Post.objects.get(id=id)
        viewers = Viewer.objects.filter(post=post)

        isViewed = False
        if user.is_authenticated:
            for viewer in viewers:
                if viewer.user.email == user.email:
                    isViewed = True
                    break
            if not isViewed:
                new_viewer = Viewer(user=user, post=post)
                new_viewer.save()

    def ViewPost(self, id, user):
        post = Post.objects.get(id=id)
        viewers = Viewer.objects.filter(post=post)

        list_comment = []
        comments = Comment.objects.none()

        for viewer in viewers:
            comments |= Comment.objects.filter(viewer=viewer).filter(reply_comment=None)

        numOfComments = len(comments)
        for comment in comments:
            replies = Comment.objects.filter(reply_comment=comment)
            for reply in replies:
                reply.time_display = DateTimeProccessing().calculateDateTime(reply.comment_date)

            numOfComments += len(replies)
            comment.replies = list(replies)
            comment.replies.sort(key=lambda k: k.comment_date)
            comment.time_display = DateTimeProccessing().calculateDateTime(comment.comment_date)
            list_comment.insert(1, comment)

        list_comment.sort(key=lambda k: k.comment_date, reverse=True)
        result = {
            'id': post.id,
            'title': post.title,
            'post_date': post.post_date,
            'rate': post.rate,
            'author': post.author,
            'topic': post.topic.all(),
            'body': post.body,
            'numOfViews': len(viewers),
            'list_comment': list_comment,
            'numOfComments': numOfComments,
        }

        return result
