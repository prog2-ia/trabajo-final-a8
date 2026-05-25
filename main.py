"""
Código principal e interactivo para comprobar el funcionamiento de las
clases sobre ingredientes, platos y menús semanales.
"""

from models.dishes import Dish, MeatDish, MixedDish, VeganDish
from models.ingredients import Ingredient, AnimalIngredient, MineralIngredient, PlantIngredient
from models.weekly_menu import WeeklyMenu
from models.recipe_book import RecipeBook
from services.menu_service import generate_weekly_menu
from persistence.pickle_manager import save_to_file, load_from_file
from persistence.menu_semanal_pdf import export_menu_to_pdf


def initialize_sample_data() -> tuple[list[Ingredient], list[Dish]]:
    """
    Crea tres ingredientes y tres platos ya predefinidos.

    Returns:
        tuple[list[Ingredient], list[Dish]]: Tupla con listas de ingredientes y platos predefinidos
    """
    ingredientes: list[Ingredient] = []
    platos: list[Dish] = []

    # ingredientes predefinidos
    pollo = AnimalIngredient("Pechuga de Pollo", 500.0, 165.0, [], "Pollo")
    tomate = PlantIngredient("Tomate", 300.0, 18.0, [], True)
    sal = MineralIngredient("Sal", 50.0, 0.0, [], "Cloruro de Sodio")
    ingredientes = [pollo, tomate, sal]

    # platos predefinidos
    plato1 = MeatDish("Pollo a la Plancha", [], 1)
    plato2 = VeganDish("Ensalada", [], 1)
    plato3 = MixedDish("Arroz con pollo", [], 1)
    platos = [plato1, plato2, plato3]

    return ingredientes, platos


