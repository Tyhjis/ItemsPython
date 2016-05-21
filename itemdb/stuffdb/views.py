from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Item


class IndexView(generic.ListView):
	template_name = 'stuffdb/index.html'
	context_object_name = 'item_list'

	def get_queryset(self):
		return Item.objects.order_by('-created_at')

class DetailView(generic.DetailView):
	model = Item
	template_name = 'stuffdb/detail.html'

def update(request, item_id):
	item = get_object_or_404(Item, pk=item_id)
	try:
		new_name = request.POST['name']
		if not new_name:
			raise ValueError('empty string')
	except (ValueError):
		return render(request, 'stuffdb/detail.html', {
			'item': item,
			'error_message': "Something went wrong. You have to give a name.",
			})
	else:
		item.name = new_name
		item.save()
		return HttpResponseRedirect(reverse('stuffdb:detail', args=(item.id,)))
