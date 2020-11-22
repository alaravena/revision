let modalId = $('#galeria-img');

$(document).ready(function () {

    cargarGaleria(true, 'a.thumbnail');

    function disableButtons(counter_max, counter_current) {
        $('#mostrar-imagen-anterior, #mostrar-imagen-siguiente')
            .show();
        if (counter_max === counter_current) {
            $('#mostrar-imagen-siguiente')
            .hide();
        } else if (counter_current === 1) {
            $('#mostrar-imagen-anterior')
            .hide();
        }
    }

    function cargarGaleria(setIDs, setClickAttr) {
        let current_image,
        selector,
        counter = 0;

        $('#mostrar-imagen-siguiente, #mostrar-imagen-anterior')
            .click(function () {
            if ($(this)
                .attr('id') === 'mostrar-imagen-anterior') {
                current_image--;
            } else {
                current_image++;
            }

            selector = $('[data-image-id="' + current_image + '"]');
            updateGallery(selector);
        });

        function updateGallery(selector) {
            let $sel = selector;
            current_image = $sel.data('image-id');
            $('#galeria-img-titulo')
            .text($sel.data('title'));
            $('#galeria-img-imagen')
            .attr('src', $sel.data('image'));
            disableButtons(counter, $sel.data('image-id'));
        }

        if (setIDs == true) {
            $('[data-image-id]')
            .each(function () {
                counter++;
                $(this)
                .attr('data-image-id', counter);
            });
        }
        $(setClickAttr)
            .on('click', function () {
            updateGallery($(this));
            });
        }
});

$(document).keydown(function (e) {
    switch (e.which) {
      case 37: // izquierda
        if ((modalId.data('bs.modal') || {})._isShown && $('#mostrar-imagen-anterior').is(":visible")) {
            $('#mostrar-imagen-anterior')
            .click();
        }
        break;

        case 39: // derecha
        if ((modalId.data('bs.modal') || {})._isShown && $('#mostrar-imagen-siguiente').is(":visible")) {
            $('#mostrar-imagen-siguiente')
            .click();
        }
        break;

        default:
            return;
    }
    e.preventDefault(); 
});

$(function() {
    $("#formularioReg").validate({
        rules: {
            nombre: "required",
            apellido: "required", 
            email:{
                required: true,
                email: true
            },
            password: "required",
            password2: {
                required: true,
                equalTo: "#passCl"
            }
        },
        messages: {
            nombre:{
                required: "Ingresa un Nombre"
            },
            apellido:{
                required: "Ingresa un Apellido"
            },
            email:{
                required: "Debes ingresar un correo electronico",
                email: "Formato de correo no válido"
            },
            password: {
                required: "Ingresa una contraseña",
                minlength: "Caracteres insuficientes, ingrese minimo 5"
            },
            password2: {
                required: 'Reingrese la contraseña',
                equalTo: 'Las contraseñas ingresadas no coinciden',
                minlength: 'Caracteres insuficientes'
            }
        }
    });
});

function alertaSuscription(mensaje) {
    Swal.fire(
        {
            "title": "Felicitaciones",
            "text": mensaje,
            "icon": "success"
        }
    )
}

function entrarAdmin() {
    window.location = "/inicioAdmin/"    
}