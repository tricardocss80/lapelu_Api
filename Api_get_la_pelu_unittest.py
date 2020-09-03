import requests
import json
import unittest


class TestLaPeluApis(unittest.TestCase):
    def test_token_la_pelu(self):
        with open('lapelu.json') as lapelu:
            data = json.load(lapelu)

        header = {'x-auth-token': data['token']}

        response = requests.get(data['url'], headers=header)

        my_response = response.json()

        print(response.status_code)
        print(my_response)
        self.assertEqual(data['status_code_ok'], response.status_code)
        self.assertTrue(True, my_response['result'])
        self.assertEqual(data['id_employees'][0], my_response['data']['employees'][0]['id'])
        self.assertEqual(data["id_locations"], my_response['data']['employees'][0]['locations'][0]['id'])
        self.assertEqual(data['name_employees'][0], my_response['data']['employees'][0]['name'])
        self.assertEqual(data['name_brand'], my_response['data']['employees'][0]['locations'][0]['name'])
        self.assertEqual(data['id_brand'], my_response['data']['employees'][0]['locations'][0]['brand']['id'])
        self.assertEqual(data['name_brand'], my_response['data']['employees'][0]['locations'][0]['brand']['name'])
