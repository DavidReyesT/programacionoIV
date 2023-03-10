import sqlite3


def Insertadato(palabra , significado):
    conn = sqlite3.connect('slam.db')
    strsql = "insert into SLAM (id, expresion, significado) values (null,'" + palabra + "','" + significado + "')"

    conn.execute(strsql)
    conn.commit()
    print("")
    print("                                 -->Registro Insertado Con exito")
    print("")
    p=input("Presione una <Enter> para continuar")
    conn.close()

def Editadato(palabra , significado, idpalabra):
    conn = sqlite3.connect('slam.db')
    strsql = "update SLAM set expresion = '" + palabra + "', significado = '" + significado + "' where id = " + str(idpalabra)
    conn.execute(strsql)
    conn.commit()
    print("                                 --> Registro Actualizado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")
    conn.close()

def Borradato(idpalabra):
    conn = sqlite3.connect('slam.db')
    strsql = "delete from  SLAM where id = " + str(idpalabra)
    conn.execute(strsql)
    conn.commit()
    print("                                 --> Registro Eliminado con Exito")
    print("")
    p = input("Presione una <Enter> para continuar")
    conn.close()

def BuscaDato(palabra, muestra):
    conn = sqlite3.connect('slam.db')
    cursor = conn.cursor()
    strsql = "SELECT ID,Expresion, significado FROM SLAM where EXPRESION like '%" + palabra + "%'"
    cursor.execute(strsql)
    datos = cursor.fetchall()
    print("")
    for dato in datos:
            print (dato)
    if muestra == 1:
        print("                                 --> Registros encontrados")
        print("")
        p=input("Presione una <Enter> para continuar")

    conn.close()

