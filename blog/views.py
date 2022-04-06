from django.http import Http404
from django.shortcuts import render

# Create your views here.
from blog.domain import PostDomain
from blog.viewmodel.forms import CommentForm
from reddit.domain import UserDomain


def loadProfile(request):
    user = request.user
    if request.method == 'POST':
        print(len(request.FILES))
        avatar = request.FILES.get('avatar_image', None)
        if avatar:
            userDomain = UserDomain()
            userDomain.UploadAvatar(user, avatar)

    if user.is_authenticated:
        postDomain = PostDomain()

        posts = postDomain.GetPostsByAuthor(user)
        profile = postDomain.GetAuthorInfor(user)
        result = {'posts': posts, 'profile': profile}
        return render(request, 'pages/profile.html', {'result': result})
    else:
        raise Http404('')


def list(request):
    postDomain = PostDomain()
    userDomain = UserDomain()

    topUser = userDomain.LoadTopUser(4)
    result = {'posts': postDomain.GetListPost(), 'top_users': topUser}

    return render(request, 'pages/index.html', {'result': result})


def viewPost(request, id):
    user = request.user
    postDomain = PostDomain()
    postDomain.ProccessNewViewer(id, user)

    if request.method == 'POST':
        if request.POST.get('comment_button'):
            txt_comment = request.POST['comment']
            postDomain.CommentPost(id, user, txt_comment)
        elif request.POST.get('reply_button'):
            comment_id = request.POST['comment_id']
            txt_comment = request.POST['comment']
            if (txt_comment != ''):
                postDomain.ReplyComment(post_id=id, txt_comment=txt_comment, comment_id=comment_id, user=user)

    commentForm = CommentForm()
    post = postDomain.GetPostById(id)
    author = postDomain.GetAuthorInfor(post.author)
    result = {'post': postDomain.ViewPost(id, user), 'comment_form': commentForm, 'author': author}
    return render(request, 'pages/post.html', {'result': result})
