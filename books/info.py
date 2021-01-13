import requests
from . import save


def retrieve_epl():
    response = requests.get("https://data.edmonton.ca/resource/qdgm-hex6.json?$order=date%20DESC,%20holds%20DESC")

    if response.status_code == 200:
        data = response.json()
        
        #if it is up to date dont pull new data
        if save.check_db(data[0]):
            return None
        else:
            save.deactivate_all()
            return data
    else:
        return None

def get_top_ten(data):
    first_date = data[0]["date"]
    
    index = 0
    holds_data = {}
    while data[index]["date"] == first_date:
        
        if data[index]["title"] in holds_data:
            holds_data["title"][1] += data[index]["holds"]
        else:
            holds_data[data[index]["title"]] = [data[index], data[index]["holds"]]

        index += 1
    
    sorted_data = sorted(holds_data, key=holds_data.get()[1], reverse = True)
  
    data = [obj[0] for obj in sorted_data.values()][0:10]

    return data
    
    

    

def change_title_author(data):
    for obj in data:
        title = obj["title"]
        raw_title = title.split("/")

        new_title = raw_title[0].strip().split()
        obj["title"] = " ".join([word.capitalize() for word in new_title])


        raw_auth = raw_title[1].strip().split()
        if raw_auth[0] == "by":
            raw_auth = raw_auth[1::]
    
        obj["authour"] = " ".join(raw_auth)
        
        #obj.pop('date', None)

def retrieve_google(title, authour):
    google_rsp = requests.get(f"https://www.googleapis.com/books/v1/volumes/?q={title}+inauthor:{authour}&fields=items(volumeInfo(description),id)")
    
    if google_rsp.status_code == 200:
        raw_data = google_rsp.json()["items"]

        for test_obj in raw_data:
            if "description" in test_obj["volumeInfo"]:
                obj = test_obj
                dsc = obj["volumeInfo"]["description"]
                break
        else:
            dsc = "No description available"

    """
    link = f"https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyBMFZ8q7dLwkWbmlC94QRBdCr9ZzbyAgqA&cx=46c33dd388e2032df&imgSize=large&searchType=image&q={title} cover"

    img_rsp = requests.get(link)
    
    if img_rsp.status_code == 200:
        img_data = img_rsp.json()["items"][0]

        img = img_data["link"]
    
    else:
        """
    img = "https://unmpress.com/sites/default/files/default_images/no_image_book.jpg"

    return dsc, img
    

def combine(data):
    i = 1
    for obj in data:
        dsc, img = retrieve_google(obj["title"], obj["authour"])
        obj["dsc"] = dsc
        obj["image"] = img
        obj["rank"] = i
        i+=1
    return data

def finalcheck():
    data = retrieve_epl()

    if data:
        data = get_top_ten(data)
        change_title_author(data)
        new_data = combine(data)
        for obj in new_data:
            save.create_obj(obj)
        
    
