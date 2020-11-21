const compra = new Carrito();
const listaCompra = document.querySelector("#lista-compra tbody");
const carrito = document.getElementById('carrito');
const procesarCompraBtn = document.getElementById('procesar-compra');
const cliente = document.getElementById('cliente');
const correo = document.getElementById('correo');

cargarEventos();

function cargarEventos() {
    document.addEventListener('DOMContentLoaded', compra.leerLocalStorageCompra());

    //Eliminar productos del carrito
    carrito.addEventListener('click', (e) => { compra.eliminarProducto(e) });

    compra.calcularTotal();

    //cuando se selecciona procesar Compra
    procesarCompraBtn.addEventListener('click', procesarCompra);

    carrito.addEventListener('change', (e) => { compra.obtenerEvento(e) });
    carrito.addEventListener('keyup', (e) => { compra.obtenerEvento(e) });

}

function procesarCompra() {
    
    if (compra.obtenerProductosLocalStorage().length === 0) {
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'No hay productos, selecciona alguno',
            showConfirmButton: false,
            timer: 2000
        }).then(function () {
            window.location.href = "/productos";
        })
    }
    else if (cliente.value === '' || correo.value === '') {
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'Ingrese todos los campos requeridos',
            showConfirmButton: false,
            timer: 2000
        })
    }
    else {
        (function () {
            emailjs.init("user_UQw6SrsMqrbjBiuuKnz9q");
        })();

        let cadena = "";
        productosLS = compra.obtenerProductosLocalStorage();
        productosLS.forEach(function (producto) {
            cadena += `
                    Producto : ${producto.titulo}
                    Precio : ${producto.precio}
                    Cantidad: ${producto.cantidad}
                
                `;
        });
        document.getElementById('detalleCompra').innerHTML = cadena;

        var myform = $("form#procesar-pago");

        myform.submit((event) => {
            event.preventDefault();

            var service_id = "default_service";
            var template_id = "template_3spoqn5";

            const cargandoGif = document.querySelector('#cargando');
            cargandoGif.style.display = 'block';

            emailjs.sendForm(service_id, template_id, myform[0])
                .then(() => {
                    cargandoGif.style.display = 'none';
                    realizada();
                    setTimeout(() => {
                        compra.vaciarLocalStorage();
                        window.location.href = "/";
                    }, 2000);

                }, (err) => {
                    alert("Error al enviar el email\r\n Response:\n " + JSON.stringify(err));
                });
            return false;
        });
    }
};

function realizada() {
    Swal.fire({
        position: 'top-center',
        icon: 'success',
        title: 'Compra Realizada',
        showConfirmButton: false,
        timer: 1500
    })
}


