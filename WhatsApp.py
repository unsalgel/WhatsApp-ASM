from selenium import webdriver
import time
sayi=1
driver=webdriver.Firefox() 
driver.get('https://web.whatsapp.com/') 
mesaj=input(' yazılması istediginiz mesajınız ')
input("bilgiler alındı bekleyin: ")
while sayi==1:
	mesajsayisi = driver.find_elements_by_css_selector('.OUeyt')
	for mesajsayi in mesajsayisi:
		username = mesajsayi.find_element_by_xpath('../../../../..//span[@class = "_1wjpf"]')
		username.click()
		mesajkutusu=driver.find_element_by_class_name('_2S1VP')  
		mesajkutusu.send_keys(mesaj) 
		driver.find_element_by_class_name('_2lkdt').click()
		driver.back()



		

	

















