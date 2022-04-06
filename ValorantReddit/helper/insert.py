import datetime
import os, sys
sys.path.append('D:\py\ValorantReddit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ValorantReddit.settings'
import django
django.setup()

from reddit.models import User
from blog.models import Post, Viewer, Topic

# user = User(email="haipm@gmail.com", password="123")
# user.save()
# user = User(email="duytm@gmail.com", password="123")
# user.save()

# topic = Topic(name="Skill", description="Skill description")
# topic.save()
# topic = Topic(name="Event", description="Event description")
# topic.save()
# topic = Topic(name="Agent", description="Agent description")
# topic.save()
# topic = Topic(name="Gun", description="Gun description")
# topic.save()

# topic1 = Topic.objects.get(name="Skill")
# topic2 = Topic.objects.get(name="Event")
# topic3 = Topic.objects.get(name="Agent")
# topic4 = Topic.objects.get(name="Gun")
#
# user1 = User.objects.get(email="huytg@gmail.com")
# user2 = User.objects.get(email="thaonhi@gmail.com")
# user3 = User.objects.get(email="haipm@gmail.com")
#
# post = Post(title="How to use Omen's smoke", body="Watch lineup on youtube", post_date=datetime.datetime.utcnow(),
#             rate=3, author=user2)
# post.save()
# post.topic.add(topic1)
# post.topic.add(topic2)
#
# post = Post(title="How to use Sova's recon", body="Watch lineup on youtube", post_date=datetime.datetime.utcnow(),
#             rate=3, author=user2)
# post.save()
# post.topic.add(topic1)
# post.topic.add(topic2)
#
# post = Post(title="Prime vandal or reaver vandel ?", body="Prime is better", post_date=datetime.datetime.utcnow(),
#             rate=3, author=user3)
# post.save()
# post.topic.add(topic4)
