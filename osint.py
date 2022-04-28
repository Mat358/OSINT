from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

email_ok = str(input("Imput an email: "))
pass_sample = "QazWsx193!"

PATH = "C:\Program Files\Python310\Scripts\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def facebook_check():

    driver.get("https://pl-pl.facebook.com/")
    time.sleep(5)

    fb_cookie_accept = driver.find_element(By.CSS_SELECTOR, "[title='Zezwól tylko na niezbędne pliki cookie']").click()
    fb_input_email = driver.find_element(By.ID, "email").send_keys(email_ok)
    fb_input_email_button = driver.find_element(By.NAME, "login").click()

    time.sleep(5)
    fb_id_found = driver.find_elements(By.ID, "not_me_link")
    fb_not_found = driver.find_elements(By.LINK_TEXT, "Znajdź swoje konto i zaloguj się.")
    fb_forg_pass = driver.find_element(By.LINK_TEXT, "Nie pamiętasz hasła?")

    if bool(fb_id_found) == True:

        fb_login_name = driver.find_element(By.XPATH, '//*[@id="header_block"]/span/div/div[1]/div[2]/span')
        fb_login_split = fb_login_name.text.split(" ")

        if len(fb_login_split) >= 5:
            fb_login_name = fb_login_split[3:5]
            print("Facebook account found.")
            print(f"FaceBook Name: {fb_login_name[0]}.")
            print(f"FaceBook Surename: {fb_login_name[1]}.")

        elif len(fb_login_split) == 4:
            fb_login_name = fb_login_split[3:4]
            print("Facebook account found.")
            print(f"FaceBook Name: {fb_login_name[0]}")

        else:
            pass

    elif bool(fb_not_found) == True:
        print("Facebook account not found.")
    
    elif bool(fb_forg_pass) == True:
        print(f"Facebook account found.")

    else:
        print("Some problem occured, skiping Facebook.")
        pass

    

def instagram_check():

    driver.get("https://www.instagram.com/accounts/login/?next=/login/")
    
    time.sleep(5)

    ig_cookie_accept = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
    ig_input_email = driver.find_element(By.NAME, "username").send_keys(email_ok)
    ig_input_pass = driver.find_element(By.NAME, "password").send_keys(pass_sample)

    time.sleep(5)
    ig_input_email_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
    
    time.sleep(3)
    ig_id_found = driver.find_element(By.ID, "slfErrorAlert")


    if bool(ig_id_found) == True:
            ig_login_split = ig_id_found.text.split(" ")             

            if ig_login_split[0] == "Sorry,":
                print(f"Instagram account found.")

            elif ig_login_split[0] == "The":
                print("Instagram account not found.")

            else:
                pass

    elif bool(ig_id_found) == False:
        print("Instagram account not found.")

    else:
        print("Some problem occured, skiping Instagram.")
        pass

   
def tiktok_check():
    driver.get("https://www.tiktok.com/login/email/forget-password")
    
    time.sleep(5)
    tt_input_email = driver.find_element(By.NAME, "email").send_keys(email_ok)

    time.sleep(3)
    tt_input_email_button = driver.find_elements(By.CSS_SELECTOR, "[class='login-button-31D24 line-ErmhG highlight-1TvcX']")

    if tt_input_email_button == True:

        driver.find_element(By.CSS_SELECTOR, "[class='login-button-31D24 line-ErmhG highlight-1TvcX']").click()

        time.sleep(5)
        tt_id_found = driver.find_element(By.CLASS_NAME, "errMsg-1ZYT3")
        
        if tt_id_found.text == "Too many attempts. Try again later.":
            print("Too many attemps, cant check.")

        elif tt_id_found.text() == "The":
            print("TikTok account not found.")

        else:
            print("Some problem occured, skiping TikTok.")
            pass
    else:
        print("Some problem occured, skiping TikTok.")
        pass

facebook_check()
instagram_check()
tiktok_check()

driver.quit()




