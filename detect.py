import requests
from api import translate
def detect(input):
    url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/nlp/lid/detectLanguage/document"
    querystring = {"input":input}

    headers = {
        'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
        'x-rapidapi-key': "a03ee70f38msh668bb7cac193421p14c8a6jsncb658a19b591"
        }

    response_json = requests.request("GET", url, headers=headers, params=querystring).json()
    return [l['lang'] for l in response_json['detectedLanguages']]

detected = detect('tratar')
for s in detected:
    try:
        t = translate(s, 'en', 'tratar')
        print(t)
    except KeyError:
        continue
