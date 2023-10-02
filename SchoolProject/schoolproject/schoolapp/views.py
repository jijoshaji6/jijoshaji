from django.shortcuts import render
from django.http import JsonResponse
from .models import Course
from .forms import CategoryForm
# Create your views here.


def store(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            course = form.cleaned_data['course']
    else:
        form = CategoryForm()

    return render(request, 'store.html', {'form': form})

def get_course(request):
    department = request.GET.get('department')
    course_options = []
    if department == 'civil':
        course_options = [('Construction Management'), ( 'Structural')]
    elif department == 'mech':
        course_options = [( 'Machinery'), ( 'Automobile')]
    elif department == 'cs':
        course_options = [( 'Machine Learning'), ( 'Python')]
    elif department == 'elec':
        course_options = [('Power'), ( 'Telecommunication')]
    return JsonResponse({'course': course_options})
def index(request):
    return render(request,'index.html')
