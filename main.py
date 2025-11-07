# Programa qe permite a un profesor registrar las notas de sus alumnos y luego muestre un resumen de los resultados
# El programa debe cumplir con los siguientes requisitos
#   1.Ingreso de cantidad: Preguntar cuantos alumnos hay en clase (validar que sea un numero positivo)
#   2.Registro de calificaciones (Lista y for):
#       Utiliza una lista de tipo duble (o float)para almacenar las calificaciones.
#       Usar un ciclo for parasolicitarlacalificacion decadaalumnos
#   3.Validacion de datos (if):
#       Cada calificacion debe ser validada. Si la nota ingresada no esta en el rango [0.0 - 10.0],el programa debe mostrar n mensaje de error y volver a solicitar lanota para ese mismo  aluno (se recomienda un cilo do-while dentro del for para esto).
#   4.Analisis de resultados (if y for): Despues de ingresar todas las notas, el programa debe:
#       Calcular elpromedio de la clase
#       Contar cuantos alumnos aprobaron (nota >= 7.0) y cuantos reprobaron (nota < 7.0).
#   5.Resumen final:Mostrar el resumen de los datos por pantalla.
 
def obtener_numero_alumnos():
    while True:
        try:
            num_alumnos = int(input("Ingrese el número de alumnos: "))
            if num_alumnos > 0:
                return num_alumnos
            else:
                print("El número de alumnos debe ser un entero positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
def registrar_calificaciones(num_alumnos):
    calificaciones = []
    for i in range(num_alumnos):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
                if 0.0 <= calificacion <= 10.0:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar en el rango de 0.0 a 10.0.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
    return calificaciones

def analizar_resultados(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    aprobados = sum(1 for calificacion in calificaciones if calificacion >= 7.0)
    reprobados = len(calificaciones) - aprobados
    return promedio, aprobados, reprobados

def mostrar_resumen(promedio, aprobados, reprobados):
    print(" Resumen de Resultados ")
    print(f"Promedio de la clase: {promedio:.2f}")
    print(f"Alumnos aprobados: {aprobados}")
    print(f"Alumnos reprobados: {reprobados}")

def main():
    num_alumnos = obtener_numero_alumnos()
    calificaciones = registrar_calificaciones(num_alumnos)
    promedio, aprobados, reprobados = analizar_resultados(calificaciones)
    mostrar_resumen(promedio, aprobados, reprobados)

if __name__ == "__main__":
    main()
