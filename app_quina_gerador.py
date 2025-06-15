
import streamlit as st
import random

st.set_page_config(page_title="Gerador de Combinações Quina", layout="centered")

st.title("🎯 Gerador de Combinações - Quina")
st.markdown("Gere combinações baseadas em padrões estatísticos confiáveis.")

# Funções
def tem_numeros_proximos(combinacao):
    combinacao_ordenada = sorted(combinacao)
    for i in range(1, len(combinacao_ordenada)):
        if abs(combinacao_ordenada[i] - combinacao_ordenada[i - 1]) <= 1:
            return True
    return False

def gerar_padrao_classico():
    candidatos = list(range(1, 81))
    while True:
        c = sorted(random.sample(candidatos, 5))
        pares = sum(1 for n in c if n % 2 == 0)
        if pares in [2, 3] and not tem_numeros_proximos(c):
            return c

def gerar_padrao_extremos():
    candidatos = list(range(1, 81))
    while True:
        c = sorted(random.sample(candidatos, 5))
        if any(n <= 10 for n in c) and any(n >= 71 for n in c) and not tem_numeros_proximos(c):
            return c

def gerar_padrao_fibonacci_frequentes():
    fibonacci = [1, 2]
    while fibonacci[-1] + fibonacci[-2] <= 80:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    top_frequentes = [2, 8, 12, 21, 34, 39, 45, 51, 59, 67, 71, 74]
    fib_cand = [n for n in fibonacci if n <= 80]
    while True:
        combinacao = sorted(random.sample(fib_cand, 2) + random.sample(top_frequentes, 3))
        if not tem_numeros_proximos(combinacao):
            return combinacao

# Interface
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎲 Clássico"):
        st.success(f"Combinação: {gerar_padrao_classico()}")

with col2:
    if st.button("🔢 Extremos"):
        st.info(f"Combinação: {gerar_padrao_extremos()}")

with col3:
    if st.button("🌀 Fibonacci + Frequentes"):
        st.warning(f"Combinação: {gerar_padrao_fibonacci_frequentes()}")

st.markdown("---")
st.caption("Desenvolvido por ChatGPT com base nos seus padrões e sorteios anteriores.")
