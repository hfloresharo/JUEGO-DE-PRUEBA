```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pikicha en La Chutana",
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
}

.subtitulo {
    text-align: center;
    font-size: 20px;
    color: #4b4b4b;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="titulo">🐶 Pikicha en La Chutana 🐷</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    '¡Atrapa a los chanchitos antes de que Luca atrape a Pikicha!'
    '</div>',
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

#scoreboard {
    width: 620px;
    margin: 10px auto;

    display: flex;
    justify-content: space-around;

    font-size: 21px;
    font-weight: bold;

    color: #5a3500;
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

    overflow: hidden;
}

.wall {
    position: absolute;

    background: #8b5a2b;

    border: 3px solid #603813;

    border-radius: 7px;
}

.character {

    position: absolute;

    width: 45px;
    height: 45px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 38px;

    z-index: 10;

    user-select: none;
}

#pikicha {
    left: 290px;
    top: 330px;
}

#luca {
    left: 40px;
    top: 550px;

    font-size: 40px;

    z-index: 9;
}

.pig {

    position: absolute;

    font-size: 34px;

    z-index: 5;

    transition: transform .1s;
}

#message {

    font-size: 24px;

    font-weight: bold;

    color: #7b3f00;

    height:
