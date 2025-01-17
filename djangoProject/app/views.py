from django.shortcuts import render
from .models import ChaiVarity, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiForm

# Create your views here.
def all(request):
    chais = ChaiVarity.objects.all()
    
    return render(request, 'web/all.html', {'chais': chais})

def detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'web/detail.html', {'chai': chai})


def new(request):
    stores = None
    if request.method == 'POST':
        form = ChaiForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varieties=chai_variety).delete()
    else:
        form = ChaiForm()
        
    return render(request, 'web/new.html', {'stores': stores, 'form': form})