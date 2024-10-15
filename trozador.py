# Funcionalidad:

# Dado un texto (se da uno por defecto) y un número de participantes
# el programa entrega el texto partido en partes iguales para cada persona


texto = """
El fin de semana se realizaron cientos de actividades programadas en museos, galerías y centros culturales en todo el país, en el marco de la Noche de los Museos. Según información preliminar, más de cien mil personas visitaron más de doscientos espacios y circuitos patrimoniales gratuitos en horario extendido, en un evento organizado por el Ministerio de las Culturas, las Artes y el Patrimonio. La multitudinaria inauguración, que fue encabezada por la ministra de las Culturas, Carolina Arredondo, se realizó en el Museo Nacional de Bellas Artes, donde se llevó a cabo un recorrido por las salas de exposiciones y donde también se presenció un concierto del Grupo Cámara Boecio. Todo, ante los aplausos de miles de personas que congregó el espacio ubicado en Parque Forestal. Además, la jornada de ayer, contó con un plan de recorridos especial de buses del sistema Red de Movilidad para distintos sectores de la capital. “Estamos muy felices porque la cifra preliminar que tenemos de asistencia de personas a Noche de Museos es de más de cien mil personas. Durante estos días vamos a terminar de obtener los números finales de asistentes a los distintos espacios, a los más de doscientos espacios que se sumaron a esta Noche de Museos a lo largo de todo el país. Es algo que nos llena de alegría ya que es la respuesta también de la ciudadanía hacia el arte, la cultura y el patrimonio”, afirmó la ministra. Los museos nacionales Museo Nacional de Bellas Artes, Museo Nacional de Historia Natural y Museo Histórico Nacional, concentraron altas cifras de concurrencia, con visitantes que participaron activamente de las actividades programadas. Estos espacios, que son parte del Servicio de Patrimonio Cultural recibieron preliminarmente más de veintitrés mil visitas durante toda la jornada del viernes. Solamente el Museo Nacional de Bellas Artes registró cerca de once mil asistentes. En tanto, Valparaíso es la región que ha registrado la mayor cantidad de visitas con más de diez mil personas, destacando los ocho museos de la Red Viva, zona que también fue recorrida por la directora del Servicio Nacional del Patrimonio Cultural, Nélida Pozo. Le siguió Maule (tres mil cuatrocientas ochenta y uno) destacando el Museo ogiguiniano y de Bellas Artes de Talca con dos mil diez, Biobío (tres mil trescientos sesenta y seis) y Coquimbo (tres mil cuarenta y seis). Esta es la primera versión de Noche de Museos la que se inspira en Museos de Medianoche, una celebración que vuelve luego de seis años y que permitió abrir espacios patrimoniales públicos y privados de manera gratuita con horario extendido y actividades especiales.

"""

def trozado_de_texto(texto, participantes):

    por_palabras = texto.split()

    largo_texto = len(por_palabras)

    repartija = round(largo_texto/participantes)

    for i_cadena in range(0, len(por_palabras), repartija):

        inicio_cadena = i_cadena + repartija

        retazo = (por_palabras[i_cadena:inicio_cadena])

       # print(retazo)

        concatenada = " ".join(retazo)

        print(concatenada)

participantes = int(input("Cantidad de participantes"))

trozado_de_texto(texto, participantes)
