import requests
import xmltodict

url = 'http://www.cbr.ru/scripts/XML_val.asp/'
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)

my_array = []
for item in data['Valuta']['Item']:
    my_set = [item['ParentCode'], item['Name'], item['Nominal']];
    my_array.append(my_set)
    print(my_set)
