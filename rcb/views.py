from django.shortcuts import render
def virat(request):
    d={'virat_score':229,'dhoni_score':200}
    return render(request,'virat.html',d)
# Create your views here.
def dhoni(request):
    d={'virat_score':229,'dhoni_score':300,'jadeja_score':200}
    return render(request,'dhoni.html',d)