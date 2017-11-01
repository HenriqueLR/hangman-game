#coding: utf-8

from random import randint
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from main.models import Words
from main.decorators import ajax_required


def home(request):
	template_name = 'main/home.html'
	context = {}
	return render(request, template_name, context)


@ajax_required
def sort(request):
	if request.method == 'GET':
		words = Words.objects.all()
		count_words = words.count()
		sort_word = words.get(id_words=randint(1, count_words))

		request.session['word'] = sort_word.word.lower()
		request.session['count_error'] = 0
		request.session['count_assert'] = 0

		context = {
			'len_words': len(sort_word.word),
			'count_error': request.session['count_error'],
		}

		data = {'context': context, 'message': 'start game',}
		#app_list.sort(key=lambda x: x['name'])

		return JsonResponse(data, status=201)


def game_over(request):
	data = {
		'context': {
			'result': 'false',
			'len_words': len(request.session['word']),
			'count_error': request.session['count_error']
		},
		'message': 'Game Over',
	}
	return JsonResponse(data, status=200)

def finish(request):
	data = {
		'context': {
			'result': 'finish',
			'len_words': len(request.session['word']),
			'count_error': request.session['count_error']
		},
		'message': 'Parabens você acertou a palavra',
	}
	return JsonResponse(data, status=200)


def assert_word(request):
	if request.method == 'POST':
		data = {
			'context': {},
			'message': '',
		}

		if not request.session.has_key('word'):
			data['message'] = 'Não é possivel escolher uma letra, antes de sortear uma palavra'
			return JsonResponse(data, status=403)

		key = request.POST.get('key').lower()
		word = request.session['word']
		index_word = []

		if not key or key not in word:
			if request.session['count_error'] == 6:
				return game_over(request)
			request.session['count_error'] += 1
		else:
			if request.session['count_assert'] == len(word):
				return finish(request)

			index_word = [x for x,y in enumerate(word) if y == key]
			request.session['count_assert'] += len(index_word)

		context = {
			'index_word':index_word,
			'count_error': request.session['count_error'],
			'key': key,
		}
		data['context'] = context

		return JsonResponse(data, status=200)


def clear_sessions(request):
	if request.method == 'GET':
		try:
			del request.session['word']
			del request.session['count_error']
		except KeyError as Error:
			pass

		context = {
			'context': {},
			'message': 'clear sort words',
		}

		return JsonResponse(context, status=200)