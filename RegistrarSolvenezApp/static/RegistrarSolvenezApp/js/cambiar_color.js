function cambiarColorTex() {

    document.getElementById('cedula').addEventListener('change', function() {
        var tipo_doc = document.getElementById("Tipo_doc");
        var documento = document.getElementById("cedula");
        var boton = document.getElementById("boton_2");

        if (tipo_doc.value === "" || documento.value === "") {
            boton.disabled = true;
            boton.style.backgroundColor = "#d6d6d6";
            boton.style.color = "#000000";
        } else {
            boton.disabled = false;
            boton.style.backgroundColor = "#872341";
            boton.style.color = "#ffffff";
        }
    })
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