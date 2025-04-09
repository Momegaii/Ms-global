import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def upload_video():
    # Get user input for video details
    video_path = input("Enter the full path of the video file: ")
    title = input("Enter the video title: ")
    description = input("Enter the video description: ")

    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open YouTube Studio
        driver.get("https://studio.youtube.com")

        # Wait for manual login
        input("Log in to YouTube Studio and press Enter here...")

        # Click "Create" button
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@aria-label='Create']").click()

        # Click "Upload videos"
        time.sleep(2)
        driver.find_element(By.XPATH, "//ytcp-ve[@id='text-item-0']").click()

        # Upload the video file
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(video_path)

        # Wait for upload to process
        time.sleep(10)

        # Add video title & description
        driver.find_element(By.XPATH, "//ytcp-social-suggestion-input[@id='title-textarea']//div[@id='textbox']").send_keys(title)
        driver.find_element(By.XPATH, "//ytcp-social-suggestion-input[@id='description-textarea']//div[@id='textbox']").send_keys(description)

        # Click "Next" (3 times)
        for _ in range(3):
            driver.find_element(By.XPATH, "//ytcp-button[@id='next-button']").click()
            time.sleep(2)

        # Click "Public" option
        driver.find_element(By.NAME, "PUBLIC").click()

        # Click "Publish"
        driver.find_element(By.XPATH, "//ytcp-button[@id='done-button']").click()

        print("✅ Video upload initiated. Check YouTube Studio for processing status.")

    finally:
        # Close WebDriver
        time.sleep(5)
        driver.quit()

# Run the function



def main_yt():
	while True :
		
		UI_YT = input("MS LIQUID FOR YT UPLOADING SYS DO YOU WANT TO PROCESEED ? 1 .YES ||| 2. NO  ")
		if UI_YT == "1" :
			upload_video()
			
		elif UI_YT == "2": 
			print("wont be uploading peace solid ms")
			
		
