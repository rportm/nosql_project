import requests

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=metal%20raiders"

response = requests.get(url)

print(response.json())