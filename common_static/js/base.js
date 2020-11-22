function alerta(mensaje) {
    Swal.fire(
        {
            "title": "Felicitaciones",
            "text": mensaje,
            "icon": "success"
        }
    )
}

function eliminar(ventana, id) {
    Swal.fire(
        {
            "title":"¿Estas Seguro?",
            "text":"Esta acción no se puede deshacer",
            "icon":"question",
            "showCancelButton":true,
            "cancelButtonText":"No, Cancelar",
            "confirmButtonText":"Si, Eliminar",
            "reverseButtons":true,
            "confirmButtonColor":"#B41C07"
        }
    )
    .then(function(result) {
        if(ventana == "pr")
            if(result.isConfirmed){
                window.location.href = "/eliminarProducto/"+id+"/"
            }
        if(ventana == "pi")
            if(result.isConfirmed){
                window.location.href = "/eliminarPromocionInicio/"+id+"/"
            }
        if(ventana == "pp")
            if(result.isConfirmed){
                window.location.href = "/eliminarPromocionProducto/"+id+"/"
            }
        if(ventana == "ca")
            if(result.isConfirmed){
                window.location.href = "/eliminarCategoria/"+id+"/"
            }
        if(ventana == "ga")
            if(result.isConfirmed){
                window.location.href = "/eliminarGaleria/"+id+"/"
            }
    })
}