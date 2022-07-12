const form = document.getElementById('form');
const nombre = document.getElementById('name');
const email = document.getElementById('email');
const asunto = document.getElementById('asunt');
const mensaje = document.getElementById('msj');


form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});

function checkInputs() {
	const nombreValue = nombre.value.trim();
	const emailValue = email.value.trim();
    const asuntoValue = asunto.value.trim();
    const mensajeValue = mensaje.value.trim();

	
	if(nombreValue === '') {
		setErrorFor(nombre, 'Complete el nombre');
	} else {
		setSuccessFor(nombre);
	}

	if(emailValue === '') {
		setErrorFor(email, 'El email no puede estar en blanco');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Ingrese un email válido');
	} else {
		setSuccessFor(email);
	}

    if(asuntoValue === '') {
		setErrorFor(asunto, 'Complete el asunto');
	} else {
		setSuccessFor(asunto);
	}

    if(mensajeValue === '') {
		setErrorFor(mensaje, 'Escriba su mensaje');
	} else {
		setSuccessFor(mensaje);
	}

    
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}