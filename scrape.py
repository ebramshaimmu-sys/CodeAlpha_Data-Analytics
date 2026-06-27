import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select(".product_pod")

data = []
for book in books:
    title = book.h3.a["title"]

    price_text = book.select_one(".price_color").text
    price = float(
        price_text.encode("ascii", "ignore").decode().replace("£", "").strip()
    )

    data.append({"title": title, "price": price})

df = pd.DataFrame(data)
print(df)
df.to_csv("books.csv", index=False)