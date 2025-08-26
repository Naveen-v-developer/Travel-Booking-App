from django.shortcuts import render, get_object_or_404
from .models import TravelOption
from .forms import TravelFilterForm

def travel_list_view(request):
    form = TravelFilterForm(request.GET or None)
    travels = TravelOption.objects.all()
    if form.is_valid():
        if form.cleaned_data['type']:
            travels = travels.filter(type=form.cleaned_data['type'])
        if form.cleaned_data['source']:
            travels = travels.filter(source__icontains=form.cleaned_data['source'])
        if form.cleaned_data['destination']:
            travels = travels.filter(destination__icontains=form.cleaned_data['destination'])
        if form.cleaned_data['date']:
            travels = travels.filter(date_time__date=form.cleaned_data['date'])
    return render(request, 'travels/travel_list.html', {'travels': travels, 'form': form})

def travel_detail_view(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    return render(request, 'travels/travel_detail.html', {'travel': travel})
