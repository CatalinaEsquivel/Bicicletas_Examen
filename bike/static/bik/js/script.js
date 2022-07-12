
/*Validaciones Java Formulario de registro*/

const form = document.getElementById('form');
const nombre = document.getElementById('nombre');
const emaill = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});

function checkInputs() {
	const nombreValue = nombre.value.trim();
	const emaillValue = emaill.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
	if(nombreValue === '') {
		setErrorFor(nombre, 'El nombre no debe estar vacío');
	} else {
		setSuccessFor(nombre);
	}
	
	if(emaillValue === '') {
		setErrorFor(emaill, 'Introduzca su email');
	} else if (!isEmail(emaillValue)) {
		setErrorFor(emaill, 'Email no válido');
	} else {
		setSuccessFor(emaill);
	}
	
	if(passwordValue === '') {
		setErrorFor(password, 'Ingrese una contraseña');
	} else {
		setSuccessFor(password);
	}
	
	if(password2Value === '') {
		setErrorFor(password2, 'La contraseña no debe estar vacía');
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, 'Las contraseñas no coinciden');
	} else{
		setSuccessFor(password2);
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