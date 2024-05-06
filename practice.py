import requests

api_key = '3cc5d38d-b9d0-4eea-8976-42154867fa89'
word = 'apple'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)