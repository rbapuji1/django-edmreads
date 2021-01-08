from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from books import info
from books.models import Book, ReadingList
from books import views as v

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #request.user.id make a readinglist()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            new_readinglist = ReadingList(user = new_user)
            new_readinglist.save()
            login(request, new_user)
            return redirect("/") 
    else:
        form = RegisterForm()


    return render(request, "register/register.html", {
        "form": form
    })

def logout_view(request):
    logout(request)
    """
    info.finalcheck()
    books = Book.objects.filter(active=True)
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

    return render(request, "books/indexv4.html", {
        "book_states": book_states
    })
    """

    #v.index()

    