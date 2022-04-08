"use strict"
let nombre = document.getElementById("id_nombre");
let apellido1 = document.getElementById("id_apellido1");
let apellido2 = document.getElementById("id_apellido2");
let dni = document.getElementById("id_dni");
let texto = document.getElementById("id_formulario");
let enviar=document.getElementById("enviar");
let alerta=document.getElementById("errorFormulario");


window.addEventListener("load", () => {

	nombre.focus();
	nombre.addEventListener("focusout", validarNombre);
	apellido1.addEventListener("blur", validarApe1);
	apellido2.addEventListener("focusout", validarApe2);
	dni.addEventListener("blur", validarDni);
	

})


 function validarNombre(){
 	let expresion =/^[a-zA-ZÀ-ÿ\u00f1\u00d1\s]{2,20}$/;
 	let spam = document.getElementById("errorNombre"); 
 	if (!expresion.test(nombre.value)) {
		spam.innerHTML = "Debe introducir un nombre correcto";
		nombre.focus();
	} else{
		spam.innerHTML = "";
	}	
 }


 function validarApe1(){
 	let expresion =/^[a-zA-ZÀ-ÿ\u00f1\u00d1\s]{2,20}$/;
 	let spam = document.getElementById("errorAp1"); 
 	if (!expresion.test(apellido1.value)) {
		spam.innerHTML = "Debe introducir un apellido correcto";
		apellido1.focus();
	} else{
		spam.innerHTML = "";
	}	
 }


  function validarApe2(){
 	let expresion =/^[a-zA-ZÀ-ÿ\u00f1\u00d1\s]{2,20}$/;
 	let spam = document.getElementById("errorAp2"); 
 	if (!expresion.test(apellido2.value)) {
		spam.innerHTML = "Debe introducir un apellido correcto";
		apellido2.focus();
	} else{
		spam.innerHTML = "";
	}	
 }


  function validarDni(){
 	let expresion =/^\d{8}[a-zA-Z]{1}$/;
 	let spam = document.getElementById("dni"); 
 	if (!expresion.test(dni.value)) {
		spam.innerHTML = "Debe introducir un numero de ocho digitos seguido de una letra";
		dni.focus();
	} else{
		let numero;
		let letra;
		let clave;
		numero=dni.value.substr(0,dni.value.length-1);
		letra=dni.value.substr(dni.value.length-1,1);
		letra=letra.toUpperCase();
		numero=numero%23;
		clave="TRWAGMYFPDXBNJZSQVHLCKET";
		clave=clave.substring(numero,numero+1);
		if(clave!=letra){
			spam.innerHTML = "DNI incorrecto";
			dni.focus();
		}else{
			spam.innerHTML = "";
		}
	}
	
 }





		

