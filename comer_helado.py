apetece_healado_input = input("¿Te apetece un Helado? (Si / No): ").upper()

if apetece_healado_input == "SI":
    apetece_healado = True
elif apetece_healado_input == "NO":
    apetece_healado = False
else:
    print("No te he entendido pero me lo tomaro como un no")
    apetece_healado = False
tienes_dinero_input = input("¿Tienes dinero para un helado? (Si / No): ").upper()
heladero_sir_input = input("¿Esta el señor de los helados? (Si / No): ").upper()
esta_tu_tia_input = input("¿Estas con tu tia? (Si /No): ").upper()



apetece_healado = apetece_healado_input == "SI"
tienes_dinero = tienes_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
heladero_sir = heladero_sir_input == "SI"

if apetece_healado and puede_permitirselo and heladero_sir:
    print("Pa ti guapo!")
else:
    print("Pues na!")
