import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def run_agent():
    print("--- 📧 INTERNSHIP AGENT (Manual Login Support) ---")
    
    # 1. INPUTS
    my_email = input("Enter your Login Email: ")
    my_password = input("Enter your Login Password: ") 
    email_subject = input("Enter Email Subject: ")
    email_body = input("Enter Email Body: ")
    recipient = "scittest@auditram.com"

    print("\n[Status] Initializing Browser...")
    
    # 2. SETUP CHROME OPTIONS
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)

    try:
        wait = WebDriverWait(driver, 30) # Increased wait time to 30 seconds

        # 3. LOGIN PHASE
        print("[Status] Navigating to Gmail...")
        driver.get("https://gmail.com")

        # Email
        print("[Status] Entering Email...")
        email_field = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
        email_field.send_keys(my_email)
        email_field.send_keys(Keys.RETURN)

        # Password
        print("[Status] Entering Password...")
        pwd_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        time.sleep(2)
        pwd_field.send_keys(my_password)
        pwd_field.send_keys(Keys.RETURN)

        # --- MANUAL INTERVENTION PAUSE ---
        print("\n" + "="*50)
        print("⚠️  IMPORTANT: CHECK YOUR PHONE/SCREEN NOW ⚠️")
        print("The script is pausing for 20 seconds.")
        print("1. If Google asks for 2FA, approve it on your phone.")
        print("2. If a 'Not now' prompt appears, click it manually.")
        print("Make sure the GMAIL INBOX is visible before the timer ends.")
        print("="*50 + "\n")
        
        time.sleep(20) # 20 seconds for you to handle 2FA manually

        # 4. COMPOSE PHASE
        print("[Status] Searching for 'Compose' button...")
        
        # We try 2 different ways to find the Compose button (Text or Icon)
        compose_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Compose'] | //div[@aria-label='Compose'] | //div[@role='button' and text()='Compose']")))
        compose_btn.click()
        
        # To Field
        print("[Status] Filling Details...")
        to_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@peoplekit-id] | //input[@aria-label='To recipients']")))
        to_field.send_keys(recipient)
        to_field.send_keys(Keys.TAB)

        # Subject
        subject_field = driver.find_element(By.NAME, "subjectbox")
        subject_field.send_keys(email_subject)

        # Body
        body_field = driver.find_element(By.XPATH, "//div[@aria-label='Message Body']")
        body_field.send_keys(email_body)

        # 5. SEND PHASE
        print("[Status] Sending Email...")
        body_field.send_keys(Keys.CONTROL, Keys.ENTER)
        
        # Wait for success message
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Message sent']")))
        print("\n[SUCCESS] Email sent successfully!")
        
        time.sleep(5)

    except Exception as e:
        print(f"\n[ERROR] The script failed: {e}")
        print("Tip: If the error mentions 'Timeout', it means the script couldn't find the button.")

    finally:
        print("[Status] Closing Agent.")
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    run_agent()