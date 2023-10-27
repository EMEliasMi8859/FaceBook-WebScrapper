
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# options = Options()
# options.add_argument("--disable-notifications")

print("[!]Initializing dirver...")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox()

print("[!]Getting response form facebook login......")
driver.get("https://www.facebook.com")
print("[!]FB servers response recieved successfully .....")
username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
login_button = driver.find_element(By.NAME, "login")
print("[!]Initializing variables........")
username_field.send_keys("Muhammad.Elias.Muhammadi@Gmail.com")
password_field.send_keys("MuhammadiFb859@")
print("[!]Attempting to login...........")
login_button.click()
print("[!]Waiting to Login   ...........")
WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Create a post']")))

print("[!]Login susscessfull ...........")

print("[!]Getting the Recvrrlnk.........")


def SendToReciever(url):
    driver.get(url)
    print("[!]Finding message button .......")
    btn = driver.find_element(By.XPATH, "//div[@aria-label='Message']")
    btn.click()
    print("[!]Openinig message box .........")
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Message' and @role='textbox']")))
    print("Message box opened successfully .")
    chat = driver.find_element(By.XPATH, "//div[@aria-label='Message' and @role='textbox']")
    Message = '<p class="xat24cr xdj266r xdpxx8g" dir="ltr"><span data-lexical-text="true">'+ 'Hello i am testing a bot' + '</span></p>'
    # Clear the existing content in the contenteditable div (optional)
    # driver.execute_script("arguments[0].innerHTML = '';", chat)
    print("[!]typing     message ...........")
    # # Enter the desired text in the contenteditable div
    # driver.execute_script("arguments[0].innerHTML = arguments[1];", chat, Message)
    chat.click()
    for i in "This Message is Send By EMEliasMi from Ningarhar University BCS as Testing Bot":
        chat.send_keys(i)

    print("[!]Sening message     ...........")

    chat.send_keys(Keys.RETURN)  
    driver.implicitly_wait(5)
    closebtn = driver.find_element(By.XPATH, "//div[@aria-label='Close chat']")
    closebtn.click()
    driver.implicitly_wait(2)
    
for i in range(0,2):
    list1 = ["https://www.facebook.com/Monica.472", "https://www.facebook.com/Afghan.noori.378"]
    SendToReciever(list1[i])
driver.quit()

