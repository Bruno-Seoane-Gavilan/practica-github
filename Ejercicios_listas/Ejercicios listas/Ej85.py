#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
import statistics

num_alumnos=int(input("Introduce el número de alumnos: "))
notas_catalan=[]
notas_ingles=[]
notas_castellano=[]

for x in range(num_alumnos):
    nota_cat=float(input(f"Introduce la nota de catalán del alumno {x+1}: "))
    nota_ing=float(input(f"Introduce la nota de inglés del alumno {x+1}: "))
    nota_cas=float(input(f"Introduce la nota de castellano del alumno {x+1}: "))
    notas_catalan.append(nota_cat)
    notas_ingles.append(nota_ing)
    notas_castellano.append(nota_cas)
media_catalan=sum(notas_catalan)/num_alumnos
media_ingles=sum(notas_ingles)/num_alumnos
media_castellano=sum(notas_castellano)/num_alumnos
mediana_catalan=statistics.median(notas_catalan)
mediana_ingles=statistics.median(notas_ingles)
mediana_castellano=statistics.median(notas_castellano)
print(f"Media de catalán: {media_catalan}, Mediana de catalán: {mediana_catalan}")
print(f"Media de inglés: {media_ingles}, Mediana de inglés: {mediana_ingles}")
print(f"Media de castellano: {media_castellano}, Mediana de castellano: {mediana_castellano}")
