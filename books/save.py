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
    title = obj["title"]
    authour = obj["authour"]
    url = obj["web_link"]["url"]
    image = obj["image"]
    dsc = obj["dsc"]
    date = obj["date"]
    #rank = obj["rank"]

    book = Book(
        title = title,
        authour = authour,
        url = url,
        image = image,
        dsc = dsc,
        date = date,
        active = True,
        #rank = rank
    )

    book.save()
    return True


def deactivate_all():
    Book.objects.all().update(active = False)

    return True



