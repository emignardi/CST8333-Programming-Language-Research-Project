from bs4 import BeautifulSoup
import requests
import pandas as pd

def main():
    current_page = 1
    guitar_list = []
    while (current_page <= 10):
        print(f"Currently scraping page {current_page}")
        url = "https://www.kijiji.ca/b-guitar/ontario/page-" + str(current_page) + "/c613l9004"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        for i in range(40):
            guitar = soup.find("li", attrs={"data-testid": f"listing-card-list-item-{i}"})
            item = {}
            item["Title"] = guitar.find("h3", attrs={"data-testid": "listing-title"}).text
            item["Price"] = guitar.find("p", attrs={"data-testid": "listing-price"}).text
            item["Link"] = guitar.find("a", attrs={"data-testid": "listing-link"})["href"]
            guitar_list.append(item)
        current_page += 1
    df = pd.DataFrame(guitar_list)
    df.to_excel("month-one/projects/KijijiScraper/guitars.xlsx", index=False)
    df.to_csv("month-one/projects/KijijiScraper/guitars.csv", index=False)

if __name__ == "__main__":
    main()