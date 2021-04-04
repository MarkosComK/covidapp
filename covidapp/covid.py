import requests

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

inputCountry = str(input('Digite o país que você deseja obter os dados: ')).capitalize()

if inputCountry == 'Brasil':
    inputCountry = inputCountry.replace('s', 'z')


querystring = {"country":"{}".format(inputCountry)}

headers = {
    'x-rapidapi-key': "4b5862d003msh1cc0ac5d5f6cb73p1c03c1jsn6112c7f6628d",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


dic = response.json()['data']
dic['Casos ecuperados'] = dic.pop('recovered')
dic['Mortes confirmadas'] = dic.pop('deaths')
dic['Casos Confirmados'] = dic.pop('confirmed')
dic['Última data checada'] = dic.pop('lastChecked')
dic['Última data reportada'] = dic.pop('lastReported')
dic['Localização'] = dic.pop('location')

if dic['Localização'] == 'Global':
    print('País não encontrado verifique os dados')
else:
    for status, valor in dic.items():
        print(f'{status} : {valor}')