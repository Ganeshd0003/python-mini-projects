import requests
query = input("Enter they keyword you wnat to search the news:")
key = "put_api_key_here"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-18&sortBy=publishedAt&apiKey={key}"

print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1,article["title"], article['url'])
    print("\n***********************************************\n")