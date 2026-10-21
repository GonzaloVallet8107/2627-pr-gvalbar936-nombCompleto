def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formatea el nombre completo eliminando espacios y capitalizando palabras.
    Args:
        nombre: El nombre de la persona.
        apellido1: El primer apellido.
        apellido2: El segundo apellido.
    return: 
        El nombre completo formateado.
    """
    lista_nombre: list[str] = nombre.strip().split()
    lista_nombre_cap: list[str] = [palabra.capitalize() for palabra in lista_nombre]
    nombre_limpio: str = " ".join(lista_nombre_cap) #" ".join() -- Junta lo que haya dentro de la lista.
    
    lista_ape1: list[str] = apellido1.strip().split()
    lista_ape1_cap: list[str] = [palabra.capitalize() for palabra in lista_ape1]
    apellido1_limpio: str = " ".join(lista_ape1_cap)
    
    lista_ape2: list[str] = apellido2.strip().split()
    lista_ape2_cap: list[str] = [palabra.capitalize() for palabra in lista_ape2]
    apellido2_limpio: str = " ".join(lista_ape2_cap)
    
    return f"{nombre_limpio} {apellido1_limpio} {apellido2_limpio}"

def main() -> None:
    nombre: str = input("Introduce tu nombre: ")
    apellido1: str = input("Introduce tu primer apellido: ")
    apellido2: str = input("Introduce tu segundo apellido: ")
    
    resultado: str = formatear_nombre(nombre, apellido1, apellido2)
    print(resultado)

if __name__ == "__main__":
    main()
