import os
from decouple import config

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

# relevant part start here
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
# relevant part ends here 
# driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)

browser = webdriver.Chrome(executable_path='./driver/chromedriver.exe', options=options)

browser.get('https://portal.neondistrict.io/')

# NAVIGATE TO DELIVERY AGENTS =====================
# =================================================
def processDelivery():
    # Hover NEon Pizza Navigation Menu to display dropdown options
    hoverOverMenu = WebDriverWait(browser, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[1]/div[3]'))
    )
    # Hover Over Menu Action
    ActionChains(browser).move_to_element(hoverOverMenu).perform()

    # Click delivery Agent menu
    WebDriverWait(browser, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[1]/div[4]/div/a[1]/div'))
    ).click()


    # LOGOUT
    def logout():
        # GO TO PROFILE PAGE
        WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/a'))
        ).click()

        # LOGOUT ACCOUNT
        WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[5]/div/div/div[2]/button[3]'))
        ).click()

        
    # CHECK IF DELIVERY AGENT BANK PAY BUTTON IS ALREADY AVAILABLE
    bankPay = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div[3]/div/button'))
    )

    # Start New Shift
    def startNewShift():
        print("=== START NEW  SHIFT ===")
        WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div[3]/div/button[text()="Start New Shift"]'))
        ).click()

        logout()
        

    if bankPay.is_displayed():
        if bankPay.is_enabled():
            if bankPay.text == "START NEW SHIFT":
                startNewShift()
            else: 
                bankPay.click()

                browser.implicitly_wait(3) # seconds

                chkbankPay = WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div[3]/div/button'))
                )
                if chkbankPay.is_enabled():
                    startNewShift()
                else:
                    logout()
        else:
            logout()
    else:
        print("Test")
        startNewShift()


   

# LOGIN ===========================================
# =================================================
def login(uname):
    WebDriverWait(browser, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div/div[5]/form/div[1]/div/input'))
    ).send_keys(uname)

    WebDriverWait(browser, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div/div[5]/form/div[2]/div/input'))
    ).send_keys(config('NEONPWD'))

    WebDriverWait(browser, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div/div[5]/form/button'))
    ).click()


try:

    acc = [
        "neondistrict03@mailinator.com",
        "neondistrict05@mailinator.com",
        "neondistrict07@mailinator.com",
        "neondistrict08@mailinator.com",
        "neondistrict09@mailinator.com",
        "neondistrict10@mailinator.com",
        "neondistrict11@mailinator.com",
        "neondistrict12@mailinator.com",
        "neondistrict13@mailinator.com",
        "neondistrict4@mailinator.com",
        "neondistrict15@mailinator.com",
        "neondistrict16@mailinator.com",
        "neondistrict17@mailinator.com",
        "neondistrict18@mailinator.com",
        "neondistrict19@mailinator.com",
        "neondistrict20@mailinator.com",
        "neondistrict21@mailinator.com",
        "neondistrict22@mailinator.com",
        "neondistrict23@mailinator.com",
        "neondistrict24@mailinator.com",
        "neondistrict25@mailinator.com",
        "neondistrict26@mailinator.com",
        "neondistrict27@mailinator.com",
        "neondistrict28@mailinator.com",
        "neondistrict29@mailinator.com",
        "neondistrict30@mailinator.com",
        "neondistrict31@mailinator.com",
        "neondistrict32@mailinator.com",
        "neondistrict33@mailinator.com",
        "neondistrict34@mailinator.com",
        "neondistrict35@mailinator.com",
    ]

    for email in acc:
        btnLogin = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div[1]/div/div[5]/button'))
        )
        btnLogin.click()

        # Login Account
        print(email)
        login(email)

        # Process Delivery
        processDelivery()

except TimeoutException as ex:
    print(ex)


browser.close()
