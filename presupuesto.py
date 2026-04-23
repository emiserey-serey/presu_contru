import os
os.system("cls")
IVA = 0.19
PRESUPUESTO_MAXIMO = 50000000
nombre_proyecto = input("Nombre del proyecto: ")
try:
    metros_cuadrados = float(input("Cantidad de metros cuadrados a construir: "))
    if metros_cuadrados <= 0:
        print ("Error, los metro cuadrados ingresados deben ser mayor a 0.")
        os.system("cls")
    else:
        costo_por_metro = float(input("Costo por metro cuadrado: "))
        if costo_por_metro <= 0:
            print("Error, el costo por metro debe ser mayor a 0.")
            os.system("cls")
        else:
            cantidad_trabajadores = float(input("Ingrese la cantidad de trabajadores: "))
            if cantidad_trabajadores <= 0:
                print("Error, la cantidad de trabajadores debe ser mayor a 0.")
                os.system("cls")
            else:
                pago_por_trabajador = float(input("Pago por trabajador: "))
                if pago_por_trabajador <= 0:
                    print("Error, debe ingresar un pago mayor a 0.")
                    os.system("cls")
                else:
                    costo_materiales = metros_cuadrados * costo_por_metro 
                    costo_mano_obra = cantidad_trabajadores * pago_por_trabajador 
                    costo_neto = costo_materiales + costo_mano_obra
                    iva_aplicado = costo_neto + IVA
                    costo_total = costo_neto + iva_aplicado
                    if costo_total <= PRESUPUESTO_MAXIMO:
                        estado = "Dentro del presupuesto"
                    elif costo_total > PRESUPUESTO_MAXIMO and costo_total <= PRESUPUESTO_MAXIMO * 1.10:
                        estado = "Presupueso ajustado"
                    else:
                        estado = "Fuera de presupuesto"
                        print("------RESUMEN DEL PROYECTO-----")
                        print(f"Nombre del proyecto: {nombre_proyecto}")
                        print(f"Costo toal: {round(costo_total,2)}")
                        print(f"Estado del proyecto: {estado}")
                        print("-----")
except:
    print("Error, ingrese sólo número válidos")

