from django.template import RequestContext, loader
from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import render

def detail ( request , question_id ): 
    return HttpResponse ( "You're looking at question %s ." % question_id ) 
    
def results ( request , question_id ): 
    response = "You're looking at the results of question %s ." 
    return HttpResponse ( response % question_id ) 
    
def vote ( request , question_id ): 
    return HttpResponse ( "You're voting on question %s ." % question_id )
    
def index(request):
    anyvariable = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': anyvariable}
    return render(request, 'polls/index.html', context)
    
def test(request):
    a_big_boy="Mark is a big boy"
    context = {'a_big_boy':a_big_boy}
    return render(request, 'polls/test.html', context)
    