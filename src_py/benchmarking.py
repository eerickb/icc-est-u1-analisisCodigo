import random
import time
import metodos_ordenamiento as MetodosOrdenamiento
class Benchmarking:
    
    # public Benchmarking
    def __init__(self):
        print("Benchmarking instanciado")
        self.mO = MetodosOrdenamiento.MetodosOrdenamiento()
        
        arreglo = self.build_arreglo(10000)
                
        tarea_bubble = lambda: self.mO.sort_bubble(arreglo.copy())
        tiempo_bubble = self.contar_con_nano_time(tarea_bubble)
        print(f"Bubble Sort: {tiempo_bubble}")

        tarea_burbuja_mejorado = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo.copy())
        tiempo_burbuja_mejorado = self.contar_con_nano_time(tarea_burbuja_mejorado)
        print(f"Bubble Sort Mejorado: {tiempo_burbuja_mejorado}")

        tarea_seleccion = lambda: self.mO.sort_seleccion(arreglo.copy())
        tiempo_seleccion = self.contar_con_nano_time(tarea_seleccion)
        print(f"Selection Sort: {tiempo_seleccion}")

        tiempos = {
            "Bubble Sort": tiempo_bubble,
            "Bubble Sort Mejorado": tiempo_burbuja_mejorado,
            "Selection Sort": tiempo_seleccion,
        }

        mejor_metodo = min(tiempos, key=tiempos.get)
        print(f"\nEl método mas rapido es: {mejor_metodo}")
        
    def build_arreglo(self, tamano):
        arreglo = []
        for i in range(tamano):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return(fin - inicio)
        
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return(fin - inicio) / 1_000_000_000.0