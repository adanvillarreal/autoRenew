import requests
import sys

s = requests.Session()
if len(sys.argv) != 4:
    print 'Usage: python renovar.py name code pin'
    sys.exit()
r = s.post('https://millenium.itesm.mx/patroninfo*spi', data = {
    'name': '%s' % sys.argv[1],
    'code': '%s' % sys.argv[2],
    'pin': '%s' % sys.argv[3],
    'submit.x': '70',
    'submit.y': '7'
})
r2 = s.post('https://millenium.itesm.mx/patroninfo*spi/%s/items' % r.url[46: 52], data = {
    'currentsortorder': 'current_checkout',
    'renewall': 'SI'
})
print r2.text
