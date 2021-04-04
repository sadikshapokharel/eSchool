from django.shortcuts import render
from .models import Semester, Subject, Chapter, Resource, Banner

# Create your views here.
def home(request):
	context = {
		 'semesters' : Semester.objects.all(),
		 'subjects' : Subject.objects.all(),
		 'chapters' : Chapter.objects.all(),
		 'resources' : Resource.objects.all(),
		 'banners' : Banner.objects.all(),
	}
	return render(request, 'main/index.html', context)

def subjects(request):
	context = {
		'semester_name' : Category.objects.get(pk = id),
		'subjects' : Subject.objects.filter(semester=id)
	}

