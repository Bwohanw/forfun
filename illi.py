import requests

key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImdpdGh1YjU5NTA5NzU2IiwiZW1haWwiOm51bGwsInByb3ZpZGVyIjoiZ2l0aHViIiwicm9sZXMiOlsiVVNFUiJdLCJleHAiOjE3MzcxMzk3MTYuNTQ4LCJpYXQiOjE3MzcwNTMzMTZ9.x0zQJQnPi9z-y-xjgRFUDGi9SySWdTPuMnyAWrcxpU0"

header = {"Authorization": key, "Content-Type": "application/json"}

response = requests.get('https://adonix.hackillinois.org/registration/challenge/', headers=header)

# print(len(response.json()['alliances']))
json = response.json()
json = {'alliances': [['Poseidon', 'Theia'], ['Poseidon', 'Eros'], ['Iapetus', 'Theia'], ['Theia', 'Zeus'], ['Theia', 'Eris'], ['Aphrodite', 'Zeus'], ['Zeus', 'Erebus'], ['Zeus', 'Hephaestus'], ['Selene', 'Erebus'], ['Erebus', 'Harmonia'], ['Erebus', 'Iris'], ['Asclepius', 'Harmonia'], ['Harmonia', 'Chronos'], ['Harmonia', 'Tyche'], ['Demeter', 'Chronos'], ['Chronos', 'Eros'], ['Chronos', 'Uranus'], ['Poseidon', 'Iapetus'], ['Poseidon', 'Eris'], ['Poseidon', 'Aphrodite'], ['Poseidon', 'Zeus'], ['Poseidon', 'Hephaestus'], ['Poseidon', 'Selene'], ['Poseidon', 'Erebus'], ['Poseidon', 'Harmonia'], ['Poseidon', 'Tyche'], ['Poseidon', 'Demeter'], ['Poseidon', 'Chronos'], ['Poseidon', 'Uranus'], ['Eros', 'Iapetus'], ['Eros', 'Theia'], ['Eros', 'Eris'], ['Eros', 'Aphrodite'], ['Eros', 'Zeus'], ['Eros', 'Hephaestus'], ['Eros', 'Selene'], ['Eros', 'Erebus'], ['Eros', 'Iris'], ['Eros', 'Asclepius'], ['Eros', 'Harmonia'], ['Eros', 'Tyche'], ['Eros', 'Demeter'], ['Iapetus', 'Eris'], ['Iapetus', 'Aphrodite'], ['Iapetus', 'Zeus'], ['Iapetus', 'Hephaestus'], ['Iapetus', 'Selene'], ['Iapetus', 'Erebus'], ['Iapetus', 'Iris'], ['Iapetus', 'Asclepius'], ['Iapetus', 'Harmonia'], ['Iapetus', 'Demeter'], ['Iapetus', 'Uranus'], ['Theia', 'Aphrodite'], ['Theia', 'Hephaestus'], ['Theia', 'Selene'], ['Theia', 'Erebus'], ['Theia', 'Iris'], ['Theia', 'Asclepius'], ['Theia', 'Harmonia'], ['Theia', 'Tyche'], ['Theia', 'Demeter'], ['Theia', 'Chronos'], ['Theia', 'Uranus'], ['Eris', 'Aphrodite'], ['Eris', 'Zeus'], ['Eris', 'Hephaestus'], ['Eris', 'Selene'], ['Eris', 'Erebus'], ['Eris', 'Iris'], ['Eris', 'Asclepius'], ['Eris', 'Harmonia'], ['Eris', 'Tyche'], ['Eris', 'Demeter'], ['Eris', 'Chronos'], ['Eris', 'Uranus'], ['Aphrodite', 'Hephaestus'], ['Aphrodite', 'Selene'], ['Aphrodite', 'Erebus'], ['Aphrodite', 'Iris'], ['Aphrodite', 'Asclepius'], ['Aphrodite', 'Harmonia'], ['Aphrodite', 'Tyche'], ['Aphrodite', 'Demeter'], ['Aphrodite', 'Chronos'], ['Aphrodite', 'Uranus'], ['Zeus', 'Selene'], ['Zeus', 'Iris'], ['Zeus', 'Asclepius'], ['Zeus', 'Harmonia'], ['Zeus', 'Tyche'], ['Zeus', 'Demeter'], ['Zeus', 'Chronos'], ['Zeus', 'Uranus'], ['Hephaestus', 'Selene'], ['Hephaestus', 'Iris'], ['Hephaestus', 'Asclepius'], ['Hephaestus', 'Harmonia'], ['Hephaestus', 'Tyche'], ['Hephaestus', 'Demeter'], ['Hephaestus', 'Chronos'], ['Hephaestus', 'Uranus'], ['Selene', 'Iris'], ['Selene', 'Asclepius'], ['Selene', 'Harmonia'], ['Selene', 'Tyche'], ['Selene', 'Chronos'], ['Selene', 'Uranus'], ['Erebus', 'Asclepius'], ['Erebus', 'Tyche'], ['Erebus', 'Demeter'], ['Erebus', 'Chronos'], ['Erebus', 'Uranus'], ['Iris', 'Poseidon'], ['Iris', 'Asclepius'], ['Iris', 'Harmonia'], ['Iris', 'Tyche'], ['Iris', 'Demeter'], ['Iris', 'Chronos'], ['Iris', 'Uranus'], ['Asclepius', 'Poseidon'], ['Asclepius', 'Tyche'], ['Asclepius', 'Demeter'], ['Asclepius', 'Chronos'], ['Asclepius', 'Uranus'], ['Harmonia', 'Demeter'], ['Harmonia', 'Uranus'], ['Tyche', 'Iapetus'], ['Tyche', 'Demeter'], ['Tyche', 'Chronos'], ['Tyche', 'Uranus'], ['Demeter', 'Selene'], ['Demeter', 'Uranus'], ['Chronos', 'Iapetus'], ['Uranus', 'Eros'], ['Mnemosyne', 'Rhea'], ['Mnemosyne', 'Prometheus'], ['Prometheus', 'Aeolus'], ['Heracles', 'Rhea'], ['Mnemosyne', 'Aeolus'], ['Prometheus', 'Heracles'], ['Prometheus', 'Rhea'], ['Aeolus', 'Heracles'], ['Aeolus', 'Rhea'], ['Heracles', 'Mnemosyne'], ['Dionysus', 'Deimos'], ['Deimos', 'Hypnos'], ['Dionysus', 'Hypnos'], ['Hera', 'Tartarus'], ['Tartarus', 'Ares'], ['Hera', 'Ares'], ['Nike', 'Pan'], ['Pan', 'Oceanus'], ['Oceanus', 'Nike'], ['Coeus', 'Hermes'], ['Hyperion', 'Artemis'], ['Phoebe', 'Persephone'], ['Hecate', 'Phobos']], 'people': {'Poseidon': -51560036, 'Eros': -196632210, 'Iapetus': 31815119, 'Theia': 215989352, 'Eris': -71312603, 'Aphrodite': -32137854, 'Zeus': 62617021, 'Hephaestus': 52598370, 'Selene': 5123816, 'Erebus': 158562498, 'Iris': -3444743, 'Asclepius': -9400710, 'Harmonia': -102884456, 'Tyche': 150595221, 'Demeter': 71711530, 'Chronos': -18806844, 'Uranus': -199636981, 'Mnemosyne': -722113, 'Prometheus': -72018667, 'Aeolus': -11149507, 'Heracles': 29621627, 'Rhea': 118124697, 'Dionysus': -16456327, 'Deimos': 38079844, 'Hypnos': 20656678, 'Hera': 30878997, 'Tartarus': 76368832, 'Ares': -56409952, 'Nike': -126551432, 'Pan': -49163971, 'Oceanus': 200508746, 'Coeus': -25626089, 'Hermes': 60157779, 'Hyperion': 67817940, 'Artemis': 5696194, 'Phoebe': -30590005, 'Persephone': 80374378, 'Hecate': 178844864, 'Phobos': -112503353, 'Nemesis': 31812457, 'Tethys': 43422521, 'Themis': 60855333, 'Gaia': 60023030, 'Thanatos': 74351718, 'Pontus': 26463553}, 'attempts': 1, 'complete': False}

print(json.keys())
alliances = json['alliances']
people = json['people']
print(json['attempts'])


# graph construction
nodes = list(people.keys())
edges = {}
for node in nodes:
    edges[node] = []

for alliance in alliances:
    edges[alliance[0]].append(alliance[1])
    edges[alliance[1]].append(alliance[0])



seen = set()

def bfs(node):
    power = 0
    queue = [node]
    seen.add(node)
    while (len(queue) != 0):
        curr = queue.pop(0)
        power += people[curr]
        for neighbor in edges[curr]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return power

maxpower = 0
for node in nodes:
    if node in seen:
        continue
    power = bfs(node)
    if (power > maxpower):
        maxpower = power
    print(power)

print()
print(maxpower)


for person in people.keys():
    if people[person] == maxpower:
        print("wow this guy mega strong")

# r = requests.post('https://adonix.hackillinois.org/registration/challenge/', headers=header, json={"solution":maxpower})
# print(r.status_code)
# print(r.text)