from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Item

def index(request):
	item_list = Item.objects.order_by('-created_at')
	context = {'item_list': item_list}
	return render(request, 'stuffdb/index.html', context)

def detail(request, item_id):
	item = get_object_or_404(Item, pk=item_id)
	return render(request, 'stuffdb/detail.html', { 'item': item })
