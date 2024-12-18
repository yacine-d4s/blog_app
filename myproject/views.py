# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    """Show home page"""
    return render(request, "home.html")


def about(request):
    """Show about page"""
    return render(request, "about.html")
