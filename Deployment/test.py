import requests

url = 'http://127.0.0.1:5000'
given_data = {
    'Inches' : 13.3,
    'Ram' : 8,
    'Weight' : 1.3,
    'Screen_width' : 2560,
    'Screen_height' : 1600,
    'Frequency' : 2.4,
    'Memory_size' : 131072.0
}

response = requests.post(f'{url}/', json = given_data)

if response.status_code == 200 :
    print(f'Reponse de la prédiction : {response.text}')
else:
    print(f'Erreur : {response.status_code} - {response.text}')