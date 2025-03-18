import streamlit as st
import pandas as pd
import time
from database.orm import adiciona_games, atualiza_game, excluir_game, listar_games

def ler_consoles():
    with open("app/data/consoles.txt", "r") as file:
        consoles = file.readlines()
    consoles = [console.strip() for console in consoles]
    return consoles
    
st.title("Gerenciador de Games 🎮")

# Menu
menu = ["Adicionar Game", "Atualizar Game", "Listar Games", "Excluir Game"]
escolha = st.sidebar.selectbox("Menu", menu)

# Adicionar Game
if escolha == "Adicionar Game":
    st.subheader("Adicionar um Novo Game")
    nome = st.text_input("Nome do Game")
    ano = st.number_input("Ano de Lançamento", min_value=1952, max_value=2025, step=1)
    
    plataforma = st.selectbox("Selecione uma plataforma", ler_consoles())
    nota = st.slider("Nota do Game (Obrigatória)", 0.0, 10.0, 5.0)
    
    if st.button("Adicionar"):
        adiciona_games(nome, ano, nota, plataforma)
        with st.spinner('Aguarde...'):
            time.sleep(2)
        st.success("Game adicionado com sucesso!")

# Atualizar Game
elif escolha == "Atualizar Game":
    st.subheader("Atualizar um Game Existente")
    id_game = st.number_input("ID do Game", step=1)
    nome = st.text_input("Novo Nome (opcional)")
    ano = st.number_input("Novo Ano (opcional)", min_value=1952, max_value=2025, step=1)
    
    plataforma = st.selectbox("Selecione uma plataforma", ler_consoles())
    nota = st.slider("Nova Nota (opcional)", 0.0, 10.0, 5.0)
    
    
    if st.button("Atualizar"):
        atualiza_game(id_game, nome or None, ano or None, nota or None, plataforma or None)
        with st.spinner('Aguarde...'):
            time.sleep(2)
        st.success("Game atualizado com sucesso!")

# Listar Games
elif escolha == "Listar Games":
    st.subheader("Lista de Games")
    games = listar_games()

    if games:
        # Criando um DataFrame para tabelas interativas
        data = [{"Nome": game.nome, "Ano": game.ano, "Nota": game.nota, "Plataforma": game.plataforma} for game in games]
        df = pd.DataFrame(data)
        df.index =range(1, len(df) + 1)
        df.index.name = "ID"
        
        st.dataframe(df)
    else:
        st.warning("Nenhum game encontrado!")

# Excluir Game
elif escolha == "Excluir Game":
    st.subheader("Excluir um Game")
    id_game = st.number_input("ID do Game para Excluir", step=1)
    
    if st.button("Excluir"):
        with st.spinner('Aguarde...'):
            time.sleep(2)
        excluir_game(id_game)
        st.success("Game excluído com sucesso!")
