import requests

api_key = "c57f44575ba549d787810c575c539e52"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c57f44575ba549d787810c575c539e52"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Acess the article titles and description
for content in content["articles"]:
    print(content["description"])

