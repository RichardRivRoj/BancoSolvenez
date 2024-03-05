function cambiarColorTex() {

    var documento = document.getElementById("cedula");
    var boton = document.getElementById("boton_2");

    if (documento.value === ""){

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


function cambiarColorTer() {

    document.getElementById('is_acept').addEventListener('change', function() {
        var aceptar = document.getElementById('is_acept');
        var boton = document.getElementById('boton_2');

        if (aceptar.checked === true) {
            boton.disabled = false;
            boton.style.backgroundColor = "#872341";
            boton.style.color = "#ffffff";
        } else {
            boton.disabled = true;
            boton.style.backgroundColor = "#d6d6d6";
            boton.style.color = "#000000";
        }
    })

}