# ================================
# Exemplo com Números Complexos e Funções
# ================================

# Quando usamos números complexos Python.

# Engenharia elétrica → para representar corrente alternada.
# Física → ondas eletromagnéticas, mecânica quântica.
# Matemática → transformadas de Fourier, equações diferenciais.
# Ciência de dados → processamento de sinais, som e imagem.

print("===== NÚMEROS COMPLEXOS =====")

# 1e10 significa "1 vezes 10 elevado a 10" (notação científica).
# Muito usado para números muito grandes ou muito pequenos em ciência.
num1 = 1e10       
print("num1 =", num1)   # 10000000000.0

# O sufixo "j" indica parte imaginária (Python usa "j" em vez de "i").
# Isso representa o número 3i (matemática complexa).
num2 = 3j         
print("num2 =", num2)   # 3j

# Um número complexo tem PARTE REAL + PARTE IMAGINÁRIA
num3 = 7 + 4j     
print("num3 =", num3)   # (7+4j)

# Podemos acessar a parte real e imaginária separadamente:
print("Parte real de num3:", num3.real)   # 7.0
print("Parte imaginária de num3:", num3.imag)  # 4.0

# O conjugado inverte o sinal da parte imaginária: (a+bj) -> (a-bj)
print("Conjugado de num3:", num3.conjugate())  # (7-4j)

# Exemplo de operação com complexos:
resultado = (2 + 3j) * (1 - 4j)
print("\n(2+3j) * (1-4j) =", resultado)  
# Isso é usado em engenharia elétrica, transformadas de Fourier, etc.


# ===== FUNÇÕES =====
print("\n===== FUNÇÕES =====")

# Definição de uma função: blocos de código que podem ser reutilizados.
# Aqui, "soma" recebe dois parâmetros e retorna o resultado.
def soma(a, b):
    return a + b

# Exemplo de uso
print("Soma 5 + 3 =", soma(5, 3))  # 8


# Definição de função com parâmetro opcional (valor padrão).
# Se não passar o expoente, ele assume 2 (potência ao quadrado).
def potencia(base, expoente=2):  
    return base ** expoente

# Exemplo de uso
print("Potência 3² =", potencia(3))      # usa valor padrão (expoente=2) -> 9
print("Potência 2^5 =", potencia(2, 5))  # sobrescreve o valor padrão -> 32
