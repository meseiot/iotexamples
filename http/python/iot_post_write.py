"""
  Python ile IoThook REST Api Testi

  Kod çalıştırıldığında APIKEY ile doğrulama gerçekleştirilir.
  Cihaz api_key ile ilgili veriler IoThook a post edilir.

  Bu ornek IotHook servisine veri almak/gondermek icin baslangic seviyesinde
  testlerin yapilmasini amaclamaktadir.

  v1 : 20 Eylul 2017
  v2 : 19 Agustos 2019
  v3 : 21 Ekim 2021
  v4 : 31 Ekim 2022

  Sahin MERSIN - electrocoder

  Daha fazlasi icin

  http://www.iothook.com
  https://www.mesebilisim.com
  https://mesemekatronik.com
  https://electrocoder.blogspot.com
  https://github.com/meseiot/iotexamples

  sitelerine gidiniz.

  Yayin : http://mesebilisim.com

  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

  http://www.apache.org/licenses/
"""

import json
import pprint
import random
import requests

headers = {'Content-type': 'application/json'}

# demo account API_KEY
# https://iothook.com/en/device/data/650/
# 650 - iot_examples
API_KEY = '21579c1e874fda7276d94f3c'  # write api key
url = 'http://iothook.com/api/update/'

data = {
    'api_key': API_KEY,
    'field_1': random.randint(1, 10),
    'field_2': round(random.uniform(0.0, 10.0), 2),
    'field_3': round(random.uniform(0.0, 10.0), 2),
}

data_json = json.dumps(data)

response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())
