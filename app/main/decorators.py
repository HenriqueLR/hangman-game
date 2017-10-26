#coding: utf-8

from django.http import HttpResponseForbidden


def ajax_required(view):
	def wrap(request, *args, **kwargs):
		if not request.is_ajax():
			return HttpResponseForbidden('Acesso negado')
		return view(request, *args, **kwargs)
	wrap.__doc__ = view.__doc__
	wrap.__name__ = view.__name__
	return wrap