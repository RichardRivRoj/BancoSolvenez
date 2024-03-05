const texto = document.querySelector(".movi_letra");

//var  = parrafo.split(" ");//

const velocidad = 5;

var distancia = 0;

/*for (var i = 0; i < palabras.length; i++){

    var span = document.createElement("span");
    span.textContent = palabras[i] + " ";
    span.style.position = "absolute";
    span.style.left = "100%";
    span.style.transform = "translateX(0)";
    span.style.transition = "transform 0.5s linear";
    texto.appendChild(span);
    distancia[i] = 0;
}
*/

function moverTexto(){

    distancia += velocidad;

    texto.style.transform = `translateX(-${distancia}px)`;

    if (distancia > texto.offsetWidth + texto.parentElement.offsetWidth){

        distancia = 0;
    }

}

setInterval(moverTexto, 50);