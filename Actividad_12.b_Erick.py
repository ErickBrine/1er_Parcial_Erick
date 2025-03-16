# Contar apariciones de la letra a
texto = input("Frase: ")
vocales = "aeiouAEIOU"
j = 0
for i in texto:
    if i in vocales:
        j = j + 1
print(f"La Frase tiene {j} vocales")





