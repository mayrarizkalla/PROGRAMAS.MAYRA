import streamlit as st 

st.header("Sobre Mim")

nome = st.text_input("Digite o seu nome:")
if nome:
   st.success(f"Olá, {nome}! Seja bem-vindo(a)!")


nascimento = st.date_input("Quando você nasceu?")
if nascimento:
        hoje = datetime.date.today()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        st.write(f"**Idade:** {idade} anos")
        st.write(f"**Aniversário:** {nascimento.strftime('%d/%m/%Y')}")


cor_favorita = st.color_picker("Escolha sua cor favorita:", "#00ffaa")
st.write(f"Sua cor favorita: **{cor_favorita}**")


animal = st.selectbox(
    "Qual seu animal favorito?",
    ["Cachorro", "Gato", "Pássaro", "Tigre", "Leão", "Golfinho", "Outro"]
)

if animal:
    st.write(f"**Animal favorito:** {animal}")


musica = st.text_input("Qual sua música favorita?")
if musica:
    st.write(f"**Música favorita:** {musica}")


hobbies = st.multiselect(
    "O que você gosta de fazer no seu tempo livre?",
    ["Ler", "Esportes", "Música", "Jogos", "Cozinhar", "Viajar", "Programar", "Filmes/Séries", "Arte"]
)

if hobbies:
    st.write("**Seus hobbies:**")
    for hobby in hobbies:
        st.write(f"- {hobby}")


# Rodapé
st.markdown("---")
st.markdown("Feito com ❤️ usando Streamlit | Meu primeiro app!")
