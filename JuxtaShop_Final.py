# IMPORTS

import requests
from bs4 import BeautifulSoup
from tkinter import *
from PIL import ImageTk
import webbrowser


######################################################## BACK-END/FUNCTIONAL CODES ###################################################################


# FLIPKART WEB SCRAPING
def flipkart():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    url = 'https://www.flipkart.com/search?q=' + e1_value.get() + '&otracker=start&as-show=on&as=off'
    page = requests.get(url)
    page1 = page.text
    soup = BeautifulSoup(page1, 'html.parser')

    name_list = []
    result = soup.findAll('div', {'class': '_3liAhj'})
    for i in range(0, len(result)):
        name_list.append(result[i].div.img['alt'])

    price_list = []
    result_1 = soup.findAll('div', {'class': '_1vC4OE'})
    for i in range(0, len(result_1)):
        price_list.append(result_1[i].text)

    name_list_1 = []
    result = soup.findAll('div', {'class': '_3wU53n'})
    for i in range(0, len(result)):
        name_list_1.append(result[i].text)

    price_list_1 = []
    result_1 = soup.findAll('div', {'class': '_1vC4OE _2rQ-NK'})
    for i in range(0, len(result_1)):
        price_list_1.append(result_1[i].text)

    if not name_list:
        for i in name_list_1:
            i = i[:38]
            t1.insert(END, i + "\n")
        for j in price_list_1:
            t2.insert(END, "Rs." + j[1:30] + "\n")
    else:
        for i in name_list:
            i = i[:38]
            t1.insert(END, i + "\n")
        for j in price_list:
            t2.insert(END, "Rs. " + j[1:20] + "\n")


# SNAPDEAL WEB SCRAPING
def snapdeal():
    t4.delete('1.0', END)
    t5.delete('1.0', END)
    url = 'https://www.snapdeal.com/search?keyword=' + e1_value.get() + '&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    result = soup.findAll('div', {'class', 'product-desc-rating '})

    name_list = []
    for i in range(0, len(result)):
        name_list.append((result[i].a.p['title']))

    price_list = []
    for i in range(0, len(result)):
        result_1 = result[i].find('span', {'class', 'lfloat product-price'})
        price_list.append(result_1.text.strip())

    for i in range(0, 20):
        t4.insert(END, name_list[i][:38] + "\n")
        t5.insert(END, price_list[i] + "\n")


# AMAZON WEB SCRAPING
def amazon():
    t6.delete('1.0', END)
    t7.delete('1.0', END)
    amazon_page = 'http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + e1_value.get() + '&rh=i%3Aaps%2Ck%3Avr'
    page = requests.get(amazon_page).text
    soup = BeautifulSoup(page, 'html.parser')

    result_2 = []
    result_4 = []

    result_1 = soup.findAll('div', {'class': 'a-row a-spacing-none'})
    for i in range(0, len(result_1)):
        try:
            result_2.append(result_1[i].a['title'])
        except:
            print('')

    result_3 = soup.findAll('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
    for i in range(0, len(result_3)):
        try:
            result_4.append(result_3[i].text)
        except:
            print('')
    for i in result_2:
        i = i[:38]
        t6.insert(END, i + "\n")
    for j in result_4:
        t7.insert(END, "Rs." + j + "\n")


# EBAY WEBSCRAPING
def ebay():
    t6.delete('1.0', END)
    t7.delete('1.0', END)
    ebay_page = 'https://www.ebay.in/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.Xiphone.TRS0&_nkw=' + e1_value.get() + '&_sacat=0'
    page = requests.get(ebay_page).text
    soup = BeautifulSoup(page, 'html.parser')

    result_1 = soup.findAll('h3', {'class': 'lvtitle'})
    for i in result_1:
        t6.insert(END, i.a['title'][26:60] + "\n")

    result_2 = soup.findAll('li', {'class': 'lvprice prc'})
    for j in result_2:
        t7.insert(END, j.text.strip() + "\n")


# COMBINED FUNCTION TO CALL
def combine():
    flipkart()
    ebay()
    snapdeal()


# FUNCTIONS TO OPEN WEBSITES
def open_flipkart():
    webbrowser.open('https://www.flipkart.com/search?q=' + e1_value.get() + '&otracker=start&as-show=on&as=off')


def open_snapdeal():
    webbrowser.open(
        'https://www.snapdeal.com/search?keyword=' + e1_value.get() + '&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy')


def open_ebay():
    webbrowser.open(
        'https://www.ebay.in/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.Xiphone.TRS0&_nkw=' + e1_value.get() + '&_sacat=0')


######################################################## USER INTERFACE/FRONT-END CODES ###################################################################

window = Tk()

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=2)
b1 = Button(window, text="Search", command=combine)
b1.grid(row=0, column=3)

# FLIPKART
t1 = Text(window, height=20, width=40, bg='black', fg='white')
t1.grid(row=2, column=0)
t2 = Text(window, height=20, width=20, bg='black', fg='white')
t2.grid(row=2, column=1)
image = ImageTk.PhotoImage(file="img/flip.jpg")
b2 = Button(window, command=open_flipkart)
b2.config(image=image)
b2.image = image
b2.grid(row=1, column=0)

# SNAPDEAL
t4 = Text(window, height=20, width=40, bg='black', fg='white')
t4.grid(row=2, column=2)
t5 = Text(window, height=20, width=20, bg='black', fg='white')
t5.grid(row=2, column=3)
image = ImageTk.PhotoImage(file="img/snap.jpg")
b3 = Button(window, command=open_snapdeal)
b3.config(image=image)
b3.image = image
b3.grid(row=1, column=2)

# EBAY
t6 = Text(window, height=20, width=40, bg='black', fg='white')
t6.grid(row=2, column=4)
t7 = Text(window, height=20, width=20, bg='black', fg='white')
t7.grid(row=2, column=5)
image = ImageTk.PhotoImage(file="img/ebay.jpg")
b5 = Button(window, command=open_ebay)
b5.config(image=image)
b5.image = image
b5.grid(row=1, column=4)

window.title('JuxtaShop')
window.configure(background='black')

window.mainloop()