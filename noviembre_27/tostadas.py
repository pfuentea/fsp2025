print("Bienvenido al asistente de tostadas ÑAM!")
hay_pan=input("Hay pan disponible? (s/n):")

if hay_pan=="n":
    print("No hay pan. No podemos hacer tostadas :''( ")
else:
    tostado=input("El pan está tostado?(s/n):")

    if tostado=="n":
        print("Tostando el pan...")

    mantequilla=input("Quiere ponerle mantequilla?(s/n):")
    if mantequilla=="s":
        print("Agregando mantequilla al pan tostado!")
    print("Tostada lista para servir! Disfrute su pan tostado!")
  
print("Gracias por usar el asistente!")