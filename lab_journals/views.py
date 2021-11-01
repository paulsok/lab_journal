from django.shortcuts import render
from .models import Topic
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404


# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'index.html')


def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'lab_journals/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)

    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'lab_journals/topic.html', context)


def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'lab_journals/new_topic.html', context)

