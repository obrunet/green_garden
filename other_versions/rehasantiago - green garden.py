from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains


#user_agent = "Mozilla/5.0 (compatible; github_commits/1.0)"#name ur bot
#cap = DesiredCapabilities().FIREFOX
#cap["marionette"] = False
username = input("Enter your username:")
password = input("enter your password:")
driver = webdriver.Firefox()
driver.get("https://github.com/login")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='login_field']").send_keys(username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
driver.find_element_by_xpath("//input[@value='Sign in']").click()
driver.find_element_by_xpath("//ul[@class='list-style-none']//li[1]//div//a//span[2]").click()
driver.find_element_by_xpath("//div[@id='readme']//div//div//a").click()
#title = driver.find_element_by_xpath("//div[@class='CodeMirror-lines' and @role='presentation']//div//div[@class='CodeMirror-code']//div[1]//pre//span//span").get_attribute("innerText")
#driver.find_element_by_xpath("//div[@class='CodeMirror-lines' and @role='presentation']//div//div[@class='CodeMirror-code']//div[1]//pre//span//span").click()
#elem = driver.find_element_by_xpath("//div[@class='CodeMirror-lines' and @role='presentation']//div//div[@class='CodeMirror-code']//div[1]//pre//span//span")
#driver.execute_script('arguments[0].innerHTML = "abc";',elem)

#a = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div[1]/div/form[2]/div[3]/div[2]/textarea").get_attribute('innerText')
#print(a)
#a = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div[1]/div/form[2]/div[3]/div[2]/textarea")

driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div[1]/div/form[2]/div[1]/span/input").clear()
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div[1]/div/form[2]/div[1]/span/input").send_keys('READM.md')
driver.find_element_by_xpath("//button[@id='submit-file']").click()
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div[1]/div[4]/div[1]/div[2]/div[2]/form[1]/button").click()
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div[1]/div/form[2]/div[1]/span/input").clear()
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div[1]/div/form[2]/div[1]/span/input").send_keys('README.md')
driver.find_element_by_xpath("//button[@id='submit-file']").click()
driver.quit()