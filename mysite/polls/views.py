from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# Each generic view needs to know what model it will be acting upon. This is provided using the model attribute....

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# Vote is too specialised to be able to use a generic view so 


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
            # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
    
            # request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. So next, we check for KeyError and redisplay the question form with an error message if choice isn’t given.
    except (KeyError, Choice.DoesNotExist):
        # unsuccessful vote. Redisplay the question voting form.
        return render(request, polls/detail.html, {
            question: question,
            error_message: "You didn't select a choice."
        })
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect rather than a normal HttpResponse after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button...
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # Here, reverse() is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view. This reverse() call will return a string like '/polls/3/results/' where 3 is the value of the question.id