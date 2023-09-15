import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json() #transforma el str en archivo json, y así python lo reconocerá como una lista 
    for category in categories: #ahora se puede iterar y trabajar en el
        print(category['name'])