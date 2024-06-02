import requests
from bs4 import BeautifulSoup

def scrape_imdb_mobile(url):
    # Send a GET request to the IMDb mobile URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the movie titles and ratings
        movie_titles = soup.find_all('h3', class_='lister-item-header')
        movie_ratings = soup.find_all('div', class_='ratings-bar')

        # Iterate over the movie titles and ratings and print them
        for title, rating in zip(movie_titles, movie_ratings):
            movie_title = title.a.text
            movie_rating = rating.strong.text
            print(f"Title: {movie_title}, Rating: {movie_rating}")
    else:
        print("Failed to retrieve data from IMDb mobile site.")

# URL of the IMDb mobile page you want to scrape
imdb_mobile_url = "https://m.imdb.com/chart/top/"
scrape_imdb_mobile(imdb_mobile_url)
