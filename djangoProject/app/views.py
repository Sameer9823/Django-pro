from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all(request):
    chais = ChaiVarity.objects.all()
    
    return render(request, 'web/all.html', {'chais': chais})

def detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'web/detail.html', {'chai': chai})
