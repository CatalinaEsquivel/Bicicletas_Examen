
//validator personalizado
$.validator.addMethod("terminaPor", function(value, element, parametro){

    if(value.endsWith(parametro)){
        return true;
    }
    return false;
}, "Debe terminar con {0}")


$("#formulario_contacto").validate({
    rules:{
        email:{
            required: true,
            email: true,
            terminaPor: "@gmail.com"
        },
        password:{
            required: true,
            minlength: 3,
            maxlength: 30
        }
    }
})

$("#btn").click(function(){
    if( $("#formulario_contacto").valid()==false){
        return;
    }
  let email = $("#email").val()
  let password = $("#password").val()
})


