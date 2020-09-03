import requests
import json
import time

x_auth_token = '205b8aee07671127f2c9883586d62ebdd3f089d23caad41c85971d96b6de89149dbd53320b6c44c6d115b9ba647d517f659fb0fc28e95d720b4b8eeb'

header = {'x-auth-token': x_auth_token}

url = "https://stg-api.lapelu.com.ar/api/employee"

response = requests.get(url, headers=header)

if response.status_code == 200:
    print('Ok')
else:
    print('El status code no es 200')

response_json = json.loads(response.text)

time.sleep(1)

response1 = response_json['result']
response2 = response_json['data']['employees'][0]['id']
response3 = response_json['data']['employees'][0]['locations'][0]['id']
response4 = response_json['data']['employees'][0]['name']
response5 = response_json['data']['employees'][0]['locations'][0]['name']
response6 = response_json['data']['employees'][0]['locations'][0]['brand']['id']
response7 = response_json['data']['employees'][0]['locations'][0]['brand']['name']

def chequear_datos(respuesta, dato, resultado, mensaje):
    assert type(respuesta) == dato and respuesta == resultado, mensaje


chequear_datos(response1, bool, True, 'El resultado no es el esperado')
chequear_datos(response2, int, 265, 'El resultado no es el esperado')
chequear_datos(response3, int, 12, 'El resultado no es el esperado')
chequear_datos(response4, str, 'Andres Sosa', 'El resultado no es el esperado')
chequear_datos(response5, str, 'ETTIOS', 'El resultado no es el esperado')
chequear_datos(response6, int, 11, 'El resultado no es el esperado')
chequear_datos(response7, str, 'ETTIOS', 'El resultado no es el esperado')

