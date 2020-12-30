import requests, json

URL = 'http://localhost:5000/track'

params = {
    'dept': 'Dept',
    'mcode': 'MCODE',
    'device': 'Device',
    'agency': 'Agency',
    'name': 'Name',
    'mobile': 'Mobile',
    'parent_name': 'ParentName',
    'parent_mobile': 'ParentMobile',
    'call_date': '2020-12-30',
    'image_url': 'https://example.com/image.jpg',
    'lon': 127.269311,
    'lat': 126.734086,
    'geom': 'GeomText',
    'init_time': '2020-12-30 16:59',
    'address': 'Address',
    # 'addr': settlements
}
params = (
    ('name', params['name']),
    ('mobile', params['mobile']),
    ('parent_name', params['parent_name']),
    ('parent_mobile', params['parent_mobile']),
    ('address', params['address']),
    ('image_url', params['image_url'])
)
headers = {}

res = requests.get(URL, headers=headers, params=params)