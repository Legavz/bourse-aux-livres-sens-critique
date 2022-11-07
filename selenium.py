import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

liste_livres = []

while True:
    print("Que voulez-vous faire ?")
    print("0 - Quitter")
    print("1 - Lancer la recherche")
    print("2 - Rajouter un livre dans ma liste")
    "-" * 30
    choice = int(input("Ton choix: "))
    if choice == 1:
        driver = webdriver.Chrome(executable_path="C:/Users/Alexis/chromedriver.exe")
        driver.get("https://shop.labourseauxlivres.fr/")
        for i in liste_livres:
            search_bar = driver.find_element(By.CLASS_NAME, "search-bar__input")
            search_bar.send_keys(i)
            time.sleep(2)
            find_button = driver.find_element(By.CLASS_NAME, "search-bar__submit")
            find_button.click()
            time.sleep(2)
            product_link = driver.find_element(By.CLASS_NAME, "product-item__info-inner")
            product_link.click()
            time.sleep(2)
            try:
                product_link_2 = driver.find_element(By.CSS_SELECTOR, ".product-form__add-button.button.button--primary")
                product_link_2.click()
            except:
                pass
            time.sleep(4)
    elif choice == 2:
        livre = input("Quel livre souhaitez-vous rajouter (Titre + auteur) ? ")
        liste_livres.append(livre)
    elif choice == 0:
        break
    else:
        print("Veuillez entrer un choix valide")
