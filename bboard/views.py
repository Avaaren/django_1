from django.http import HttpResponse
from django.template import loader

from .models import Bb

def index(request):
	bbs = Bb.object.order_by('-published')
	return render(request, 'bboard/	index.html', {'bbs': bbs})
# Create your views here.
