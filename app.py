import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pikicha - La Chutana",
    page_icon="🐶",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(#dff6ff, #fff7d6);
    }

    header {
        visibility: hidden;
    }

    .titulo {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #7b3f00;
        margin-bottom: 0;
    }

    .subtitulo {
        text-align: center;
        font-size: 20px;
        color: #4b4b4b;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="titulo">🐶 Pikicha en La Chutana 🐷</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">¡Ayuda a Pikicha a atrapar todos los chanchitos!</div>',
    unsafe_allow_html=True
)

game = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #c9f2b3;
    text-align: center;
    overflow: hidden;
}

#game {
    position: relative;
    width: 620px;
    height: 620px;
    margin: auto;
    background:
        linear-gradient(45deg, #8bc34a 25%, transparent 25%),
        linear-gradient(-45deg, #8bc34a 25%, transparent 25%),
        #a8d66d;
    background-size: 40px 40px;
    border: 8px solid #704214;
    border-radius: 18px;
    box-shadow: 0 8px 20px #555;
}

.wall {
    position: absolute;
    background: #8b5a2b;
    border: 3px solid #603813;
    border-radius: 7px;
}

#pikicha {
    position: absolute;
    width: 42px;
    height: 42px;
    font-size: 38px;
    z-index: 10;
    transition: left .08s, top .08s;
}

.pig {
    position: absolute;
    font-size: 34px;
    z-index: 5;
}

#scoreboard {
    width: 620px;
    margin: 10px auto;
    display: flex;
    justify-content: space-around;
    font-size: 22px;
    font-weight: bold;
    color: #5a3500;
}

#message {
    font-size: 24px;
    font-weight: bold;
    color: #7b3f00;
    height: 35px;
}

#start {
    padding: 10px 25px;
    font-size: 18px;
    background: #ffca28;
    border: 3px solid #8d6e00;
    border-radius: 12px;
    cursor: pointer;
    font-weight: bold;
}

</style>
</head>

<body>

<div id="scoreboard">
    <div>⭐ Puntos: <span id="score">0</span></div>
    <div>❤️ Vidas: <span id="lives">3</span></div>
    <div>🐷 Restantes: <span id="remaining">10</span></div>
</div>

<div id="message">¡Atrapa a los chanchitos!</div>

<button id="start">▶️ EMPEZAR</button>

<br><br>

<div id="game">

    <div class="wall" style="left:120px;top:80px;width:150px;height:30px;"></div>
    <div class="wall" style="left:350px;top:80px;width:150px;height:30px;"></div>

    <div class="wall" style="left:70px;top:180px;width:30px;height:180px;"></div>
    <div class="wall" style="left:520px;top:180px;width:30px;height:180px;"></div>

    <div class="wall" style="left:200px;top:180px;width:220px;height:30px;"></div>
    <div class="wall" style="left:200px;top:410px;width:220px;height:30px;"></div>

    <div class="wall" style="left:120px;top:500px;width:150px;height:30px;"></div>
    <div class="wall" style="left:350px;top:500px;width:150px;height:30px;"></div>

    <div id="pikicha">🐶</div>

    <div class="pig" id="pig1" style="left:30px;top:30px;">🐷</div>
    <div class="pig" id="pig2" style="left:300px;top:30px;">🐷</div>
    <div class="pig" id="pig3" style="left:550px;top:30px;">🐷</div>
    <div class="pig" id="pig4" style="left:30px;top:400px;">🐷</div>
    <div class="pig" id="pig5" style="left:550px;top:400px;">🐷</div>
    <div class="pig" id="pig6" style="left:300px;top:250px;">🐷</div>
    <div class="pig" id="pig7" style="left:130px;top:250px;">🐷</div>
    <div class="pig" id="pig8" style="left:450px;top:250px;">🐷</div>
    <div class="pig" id="pig9" style="left:130px;top:450px;">🐷</div>
    <div class="pig" id="pig10" style="left:450px;top:450px;">🐷</div>

</div>

<script>

const pikicha = document.getElementById("pikicha");
const game = document.getElementById("game");

let x = 290;
let y = 330;

let score = 0;
let lives = 3;
let playing = false;

const speed = 10;

pikicha.style.left = x + "px";
pikicha.style.top = y + "px";

function updatePosition() {

    pikicha.style.left = x + "px";
    pikicha.style.top = y + "px";

    checkPigs();
}

function checkCollision(a, b) {

    const r1 = a.getBoundingClientRect();
    const r2 = b.getBoundingClientRect();

    return !(
        r1.right < r2.left ||
        r1.left > r2.right ||
        r1.bottom < r2.top ||
        r1.top > r2.bottom
    );
}

function checkPigs() {

    document.querySelectorAll(".pig").forEach(pig => {

        if (
            pig.style.display !== "none" &&
            checkCollision(pikicha, pig)
        ) {

            pig.style.display = "none";

            score += 100;

            document.getElementById("score").innerText = score;

            let remaining =
                document.querySelectorAll(
                    '.pig:not([style*="display: none"])'
                ).length;

            document.getElementById("remaining").innerText = remaining;

            if (remaining === 0) {
                playing = false;

                document.getElementById("message").innerText =
                    "🎉 ¡PIKICHA GANÓ! 🎉";

                alert(
                    "🐶🏆 ¡Felicidades! Pikicha atrapó todos los chanchitos de La Chutana."
                );
            }
        }
    });
}

function move(dx, dy) {

    if (!playing) return;

    let newX = x + dx;
    let newY = y + dy;

    newX = Math.max(0, Math.min(570, newX));
    newY = Math.max(0, Math.min(570, newY));

    x = newX;
    y = newY;

    updatePosition();
}

document.addEventListener("keydown", function(e) {

    if (e.key === "ArrowUp" || e.key === "w") {
        e.preventDefault();
        move(0, -speed);
    }

    if (e.key === "ArrowDown" || e.key === "s") {
        e.preventDefault();
        move(0, speed);
    }

    if (e.key === "ArrowLeft" || e.key === "a") {
        e.preventDefault();
        move(-speed, 0);
    }

    if (e.key === "ArrowRight" || e.key === "d") {
        e.preventDefault();
        move(speed, 0);
    }

});

document.getElementById("start").onclick = function() {

    playing = true;

    document.getElementById("message").innerText =
        "🐷 ¡Atrapa a los chanchitos!";

};

</script>

</body>
</html>
"""

components.html(game, height=780, scrolling=False)

st.markdown("""
### 🎮 Cómo jugar

**⬆️ ⬇️ ⬅️ ➡️** para mover a Pikicha.

También puedes utilizar **W A S D**.

🎯 **Objetivo:** atrapar los 10 chanchitos.

🏆 Cada chanchito atrapado = **100 puntos**.

🐶 ¡Completa la granja y conviértete en el campeón de La Chutana!
""")
