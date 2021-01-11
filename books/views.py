from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Book, ReadingList
from . import info
#from django.http import HttpResponse

# Create your views here.
def index(request):
    info.finalcheck()
    books = Book.objects.filter(active=True).order_by('rank')
    
    states = []

    if request.user.is_authenticated:
        reading_list = ReadingList.objects.get(user = request.user)
        for book in books:
            if book in reading_list.books.all():
                states.append(True)
            else:
                states.append(False)
    else:
        states = [False] * 10

    book_states = zip(books, states)
    book_states2 = zip(books, states)

    return render(request, "books/index.html", {
        "book_states": book_states,
        "book_states_2": book_states2
    })

def update_list(request):
    if request.method == "POST":
        current_list = ReadingList.objects.get(user = request.user)

        title = request.POST["title"]

        new_book = Book.objects.get(title=title)

        if new_book in current_list.books.all():
            current_list.books.remove(new_book)
        else:
            current_list.books.add(new_book)

        return redirect("/")  

    else:
        return redirect("/")

def readinglist_view(request):
    if request.user.is_authenticated:
        reading_list = ReadingList.objects.get(user = request.user)
        reading_list.refresh_from_db()

        return render(request, "books/readinglist.html", {
            "readinglist": reading_list.books.all()
        })
    else:
        return render(request, "books/readinglist.html")



