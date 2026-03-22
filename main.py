"""
Código para comprobar el funcionamiento de las clases 
sobre ingredientes y las de los platos
"""

from models.dishes import MeatDish, MixedDish, VeganDish
from models.ingredients import AnimalIngredient, MineralIngredient, PlantIngredient
from models.weekly_menu import WeeklyMenu
from models.recipe_book import RecipeBook
from services.menu_service import generate_weekly_menu
from persistence.pickle_manager import save_to_file, load_from_file
from exceptions.custom_exceptions import InvalidServingError, IncompatibleIngredientError, InvalidUnitError
from persistence.menu_semanal_pdf import export_menu_to_pdf


def main():
    ingredientes = []
    platos = []
    recetario = RecipeBook("Mi recetario")
    menu_semanal = None

    while True:
        print("\n--- MENÚ DE PRUEBA ---")
        print("1. Crear ingrediente")
        print("2. Crear plato")
        print("3. Añadir ingrediente a plato")
        print("4. Quitar ingrediente de plato")
        print("5. Mostrar ingredientes")
        print("6. Mostrar platos")
        print("7. Salir")
        print("8. Añadir plato al recetario")
        print("9. Generar menú semanal")
        print("10. Mostrar menú semanal")
        print("11. Guardar menú (pickle)")
        print("12. Cargar menú (pickle)")
        print("13. Exportar menú a PDF")
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
            except Exception as e:
                print("Error:", e)

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

        elif opcion == "8":
            if not platos:
                print("No hay platos para añadir")
                continue

            print("Platos disponibles:")
            for i, pl in enumerate(platos):
                print(f"{i + 1}. {pl.name}")

            idx = int(input("Selecciona plato: ")) - 1

            try:
                recetario.add_dish(platos[idx])
                print("Plato añadido al recetario")
            except Exception as e:
                print(e)

        elif opcion == "9":
            if not platos:
                print("No hay platos disponibles")
                continue

            menu_semanal = generate_weekly_menu(platos)
            print("Menú semanal generado correctamente")

        elif opcion == "10":
            if not menu_semanal:
                print("No hay menú generado")
            else:
                print("\nMENÚ SEMANAL:")
                print(menu_semanal)

        elif opcion == "11":
            if not menu_semanal:
                print("No hay menú para guardar")
                continue

            save_to_file(menu_semanal, "menu.pkl")
            print("Menú guardado correctamente")

        elif opcion == "12":
            try:
                menu_semanal = load_from_file("menu.pkl")
                print("Menú cargado correctamente")
            except Exception as e:
                print("Error al cargar:", e)

        elif opcion == "13":
            if not menu_semanal:
                print("No hay menú para exportar")
                continue

            export_menu_to_pdf(menu_semanal)
            print("PDF generado correctamente")

        else:
            print("Opción no válida, inténtalo de nuevo.")


if __name__ == "__main__":
    main()
