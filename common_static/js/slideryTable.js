$(document).ready( function () {
    $('#lista-carrito').DataTable({
        "scrollY":"200px",
        "scrollCollapse":true,
        "paging":false,
        "language": {
            "url": "https://cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json"
        }
    });

    $(".carouselItem").owlCarousel({
        margin: 20,
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000, /* 2 segundos */
        autoplayHoverPause: true, /* se posiciona el mouse y queda sin movimiento */ 
        responsive: {
        0:{
            items:1,
            nav: false
        },
        450:{
            items:2,
            nav: false
        },
        800:{
            items:3,
            nav: false
        },
        1000:{
            items:4,
            nav: false
        }
        }
    });
} );