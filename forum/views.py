from django.shortcuts import render
from forum.models import Topic, Reply
from django.http import HttpResponseRedirect


# Create your views here.
def view(request):
    state = None
    topics = Topic.objects.order_by('-time')
    reply = Reply.objects.all()
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'topic': topics,
            'reply': reply,
        }
    else:
        content = {
            'state': state,
            'topic': topics,
            'reply': reply,
        }
    return render(request, 'forum.html', content)


def topic(request):
    state = None
    id = int(request.GET['id'])
    topic = Topic.objects.get(id=id)
    reply = Reply.objects.filter(topic_id=id).order_by('time')
    count = len(reply) + 1
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'topic': topic,
            'reply': reply,
            'count': count,
        }
    else:
        content = {
            'state': state,
            'topic': topic,
            'reply': reply,
            'count': count,
        }
    return render(request, 'topic.html', content)


def add_topic(request):
    author = request.user.first_name
    title = str(request.POST['new_title'])
    content = str(request.POST['new_content'])
    new_topic = Topic.objects.create(author=author, title=title, content=content)
    new_topic.save()
    return HttpResponseRedirect('forum.html')


def add_reply(request):
    author = request.user.first_name
    topic_id = int(request.POST['id'])
    content = str(request.POST['new_reply'])
    new_reply = Reply.objects.create(author=author, topic_id=topic_id, content=content)
    new_reply.save()
    # this_topic = Topic()
    this = Topic.objects.get(id=topic_id)
    print(this.reply_count)
    this.reply_count += 1
    this.save()
    print(this.reply_count)
    # this_topic.save()
    return HttpResponseRedirect('topic.html?id=' + str(topic_id))
