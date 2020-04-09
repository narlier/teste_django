from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Pergunta, Resposta


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_pergunta_list'

    def get_queryset(self):
        """ Retorna as cinco ultimas perguntas."""
        return Pergunta.objects.order_by('-data_publicacao')[:5]


class DetailView(generic.DetailView):
    model = Pergunta
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Pergunta
    template_name = 'polls/results.html'


def vote(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        selected_resposta = pergunta.resposta_set.get(
            pk=request.POST['resposta'])
    except (KeyError, Resposta.DoesNotExist):
        # Redisplay the pergunta voting form.
        return render(request, 'polls/detail.html', {
            'pergunta': pergunta,
            'error_message': "Você não selecionou uma resposta.",
        })
    else:
        selected_resposta.votos += 1
        selected_resposta.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(pergunta.id,)))
