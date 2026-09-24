```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pikicha en La Chutana",
    page_icon="🐶",
    layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(#dff6ff, #fff3c4);
    }

    header {
        visibility: hidden;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #7b3f00;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #4b4b4b;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">🐶 Pikicha en La Chutana 🐷</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Atrapa los chanchitos y escapa de Luca 👦'
    '</div>',
    unsafe_allow_html=True
)

html = """
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 10px;
    font-family: Arial, sans-serif;
    text-align: center;
    background: #d9f5c4;
}

.info {
    width: 620px;
    max-width: 95vw;
    margin: auto;
    display: flex;
    justify-content: space-around;
    font-size: 20px;
    font-weight: bold;
    color: #5b3800;
}

#mensaje {
    height: 35px;
    font-size: 21px;
    font-weight: bold;
    color: #7b3f00;
}

#juego {
    position: relative;

    width: 620px;
    height: 620px;

    max-width: 95vw;

    margin: auto;

    background-color: #91c957;

    border: 8px solid #704214;

    border-radius: 18px;

    overflow: hidden;

    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

/* CAMPO */

#juego::before {
    content: "🌾";
    position: absolute;
    left: 15px;
    top: 15px;
    font-size: 30px;
}

#juego::after {
    content: "🌻";
    position: absolute;
    right: 15px;
    bottom: 15px;
    font-size: 30px;
}

/* MUROS */

.muro {
    position: absolute;

    background: #8b5a2b;

    border: 3px solid #603813;

    border-radius: 8px;
}

/* PERSONAJES */

.personaje {
    position: absolute;

    width: 45px;
    height: 45px;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 36px;

    z-index: 20;

    user-select: none;
}

#pikicha {
    left: 285px;
    top: 330px;
}

#luca {
    left: 45px;
    top: 540px;
}

/* CHANCHITOS */

.chanchito {
    position: absolute;

    width: 40px;
    height: 40px;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 32px;

    z-index: 10;
}

/* BOTON */

button {
    margin: 10px;

    padding: 10px 25px;

    font-size: 18px;

    font-weight: bold;

    border-radius: 12px;

    border: 3px solid #8d6e00;

    background: #ffca28;

    cursor: pointer;
}

button:hover {
    transform: scale(1.05);
}

.ayuda {
    font-size: 16px;
    color: #513b00;
}

</style>

</head>


<body>


<div class="info">

    <div>
        ⭐ Puntos:
        <span id="puntos">0</span>
    </div>

    <div>
        ❤️ Vidas:
        <span id="vidas">3</span>
    </div>

    <div>
        🐷:
        <span id="restantes">10</span>
    </div>

</div>


<div id="mensaje">

    ¡Atrapa los chanchitos!

</div>


<button onclick="iniciarJuego()">

    ▶️ EMPEZAR

</button>


<div class="ayuda">

    Usa ⬆️ ⬇️ ⬅️ ➡️ o W A S D

</div>


<br>


<div id="juego">


    <!-- MUROS -->

    <div
        class="muro"
        style="left:110px; top:80px; width:150px; height:30px;">
    </div>

    <div
        class="muro"
        style="left:360px; top:80px; width:150px; height:30px;">
    </div>


    <div
        class="muro"
        style="left:70px; top:170px; width:30px; height:180px;">
    </div>


    <div
        class="muro"
        style="left:520px; top:170px; width:30px; height:180px;">
    </div>


    <div
        class="muro"
        style="left:190px; top:190px; width:230px; height:30px;">
    </div>


    <div
        class="muro"
        style="left:190px; top:410px; width:230px; height:30px;">
    </div>


    <div
        class="muro"
        style="left:110px; top:500px; width:150px; height:30px;">
    </div>


    <div
        class="muro"
        style="left:360px; top:500px; width:150px; height:30px;">
    </div>


    <!-- PIKICHA -->

    <div
        id="pikicha"
        class="personaje">

        🐶

    </div>


    <!-- LUCA -->

    <div
        id="luca"
        class="personaje">

        👦

    </div>


    <!-- CHANCHITOS -->

    <div
        class="chanchito"
        id="c1"
        style="left:30px; top:30px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c2"
        style="left:300px; top:30px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c3"
        style="left:550px; top:30px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c4"
        style="left:30px; top:390px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c5"
        style="left:550px; top:390px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c6"
        style="left:300px; top:250px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c7"
        style="left:130px; top:250px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c8"
        style="left:450px; top:250px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c9"
        style="left:130px; top:450px;">

        🐷

    </div>


    <div
        class="chanchito"
        id="c10"
        style="left:450px; top:450px;">

        🐷

    </div>


</div>


<script>

let px = 285;
let py = 330;

let lx = 45;
let ly = 540;

let puntos = 0;
let vidas = 3;

let jugando = false;

let chanchitos = 10;

const velocidadPikicha = 8;

const velocidadLuca = 1.8;


const pikicha =
    document.getElementById("pikicha");

const luca =
    document.getElementById("luca");


function actualizar() {

    pikicha.style.left =
        px + "px";

    pikicha.style.top =
        py + "px";


    luca.style.left =
        lx + "px";

    luca.style.top =
        ly + "px";

}


function iniciarJuego() {

    puntos = 0;

    vidas = 3;

    chanchitos = 10;

    px = 285;

    py = 330;

    lx = 45;

    ly = 540;

    jugando = true;


    document.getElementById("puntos")
        .innerText = puntos;

    document.getElementById("vidas")
        .innerText = vidas;

    document.getElementById("restantes")
        .innerText = chanchitos;

    document.getElementById("mensaje")
        .innerText =
        "🐷 ¡Atrapa los chanchitos y escapa de Luca!";


    document
        .querySelectorAll(".chanchito")
        .forEach(function(c) {

            c.style.display = "flex";

        });


    actualizar();

}


function mover(dx, dy) {

    if (!jugando) {
        return;
    }


    px += dx;
    py += dy;


    if (px < 0) {
        px = 0;
    }

    if (py < 0) {
        py = 0;
    }

    if (px > 570) {
        px = 570;
    }

    if (py > 570) {
        py = 570;
    }


    actualizar();

    revisarChanchitos();

}


document.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "ArrowUp" ||
