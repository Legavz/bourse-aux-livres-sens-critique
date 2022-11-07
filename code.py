import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Script a lancer depuis GitBash quand on recherche des livres manuellement

liste_livres = []

while True:
    print("Que voulez-vous faire ?")
    print("0 - Quitter")
    print("1 - Lancer la recherche")
    print("2 - Rajouter un livre dans ma liste")
    "-" * 30
    choice = int(input("Ton choix: "))
    if choice == 1:
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("https://shop.labourseauxlivres.fr/")
        for i in liste_livres:
            search_bar = driver.find_element(By.CLASS_NAME, "search-bar__input")
            search_bar.send_keys(i)
            find_button = driver.find_element(By.CLASS_NAME, "search-bar__submit")
            find_button.click()
            try:
                product_link = driver.find_element(By.CLASS_NAME, "product-item__info-inner")
                product_link.click()
            except:
                pass
            try:
                product_link_2 = driver.find_element(By.CSS_SELECTOR, ".product-form__add-button.button.button--primary")
                product_link_2.click()
            except:
                pass
            time.sleep(2)
    elif choice == 2:
        livre = input("Quel livre souhaitez-vous rajouter (Titre + auteur) ? ")
        liste_livres.append(livre)
    elif choice == 0:
        break
    else:
        print("Veuillez entrer un choix valide")

        
# Scrapping de listes de livres sur Sens Critiques

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.senscritique.com/top/resultats/les_meilleurs_livres_de_2016/1166333")

titres = soup.find_all("h2", {"class" : "Text__SCText-sc-14ie3lm-0 cECGzR"})
auteurs = soup.find_all("p", {"class" : "Text__SCText-sc-14ie3lm-0 Creators__Text-sc-1t34n5u-0 fzhdFi hqDnDC ProductListItem__StyledCreators-sc-ico7lo-6 cMTDEQ"})

liste_livres_sc = []

for i in range(len(titres)):
    liste_livres_sc.append(titres[i].get_text() + " - " + auteurs[i].get_text()[9:]) 
    #puis tu relances la partie de script au dessus pour les prendre sur la bourse aux livres
