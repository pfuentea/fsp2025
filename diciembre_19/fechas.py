import datetime

fecha_hora_actual=datetime.datetime.now()
fecha_actual=datetime.date.today()
hora_actual=fecha_hora_actual.time()
fecha_formato=fecha_hora_actual.strftime("%d-%m-%Y %H:%M:%S")

fecha_custom=datetime.datetime(2025,10,15,12,30,23).strftime("%d-%m-%Y %H:%M:%S")

print(f" Fecha y hora actual: {fecha_hora_actual}") 
print(f" Fecha actual: {fecha_actual}") 
print(f" Hora actual: {hora_actual}") 
print(f" Fecha y hora con formato: {fecha_formato}")
print(f" Tipo de objeto:{type(fecha_hora_actual)}") 
print(f" Fecha Personalizada:{fecha_custom}") 

