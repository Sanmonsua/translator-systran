import requests

def translate(source, target, input):
    url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"
    querystring = {"source":source,"target":target,"input":input}
    headers = {
        'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
        'x-rapidapi-key': "a03ee70f38msh668bb7cac193421p14c8a6jsncb658a19b591"
        }
    response_json = requests.request("GET", url, headers=headers, params=querystring).json()
    print(response_json)
    return response_json['outputs'][0]['output']

def detect(input):
    url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/nlp/lid/detectLanguage/document"
    querystring = {"input":input}

    headers = {
        'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
        'x-rapidapi-key': "a03ee70f38msh668bb7cac193421p14c8a6jsncb658a19b591"
        }

    response_json = requests.request("GET", url, headers=headers, params=querystring).json()
    return [l['lang'] for l in response_json['detectedLanguages']]

if __name__ == "__main__":
    print(translate('en', 'es', 'hello world'))
