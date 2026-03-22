"""
Código para comprobar el funcionamiento de las clases 
sobre ingredientes y las de los platos
"""

from models.dishes import MeatDish, MixedDish, VeganDish
from models.ingredients import AnimalIngredient, MineralIngredient, PlantIngredient

def main():
    ingredientes = []
    platos = []

    while True:
        print("\n--- MENÚ DE PRUEBA ---")
        print("1. Crear ingrediente")
        print("2. Crear plato")
        print("3. Añadir ingrediente a plato")
        print("4. Quitar ingrediente de plato")
        print("5. Mostrar ingredientes")
        print("6. Mostrar platos")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tipo = input("Tipo de ingrediente (ANIMAL/PLANTA/MINERAL): ").upper()
            nombre = input("Nombre: ")
            cantidad = float(input("Cantidad en gramos: "))
            calorias = float(input("Calorías por 100g: "))
            tiene_alergenos = input("¿Tiene alérgenos? (s/n): ").lower() == "s"
            alergenos = []
            if tiene_alergenos:
                alergenos = input("Lista de alérgenos separados por coma: ").split(",")

            if tipo == "ANIMAL":
                animal_source = input("Fuente animal (Cerdo, Vaca, Pollo...): ")
                ing = AnimalIngredient(nombre, cantidad, calorias, alergenos, animal_source)
            elif tipo == "PLANTA":
                is_fruit = input("¿Es fruta? (s/n): ").lower() == "s"
                ing = PlantIngredient(nombre, cantidad, calorias, alergenos, is_fruit)
            elif tipo == "MINERAL":
                mineral_type = input("Tipo de mineral: ")
                ing = MineralIngredient(nombre, cantidad, calorias, alergenos, mineral_type)
            else:
                print("Tipo no válido")
                continue

            ingredientes.append(ing)
            print(f"Ingrediente {nombre} creado correctamente.")

        elif opcion == "2":
            nombre_plato = input("Nombre del plato: ")
            print("Tipo de plato: 1=CARNE, 2=VEGANO, 3=MIXTO")
            tipo_plato = input("Selecciona tipo: ")
            if tipo_plato == "1":
                plato = MeatDish(nombre_plato, [], 1)
            elif tipo_plato == "2":
                plato = VeganDish(nombre_plato, [], 1)
            elif tipo_plato == "3":
                plato = MixedDish(nombre_plato, [], 1)
            else:
                print("Tipo no válido")
                continue
            platos.append(plato)
            print(f"Plato {nombre_plato} creado correctamente.")

        elif opcion == "3":
            if not ingredientes or not platos:
                print("Primero crea ingredientes y platos")
                continue
            print("Ingredientes disponibles:")
            for i, ing in enumerate(ingredientes):
                print(f"{i+1}. {ing.name}")
            ing_sel = int(input("Selecciona ingrediente: ")) - 1

            print("Platos disponibles:")
            for i, pl in enumerate(platos):
                print(f"{i+1}. {pl.name}")
            pl_sel = int(input("Selecciona plato: ")) - 1

            try:
                platos[pl_sel].add_ingredient(ingredientes[ing_sel])
                print("Ingrediente añadido correctamente")
            except ValueError as e:
                print(e)

        elif opcion == "4":
            if not platos:
                print("No hay platos creados")
                continue
            print("Platos disponibles:")
            for i, pl in enumerate(platos):
                print(f"{i+1}. {pl.name}")
            pl_sel = int(input("Selecciona plato: ")) - 1
            plato = platos[pl_sel]

            print("Ingredientes en el plato:")
            for i, ing in enumerate(plato.ingredients):
                print(f"{i+1}. {ing.name}")
            ing_sel = int(input("Selecciona ingrediente a quitar: ")) - 1

            if plato.remove_ingredient(plato.ingredients[ing_sel]):
                print("Ingrediente eliminado correctamente")
            else:
                print("No se pudo eliminar el ingrediente")

        elif opcion == "5":
            print("Ingredientes creados:")
            for ing in ingredientes:
                print(ing)

        elif opcion == "6":
            print("Platos creados:")
            for pl in platos:
                print(pl)

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, inténtalo de nuevo.")

if __name__ == "__main__":
    main()