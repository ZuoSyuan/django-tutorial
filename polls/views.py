#from django.http import Http404
#from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from polls.models import Poll, Choice
from django.utils import timezone

'''
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
    
def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
'''

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def newpoll(request):
    return render(request, 'polls/newpoll.html')
    
def addpoll(request):
	quest = request.POST.get('question', "")
	if(quest != ""):
		#'''
		pl = Poll(question=quest, pub_date=timezone.now())
		pl.save()
		num_choice = int(request.POST.get('num_input', 0))
		for i in range(1, num_choice+1):
			ct = request.POST.get('choice' + str(i), "")
			if(ct != ""):
				pl.choice_set.create( choice_text=ct, votes=0 )
		pl.save()
		#'''
		return HttpResponseRedirect('/polls/')
	else:
		return HttpResponseRedirect('/admin')
    
    
    
    
