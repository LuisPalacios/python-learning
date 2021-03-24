# Comprobar el precio de un producto en Amazon

'''

Ejercicio: 

    Mostar el precio de todos los productos referenciados en una página de amazon.es
    Actualizar dichos datos cada 10 seg.
    
    Tomamos como ejemplo un producto de ejemplo
    https://www.amazon.es/Nuevo-Apple-iPhone-12-128-GB/dp/B08L5S3XNM

    Buscar los enlaces del panel de iphone
    Encontrar los enlaces. 
    Lista de enlaces cada 10seg.
    Entrar en esas URL's
    Mostrar por pantalla el título y precio. 

    Nota: Librerias para hacer Web scraping:
    - BeautifulSoup
    - Selenium
    - Machanize

    Nota2: Cómo investigar una página Web
    Chrome -> Alt-Cmd-i (Sección Elementos)
    Abro amazon.es
    Busco por ejemplo iphone12, entro en uno de ellos
    Select Element Shift+Cmd+C
    Buscar el id que me interesa, por ejemplo:
    
    Título: <span id="productTitle" ....
    Precio: <span id="priceblock_ourprice" 

'''

# Web Scrapping. 
import time         # Gestión de campos fecha y tiempo.
import re           # Regular expressions
import requests     # Peticiones HTML (pip install requests)
from bs4 import BeautifulSoup   # Librería navegar y parser de páginas web.  (pip install bs4)
                                # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
                                # pip install html5lib
                                # pip install lxml
import smtplib      # Para luego mandar un mail con la información.

# Let's Go !!!
urlInicial = "https://www.amazon.es/Nuevo-Apple-iPhone-12-128-GB/dp/B08L5S3XNM"
urlPre = "https://www.amazon.es"

# Para saber mi user-agent, buscar en Google "mi user-agent"
header = { 'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36" }

# Función para dividir una Cadena. 
# 
#   Entrada : Cadena (s) en la ocurrencia (n) del delimitador (delim)
#   Salida  : Dupla
#
# Ejemplo, para limpiar URL's de Amazon
#     s = "/dp/B08L6XHW5C/ref=es_a_phone11_3/257-2200312-1771441"
#     out = split_at(s, '/', 3)
#
#     out = ('/dp/B08L6XHW5C', 'ref=es_a_phone11_3/257-2200312-1771441')
#
def split_at(cadena, delim, n):
    r = cadena.split(delim, n)[n]
    return cadena[:-len(r)-len(delim)], r

# Dado un contenido busco y muestro el nombre del producto y su precio 
# 
def comprobar_precio(soup):

    # Ver nota2
    titulo = soup.find(id='productTitle').get_text().strip()
    precio = soup.find(id='priceblock_ourprice').get_text().strip()
    print("  Título: ", titulo)
    print("  Precio: ", precio[:-5])

# Dado un contenido leído de la Web, averiguar los enlaces a todos los teléfonos
#
def enlacesTelefonosEnPanel(soup):
    # Panel con todos los teléfonos: id = kfs-item-container
    panel = soup.find(id='kfs-item-container0')

    # Busco los enlaces en el PANEL. 
    lista=[]
    listavalidos=[]
    enlaces = panel.find_all('a')
    for link in enlaces:
        linkhref = link.get('href')
        if linkhref.startswith('/dp'):
            # En linkhref tengo entradas del tipo "/dp/B08L5QJDLC/257-3222011-4811726"
            # Uso la función split_at para quedarme con /dp/B08L5QJDLC
            linkhref = split_at(linkhref, '/', 3)[0]
            lista.append(linkhref)
    return(lista)


## -- Main
## ----------------

# Pido la primera página ... 
pagina = requests.get(urlInicial, headers=header)
soup = BeautifulSoup(pagina.content, 'html.parser')

# Entro en los productos listados en el panel de dicha página
# NOTA: Solo hago 5 iteracciones, 
#       para hacerlo permanente sustituir este for por 
#       While True:
# 
for count in range(2):

    # Muestro la hora actual
    print("\n"+time.ctime()+"\n========================")

    # Averiguo los enlaces a todos los teléfonos
    urlsTelefonos = enlacesTelefonosEnPanel(soup)
    for url in urlsTelefonos:
        # Construyo la URL con "https://www.amazon.es + /dp/XXXX..."
        url = urlPre + url
        print(url,":")
        
        ## Entro en la nueva URL y busco el Título y el Precio
        producto = requests.get(url, headers=header)
        prodsoup = BeautifulSoup(producto.content, 'html.parser')
        # busco y muestro el nombre del producto y su precio 
        comprobar_precio(prodsoup)

    # Espero 10secs
    time.sleep(5)
