import requests

# URL
url = 'http://putrisqiana.pythonanywhere.com/api'

# Change the value of experience that you want to test
r = requests.post(url,json={'exp':200,})
print(r.json())
