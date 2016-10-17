var doc=document.getElementById('id_favourite_musics')
doc.className+=" selectpicker"
doc.setAttribute("data-actions-box", "true")
doc.setAttribute("data-selected-text-format","count")
doc.required=false;

var email_input=document.getElementsByName('email')[0]
email_input.setAttribute("type", "email")
