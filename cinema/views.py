from django.shortcuts import render, redirect
from .models import Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def add_movie(request):
    if request.method == 'POST':
        Movie.objects.create(
            name=request.POST['name'],
            director=request.POST['director'],
            year=request.POST['year'],
            show_time=request.POST['show_time'],
            ticket_price=request.POST['ticket_price'],
            available_seats=request.POST['available_seats']
        )
        return redirect('home')

    return render(request, 'add_movie.html')


def book_ticket(request, id):
    movie = Movie.objects.get(id=id)

    return render(request, 'confirm_ticket.html', {'movie': movie})


def confirm_booking(request, id):
    movie = Movie.objects.get(id=id)

    if movie.available_seats > 0:
        movie.available_seats -= 1
        movie.save()

    return render(request, 'ticket_success.html', {'movie': movie})