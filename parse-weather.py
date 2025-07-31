import json

f= open('f.json')


data=json.load(f)
print(data)

'''
for i in data['current']:
    print(i)
'''
f.close()