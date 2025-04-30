

# Práctica de Depuración - Ordenamiento en Java

### Descripción de la Práctica

El objetivo de esta práctica es que los estudiantes desarrollen habilidades de depuración y corrección de errores en código Java. Se proporcionan varios métodos de ordenamiento que contienen errores intencionales. Los estudiantes deberán identificar estos errores, corregirlos y documentar los cambios realizados.

Los métodos incluyen:
- Métodos de ordenamiento **Burbuja** (3 variaciones)
- Métodos de ordenamiento **Selección** (3 variaciones)
- Métodos de ordenamiento **Inserción** (3 variaciones)

---

### Pasos a Seguir

1. **Leer y Comprender el Código**
   - Los estudiantes deberán leer completamente el código antes de comenzar a depurar. Entender el propósito de cada método y cómo se espera que funcionen.
   
2. **Identificar Errores**
   - Sin modificar el código inicialmente, los estudiantes deben identificar posibles errores en los métodos y anotarlos.

3. **Depurar y Corregir Errores**
   - Comenzar la depuración descomentando un método a la vez en la clase `App`. Cada vez que se descomente un método, verificar si el código se ejecuta correctamente y corregir los errores encontrados en la clase `MetodosOrdenamiento`.
   - **Nota:** Al finalizar cada corrección, el código debe ejecutarse sin errores.

4. **Documentar Cambios**
   - Los estudiantes deben anotar en cada método el error encontrado y cómo lo corrigieron.
   - **Formato de Comentario**: Antes de cada método modificado en `MetodosOrdenamiento`, deben agregar un comentario explicando el error y la solución aplicada.

5. **Ejecutar Pruebas**
   - Ejecutar el proyecto y verificar los resultados después de cada cambio para asegurarse de que el código funcione correctamente.



### Instrucciones para Ejecutar el Proyecto

1. **Clonar el Repositorio**
   - Clona el proyecto desde el siguiente enlace:
   - [Repositorio GitHub](https://github.com/PabloT18/icc-estructura-01-practicaAutonoma-.git)

2. **Descomentar Métodos en la Clase `App`**
   - En la clase `App.java`, descomenta cada método de forma secuencial para ejecutarlos uno por uno y depurar posibles errores.
   - La idea es que descomentes un método, lo ejecutes, corrijas los errores, y luego avances al siguiente.

   ```java
   // Ejemplo
   int[] arregloBurbujaOrdenado1 = ordenador.burbujaTradicional(arregloBurbuja);
   System.out.println(
       "Resultado burbuja tradicional Metodo 1: " +
       java.util.Arrays.toString(arregloBurbujaOrdenado1));
   ```

3. **Corrección de Errores**
   - Todos los métodos en la clase `MetodosOrdenamiento.java` contienen errores. Revisa la implementación, aplica la corrección necesaria y documenta los cambios realizados directamente en el código.

4. **Pruebas y Verificación**
   - Cada vez que se corrige un error, prueba el código para asegurarte de que el resultado es el esperado. Utiliza el método `System.out.println` para visualizar los arreglos ordenados y verificar que todo funcione correctamente.

---

### Resultados Esperados

- **Mejorar Habilidades de Depuración:** Al identificar y corregir los errores en el código, los estudiantes perfeccionarán su capacidad para depurar programas en Java.
- **Comprensión del Control de Flujo:** Aprenderán cómo afectan las estructuras condicionales y los ciclos en el flujo de ejecución de un programa.
- **Documentación del Proceso:** Cada corrección deberá estar claramente documentada, explicando el error original y la solución aplicada.



### Documentación de Errores y Soluciones

A continuación se incluye un ejemplo de cómo documentar los errores y las correcciones realizadas:

```java
// Método burbujaTradicional
// Error: El método retornaba un arreglo vacío debido a un return incorrecto.
// Solución: Cambié el `return new int[] {}` por `return arreglo` para devolver el arreglo ordenado correctamente.

public int[] burbujaTradicional(int[] arregloOriginal) {
    int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

    int n = arreglo.length;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arreglo[i] > arreglo[j]) {
                int temp = arreglo[i];
                arreglo[i] = arreglo[j];
                arreglo[j] = temp;
            }
        }
    }
    return arreglo;  // Arreglo correctamente ordenado y retornado
}
```


### Consideraciones Finales

- Asegúrate de haber depurado todos los métodos de ordenamiento.
- Cada corrección debe estar documentada en el código con un comentario claro.
- Verifica los resultados con las salidas esperadas para cada método.


---

## Contribute

To contribute to this project, please create a fork and send a pull request, or simply open an issue with your comments and suggestions.

## Authors

- [PABLO TORRES] - Initial development
