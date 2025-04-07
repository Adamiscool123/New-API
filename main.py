import requests
from Send_email import send_email

api_key = "c57f44575ba549d787810c575c539e52"
url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&"
       "category=business"
       "&apiKey=c57f44575ba549d787810c575c539e52&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
for content in content["articles"][0:20]:
    if content['title'] is not None:
        body += str(content["description"]) + "\n" + str(content['url'] + 2*"\n")
send_email(body)


