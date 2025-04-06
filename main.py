import requests
from Send_email import send_email

api_key = "c57f44575ba549d787810c575c539e52"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c57f44575ba549d787810c575c539e52"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for content in content["articles"]:
    send_email(content["description"])


