import core
import json

# Settings
ps1 = '\033[94m::\033[0m'
tracks: list = json.load(open('tracks.json'))
liked: list = json.load(open('liked.json'))

for item in tracks:
    
    print(ps1, 'Saving', item)
    
    url = core.finder.fetch_url(item['title'], item['artist'])
    
    print(ps1, '->', url)
    
    item['url'] = url
    liked.append(item)

open('liked.json', 'w').write(json.dumps(liked, indent = 3))
open('tracks.json', 'w').write('[]') # reset tracks