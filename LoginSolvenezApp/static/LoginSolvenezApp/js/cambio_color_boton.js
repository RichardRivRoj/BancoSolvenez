function cambiarColor() {

    var usuario = document.getElementById("id_username");
    var contraseña = document.getElementById("id_password");
    var boton = document.getElementById("boton_1");

    if (usuario.value === "" || contraseña.value === ""){

        // si no estan rellenos, bloquear el botón y cambiar su color de fondo a #d6d6d6
        boton.disabled = true;
        boton.style.backgroundColor = "#d6d6d6";
        boton.style.color = "#000000";

    } else {

        // si estan rellenos, desbloquear el botón y cambiar su color de fondo a #872341
        boton.disabled = false;
        boton.style.backgroundColor = "#872341";
        boton.style.color = "#ffffff";
    }
}