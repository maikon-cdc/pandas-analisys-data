# ================================
# Exemplo com Listas, Tuplas, Sets e Operadores
# ================================

# LISTAS (mutáveis)
print("===== LISTAS =====")
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
mistura = [1.0, 'a', True]

print("Lista números:", numeros)
print("Lista letras:", letras)
print("Lista mista:", mistura)

numeros.append(4)      # adiciona elemento
numeros[0] = 99        # altera elemento
print("Lista alterada:", numeros)

# TUPLAS (imutáveis)
print("\n===== TUPLAS =====")
tupla = ("what", "who", "where")# ================================
# Exemplo com Listas, Tuplas, Sets e Operadores
# ================================

# ===== LISTAS =====
print("===== LISTAS =====")

# Uma lista é uma coleção ORDENADA e MUTÁVEL (podemos alterar os elementos).
numeros = [1, 2, 3]          # Lista de inteiros
letras = ['a', 'b', 'c']     # Lista de strings
mistura = [1.0, 'a', True]   # Lista com tipos diferentes (float, string e boolean)

print("Lista números:", numeros)
print("Lista letras:", letras)
print("Lista mista:", mistura)

# O método append() adiciona um novo elemento AO FINAL da lista.
# Aqui, estamos adicionando o número 4 à lista "numeros".
numeros.append(4)      
# Agora a lista virou: [1, 2, 3, 4]

# Como listas são MUTÁVEIS, podemos trocar qualquer elemento.
# Aqui, trocamos o elemento da posição 0 (primeiro) para 99.
numeros[0] = 99        
# Agora a lista virou: [99, 2, 3, 4]

print("Lista alterada:", numeros)


# ===== TUPLAS =====
print("\n===== TUPLAS =====")

# Tupla é uma coleção ORDENADA e IMUTÁVEL (não pode ser alterada).
tupla = ("what", "who", "where")
print("Tupla:", tupla)

# Podemos acessar elementos por índice, igual lista.
print("Primeiro elemento:", tupla[0])

# Se tentarmos alterar, dá ERRO, porque tuplas são imutáveis.
# Descomente a linha abaixo para testar e ver o TypeError:
# tupla[0] = "new"  


# ===== SETS =====
print("\n===== SETS =====")

# Um set é uma coleção NÃO ORDENADA e que NÃO permite duplicados.
# Aqui, "uva" foi repetido, mas no set final só aparece UMA vez.
frutas = set(["batata", "alface", "uva", "uva"])
print("Set sem duplicados:", frutas)

# Adiciona um elemento ao set (a ordem não é garantida).
frutas.add("banana")
print("Set após add:", frutas)

# Remove um elemento existente.
# Se tentar remover algo que NÃO existe, gera erro.
frutas.remove("alface")
print("Set após remove:", frutas)


# ===== FROZENSET =====
print("\n===== FROZENSET =====")

# Frozenset é igual ao set, mas é IMUTÁVEL (não podemos adicionar ou remover depois).
conjunto = frozenset(['batata', 'alface', 'uva'])
print("Frozenset:", conjunto)

# conjunto.add("banana")  # Se descomentar, dará erro (AttributeError)


# ===== OPERAÇÕES ENTRE SETS =====
a = {1, 2, 3}
b = {3, 4, 5}

# União (elementos de A ou B)
print("\nUnião:", a | b)  

# Interseção (elementos que aparecem em ambos)
print("Interseção:", a & b)  

# Diferença (elementos que estão em A mas não em B)
print("Diferença:", a - b)  


# ===== OPERADORES =====
print("\n===== OPERADORES =====")

x, y = 10, 5

# Operadores de COMPARAÇÃO retornam True ou False
print("x == y:", x == y)   # Igualdade
print("x != y:", x != y)   # Diferença
print("x > y:", x > y)     # Maior que
print("x < y:", x < y)     # Menor que
print("x >= y:", x >= y)   # Maior ou igual
print("x <= y:", x <= y)   # Menor ou igual


# Operadores LÓGICOS (com valores booleanos)
p, q = True, False
print("\np AND q:", p and q)  # True só se ambos forem True
print("p OR q:", p or q)      # True se pelo menos um for True
print("not p:", not p)        # Inverte o valor (True -> False)


# Operadores ARITMÉTICOS
print("\nAritméticos:")
print("5 + 2 =", 5 + 2)   # Soma
print("5 - 2 =", 5 - 2)   # Subtração
print("5 * 2 =", 5 * 2)   # Multiplicação
print("5 / 2 =", 5 / 2)   # Divisão (resultado float)
print("5 // 2 =", 5 // 2) # Divisão inteira (descarta decimais)
print("5 % 2 =", 5 % 2)   # Módulo (resto da divisão)
print("5 ** 2 =", 5 ** 2) # Potência

print("Tupla:", tupla)
print("Primeiro elemento:", tupla[0])

# Descomente a linha abaixo para ver erro (imutável)
# tupla[0] = "new"  

# SETS (mutáveis, sem duplicados)
print("\n===== SETS =====")
frutas = set(["batata", "alface", "uva", "uva"])
print("Set sem duplicados:", frutas)
frutas.add("banana")
print("Set após add:", frutas)
frutas.remove("alface")
print("Set após remove:", frutas)

# FROZENSET (imutável)
print("\n===== FROZENSET =====")
conjunto = frozenset(['batata', 'alface', 'uva'])
print("Frozenset:", conjunto)

# OPERAÇÕES ENTRE SETS
a = {1, 2, 3}
b = {3, 4, 5}
print("\nUnião:", a | b)
print("Interseção:", a & b)
print("Diferença:", a - b)

# OPERADORES
print("\n===== OPERADORES =====")
x, y = 10, 5
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

p, q = True, False
print("\np AND q:", p and q)
print("p OR q:", p or q)
print("not p:", not p)

print("\nAritméticos:")
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 // 2 =", 5 // 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)