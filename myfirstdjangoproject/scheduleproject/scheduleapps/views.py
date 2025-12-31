from django.shortcuts import render
from .models import Table

# Create your views here.
def index(request):
    table = Table.objects.all()
    context = {'table': table}
    return render(request, 'tables\index.html', context)
