from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the webpage
URL = "https://brainlox.com/courses/category/technical"
driver.get(URL)
time.sleep(5)  # Allow time for the page to load

# Find course elements using the correct class name
course_elements = driver.find_elements(By.CLASS_NAME, "courses-content")  # Update with correct class

courses = []
for course in course_elements:
    try:
        title = course.find_element(By.TAG_NAME, "h3").text  # Adjust if needed
        description = course.find_element(By.TAG_NAME, "p").text  # Adjust if needed
        price = course.find_element(By.CLASS_NAME, "price-per-session-text").text  # Adjust if needed
        
        courses.append({
            "title": title,
            "description": description,
            "price": price
        })
    except:
        continue

# Save to JSON
with open("courses.json", "w", encoding="utf-8") as f:
    json.dump(courses, f, ensure_ascii=False, indent=4)

print(f"Scraped {len(courses)} courses. Data saved in courses.json.")

# Close the browser
driver.quit()
