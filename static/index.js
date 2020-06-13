document.addEventListener('DOMContentLoaded', () =>{

    lang_request = new XMLHttpRequest();
    lang_request.open('GET', '/languages');

    lang_request.onload = () =>{
      const data = JSON.parse(lang_request.responseText);
      console.log(data.languages[0]);
      const select = document.querySelector('#select-lang');
      data.languages.forEach(lang => {
        const opt = document.createElement('option');
        opt.setAttribute('value', lang.code);
        opt.innerHTML = lang.name;
        select.appendChild(opt);
      });

    }
    lang_request.send();

    document.querySelector('#form-translate').onsubmit = () =>{
      const translate_request = new XMLHttpRequest();
      translate_request.open('POST', '/translate');

      translate_request.onload = () => {
        const data = JSON.parse(translate_request.responseText);

        if (data.success){
          let result = document.createElement('h6');
          result.innerHTML = `Translate from ${data.source} : ${data.result}`;
          document.querySelector('#results').appendChild(result);
        } else{
          alert(data.message);
        }
      }

      const data = new FormData();
      const input = document.querySelector('#to-translate').value;
      data.append('input', input);
      const select = document.querySelector('#select-lang');
      const opt = select.options[select.selectedIndex];
      data.append('target', opt.value);
      translate_request.send(data);

      return false;
    }
})
