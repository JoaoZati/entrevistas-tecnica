d = {
    'pt-br': 'portugues brasileiro',
    'en-US': 'Inglês Americano'
}

print(f'd["en-US"]: {d["en-US"]}')
# print(f'd["es-EP"]: {d["es-EP"]}')
d['en'] = 'Inglês'
print(f'd["en"] = "Inglês": {d["en"]}')
d['en'] = 'Ingles'
print(f'd["en"] = "Ingles": {d["en"]}')

for k in d.keys():
    print('#########Keys##############')
    print(k)

for k in d.values():
    print('########Values##############')
    print(k)

for k, v in d.items():
    print('#########Keys and value##############')
    print(k, v)
