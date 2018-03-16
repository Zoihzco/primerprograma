apetece_fumar = input("Quieres Maria? (Si / No): ").upper()

if apetece_fumar == "SI":
    apetece_fumar_input = True

elif apetece_fumar == "NO":
    apetece_fumar_input = False
else:
    print("No te he entendido pero me lo tomare como que no , mejor mas hay")
    apetece_fumar_input = False


dinero = input("Tienes las pasta (Si / No): ").upper()
tu_madre = input ("Te dara dinero tu madre (Si / No): ").upper()
estara_cam = input ("Esta cam para ir? (Si / No): ").upper()


apetece_fumar_input = apetece_fumar == "SI"
dinero_input = dinero == "SI"
tu_madre_input = tu_madre == "SI"
dinero_permitirmelo = dinero or tu_madre
estara_cam_input = estara_cam == "SI"
if apetece_fumar_input and dinero_permitirmelo and estara_cam_input:
    print("Prueba completada")

else:
    (print("No gordi hoy hay nada"))