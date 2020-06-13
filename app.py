from flask import Flask, render_template, request, jsonify
import csv
from api import *

api_url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"
app = Flask(__name__)

f = open('languages.csv')
reader = csv.reader(f)
languages = []
for code, name in reader:
    l = {
        "code":code,
        "name":name
    }
    languages.append(l)

@app.route('/languages')
def get_languages():
    return jsonify({
        "languages":languages
    })


@app.route('/')
def index():
    return render_template('index.html')


def get_result(sources, target, input):
    for s in sources:
        try:
            return (s['name'], translate(s['code'], target, input))
        except:
            continue
    return None

@app.route('/translate', methods=['POST'])
def result():
    target = request.form.get('target')
    input = request.form.get('input')
    detected = detect(input)
    sources = [l for l in languages if l['code'] in detected]
    result = get_result(sources, target, input)
    if result != None:
        lang, translate = result
        return jsonify({
            "success":True,
            "source":lang,
            "result":translate
        })
    return jsonify({
        "success":False,
        "message":"It wasn't possible to translate the introduced text. Check ortography or others typos."
    })
