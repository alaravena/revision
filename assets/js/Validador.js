$( document ).ready(function() {
    $("#registro").validate({
        rules: {
            nombreRegistro: "required",
            usuarioRegistro: "required",
            contRegistro: "required",
            confcontRegistro: {
                required: true,
                equalTo : "#contRegistro"
            },
            correoRegistro: {
                required: true,
                email: true
            }
        },
        messages: {
            nombreRegistro:{
                required: "Debe ingresar su nombre"
            },
            usuarioRegistro:{
                required: "Debe ingresar su nombre de usuario"
            },
            contRegistro:{
                required: "Debe ingresar su contraseña"
            },
            confcontRegistro:{
                required: "Debe ingresar un contraseña nuevamente",
                equalTo : "Las contraseñas deben ser iguales"
            },
            correoRegistro:{
                required: "Debe ingresar su email",
                email: "El email debe ser valido"
            },
        },
    });
    $("#login").validate({
        rules: {
            usuarioLogin: "required",
            contLogin: "required",
        },
        messages: {
            usuarioLogin:{
                required: "Debe ingresar su nombre de usuario"
            },
            contLogin:{
                required: "Debe ingresar su contraseña"
            },
        },
    });
});