def CreaBD():
    conn = sqlite3.connect('slam.db')
    consulta = conn.execute("select coalesce(1,0) existe from sqlite_master where name = 'SLAM'")
    for c in consulta:
        if c[0] == 1:
            conn.execute('''DROP TABLE SLAM''')

    conn.execute('''CREATE TABLE SLAM
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            EXPRESION TEXT NOT NULL,
            SIGNIFICADO TEXT NOT NULL)''')

    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'A GUANCHINCHE',' A CABALLITO, CARGANDO A ESPALDAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'A MONCHINCHE',' A CABALLITO, CARGANDO A ESPALDAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ABUELAZ??N ',' D??CESE DE LA CONDUCTA DE ENTUSIASMO EXCESIVO QUE LOS ABUELOS SIENTEN POR LOS NIETOS; ACTITUD T??PICA DE PERSONAS ANCIANAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AGARRAR LOS MANGOS BAJITOS',' HACER ALGO DE LA FORMA M??S FACIL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AHUEVADO',' SIN??NIMO DE HUEV??N, LENTO, IMB??CIL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AHUEVAO',' SIN??NIMO DE HUEV??N, LENTO, IMB??CIL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AHUEVAZ??N',' SITUACION CALIFICADA DE AHUEVADA (SITUACI??N CAUSADA PUR UNA TONTERA/POR UN TONTO).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ALL?? ADONDE UNO ',' EL INTERIOR.(NORMALMENTE PRONUNCIADO ALLA ONDE UNO) ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRABALERO',' BUSCAPLEITOS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRABALERA',' BUSCAPLEITOS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRANQUE',' PARRANDA.((DE ARRANCARSE [IRSE DE FIESTA/A PARRANDEAR]) )')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARREBATI??A, PATA Y PU??ETE ',' LO QUE PASA DESPUES QUE ALGUIEN ROMPE LA PI??ATA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRECHO',' PERSONA QUE ESTA EXCITADA SEXUALMENTE. PERSONA QUE PUEDE REALIZAR CUALQUIER TRABAJO O HAZA??A(TERMINO UTILIZADO CON MAYOR FRECUENCIA EN EL INTERIOR DEL PA??S).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARRECHA ',' PERSONA QUE ESTA EXCITADA SEXUALMENTE. PERSONA QUE PUEDE REALIZAR CUALQUIER TRABAJO O HAZA??A(TERMINO UTILIZADO CON MAYOR FRECUENCIA EN EL INTERIOR DEL PA??S).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARREPINCHOSO ',' PERSONA QUE LE GUSTA EL ARRANQUE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARREPINCHOSA ',' PERSONA QUE LE GUSTA EL ARRANQUE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARROPAR',' HACER EL AMOR CON LA ROPA, COM??NMENTE VISTO EN SARAOS O EN LUGARES CON POCA INTIMIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ARROZ CON MANGO',' GRANDES PROBLEMAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TREPA QUE SUBE',' GRANDES PROBLEMAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PANDEMONIO',' GRANDES PROBLEMAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'AYALA ',' INTERJECCI??N DE SORPRESA O ENOJO. ADAPTADO DE VAYA LA. USUALMENTE UTILIZADO CON PALABRAS CURIOSAS Y SOECES. EJM: AYALA PESTE, ??YALA M??QUINA, ??YALA VIDA. (PRONUNCIADO TAMBI??N ??SHALA)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BAGRE',' MUJER HORRIBLE O POCO AGRACIADA F??SICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CANGREJA',' MUJER HORRIBLE O POCO AGRACIADA F??SICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'G??RGOLA',' MUJER HORRIBLE O POCO AGRACIADA F??SICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COCOBOLA',' MUJER HORRIBLE O POCO AGRACIADA F??SICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BA??O DE PUEBLO ',' PARTICIPAR DE ALGUNA ACTIVIDAD NORMALMENTE DE TIPO FOLKLORICA PARA RENOVAR EL ESPIRITU PANAMENO... IRSE A UN PINDIN, CANTADERAS, COMER FRITURAS, BAILE TIPICO, ETC.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BARRIADA BRUJA',' ASENTAMIENTO HUMANO INFORMAL/ VILLA M??SERA O FAVELA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BARRIO BRUJO ',' ASENTAMIENTO HUMANO INFORMAL/ VILLA M??SERA O FAVELA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BATE','EXCUSA DIF??CIL DE CREER, O GOLPE DE SUERTE. EJM:JAMES BOND ES UN BATOSO, ME METI?? UN BATE; CIGARRO DE MARIHUANA DE GRAN TAMA??O')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BATER??A ',' PAPEL CON RESPUESTAS DE UN EXAMEN')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BERRACO',' (SUST) PERSONA DIESTRA, H??BIL; (ADJ) FURIOSO; (ADJ) D??FICIL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BERRACA',' (SUST) PERSONA DIESTRA, H??BIL; (ADJ) FURIOSO; (ADJ) D??FICIL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BERRINCHE ',' ARMAR UN ESC??NDALO O NECEDAD [EJM. ESE NI??O TIENE UN BERRINCHE]. OLOR FUERTE A ORINE [EJM. ESTE BA??O HUELE A BERRINCHE].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BIENCUIDAO ',' INDIVIDUO QUE SE GANA LA VIDA CUIDANDO AUTOS Y CONSIGUIENDO ESTACIONAMIENTOS EN LUGARES COMO CENTROS COMERCIALES, DISCOTECAS, CINES, ALMACENES.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BIRRIA ',' JUEGO MUY REPETITIVO SIN ESPIRITU DE COMPETENCIA O FINALIDAD ALGUNA, COMUNMENTE USADO PARA LOS VIDEOJUEGOS, FUTBOL O BALONCESTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BLANCO ',' CIGARRILLO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BLAZEAR',' OFENDER.(SE UTILIZA COMO VERBO EN INFINITIVO-GERUNDIO, EJ: JUAN ME ESTABA BLAZEANDO.)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BOCHINCHE',' CHISME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BORRADOR',' UN GRAN AUTOB??S O CAMION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BOTE',' PEDIR QUE TE LLEVEN O TE DEN UN AVENTON A ALGUN LUGAR (HEY UN BOTE PUE).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BOTELLA ',' PERSONA QUE COBRA PERO NO TRABAJA; SE DA MUCHO ESTA SITUACI??N EN SECTOR P??BLICO PANAME??O.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BRAVOS DE BOSTON ',' EL MEJOR DE UNA PROFESI??N. DEDICADO A LOS BRAVOS DE BOSTON DE 1914. [1]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BRUJO',' BARATO, DE POCA CALIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLO ',' BARATO, DE POCA CALIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BUCO ',' MUCHO (GALICISMO; DERIVADO DE BEAUCOUP).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BUENO',' QUE ESTA MUY BONITA O BONITA Y TIENE BUEN FISICO, [EJM. MAMI TAS WENA]; TAMBI??N PAY (COMO EN ES UN PAY).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BUENA',' QUE ESTA MUY BONITA O BONITA Y TIENE BUEN FISICO, [EJM. MAMI TAS WENA]; TAMBI??N PAY (COMO EN ES UN PAY).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BULTO',' PERSONA QUE NO TIENE UN BUEN DESEMPE??O DE SUS FUNCIONES, VIENE DE OCUPAR UN ESPACIO DETERMINADO SIENDO IRRELEVANTE PARA LA SITUACION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'BURUNDANGA','ALIMENTO DE POCO VALOR NUTRITIVO. EJM: CARAMELOS, CHOCOLATES, CHICLES, ETC...')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CAF?? ',' UNA PALMADA FUERTE ??TRAS EN LA CABEZA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CAMAR??N',' ACTIVIDAD EXTRACURRICULAR QUE PERMITE A UN INDIVIDUO GANAR DINERO EXTRA. SU ORIGEN SE REMONTA A LOS TIEMPOS EN QUE LOS GRINGOS LE DEC??AN A LOS LOCALES COME AROUND... (P??SATE POR AQU??). [EJM. VOY A HACER UN CAMAR??N]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CANGREJA ',' MUJER DE BAJA CATEGORIA QUE USALMENTE SALE POR LAS NOCHES Y NO PUEDE CAMINAR NORMALMENTE DE TANTA PROFESION... BAJA LA MAREA Y SUBEN LAS CANGREJAS EXPRESION QUE SE USA CUANDO CAE LA NOCHE EN PANAMA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHACHAI ',' VESTIDO DE NI??A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHAMB??N ',' TORPE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHANTIN ',' CASA, HOGAR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHEN CHEN ',' DINERO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHEQUEAR',' REVISAR')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHICHA ',' REFRESCO O BEBIDA FERMENTADA. (ESTA PALABRA, RECOGIDA POR LA RAE Y DE ETIMOLOG??A PANAME??A ES USADA EN CENTROAM??RICA, CHILE Y PER??, CON CIERTAS VARIACIONES)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHICH?? ',' 1)FORMA CARI??OSA DE DECIR BEBE; FORMA CARI??OSA DE DEICIRLE A NOVIA O NOVIO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIFEAR ',' NO INVITAR/IGNORAR A ALGUNA PERSONA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHILIN ',' DEL INGLES CHILLING ESTAR TRANQUILO; PARKEAR COOL; EJM: ESTABA PARKEANDO CHILLIN EN LA CHANTIN.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHINGUEAR ',' APOSTAR')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHINO O CHINITO ',' BODEGA / TIENDA DE ABARROTES (D??CESE PORQUE GENERALMENTE EST??N ADMINISTRADAS POR CHINOS)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIQUISHOW',' DICESE DE UN ESPECT??CULO P??GIL NO PROGRAMADO EN EL QUE LOS COMBATIENTES POR LO GENERAL NO SABEN PELEAR DE FORMA VISTOSA. TAMBI??N UTILIZADO PARA INDICAR CUANDO A ALGUIEN LE HACEN UN ESPECTACULO FRENTE A OTRAS PERSONAS, REGULARMENTE REALIZADO POR EL SEXO FEMENINO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIRRISCO ',' BEBIDA HECHA EN CASA PROVENIENTE COM??NMENTE DE LA FERMENTACION Y DESTILACION DEL MAIZ O LA CA??A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHIVA ',' TRANSPORTE COLECTIVO DE CAPACIDAD MEDIA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOBORRO',' PERSONA BRUSCA Y DE POCA CAPACIDAD PARA DESARROLLAR UNA ACTIVIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOBORRA',' PERSONA BRUSCA Y DE POCA CAPACIDAD PARA DESARROLLAR UNA ACTIVIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLIPAY ',' MUJER MESTIZA/IND??GENA ATRACTIVA F??SICAMENTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLO',' EN ZONAS DEL INTERIOR HACIENDO REFERENCIA A AMIGO, EN LA CIUDAD HACE REFERENCIA A PERSONAS DEL INTERIOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLOMETAL ',' CHOLO O INDIGENA QUE SIGUE MODISMOS DE ROQUEROS, PUNKS Y/O HEAVYMETALS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLOPOP ',' UN COMPA QUE ACABA DE LLEGAR A LA CAPITAL VESTIDO COMO EN LOS 70S, CON EL PECHO AFUERO Y USANDO ESSENCIA DE PACHOLI COMO PERFUME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOLYWOOD',' FORMA GRACIOSA, DESPECTIVA O UNA MANERA PARA DEFINIR LA FAR??NDULA PANAME??A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOMBO',' PERSONA DE RAZA NEGRA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOMBA',' PERSONA DE RAZA NEGRA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHONTA ',' CABEZA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOTA ',' MINIVAN DE LA POLIC??A. TAMBI??N UTILIZADA PARA REFERIRSE A JODER.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHOTA',' POLICIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TONGO',' POLICIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUAIN ',' (DE PRONUNCIACI??N R??PIDA) ESTA ES UN SIN??NIMO DE YEYE Y ES UNA PERSONA ACOMODADA, ALTA ALCURNIA, DELICADA O ADINERADA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUCHA ',' VULVA; TAMBI??N USADO COMO INTERJECCI??N (EJEMPLO:??CHUCHA!, QUE CHUCHA ME IMPORTA!)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUCHITA ',' V??ASE CONGO. [EJM. TE TAN (EST??N) COGIENDO DE CONGO!!!]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHULETA ',' EXCLAMACION DE SORPRESA O ADMIRACION')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUPAR ',' INGERIR BEBIDAS ALCOHOLICAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUZO ',' VER CHULETA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COCHO ',' GOLPE EN LA CABEZA PROPINADO CON LOS NUDILLOS DE LA MANO. EJEMPLO TE VOY A DAR UN COCHO!')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COCOA',' CUENTO O HISTORIA RELACIONADA A UN SUCESO O EVENTO, NORMALMENTE UN BOCHINCHE O CHISME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CINTA ',' CUENTO O HISTORIA RELACIONADA A UN SUCESO O EVENTO, NORMALMENTE UN BOCHINCHE O CHISME.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COMPA ',' FRASE CARI??OSA REFIRIENDOSE A UN CAMPESINO O A UN COMPADRE... BUEN AMIGO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CONFLEI ',' CUALQUIER CEREAL DE CUALQUIER MARCA QUE SE COME EN EL DESAYUNO, DEL INGL??S CORN FLAKES')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'COSCORR??N ',' INSECTO REDONDO Y CAFE, GOLPE DADO CON LOS NUDILLOS (VEASE COCHO).(NORMALMENTE COCORR??N) ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CUATRERA ',' MUJER LA CUAL ESTA EN BUSCA O ACECHO DE ALGUN HOMBRE CAZADO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CUECO',' HOMOSEXUAL O LESBIANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CUECA',' HOMOSEXUAL O LESBIANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULANTRO ',' UNA BELLA DAMA. PROVENIENTE DEL SEGMENTO DOBLE VIDA DEL PROGRAMA TELEVISIVO PARECEN NOTICIAS. TAMBIEN ES UNA UN PLANTA QUE SE UTILIZA PARA SAZONAR LA SOPA Y OTROS ALIMENTOS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULEAR ',' MANERA VULGAR DE DECIR TENER RELACIONES SEXUALES O SEXO CON UNA PERSONA .')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULILLO',' MIEDO, TERROR O TEMOR A UNA COSA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??????ARA ',' MIEDO, TERROR O TEMOR A UNA COSA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULITO ',' VER PAY')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CULO ',' NALGAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DATIEN ',' TRASPALANTE DE TIENDA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE A VAINA',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE A VAINILLA',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'POR UN PELITO',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'POR UN COCOAZO',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'POR PURA LECHE',' GANAR ALGO POR PURA BUENA SUERTE EN EL ULTIMO MOMENTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE AGENCIA ','N??TIDO, BONITO, NUEVO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DE VEZ ',' DE UNA VEZ, EN EL ACTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DIABLO ROJO ',' AUTOBUS GENERALMENTE PINTADO DE VARIOS COLORES PROCEDENTE DE LAS ESCUELAS ESTADOUNIDENSES QUE COM??NMENTE SE LES LLAMA BORRADORES POR EL EFECTO QUE PRODUCE DURANTE UNA COLISION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'EN TUCO ',' SINONIMO QUIEBRA DE NO TENER DINERO, HACE REFERENCIA A CUANDO UN AUTOMOVIL ESTA MONTADO SOBRE PEDAZOS DE MADERA, GENERALMENTE SIN LLANTAS O EN REPARACION.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'EN VERGA ',' ALGO DE MALA CALIDAD, NO COMPLACIENTE AL GUSTO DE NADIE ESE SHOW ESTA EN VERGA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FALTA DE TODO',' VERSI??N MODERNA DE LA FAMOSA FRASE VENEZOLANA POPULARIZADA EN LOS 80 FALTA DE GLAMOUR. SIGNIFICA FALTA DE RESPETO, FALTA DE ??TICA, FALTA DE ELEGANCIA, FALTA DE CLASE, FALTA DE CONSIDERACI??N, FALTA DE... TODO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FICHA',' PERSONA IMPORTANTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FILO',' ARMA PUNZOCORTANTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FLINTIN',' PROVENIENTE DE EL PATOIS( VER GUARI-GUARI), REFERENTE A UNA PAREJA PELEANDO, DONDE LA MUJER LE TIRA COSAS AL HOMBRE, EN INGLES JAMAIQUINO(PATOIS) FLYING THINGS , USADO PARA DESCRIBIR UN PROBLEMA, CONFLICTO O PELEA. YO NO QUIERO FLINTIN CON ESE MAN.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FULO',' RUBIO/A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FULA',' RUBIO/A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FUNDILLO',' ESPECIFICAMENTE EL ORIFICIO ANAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FUSTE',' NALGAS, TRASERO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GADACA',' TRASPALANTE DE. CAGADA(ALGO QUE SALE MAL DE MOMENTO)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLINERO','LA ENTREDA GENERAL O AREA POPULAR DE ALGUN EVENTO CULTURAL (CONCIERTO) O EVENTO DEPORTIVO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLO',' BARATO, DE POCA CALIDAD; PERSONA SIN GRACIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GALLA',' BARATO, DE POCA CALIDAD; PERSONA SIN GRACIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GANDOCA',' TRASPALANTE DE CAGANDO(DEFECAR)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GARNAT??N',' BOFET??N. *GARNATADA NORMALMENTE SE DICE GARNAT??.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GARNATADA ',' BOFET??N. *GARNATADA NORMALMENTE SE DICE GARNAT??.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GLOBITO',' CONDON, PRESERVATIVO; *FORRITO HA SIDO POPULARIZADO POR EL HOM??NIMO PERSONAJE COND??N DEL POPULAR PROGRAMA LA C??SCARA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FORRITO ',' CONDON, PRESERVATIVO; *FORRITO HA SIDO POPULARIZADO POR EL HOM??NIMO PERSONAJE COND??N DEL POPULAR PROGRAMA LA C??SCARA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GOLPE DE ALA ',' AROMA INTOLERABLE QUE PROCEDE DE LAS EXILAS... VULG. VER GRAJO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GRAJO ',' SUDOR DE LAS EXILAS SUMAMENTE APESTOSO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GRUBEO',' ESTAR CON UNA PERSONA POR UN TIEMPO O POR UNA NOCHE PARA PASARLA BIEN Y PARA NADA SERIO O FORMAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GRUBEAR',' ESTAR CON UNA PERSONA POR UN TIEMPO O POR UNA NOCHE PARA PASARLA BIEN Y PARA NADA SERIO O FORMAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUABAZO',' GRAN GOLPE, USUALMENTE SEGUIDO DE HEMATOMA DE ALGUNA CLASE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUABANAZO',' GRAN GOLPE, USUALMENTE SEGUIDO DE HEMATOMA DE ALGUNA CLASE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUACHO','ES UNA SOPA ESPESA QUE LLEVA ??AME, YUCA, CULANTRO, ARROZ, VERDURAS Y ALGUNA CARNE, QUE PUEDE SER RES, RABITO DE PUERCO O CHICHARR??N. EL GUACHO SE SIRVE TRADICIONALMENTE EN UNA TOTUMA, PLATO QUE SE FABRICA PARTIENDO A LA MITAD UNOS FRUTOS REDONDOS Y DUROS QUE CRECEN EN EL MONTE. TAMBIEN SIGINFICA LA COMBINACION DE VARIAS COSAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUAGUA ',' SE DICE DE UN AUTOM??VIL MUY VIEJO O EN MAL ESTADO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUAPIN',' SALUDO QUE INDICA QUE PASA. DEL INGL??S WHAT HAPPENED? / WHAT IS HAPPENING?.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JUATAPIN ',' SALUDO QUE INDICA QUE PASA. DEL INGL??S WHAT HAPPENED? / WHAT IS HAPPENING?.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUAPOTE ',' INDIVIDUO USUALMENTE CON POCA AUTOESTIMA QUE HACE MUCHA FISICULTURA PERO QUE AL FINAL SIEMPRE SIGUE SIENDO BIEN FEO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUARI-GUARI',' DIALECTO DE LA PROVINCIA DE BOCAS DEL TORO, ES UNA MEZCLA DE ESPA??OL, FRANC??S, INGL??S Y LENGUAS IND??GENAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUARO ',' ALCOHOL; BEBIBA ALCOH??LICA; LICOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'GUILLADO ',' 1.INFLUENCIADO POR ALUCIN??GENOS 2.EMOCIONADO, INSPIRADO. (NORMALMENTE SE DICE GUILLAO) ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'HUEVEAR ',' PERDER EL TIEMPO DE LA PEOR FORMA. [EJM. P??NTE A TRABAJ?? Y DEJA DE TA WEBIANDO!!!]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'IR AL CHOQUE',' IR DE FRENTE ANTE CUALQUIER ADVERSIDAD.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JODER',' BROMEAR, MOLESTAR, IRRITAR. EJM: NO JODAS!')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JUEGA VIVO ',' CON ASTUCIA, GENERALMENTE SIN MORAL, OPORTUNISTA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'JUGO-E-POLICIA ',' AGUA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'KENKE ',' BATE DE MARIHUANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LA KENTON ',' LLAVE EN LUCHA LIBRE QUE SE USA PARA AMARRAR AL ADVERSARIO, USANDO LAS PIERNAS, MIENTRAS LO REPLETAN DE RONCABALAOS... USALMENTE ESTA LLAVE SE USA POR MUJERES QUE QUIEREN TENER HIJOS OBLIGANDO AL NOVIO A EJACULAR DENTRO DEL VIENTRE... POR ESO SE DICE CUIDAO Y TE HACE LA KENTON.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LABIA ',' ADULACI??N, NORMALMENTE PARA CONVENCER A LA PERSONA DE CUAL ES LA MEJOR ALTERNATIVA EN UNA SITUACI??N DADA O PARA CONSEGUIR APOYO DE LA MISMA; MUY COMUN EN EL AMBITO DE LA POLITICA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'L??ITER',' ENCENDEDOR, ANGLICISMO [DE LIGHTER].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LAOP?? ',' TRASPALANTE DE PELAO (MUCHACHO)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LEVANTE','NOVIO/A, QUI??NES SE GUSTAN Y TIENEN QU??MICA ENTRE ELLOS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LIMADO',' DICESE DE LA PERSONA QUE SE ENCUENTRA MUY CANSADA LUEGO DE TRABAJAR O BEBER MUCHO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LIMPIO (A) ',' SIN DINERO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LLECA ',' TRASPALANTE DERIVADO DE CALLE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'LOCO ',' ES COMO SE LLAMAN LOS AMIGOS DE CARI??O. MUY COMUN ENTRE ORIUNDOS DE PANAM??.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHIUA',' MAS CHOLO QUE UN CHOLO POP... USUALMENTE UN INDIGENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHIGUA',' MAS CHOLO QUE UN CHOLO POP... USUALMENTE UN INDIGENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHIHUA ',' MAS CHOLO QUE UN CHOLO POP... USUALMENTE UN INDIGENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MACHOEMONTE ',' TIPO MAS TOF QUE RAMBO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MAF?? ',' ABREBOCAS DE HARINA (FRITURA) EN FORMA DE TRENZA; D??CESE DE UN ENREDO, ASUNTO COMPLICADO, O PERSONAS ABRAZADAS DE FORMA MUY AFECTIVA (COMO MAF??).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MALEANTE ',' DELINCUENTE O PERSONA QUE QUIERE SER COMO LOS DELINCUENTES.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MANACHO ',' HOMBRE JOVEN DE CLASE OBRERA, CUERPO ATL??TICO Y ASPECTO UN POCO RUDO Y MUY MASCULINO. MANACHA: LESBIANA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MANZANILLO ',' SIN PERSONALIDAD, INFLUENCIABLE CON FACILIDAD, TAMBI??N SE DICE AS?? A LOS VIVIDORES.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MATAPUERCO O SOPLAMOCO ',' GOLPE EXAGERADO Y CERTERO, QUE DUELE MUCHO. N??TESE QUE SOPLAMOCO ES EHN LA MEJILLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ME VALE VERGA',' SITUACI??N QUE NO GENERA NINGUNA CLASE DE REACCI??N NI DE INTER??S EN LA PERSONA.(VULGAR)/UN PEPINO/UN COMINO ')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ME??A ',' J??VENES DE LA CALLE DE MAL HABLAR Y VESTIR. DENOTA LAS ??LTIMAS 4 LETRAS DE LA NACIONALIDAD PANAME??A. TAMBI??N TRASPALANTE DEL TUB??RCULO ??AME)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'METO ',' UNA EXPRESI??N QUE DENOTA UNA FRASE DE ADMIRACI??N Y AFIRMACI??N MUY UTILIZADA EN LA PROVINCIA DE CHIRIQU??. EN LA CIUDAD DE PANAM?? (SOBRETODO) OFI.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MILLO ',' PALOMITAS DE MA??Z. MILLO VIENE DE LA LENGUA GALLEGA Y QUIERE DECIR MA??Z. EN GALICIA SE LE LLAMA A LAS PALOMITAS DE MA??Z, FLOCOS DE MILLO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MOCOCOA ',' LIQUIDO PRODUCIDO POR LOS MIEMBROS NASALES, REGULARMENTE DE COLOR VERDE, ESTA SE BEBE EN GRANDES CANTIDADES USUALMENTE LUEGO DE QUE A UNO LO HAN TRAICIONADO (VER QUEMADO) EN UNA RELACION SE CREIA SERIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MONTADO',' QUE TIENE BUENA SITUACI??N ECON??MICA.  (NORMALMENTE SE DICE MONTAO/A)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??AMER??A ',' LOCURA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??AMPEARSE ',' VOLVERSE LOCO/A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'????NGARA ',' FORMA DESPECTIVA DE DEFINIR A LOS COMUNISTAS O MIEMBROS DE PARTIDO DE IZQUIERDA O EXTREMA IZQUIERDA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??ANGOTADO',' PERSONA QUE CAMINA EN CUCLILLAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'A??INGOTADO',' PERSONA QUE CAMINA EN CUCLILLAS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??APA',' UN REGALO QUE DAN CUANDO SE COMPRA ALGO EN UN TIENDA O ABARROTERRIA (INTRODUCIDO POR LOS CHINOS PARA CAPTAR CLIENTES FRECUENTES).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??ECKS ',' VERSI??N DECENTE DE MIERDA. [EJM. TE WA (VOY A) SAC?? LA ??ECKS!!!]')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'NEVERA ',' REFRIGERADORA; AUTOB??S CON AIRE ACONDICIONADO (D??CESE DE LOS TRANS-PROVINCIALES [EJM: PANAM??-DAVID] PORQUE NORMALMENTE VAN A TEMPERATURAS MUY FR??AS); MUJER CUADRADA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'NO ME PARECE',' FRASE POPULARMENTE UTILIZADA PARA DEMOSTRAR DESCONTENTO POR ALGO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??ORRO ',' HOMOSEXUAL/ ESE MAN ES ??ORRO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'OFI ',' ENTENDIDO, OK (ACORTACI??N DE OFICIAL, UTILIZADO PARA APROBAR O RECIBIR APROBACI??N).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PALANTE ',' REDUCCI??N DERIVADA DE PARA ADELANTE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PACIERO(S)',' AMIGO, GENERALMENTE AMIGOS CON QUIENES SE COMPARTE PARRANDAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAJA',' MASTURBARSE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VOLAR COMETA ',' MASTURBARSE')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAJIZO ',' PERSONA QUE SE MASTURBA CONSTANTEMENTE; PERSONA QUE MUESTRA DEBILIDAD ANTE UNA ACTIVIDAD F??SICA. [EJM. JO! NO PUEDES NI LEVANTAR ESO... TAS PAJIZO!!!].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAJIZA ',' PERSONA QUE SE MASTURBA CONSTANTEMENTE; PERSONA QUE MUESTRA DEBILIDAD ANTE UNA ACTIVIDAD F??SICA. [EJM. JO! NO PUEDES NI LEVANTAR ESO... TAS PAJIZO!!!].')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAKA ',' CARGAMENTO DE DROGA; PERSONA QUE TIENE FARDOS/MOCHILAS/ BULTOS [DEL INGL??S PACKS]; REFERENTE A CARTUCHOS DE BALAS; DELINCUENTE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARACA??DAS',' PERSONA QUE ACUDE A UNA REUNI??N O FIESTA SIN INVITACI??N.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARAPAPEO',' PALABRA QUE DESCRIBE EL BAILE DE LAS REINAS DE CARNAVAL. VERBO: PARAPAPEAR; EJM: EST?? PARAPAPEANDO. EL T??RMINO SE DERIVA DEL SONIDO DE LAS TROMPETAS DE UNA MURGA: PARA PA P??')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARKIN',' FIESTA O REUNI??N ENTRE AMIGOS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PARQUEARR',' SALIR CON ALGUIEN A PASAR EL RATO: PARQUEAR CON MIS AMIGOS; PONER A ALGUIEN EN SU SITIO QUISO INSULTARME Y LO PARQUE??. NORMALMENTE LA GENTE DICE PARQUIAR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATAC??N ',' POPULAR ACOMPA??AMIENTO DE COMIDA, EL CUAL CONSISTE EN RODAJAS DE PL??TANO APLASTADAS Y LUEGO FRITAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATACONCITO ',' PEQUE??A ACUMULACI??N DE BASURA, VIENE DEL RELLENO SANITARIO DE LA CIUDAD DE PANAM?? (CERRO PATAC??N).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATAT??S ',' DESMAYO, ATAQUE CARD??ACO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATI-AMARILLO ',' CIGARRILLO CON EL FILTRO DE COLOR AMARILLO O ANARANJADO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PATO ',' VER SACALODO, TUTIFRUTI, PUNKY-PUNCH ...I.E. HOMOSEXUAL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'??ORRO',' VER SACALODO, TUTIFRUTI, PUNKY-PUNCH ...I.E. HOMOSEXUAL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,' ??A??O ',' VER SACALODO, TUTIFRUTI, PUNKY-PUNCH ...I.E. HOMOSEXUAL')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PEBRE',' COMIDA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REFINE ',' COMIDA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PELO PELO ',' BAILE ER??TICO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PELONERA ',' GOLPIZA PROPICIADA ENTRE VARIOS SIN SER FUERTE, COM??NMENTE EN LA CEBEZA Y EN LA SECUNDARIA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PERRO',' DESPECTIVO UTILIZADO COMO SIN??NIMO DE MUJERIEGO; USADO COMO INSULTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PERRON ',' PERSONA DE POCA CAPACIDAD. DICESE DE UNA PERSONA QUE NO ES MUY POPULAR DENTRO DE UN CIRCULO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PERR??N',' PERSONA QUE NO DESEMPE??A BIEN UNA FUNCION REFERENCIADA O EXAGERACION DE PERRO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PESCUEZONA ',' CERVEZA DE BOTELLA TAMA??O GRANDE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PESO',' MONEDA DE 50 CENTAVOS, VIENE DEL PERIODO DE LA SEPARACI??N DE PANAMA DE COLOMBIA DONDE EQUIVAL??A EL PESO COLOMBIANO A 50 CENTAVOS DE D??LAR; USADO COM??NMENTE EN LAS PELEAS DE GALLOS PARA CUANTIFICAR LAS APUESTAS.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PICANDO ',' ALGO QUE EST?? DE MODA.(SU USO SE DEBE AL FAMOSO BAILE DEL PIQUE, EN PANAM??.)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PICHI',' DROGA, D??CESE COM??NMENTE A LA COCAINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIEDRA ',' CRACK (DROGA).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIEDRERO',' PERSONA DROGADICTA QUE HA LLEGADO A LA INDIGENCIA POR SER DROGADICTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIEDRERA',' PERSONA DROGADICTA QUE HA LLEGADO A LA INDIGENCIA POR SER DROGADICTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PILAR ',' ESTUDIAR CON AF??N; PIL??N(A) ES ALGUIEN MUY ESTUDISO O SABELOTODO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PILINQUI ',' PERSONA MEZQUINA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PILLAR ',' SYNONIMO DE TOMAR/COGER/AGARRAR, EJM: PILLA LA PLUMA...; ENCONTRAR A HURTADILLAS UNA SITUACION O VER ALGO EN ESPECIAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PINTA',' CERVEZA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'FR??A ',' CERVEZA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PIP?? ',' PENE, MIEMBRO VIRIL; ORINE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PLENA ',' USADO PARA CANCIONES/RITMOS DE REGGAE PERO TAMBI??N USADA PARA OTROS G??NEROS CUANDO LA CANCION ES BUENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PONCHAR ',' DESINFLAR; TENER SEXO; SACAR A UN BATEADOR POR OUT EN B??ISBOL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PONCHERA ',' DESORDEN, ALGARAB??A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PORC??N',' ENTI??NDASE POPCON O PALOMITAS DE MAIS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MILLO ',' ENTI??NDASE POPCON O PALOMITAS DE MAIS')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PRAKA PRAKA ',' DERIVACION DE RAKATACA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PUESTO QUEMADO ',' PUESTO RESERVADO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QU?? BATE ',' USADO COMO DESCRIPCI??N DE ALGO FICTICIO, ASOMBROSO O ESPECTACULAR')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUE ES LO QUE ES',' QUE HAY DE NUEVO. (PRONUNCIADO QUE LO QUE ?? O QUELOQU??)')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QU?? XOP?? ',' TRASPALANTE, DERIVADO DE ??QU?? PASO?')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUEMADO',' PERSONA A LA CUAL SU NOVIO/NOVIA ESPOSO/ESPOSA LO HA TRAICIONADO CON OTRA/O.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'QUESO',' CIERTA ATRACCI??N MERAMENTE F??SICA Y SEXUAL.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RAKATACA ',' HOMBE O MUJER SIN CLASE, COMUNMENTE UTILIZA MAYORMENTE LA JERGA PANAME??A AUTOCTONA. DERIVADO DEL SONIDO DE LAS METRALLETAS AL DISPARAR RAKATAKATAKATAKATAKA POPULARIZADO DURANTE UNA CANCI??N DEL GRUPO JAM & SUPPOSE EN 1992: CAMI??N LLENO DE GUN.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RAMBULERO',' PERSONA USUALMENTE DE LOS BARRIOS POPULARES QUE GUSTA DE LAS PELEAS, INTRIGAS, CHISMES, BAILE Y OTRAS MANIFESTACIONES DE COMUNICACI??N SIN CLASE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RANG??LIDO ',' DE MAL ASPECTO, FLACO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RANTAN ',' MUCHO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REAL ',' MONEDA DE 5 CENT??SIMOS DE BALBOA. LA PALABRA VIENE DE LA ??POCA DE LA COLONIA EN LA CUAL SE LE DENOMINABA REAL A LAS MONEDAS ACU??ADAS EN POTOS??, LIMA Y EN ALGUNOS OTROS LUGARES. EN TABOGA, PANAM??, POR EJEMPLO UNA FAMILIA LLEG?? A ENCONTRAR UNA CANTIDAD DE MONEDAS DE DENOMINACI??N DE PESOS DE 8 REALES, MIENTRAS CONSTRU??AN SU CASA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PAU PAU ',' CASTIGO A LOS HIJOS, YA SEA DARLES CON LA CORREA (REJERA) O CON NALGADAS (PAU PAU).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REJERA',' CASTIGO A LOS HIJOS, YA SEA DARLES CON LA CORREA (REJERA) O CON NALGADAS (PAU PAU).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REJEROS ',' GRUPOS DE HOMBRES (AMIGOS ENTRE S??) QUE VAN A UNA DISCOTECA, CLUBES NOCTURNOS O FIESTA A LIGARSE CON MUJERES O QUE SIMPLEMENTE SE RE??NEN PARA PASARLA BIEN. TAMBI??N SE RE??NEN EN UN CASA PARA LIBAR LICOR Y ECHAR HISTORIAS U APSPECTOS PERSONALES QUE LE HAN PASADO. EL PROGRAMA DE HUMOR DE LA CASCARA HIZO UNA PARODIA DE ESTO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REJO ',' AZOTE, PENE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'REVENTAR',' VACILAR, TOMAR EL TIEMPO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'DETONAR',' VACILAR, TOMAR EL TIEMPO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ROMPER ',' VACILAR, TOMAR EL TIEMPO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ROMPE PECHO',' UNA BOTELLA DE CERVEZA MUY GRANDE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MANGA LARGA',' UNA BOTELLA DE CERVEZA MUY GRANDE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RONCABALAO','GOLPE EXAGERADO CAPAZ DE MATAR A UNA PERSONA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SABROS??N ',' ALGO O ALGUIEN QUE SE ENCUENTRE EN EXCELENTES CONDICIONES O ALG??N EVENTO AGRADABLE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SACALODO',' VER CUECON')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TUTIFRUTI',' VER CUECON')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'PUNKYPUNCH ',' VER CUECON')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SALAO',' PERSONA QUE TIENE MALA SUERTE. EJM. MARIO TU EST??S SALADO EN LA LOTER??A.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'SARAO',' FIESTA O BAILE ORGANIZADA GENERALMENTE POR EL SEGUNDO CICLO DE SECUNDARIA. T??PICAMENTE SE REALIZA EN HORAS DE LA TARDE, EN EL GIMNASIO DE LA ESCUELA. D??CESE DE CUALQUIER FIESTA EN QUE EL OBJETIVO PRINCIPAL ES BAILAR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'S??LIDO ','SIGNIFICA EXCELENTE. TAMBI??N CH??VERE.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TALLAO','BIEN VESTIDO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TARRANTAN','M??S QUE RANTAN. MUCH??SIMO.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TATAI','BYE, HASTA LUEGO, NOS VEMOS.* T?? BIEN  (VIENE DE: EST?? BIEN; SE LE DA SIGNIFICADO SEG??N LA DICCI??N, PRONUNCIACI??N Y EL TONO DE LA VOZ USADA POR LA PERSONA) ALGO SORPRENDENTE; FALSO; EXAGERADO; EMOCIONANTE; TODOS LOS SIGNIFICADOS ANTERIORES A LA VEZ.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TELLA','BOTELLA (GENERALMENTE DE LICOR).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TOTUMA: ','ES UN PLATO QUE SE FABRICA PARTIENDO A LA MITAD UNOS FRUTOS REDONDOS Y DUROS QUE CRECEN EN EL MONTE (CALABAZO).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TONGO ',' POLICIA DE BAJO RANGO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TONT??N',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MICHA',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'MOTA',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TROZO',' VAGINA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TORTILLERA ',' LESBIANA')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TREPAQUESUBE/VERGUERO/CHUCHAMADRE/ZAPEROCO ',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VERGUERO',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUCHAMADRE',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ZAPEROCO ',' GRAN PROBLEMA, DISTURBIO, DESORDEN, CONFLICTO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'TRUENO',' ARMA DE FUEGO')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VACA ',' COLECTA DE DINERO ENTRE VARIAS PERSONAS PARA COMPRAR ALGO. HEY HAGAN UNA VACA PALA CARMEN AH??...')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VAINA ',' UTILIZADO COMO COMOD??N EN CONVERSACIONES, USADO POR COSA (TAMBI??N USADO EN OTROS PA??SES CON EL MISMO SIGNIFICADO).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VALE CEBO ',' D??CESE DE UNA SITUACI??N INJUSTA O EST??PIDA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VAMPIRA',' MUJERES DE ALTO MANTENIMIENTO, SUMAMENTE IGNORANTES EN TODO MENOS EN EL ARTE DE HACER EL AMOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'CHUPASANGRE ',' MUJERES DE ALTO MANTENIMIENTO, SUMAMENTE IGNORANTES EN TODO MENOS EN EL ARTE DE HACER EL AMOR.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VERG??ERO ',' PROBLEMA, DEBATE DISCUSION ACALORADA LLEGANDO AL PUNTO CERCANO A FORMARSE UNA TRIFULCA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VIDAJENEAR ',' HUSMEAR, ESPIAR, Y ENTROMETERSE EN LA VIDA AJENA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'VIOLINISTA',' PERSONA QUE ACOPA??A A UNA PAREJA PERO NO DEBE ESTAR PRESENTE PUES LA PAREJA QUIERE ARROPAR. (VE??SE ARROPAR).')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'YAPLA ',' PLAYA. SALE DEL REVERSO DE PLAYA, YASPLA, Y QUIT??NDOLE PLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'YEYE',' PERSONA ADINERADA QUE PRESUME DE SU CONDICI??N, COM??NMENTE USA ANGLICISMOS EN SU HABLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'RABIBLANCO',' PERSONA ADINERADA QUE PRESUME DE SU CONDICI??N, COM??NMENTE USA ANGLICISMOS EN SU HABLA.')");
    conn.execute ("insert into SLAM (id, expresion, significado) values (null,'ZAMBITO(A) ',' EXPRESI??N DE LAS PROVINCIAS DE HERRERA Y LOS SANTOS, SIGNIFICA NI??O O NI??A.')");


    conn.commit()
    print("")
    print("                                 -->Base de datos Creada y se insertaron los registros de inicio")
    print("")
    p=input("Presione una <Enter> para continuar")
    conn.close()
