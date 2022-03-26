from selenium import webdriver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://automatize.netlify.app/")
campo_email = driver.find_element_by_id("email")
campo_email.click()
campo_email.send_keys("geo-estevam@hotmail.com")
campo_senha = driver.find_element_by_xpath("//input[@name='campoSenha']")
campo_senha.click()
campo_senha.send_keys = "150105"
button = driver.find_element_by_xpath("//button[text()='Enviar']")
button.click()
