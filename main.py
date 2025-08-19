from recetas import *

#en esta parte de el codigo: se vacia el archivo ingredientes existentes.txt
with open("ingredientes_existentes.txt", "w") as file:
    file.write("")


# en esta parte se guarda los ingredientes
mas_ingredientes = "s"
with open("ingredientes_existentes.txt", "a") as file:

    while mas_ingredientes == "s":
        ingrediente = input("Ingrese el ingrediente que tenga: ").lower()
        file.write(ingrediente + ";")

        mas_ingredientes = input("¿Tenes mas ingredientes? S/N: ").lower()

#en esta parte se lee los ingredientes
with open("ingredientes_existentes.txt","r") as file:
    ingredientes_existentes = file.read().split(";")

#en esta parte se encuentra la coincideincia y te dice que se puede cocinar, teniendo en cuenta los ingredientes
    
    if "pollo" in ingredientes_existentes:
        print("🍗 Te recomiendo cocinar milanesa de pollo, aquí te dejo la receta 👇")
        r_milanesa_pollo()

    elif "carne" in ingredientes_existentes:
        print("🥩 Podés hacer milanesa de carne o empanadas de carne, aquí te dejo las receta 👇")
        r_milanesa_carne()
        r_empanadas()

    elif "harina" in ingredientes_existentes:
        print("🍕 Con harina podés hacer una pizza, aquí te dejo la receta 👇")
        r_pizza()

    elif "papas" in ingredientes_existentes:
        print("🥔 Podés hacer puré de papas o tortilla de papas, aquí te dejo las receta 👇")
        r_pure()
        r_tortilla_papas()

    elif "lentejas" in ingredientes_existentes:
        print("🍲 Con lentejas podés hacer un guiso de lentejas, aquí te dejo la receta 👇")
        r_guiso()

    else:
        print("No encontré recetas con los ingredientes que tenés.")