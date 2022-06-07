"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde por dia y por semana.
"""
horas = int(input("Ingrese horas trabajadas: "))
costo_por_hora = int(input("Ingresa cuanto cobras por hora: "))
sueldo_diario = (horas * costo_por_hora)
sueldo_semanal = (sueldo_diario * 7)
print(f"Usted cobra ${sueldo_diario} cada dia. Y cobra ${sueldo_semanal} por semana")