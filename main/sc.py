
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def upload_soundcloud():
    # Get user input for track details
    email = input("Enter your SoundCloud email: ")
    password = input("Enter your SoundCloud password: ")
    track_path = input("Enter the full path of the track file: ")
    title = input("Enter the track title: ")
    description = input("Enter the track description: ")

    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open SoundCloud login page
        driver.get("https://soundcloud.com/signin")

        # Wait for login page to load
        time.sleep(3)

        # Enter email
        driver.find_element(By.NAME, "email").send_keys(email)

        # Enter password
        driver.find_element(By.NAME, "password").send_keys(password)

        # Click "Sign In"
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").click()

        # Wait for login to complete
        time.sleep(5)

        # Navigate to upload page
        driver.get("https://soundcloud.com/upload")
        time.sleep(3)

        # Upload the track file
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(track_path)

        # Wait for file to upload
        time.sleep(15)

        # Add title
        title_input = driver.find_element(By.XPATH, "//input[@placeholder='Name your track']")
        title_input.clear()
        title_input.send_keys(title)

        # Add description
        desc_input = driver.find_element(By.XPATH, "//textarea[@placeholder='Describe your track']")
        desc_input.send_keys(description)

        # Set track as public
        time.sleep(2)
        public_button = driver.find_element(By.XPATH, "//label[contains(text(),'Public')]")
        public_button.click()

        # Click "Save" or "Publish"
        time.sleep(2)
        publish_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        publish_button.click()

        print("✅ Track upload initiated. Check SoundCloud for processing status.")

    finally:
        # Close WebDriver
        time.sleep(5)
        driver.quit()

# Run the function
def main_sc():
	while True :
		
		UI_sc = input("MS LIQUID FOR sc UPLOADING SYS DO YOU WANT TO PROCESEED ? 1 .YES ||| 2. NO  ")
		if UI_sc == "1" :
			upload_soundcloud()
			
		elif UI_sc == "2": 
			print("wont be uploading peace solid ms")
