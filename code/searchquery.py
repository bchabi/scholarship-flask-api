import json
import urllib.request
from urllib.error import HTTPError


#Attempt to load json data from url file
try:
    url_address = 'https://raw.githubusercontent.com/atilatech/atila-engineering-interview/master/data/scholarships.json'
    with urllib.request.urlopen(url_address) as url:
        data = json.loads(url.read())


except HTTPError as ex:
    print(ex.read())

#Specific keys of JSON dictionary to iterate through while doing search
keys_to_search = [
    'owner',
    'name',
    'slug',
    'slug_human_readable',
    'description',
    'criteria_info',
    'scholarship_url',
    'keywords',
    'activities',
    'eligible_schools',
    'eligible_programs',
    'specific_questions',
]


def searchQuery(word):
    """This function iterates through a list of JSON dict entries and assesses whether the argument provided
    is in any of the dict values."""

    results = []

    for i in range(len(data)): 
        for keys in keys_to_search:
            if (word in str(data[i][keys]).lower()): #converts value to lowercased string
                results.append(data[i])
                break

    if not results:
        return {'query' : word,
                'message': 'query not found'},404
    else:
        return {'query' : word,
        'results' : results}, 200
