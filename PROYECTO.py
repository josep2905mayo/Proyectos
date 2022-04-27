texto = input("Ingrese un texto: ")
letra1 = input("Ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercera letra: ")

texto2 = texto.lower()

letra1_1 = letra1.lower()

letra2_2 = letra2.lower()

letra3_3 = letra3.lower()

lista1 = list[letra1_1, letra2_2, letra3_3]

num1 = texto2.count(letra1_1)
num2 = texto2.count(letra2_2)
num3 = texto2.count(letra3_3)

print(f"La primera letra se repite: {num1} veces")
print(f"La segunda letra se repite: {num2} veces")
print(f"La tercera letra se repite: {num3} veces")

num_palabras = texto2.split()

print(f"el numero de palabras es: {len(num_palabras)}")

texto3 = list(texto2)
primera_letra = texto3[0]
ultima_letra = texto3[-1]

print(f"Primera letra: {primera_letra}")
print(f"Ultima letra: {ultima_letra}")

texto4= texto2.split()
texto4.reverse()
texto5 = " ".join(texto4)
print(f"Texto invertido: {texto5}")

python = "python" in texto2

print(python)