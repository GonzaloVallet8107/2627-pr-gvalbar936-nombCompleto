# Práctica Python - Nombre completo

**Repositorio:** `2627-pr-usuarioPasen-nombCompleto`

## Enunciado
Desarrolla un programa en Python que solicite el nombre, el primer apellido y el segundo apellido de una persona y muestre su nombre completo correctamente formateado. 

Implementa la siguiente función:
`formatear_nombre(nombre, apellido1, apellido2)`

La función debe devolver una cadena con el nombre completo, cumpliendo las siguientes condiciones:
* Eliminar los espacios sobrantes al principio y al final de cada dato.
* Convertir la primera letra de cada palabra a mayúscula y las restantes a minúscula.
* Admitir nombres compuestos.
* Unir el nombre y los dos apellidos separados por un espacio.

### Ejemplo de ejecución
* **Entrada:** `JUAN ANTONIO`, `GARCÍA`, `pérez`
* **Salida:** `Juan Antonio García Pérez`

---

## Requisitos de desarrollo
1. **Repositorio:** Crea un repositorio público de GitHub con el nombre indicado, sustituyendo `usuarioPasen` por tu usuario.
2. **Estructura del proyecto:** Utiliza la estructura básica de un proyecto Python:
   * `src/main.py`
   * `README.md`
   * `.gitignore`
3. **Documentación inicial:** Copia este enunciado en el archivo `README.md`.
4. **Función Principal:** Implementa una función `main()` que gestione la entrada y salida de datos.
5. **Modularidad:** Realiza el procesamiento del nombre dentro de `formatear_nombre()`, utilizando parámetros y devolviendo el resultado mediante `return`.
6. **Tipado:** Incluye anotaciones de tipo en variables, parámetros y retornos de las funciones.
7. **Docstrings:** Documenta la función de procesamiento mediante una *docstring* que incluya descripción, parámetros (`:param:`) y valor de retorno (`:return:`).
8. **Pruebas:** Comprueba el funcionamiento del programa con diferentes nombres y apellidos.
9. **Control de versiones:** Registra los cambios con Git y publica el repositorio en GitHub.

---

## Entrega
Entrega en esta tarea de Moodle la **URL de tu repositorio público** de GitHub.