# Comprobar el precio de un producto en Amazon

'''
    Encontrar los enlaces del panel de iphone
    La App se ejecuta cada 10 segundos. Usar Time

    Encontrar los enlaces. 
    Lista de enlaces cada 10seg.

    Entrar en esas URL's
    Mostrar por pantalla el título y precio. 


curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip install virtualenv
virutalenv venv

source venv/bin/Activate


Librerias para temas de Autenticción Web: 
- BeautifulSoup
- Selenium
- Machanize

Chrome -> Alt-Cmd-i (Sección Elementos)
Abro amazon.es
Busco por ejemplo iphone12, entro en uno de ellos
Select Element Shift+Cmd+C

Título: <span id="productTitle" class="a-size-large product-title-word-break">Nuevo Apple iPhone 12 (128&nbsp;GB) - Azul</span>
Precio: <span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">930,00&nbsp;€</span>


'''

# Web Scrapping. 
import time         # Gestión de campos fecha y tiempo.
import re           # Regular expressions
import requests     # Peticiones HTML (pip install requests)
from bs4 import BeautifulSoup   # Librería navegar y parser de páginas web.  (pip install bs4)
                                # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
                                # pip install html5lib
                                # pip install lxml
import smtplib      # 

# Let's Go !!!
urlInicial = "https://www.amazon.es/Nuevo-Apple-iPhone-12-128-GB/dp/B08L5S3XNM"
urlPre = "https://www.amazon.es"
# Para saber mi user-agent, buscar en Google "mi user-agent"
header = { 'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36" }


# Dado un contenido leído de la Web, averiguar el nombre del producto y su precio 
# 
def comprobar_precio(soup):

    # Título: <span id="productTitle" class="a-size-large product-title-word-break">Nuevo Apple iPhone 12 (128&nbsp;GB) - Azul</span>
    # Precio: <span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">930,00&nbsp;€</span>

    titulo = soup.find(id='productTitle').get_text().strip()
    precio = soup.find(id='priceblock_ourprice').get_text().strip()
    print("  Título: ", titulo)
    print("  Precio: ", precio[:-5])

# Dado un contenido leído de la Web, averiguar los enlaces a todos los teléfonos
#
def enlacesTelefonosEnPanel(soup):
    # Panel con todos los teléfonos: id = kfs-item-container
    panel = soup.find(id='kfs-item-container0')

    lista=[]
    listavalidos=[]
    enlaces = panel.find_all('a')
    for link in enlaces:
        linkhref = link.get('href')
        if linkhref.startswith('/dp'):
            lista.append(linkhref)
        #print(linkhref)
    #print(lista)
    return(lista)


## -- Main
## ----------------
# Pido la primera página ... 
pagina = requests.get(urlInicial, headers=header)
soup = BeautifulSoup(pagina.content, 'html.parser')
# Investigo los productos
for count in range(2):
    # Prints the current time 
    print("\n"+time.ctime()+"\n========================")

    urlsTelefonos = enlacesTelefonosEnPanel(soup)
    for url in urlsTelefonos:
        url = urlPre + url
        print(url,":")
        ## -- Main
        producto = requests.get(url, headers=header)
        prodsoup = BeautifulSoup(producto.content, 'html.parser')
        comprobar_precio(prodsoup)

    # Wait 10secs
    time.sleep(5)
