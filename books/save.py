from .models import Book
import requests

def check_db(obj):
    """
    returns True if it is currently up to date
    """
    first_date = obj["date"]
    if len(Book.objects.filter(date = first_date, active = True)) != 10:
        return False
    else:   
        return True



def create_obj(obj):
    #old_books = Book.objects.all()

    try:
        book = Book.objects.get(title = obj["title"], authour = obj["authour"])

        book.rank = obj["rank"]
        book.active = True
        book.date = obj["date"]

    except Book.DoesNotExist:

        book = Book(
            title = obj["title"],
            authour = obj["authour"],
            url = obj["web_link"]["url"],
            image = obj["image"],
            dsc = obj["dsc"],
            date = obj["date"],
            active = True,
            rank = obj["rank"]
        )

    book.save()


def deactivate_all():
    Book.objects.all().update(active = False)

    return True



