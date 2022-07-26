from itertools import count
from lib2to3.pgen2 import driver
from jmespath import search
import scrapy
from scrapy_selenium import SeleniumRequest
import json
from selenium.webdriver.common.keys import Keys
from sqlalchemy import true
from scrapy.selector import Selector

class Cebraspe2selenium(scrapy.Spider):
    name ='Cebraspe2selenium'

  
    def __init__(self):
     with open(r'C:\Users\hannan\Desktop\cebraspetracker\link_dataset.json', encoding='utf-8') as data_file:
       self.data = json.load(data_file)
    

    def start_requests(self):
        yield SeleniumRequest(
            url="https://security.cebraspe.org.br/PAS_21/Consulta1Chamada2Semestre_582AECCD/default.aspx",
            wait_time=10,
            screenshot=true,
            callback=self.parse
        )

        
      
    
    def parse(self, response):
     #  img = response.meta['screenshot']

    #  with open('screenshot.png','wb') as f:
     #   f.write(img)

        driver= response.meta['driver']
        searchinput = driver.find_element("xpath",'//*[@id="txtNome"]')
        searchinput.send_keys('Matheus Rodrigues da Silva')
        driver.find_element("xpath",'//*[@id="btnBuscar"]').click()
        #searchinput.send_keys(Keys.ENTER)
        driver.save_screenshot('search.png')


        html = driver.page_source
        response_obj = Selector(text=html)
        
        yield{
            'item':response_obj.xpath("//*[@id='GridView1']/tbody/tr[2]/td[2]/text()").get().strip()
          }
       
        

    

