import transcriptor_2022
import readline

f = transcriptor_2022

print("Entre el texto con el que quiere trabajar")
print("=========================================")
texto_en_minusculas, texto_sin_puntuacion_split = f.entra_texto()




def main(texto_en_minusculas, texto_sin_puntuacion_split):
    opcion_general = 1

    while True:

        opcion_general = f.menu_general()

        if opcion_general == 1:
            opcion_fonemas = f.menu_fonemas()

        elif opcion_general == 2:
            opcion_silabas = f.menu_silabas()

        elif opcion_general == 3:
            opcion_palabras = f.menu_palabras()

        if opcion_general == 1 and opcion_fonemas == 1:
            transcripcion_1, transcripcion_2, transcripcion_4, transcripcion_5 = f.transcriptor(texto_en_minusculas)

            print(" /", transcripcion_5, " /")

            f.volver_a_ejecutar()


        elif opcion_general == 1 and opcion_fonemas == 2:
            transcripcion_1, transcripcion_2, transcripcion_4, transcripcion_5 = f.transcriptor(texto_en_minusculas)

            frec_fonemas_orden, total_fonemas, cantidad_fonemas_vocales, cantidad_consonantes, \
            cantidad_vocales_anteriores, cantidad_vocales_posteriores, \
            cantidad_vocales_cerradas, cantidad_vocales_abiertas, \
            cantidad_fonemas_nasales, cantidad_fonemas_orales, cantidad_fonemas_fricativos_sordos, \
            cantidad_fonemas_posteriores, cantidad_fonemas_anteriores, cantidad_fonemas_centrales, \
            cantidad_fonemas_consonantes_sonoras, cantidad_fonemas_consonantes_sordas = \
                f.recuento_fonemas(transcripcion_4)

            print("Total de fonemas: ", total_fonemas)
            print(frec_fonemas_orden)

            f.volver_a_ejecutar()





        elif opcion_general == 1 and opcion_fonemas == 3:

            transcripcion_1, transcripcion_2, transcripcion_4, transcripcion_5 = f.transcriptor(texto_en_minusculas)

            frec_fonemas_orden, total_fonemas, cantidad_fonemas_vocales, cantidad_consonantes, \
            cantidad_vocales_anteriores, cantidad_vocales_posteriores, \
            cantidad_vocales_cerradas, cantidad_vocales_abiertas, \
            cantidad_fonemas_nasales, cantidad_fonemas_orales, cantidad_fonemas_fricativos_sordos, \
            cantidad_fonemas_posteriores, cantidad_fonemas_anteriores, cantidad_fonemas_centrales, \
            cantidad_fonemas_consonantes_sonoras, cantidad_fonemas_consonantes_sordas = f.recuento_fonemas(transcripcion_4)

            f.graficos_fonemas(frec_fonemas_orden, total_fonemas, cantidad_fonemas_vocales, cantidad_consonantes,
                               cantidad_vocales_anteriores, cantidad_vocales_posteriores,
                               cantidad_vocales_cerradas, cantidad_vocales_abiertas,
                               cantidad_fonemas_nasales, cantidad_fonemas_orales,
                               cantidad_fonemas_fricativos_sordos, cantidad_fonemas_posteriores,
                               cantidad_fonemas_anteriores, cantidad_fonemas_centrales,
                               cantidad_fonemas_consonantes_sonoras, cantidad_fonemas_consonantes_sordas)


            f.volver_a_ejecutar()


        if opcion_general == 2 and opcion_silabas == 1:
            transcripcion_1, transcripcion_2, transcripcion_4, transcripcion_5 = f.transcriptor(
                texto_en_minusculas)
            texto_convertido_cv = f.conversor_cv(transcripcion_4)

            print(texto_convertido_cv)

            f.volver_a_ejecutar()


        elif opcion_general == 2 and opcion_silabas == 2:
            transcripcion_1, transcripcion_2, transcripcion_4, transcripcion_5 = f.transcriptor(texto_en_minusculas)

            texto_convertido_cv = f.conversor_cv(transcripcion_4)

            ene_tipo_c10v0c2, ene_tipo_c10vc2, ene_tipo_c1v0c2, ene_tipo_c1vc2, ene_tipo_c0v0c, ene_tipo_cv0c2, \
            ene_tipo_c0vc2, ene_tipo_c10vc, ene_tipo_c1v0c, ene_tipo_c10v, ene_tipo_c1v0, ene_tipo_c1vc, \
            ene_tipo_c0v0, ene_tipo_0vc2, ene_tipo_0v0c, ene_tipo_v0c2, ene_tipo_cvc2, ene_tipo_c0vc, \
            ene_tipo_cv0c, ene_tipo_0vc, ene_tipo_v0c, ene_tipo_0v0, ene_tipo_c1v, ene_tipo_vc2, ene_tipo_c0v, \
            ene_tipo_cv0, ene_tipo_cvc, ene_tipo_v0, ene_tipo_0v, ene_tipo_cv, ene_tipo_vc, ene_tipo_v, \
            sumatoria_todo_tipo, n_de_v, frec_silabas_orden, frecuencias_tipos_silabas, \
            sumatoria_silabas_abiertas, sumatoria_silabas_cerradas, \
            sumatoria_diptongos, sumatoria_triptongos, sumatoria_dip_crecientes, sumatoria_dip_decrecientes, \
            sumatoria_dip_trip_tongos, sumatoria_sin_dip_trip_tongo, \
            sumatoria_inicio_consonante, sumatoria_inicio_cons_simple, \
            sumatoria_inicio_cons_comple = f.analizador_silabico(texto_convertido_cv)

            print("Total de sílabas: ", sumatoria_todo_tipo)
            print("Sílabas CV :", ene_tipo_cv, "(un ", (ene_tipo_cv * 100 / sumatoria_todo_tipo), "% )")
            print("Sílabas CVC :", ene_tipo_cvc, "(un ", (ene_tipo_cvc * 100 / sumatoria_todo_tipo), "% )")
            print("Sílabas VC :", ene_tipo_vc, "(un ", (ene_tipo_vc * 100 / sumatoria_todo_tipo), "% )")

            f.volver_a_ejecutar()


        elif opcion_general == 2 and opcion_silabas == 3:
            transcripcion_1, transcripcion_2, transcripcion_4, transcripcion_5 = f.transcriptor(texto_en_minusculas)

            texto_convertido_cv = f.conversor_cv(transcripcion_4)

            ene_tipo_c10v0c2, ene_tipo_c10vc2, ene_tipo_c1v0c2, ene_tipo_c1vc2, ene_tipo_c0v0c, ene_tipo_cv0c2, \
            ene_tipo_c0vc2, ene_tipo_c10vc, ene_tipo_c1v0c, ene_tipo_c10v, ene_tipo_c1v0, ene_tipo_c1vc, \
            ene_tipo_c0v0, ene_tipo_0vc2, ene_tipo_0v0c, ene_tipo_v0c2, ene_tipo_cvc2, ene_tipo_c0vc, \
            ene_tipo_cv0c, ene_tipo_0vc, ene_tipo_v0c, ene_tipo_0v0, ene_tipo_c1v, ene_tipo_vc2, ene_tipo_c0v, \
            ene_tipo_cv0, ene_tipo_cvc, ene_tipo_v0, ene_tipo_0v, ene_tipo_cv, ene_tipo_vc, ene_tipo_v, \
            sumatoria_todo_tipo, n_de_v, frec_silabas_orden, frecuencias_tipos_silabas, \
            sumatoria_silabas_abiertas, sumatoria_silabas_cerradas, \
            sumatoria_diptongos, sumatoria_triptongos, sumatoria_dip_crecientes, sumatoria_dip_decrecientes, \
            sumatoria_dip_trip_tongos, sumatoria_sin_dip_trip_tongo, \
            sumatoria_inicio_consonante, sumatoria_inicio_cons_simple, \
            sumatoria_inicio_cons_comple = f.analizador_silabico(texto_convertido_cv)

            f.graficos_silabas(frec_silabas_orden, sumatoria_todo_tipo, n_de_v, frec_silabas_orden,
                               frecuencias_tipos_silabas, sumatoria_silabas_abiertas, sumatoria_silabas_cerradas,
                               sumatoria_diptongos, sumatoria_triptongos, sumatoria_dip_crecientes,
                               sumatoria_dip_decrecientes,
                               sumatoria_dip_trip_tongos, sumatoria_sin_dip_trip_tongo, sumatoria_inicio_consonante,
                               sumatoria_inicio_cons_simple, sumatoria_inicio_cons_comple)

            f.volver_a_ejecutar()

        if opcion_general == 3 and opcion_palabras == 1:

            lista_palabras = f.analisis_compuestas(texto_sin_puntuacion_split)

            lista_compleja_palabras = f.identificador_silaba_tonica(lista_palabras)

            total_palabras, contador_atonas, contador_tonicas, contador_bisilabas_atonas, contador_atonas_monosilabas, \
            contador_tonicas_monosilabas, contador_agudas, contador_graves, contador_esdrujulas, contador_sobresdrujulas \
                = f.contador_palabras(lista_compleja_palabras)

            f.volver_a_ejecutar()


        elif opcion_general == 3 and opcion_palabras == 2:

            lista_palabras = f.analisis_compuestas(texto_sin_puntuacion_split)

            print(lista_palabras)

            lista_compleja_palabras = f.identificador_silaba_tonica(lista_palabras)
            contador_esdrujulas, contador_graves, contador_agudas, contador_monosilabos_tonicos, \
            contador_monosilabos_atonos, contador_bisilabos_atonos = f.recuento_tipos_palabras_g_a_e(
                lista_compleja_palabras)

            print("Palabras tónicas:    ",
                  (contador_graves + contador_agudas + contador_esdrujulas + contador_monosilabos_tonicos))
            print("Palabras átonas:     ", contador_monosilabos_atonos + contador_bisilabos_atonos)
            print("=========")
            print("esdrújulas: ", contador_esdrujulas)
            print("graves:     ", contador_graves)
            print("agudas:     ", contador_agudas)
            print("=========")
            print("Monosílabos tónicos: ", contador_monosilabos_tonicos)
            print("=========")
            print("Monosílabos átonos: ", contador_monosilabos_atonos)
            print("Bisílabos átonos: ", contador_bisilabos_atonos)

            f.volver_a_ejecutar()


        elif opcion_general == 3 and opcion_palabras == 4:
            print("Opción 4. Gráficos")

            lista_palabras = f.analisis_compuestas(texto_sin_puntuacion_split)
            lista_compleja_palabras = f.identificador_silaba_tonica(lista_palabras)
            total_palabras, contador_atonas, contador_tonicas, contador_bisilabas_atonas, contador_atonas_monosilabas, \
            contador_tonicas_monosilabas, contador_agudas, contador_graves, contador_esdrujulas, contador_sobresdrujulas = f.contador_palabras(lista_compleja_palabras)
            f.graficos_palabras(total_palabras, contador_atonas, contador_tonicas, contador_bisilabas_atonas, contador_atonas_monosilabas, \
        contador_tonicas_monosilabas, contador_agudas, contador_graves, contador_esdrujulas, contador_sobresdrujulas)

            f.volver_a_ejecutar()


        elif opcion_general == 3 and opcion_palabras == 5:
            contador_tonicas_monosilabas, contador_atonas_monosilabas, contador_bisilabas_atonas, contador_graves, \
            contador_graves_con_acento_grafico, contador_agudas, contador_agudas_con_acento_grafico, \
            contador_esdrujulas, contador_sobresdrujulas, contador_sec_cerrada_tonica = f.docencia01(texto_sin_puntuacion_split)

            total_palabras = (contador_atonas_monosilabas + contador_tonicas_monosilabas + contador_bisilabas_atonas\
                              + contador_graves + contador_agudas + contador_esdrujulas + contador_sobresdrujulas)

            diversidad_de_palabras = 0

            contador_dificultad = 0

            if contador_esdrujulas >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + (contador_esdrujulas * 2)

            if contador_atonas_monosilabas >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + (contador_atonas_monosilabas * 1)

            if contador_tonicas_monosilabas >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + (contador_tonicas_monosilabas * 2)

            if contador_bisilabas_atonas >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + (contador_bisilabas_atonas * 1)

            if contador_agudas >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + (contador_agudas * 2)

            if contador_graves_con_acento_grafico >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + (contador_graves * 2)

            if (contador_graves - contador_graves_con_acento_grafico) >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + (contador_graves * 1)

            if contador_sec_cerrada_tonica >= 1:
                diversidad_de_palabras = diversidad_de_palabras + 1
                contador_dificultad = contador_dificultad + ( contador_sec_cerrada_tonica * 2)

            grado_de_dificultad_acentual= f.indice_dificultad_acentual(total_palabras, diversidad_de_palabras, contador_dificultad)

            print(total_palabras/diversidad_de_palabras, "es total_palabras (",total_palabras,")  / tipos diversos (", diversidad_de_palabras,")")

            print("El texto contiene ", diversidad_de_palabras, "tipos diversos de palabras")

            if contador_sobresdrujulas > 0:
                print("Tiene sobresdrújulas     :   ", contador_sobresdrujulas)
            else:
                print("No tiene sobresdrújulas")

            if contador_esdrujulas > 0:
                print("Tiene esdrújulas         :   ", contador_esdrujulas)
            else:
                print("No tiene esdrújulas")

            if contador_graves_con_acento_grafico > 0:
                print("Tiene graves con tilde   :   ", contador_graves_con_acento_grafico)
            else:
                print("No tiene graves escritas con acento")

            if (contador_graves - contador_graves_con_acento_grafico) > 0:
                print("Tiene graves escritas sin acento  :", contador_graves - contador_graves_con_acento_grafico)
            else:
                print("No tiene graves escritas sin acento")

            if contador_agudas_con_acento_grafico > 0:
                print("Tiene agudas escritas con acento:  ", contador_agudas_con_acento_grafico)
            else:
                print("No tiene graves escritas con acento")

            if (contador_agudas-contador_agudas_con_acento_grafico) > 0:
                print("Tiene agudas escritas sin acento:   ", contador_agudas-contador_agudas_con_acento_grafico)
            else:
                print("No tiene agudas escritas sin acento")

            if contador_bisilabas_atonas > 0:
                print("Tiene bisílabos átonos:     ", contador_bisilabas_atonas)
            else:
                print("No tiene bisílabos átonos")

            if contador_tonicas_monosilabas > 0:
                print("Tiene monbosílabos tónicos:    ", contador_tonicas_monosilabas)
            else:
                print("No tiene monosílabos tónicos")

            if contador_atonas_monosilabas > 0:
                print("Tiene monosílabos átonos:    ", contador_atonas_monosilabas)
            else:
                print("No tiene monosílabos átonos")


            print("Dificultad: ", grado_de_dificultad_acentual)

            f.volver_a_ejecutar()


main(texto_en_minusculas, texto_sin_puntuacion_split)
