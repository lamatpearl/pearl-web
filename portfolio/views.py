from django.shortcuts import render
from .models import Project, Skill, Education

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def education(request):
    # Fetch all records from the database
    all_edu = Education.objects.all()
    # The key 'educations' MUST match the name in your {% for %} loop
    return render(request, 'portfolio/educations.html', {'educations': all_edu})

def contact(request):
    return render(request, 'portfolio/contact.html')