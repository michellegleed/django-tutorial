from django.urls import path

#  fullstop means current directory...
from . import views 

# setting app_name property helps django to work out which app a url belongs to. See polls/templates/polls/index.html to see how I referenced first the app name and then the url name in my template.
app_name = "polls"

# BELOW: first arg is the url, second is the applicable view function, third is the name you're giving to the url - so in the templates, you can refer to it by name rather than having to hard-code it (which makes it really easy to change a url if you need to without having to rewrite it in a bunch of different places)...

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("<int:question_id>/", views.detail, name="detail"),
#     path("<int:question_id>/results/", views.results, name="results"),
#     path("<int:question_id>/vote", views.vote, name="vote")
# ]

# BELOW: re-written using generic views. (Note that the name of the matched pattern in the path strings of the second and third patterns has changed from <question_id> to <pk>)...

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote", views.vote, name="vote")
]