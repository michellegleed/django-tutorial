from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
# from django.template import loader

from django.shortcuts import get_object_or_404
# from django.shortcuts import get_list_or_404
from django.shortcuts import render

from django.urls import reverse

from .models import Question

# Create your views here.

# def index(request):
    # return HttpResponse("Hello, world! You are at the polls index!")

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         "latest_question_list" : latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# The above func rewritten using render() func...        
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    propsDictionary = {
        "latest_question_list" : latest_question_list,
    }
    return render(request, "polls/index.html", propsDictionary)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})
    
# The above func rewritten using get_object_or_404() func...    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    propsDictionary = {
        "question" : question,
    }
    return render(request, "polls/detail.html", propsDictionary)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question})

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