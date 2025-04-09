import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def upload_instagram():
    # Get user input for login & post details
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    video_path = input("Enter the full path of the video file: ")
    caption = input("Enter the caption for your video: ")

    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open Instagram login page
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        # Enter username
        driver.find_element(By.NAME, "username").send_keys(username)

        # Enter password
        driver.find_element(By.NAME, "password").send_keys(password)

        # Click "Log In"
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait for login to complete
        time.sleep(10)

        # Open the upload page
        driver.get("https://www.instagram.com/")
        time.sleep(5)

        # Click the create post button (+ button)
        upload_btn = driver.find_element(By.XPATH, "//div[@role='menuitem']")
        upload_btn.click()
        time.sleep(3)

        # Upload video file
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(video_path)

        # Wait for upload to process
        time.sleep(10)

        # Click "Next"
        driver.find_element(By.XPATH, "//div[text()='Next']").click()
        time.sleep(3)

        # Click "Next" again (filters page)
        driver.find_element(By.XPATH, "//div[text()='Next']").click()
        time.sleep(3)

        # Enter caption
        caption_box = driver.find_element(By.XPATH, "//textarea[@aria-label='Write a caption...']")
        caption_box.send_keys(caption)

        # Click "Share" button
        share_button = driver.find_element(By.XPATH, "//div[text()='Share']")
        share_button.click()

        print("✅ Video uploaded successfully! Check Instagram for processing status.")

    finally:
        # Close WebDriver
        time.sleep(5)
        driver.quit()

# Run the function

def main_inst():
	while True :
		
		UI_inst = input("MS LIQUID FOR inst UPLOADING SYS DO YOU WANT TO PROCESEED ? 1 .YES ||| 2. NO  ")
		if UI_inst == "1" :
			upload_instagram()
			
		elif UI_inst == "2": 
			print("wont be uploading peace solid ms")

