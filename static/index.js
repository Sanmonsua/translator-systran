document.addEventListener('DOMContentLoaded', function onDocumentLoad() {
	requestLanguages()

	document.querySelector('#form-translate').onsubmit = onSubmitForm
})

function requestLanguages() {
	var langRequest = new XMLHttpRequest()
	langRequest.open('GET', '/languages')

	langRequest.onload = () => {
		var { languages } = JSON.parse(langRequest.responseText)
		var select = document.querySelector('#select-lang')
		languages.forEach(loadLang)

		function loadLang(language) {
			var { code, name } = language
			var opt = document.createElement('option')
			opt.setAttribute('value', code)
			opt.innerHTML = name
			select.appendChild(opt)
		}
	}
	langRequest.send()
}

function onSubmitForm() {
	const translateRequest = new XMLHttpRequest()
	translateRequest.open('POST', '/translate')

	translateRequest.onload = function loadTranslateRequest() {
		var { success, source, result, message } = JSON.parse(
			translateRequest.responseText
		)

		if (success) {
			let resultElement = document.createElement('h6')
			result.innerHTML = `Translate from ${source} : ${result}`
			document.querySelector('#results').appendChild(resultElement)
		} else {
			alert(message)
		}
	}

	var data = new FormData()
	var input = document.querySelector('#to-translate').value
	data.append('input', input)
	var select = document.querySelector('#select-lang')
	var opt = select.options[select.selectedIndex]
	data.append('target', opt.value)
	translateRequest.send(data)

	return false
}
