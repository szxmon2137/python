from bs4 import BeautifulSoup
import requests
import random

star_ratings = ["star-rating One", "star-rating Two", "star-rating Three", "star-rating Four", "star-rating Five"]
for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    print(f"\nSTRONA {i}\n")
    for book in books:
        price = str(book.find("p", class_="price_color").text).strip()[1:]
        availability = str(book.find("p", class_="instock availability").text).strip()
        title = str(book.find("h3").text).strip()

        rating = None
        while True:
            if rating == None:
                rand = random.randint(0, 4)
                rating = book.find("p", class_=star_ratings[rand])
            else:
                rating = f"{rand+1} gwiazdek"
                break

        if availability == "In stock":
            availability = "Tak"
        print(f"Tytuł książki: {title}, Cena: {price}, Dostępność: {availability}, Ocena: {rating}")
        
    