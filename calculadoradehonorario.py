# Monto
monto = int(input("Ingrese el monto: "))

# Crear lista de años
anios = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028]

# Crear lista de porcentajes asociados a cada año
porcentajes = [10.75, 11.5, 12.25, 13, 13.75, 14.5, 15.25, 16, 17]

# Mostrar porcentajes con el año correspondiente
for i in range(len(anios)):
    print(anios[i], porcentajes[i])

# Pedir al usuario que seleccione un año y obtener el índice correspondiente
anio_seleccionado = int(input("Ingrese el año para el cual desea seleccionar el porcentaje (2020-2028): "))
indice_porcentaje = anios.index(anio_seleccionado)

# Verificar que el año esté en la lista
if anio_seleccionado in anios:
    porcentaje_seleccionado = porcentajes[indice_porcentaje]
    print("Porcentaje seleccionado para el año", anio_seleccionado, ":", porcentaje_seleccionado)
else:
    print("El año ingresado no está en la lista.")

# Calcular porcentaje
porcentajeparacalculo = (100 - porcentaje_seleccionado) / 100

# Liquido
print("liquido Hacer boleta")
hacerboletaliquido=int(monto/porcentajeparacalculo)
print(hacerboletaliquido)
print("liquido Recibiras")
recibirasliquido= int(monto)
print(recibirasliquido)
print("liquido Retencion Sii")
retencionliquido=int(hacerboletaliquido-monto)
print(retencionliquido)

# Bruto
print("bruto Hacer boleta")
hacerboletabruto=int(monto)
print(hacerboletabruto)
print("bruto Recibiras")
recibirasbruto= int(monto*porcentajeparacalculo)
print(recibirasbruto)
print("bruto Retencion Sii")
retencionbruto=int(monto-recibirasbruto)
print(retencionbruto)