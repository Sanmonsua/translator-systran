from flask import Flask, render_template, request
import csv
from api import *

api_url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"
app = Flask(__name__)

class Language():
    def __init__(self, code, name):
        self.code = code
        self.name = name


f = open('languages.csv')
reader = csv.reader(f)
languages = []
for code, name in reader:
    l = Language(code=code, name=name)
    languages.append(l)

source = 'en'

@app.route('/')
def index():
    return render_template('index.html', languages=languages)


def get_result(sources, target, input):
    for s in sources:
        try:
            return (s.name, translate(s.code, target, input))
        except:
            continue
    return None

@app.route('/translate', methods=['POST'])
def result():
    target = request.form.get('target')
    input = request.form.get('input')
    detected = detect(input)
    sources = [l for l in languages if l.code in detected]
    result = get_result(sources, target, input)
    print(result)
    if result != None:
        lang, translate = result
        return render_template('translate.html', translate=translate, lang=lang)
    return render_template('error.html', message="I wasn't possible to translate the introduced word")
