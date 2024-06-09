import requests

# URL de l'API
url = 'http://100.107.141.200/add-data'

# Données à envoyer dans la requête PUT
data = {
    'rpm_counter2': value  # Remplacez 1234 par la valeur souhaitée
}

response = requests.put(url, json=data)


if response.status_code == 201:
    print("Data added successfully")
else:
    print(f"Error: {response.status_code}")
    print(response.json())