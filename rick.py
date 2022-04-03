
from pprint import pprint as pp
import requests

a = requests.get('https://rickandmortyapi.com/api/character/?name=Morty').json()

pp(f"Name: {a['results'][0]['name']}")
pp(f"status: {a['results'][0]['status']}")
pp(f"species: {a['results'][0]['species']}")
pp(f"type: {a['results'][0]['type']}")
pp(f"gender: {a['results'][0]['gender']}")
pp(f"image: {a['results'][0]['image']}")
pp(f"episode: {a['results'][0]['episode']}")
pp(f"location: {a['results'][0]['location']}")

b = requests.get('https://rickandmortyapi.com/api/character/?name=rick').json()

pp(f"Name: {b['results'][0]['name']}")
pp(f"status: {b['results'][0]['status']}")
pp(f"species: {b['results'][0]['species']}")
pp(f"type: {b['results'][0]['type']}")
pp(f"gender: {b['results'][0]['gender']}")
pp(f"image: {b['results'][0]['image']}")
pp(f"episode: {b['results'][0]['episode']}")
pp(f"location: {b['results'][0]['location']}")

c = requests.get('https://rickandmortyapi.com/api/character/?name=summer').json()

pp(f"Name: {c['results'][0]['name']}")
pp(f"status: {c['results'][0]['status']}")
pp(f"species: {c['results'][0]['species']}")
pp(f"type: {c['results'][0]['type']}")
pp(f"gender: {c['results'][0]['gender']}")
pp(f"image: {c['results'][0]['image']}")
pp(f"episode: {c['results'][0]['episode']}")
pp(f"location: {c['results'][0]['location']}")

d = requests.get('https://rickandmortyapi.com/api/character/?name=jerry').json()

pp(f"Name: {d['results'][0]['name']}")
pp(f"status: {d['results'][0]['status']}")
pp(f"species: {d['results'][0]['species']}")
pp(f"type: {d['results'][0]['type']}")
pp(f"gender: {d['results'][0]['gender']}")
pp(f"image: {d['results'][0]['image']}")
pp(f"episode: {d['results'][0]['episode']}")
pp(f"location: {d['results'][0]['location']}")
#pp(b)

e = requests.get('https://rickandmortyapi.com/api/character/?name=Squanchy').json()

pp(f"Name: {e['results'][0]['name']}")
pp(f"status: {e['results'][0]['status']}")
pp(f"species: {e['results'][0]['species']}")
pp(f"type: {e['results'][0]['type']}")
pp(f"gender: {e['results'][0]['gender']}")
pp(f"image: {e['results'][0]['image']}")
pp(f"episode: {e['results'][0]['episode']}")
pp(f"location: {e['results'][0]['location']}")

f = requests.get('https://rickandmortyapi.com/api/character/?name=beth').json()

pp(f"Name: {f['results'][0]['name']}")
pp(f"status: {f['results'][0]['status']}")
pp(f"species: {f['results'][0]['species']}")
pp(f"type: {f['results'][0]['type']}")
pp(f"gender: {f['results'][0]['gender']}")
pp(f"image: {f['results'][0]['image']}")
pp(f"episode: {f['results'][0]['episode']}")
pp(f"location: {f['results'][0]['location']}")

g = requests.get('https://rickandmortyapi.com/api/character/?name=Krombopulos').json()

pp(f"Name: {g['results'][0]['name']}")
pp(f"status: {g['results'][0]['status']}")
pp(f"species: {g['results'][0]['species']}")
pp(f"type: {g['results'][0]['type']}")
pp(f"gender: {g['results'][0]['gender']}")
pp(f"image: {g['results'][0]['image']}")
pp(f"episode: {g['results'][0]['episode']}")
pp(f"location: {g['results'][0]['location']}")

h = requests.get('https://rickandmortyapi.com/api/character/?name=reverse').json()

pp(f"Name: {h['results'][0]['name']}")
pp(f"status: {h['results'][0]['status']}")
pp(f"species: {h['results'][0]['species']}")
pp(f"type: {h['results'][0]['type']}")
pp(f"gender: {h['results'][0]['gender']}")
pp(f"image: {h['results'][0]['image']}")
pp(f"episode: {h['results'][0]['episode']}")
pp(f"location: {h['results'][0]['location']}")

i = requests.get('https://rickandmortyapi.com/api/character/?name=birdperson').json()

pp(f"Name: {i['results'][0]['name']}")
pp(f"status: {i['results'][0]['status']}")
pp(f"species: {i['results'][0]['species']}")
pp(f"type: {i['results'][0]['type']}")
pp(f"gender: {i['results'][0]['gender']}")
pp(f"image: {i['results'][0]['image']}")
pp(f"episode: {i['results'][0]['episode']}")
pp(f"location: {i['results'][0]['location']}")