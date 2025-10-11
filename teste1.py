import streamlit as st 
import datetime

st.header("Meu Perfil Pessoal")

nome = st.text_input("Digite o seu nome:")
if nome:
   st.success(f"Olá, {nome}! Seja bem-vindo(a)!")


nascimento = st.date_input("Selecione sua data de nascimento:",
        value=datetime.date(1, 1, 2000),
        min_value=datetime.date(1, 1, 1900),
        max_value=datetime.date.today()
    )
    
hoje = datetime.date.today()
idade = hoje.year - nascimento.year
    
st.write(f"**Data de nascimento:** {nascimento.strftime('%d/%m/%Y')}")
st.write(f"**Idade:** {idade} anos")

cor_favorita = st.color_picker("Escolha sua cor favorita:", "#00ffaa")
st.write(f"Sua cor favorita: **{cor_favorita}**")


animal = st.selectbox(
    "Qual seu animal favorito?",
    ["Cachorro", "Gato", "Pássaro", "Tigre", "Leão", "Golfinho", "Tubarão", "Peixe", "Macaco", "Coelho", "Outro"]
)

if animal:
    st.write(f"**Animal favorito:** {animal}")


musica = st.text_input("Qual sua música favorita?")
if musica:
    st.write(f"**Música favorita:** {musica}")


hobbies = st.multiselect(
    "O que você gosta de fazer no seu tempo livre?",
    ["Ler", "Esportes", "Música", "Jogos", "Cozinhar", "Viajar", "Programar", "Filmes/Séries", "Dançar", "Escrever", "Desenhar/Pintar"]
)

if hobbies:
    st.write("**Seus hobbies:**")
    for hobby in hobbies:
        st.write(f"- {hobby}")