def main() -> None:
    """
    Función principal que ejecuta el menú interactivo del sistema.

    Flujo:
    1. Inicializa datos predefinidos
    2. Muestra menú de opciones en un bucle infinito
    3. Procesa acciones según la opción seleccionada
    4. Termina cuando el usuario selecciona "Salir"
    """
    ingredientes, platos = initialize_sample_data()  # cargar datos predefinidos
    recetario = RecipeBook("Mi recetario")
    menu_semanal: WeeklyMenu | None = None

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

        # crear ingrediente personalizado
        if opcion == "1":
            # solicitar tipo de ingrediente y validar
            tipo = input("Tipo de ingrediente (ANIMAL/PLANTA/MINERAL): ").upper()
            nombre = input("Nombre: ")
            # para las cantidades y calorías, levantamos un ValueError si su input no es float
            try:
                cantidad = float(input("Cantidad en gramos: "))
                calorias = float(input("Calorías por 100g: "))
            except ValueError:
                print("Error: introduce números válidos")
                continue
            tiene_alergenos = input("¿Tiene alérgenos? (s/n): ").lower() == "s"
            alergenos = []
            if tiene_alergenos:
                alergenos = input("Lista de alérgenos separados por coma: ").split(",")

            # intentar crear el ingrediente y controlar posibles errores
            try:
                # crear instancia según el tipo de ingrediente seleccionado
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

                # añadir ingrediente a la lista si todo es correcto
                ingredientes.append(ing)
                print(f"Ingrediente {nombre} creado correctamente.")

            # capturar cualquier error de validación
            except Exception as e:
                print("Error:", e)

        # crear plato personalizado
        elif opcion == "2":
            nombre_plato = input("Nombre del plato: ")
            print("Tipo de plato: 1=CARNE, 2=VEGANO, 3=MIXTO")
            tipo_plato = input("Selecciona tipo: ")
            # intentar crear el plato y controlar posibles errores
            try:
                # crear instancia del plato según su tipo
                if tipo_plato == "1":
                    plato = MeatDish(nombre_plato, [], 1)
                elif tipo_plato == "2":
                    plato = VeganDish(nombre_plato, [], 1)
                elif tipo_plato == "3":
                    plato = MixedDish(nombre_plato, [], 1)
                else:
                    print("Tipo no válido")
                    continue

                # añadir plato a la lista si todo es correcto
                platos.append(plato)
                print(f"Plato {nombre_plato} creado correctamente.")

            # capturar cualquier error de validación
            except Exception as e:
                print("Error:", e)

        # añadir ingrediente a un plato existente
        elif opcion == "3":
            if not ingredientes or not platos:
                print("Primero crea ingredientes y platos")
                continue
            # mostrar lista de ingredientes disponibles y seleccionar uno
            print("Ingredientes disponibles:")
            for i, ing in enumerate(ingredientes):
                print(f"{i+1}. {ing.name}")
            ing_sel = int(input("Selecciona ingrediente: ")) - 1

            # mostrar lista de platos disponibles y seleccionar uno
            print("Platos disponibles:")
            for i, pl in enumerate(platos):
                print(f"{i+1}. {pl.name}")
            pl_sel = int(input("Selecciona plato: ")) - 1

            # intentar añadir el ingrediente (puede fallar por validaciones de tipo)
            try:
                platos[pl_sel].add_ingredient(ingredientes[ing_sel])
                print("Ingrediente añadido correctamente")
            except Exception as e:
                print("Error:", e)

        # quitar ingrediente de plato
        elif opcion == "4":
            if not platos:
                print("No hay platos creados")
                continue
            print("Platos disponibles:")
            for i, pl in enumerate(platos):
                print(f"{i+1}. {pl.name}")
            pl_sel = int(input("Selecciona plato: ")) - 1  # seleccionar plato
            plato = platos[pl_sel]

            print("Ingredientes en el plato:")
            for i, ing in enumerate(plato.ingredients):
                print(f"{i+1}. {ing.name}")
            ing_sel = int(input("Selecciona ingrediente a quitar: ")) - 1  # seleccionar ingrediente que quitar

            if plato.remove_ingredient(plato.ingredients[ing_sel]):
                print("Ingrediente eliminado correctamente")
            else:
                print("No se pudo eliminar el ingrediente")

        # listar todos los ingredientes creados
        elif opcion == "5":
            print("Ingredientes creados:")
            for ing in ingredientes:
                print(ing)

        # listar todos los platos creados
        elif opcion == "6":
            print("Platos creados:")
            for pl in platos:
                print(pl)

        # salir del programa
        elif opcion == "7":
            print("Saliendo...")
            break

        # añadir plato al recetario
        elif opcion == "8":
            if not platos:
                print("No hay platos para añadir")
                continue

            print("Platos disponibles:")
            for i, pl in enumerate(platos):
                print(f"{i + 1}. {pl.name}")

            idx = int(input("Selecciona plato: ")) - 1

            # intentar añadir el plato al recetario
            try:
                recetario.add_dish(platos[idx])
                print("Plato añadido al recetario")
            except Exception as e:
                print(e)

        # generar menú semanal automático
        elif opcion == "9":
            if not platos:
                print("No hay platos disponibles")
                continue

            # generar menú aleatorio a partir de los platos disponibles
            menu_semanal = generate_weekly_menu(platos)
            print("Menú semanal generado correctamente")

        # mostrar menú semanal generado
        elif opcion == "10":
            if not menu_semanal:
                print("No hay menú generado")
            else:
                print("\nMENÚ SEMANAL:")
                print(menu_semanal)

        # guardar menú en archivo pickle
        elif opcion == "11":
            if not menu_semanal:
                print("No hay menú para guardar")
                continue

            save_to_file(menu_semanal, "menu.pkl")
            print("Menú guardado correctamente")

        # cargar menú desde archivo pickle
        elif opcion == "12":
            try:
                menu_semanal = load_from_file("menu.pkl")
                print("Menú cargado correctamente")
            except Exception as e:
                print("Error al cargar:", e)

        # exportar menú a PDF
        elif opcion == "13":
            if not menu_semanal:
                print("No hay menú para exportar")
                continue

            export_menu_to_pdf(menu_semanal)
            print("PDF generado correctamente")

        # opción no valida
        else:
            print("Opción no válida, inténtalo de nuevo.")


if __name__ == "__main__":
    main()
