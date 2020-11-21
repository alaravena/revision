function validar()
{
  var usuario = document.getElementById("usuarioLogin").value; 
  var contraseña = document.getElementById("contLogin").value;

  if (usuario=="meme" && contraseña =="12345")
  {
      alert("Bienvenido "+usuario+"!")
  }
  else{
    alert("Los datos ingresados no son validos");
  }
}
function registro()
{
  var nombre = document.getElementById("nombreRegistro").value; 
  var usuario = document.getElementById("usuarioRegistro").value;
  var contraseña = document.getElementById("contRegistro").value;
  var confirmarcontraseña = document.getElementById("confcontRegistro").value;
  var correo = document.getElementById("correoRegistro").value;
  var dia = new Date();
  if (nombre !="" && usuario !="" && correo !="" && contraseña !="" && confirmarcontraseña !=""&& contraseña==confirmarcontraseña)
  {
    alert("Hola "+nombre+", gracias por registrarte, pero el servicio de registro no está disponible.");
  }
  else{
    alert("Los datos ingresados no son validos");
  }
}
