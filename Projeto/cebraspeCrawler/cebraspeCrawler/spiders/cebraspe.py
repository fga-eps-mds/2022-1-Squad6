import scrapy
from scrapy_splash import SplashRequest

class CebraspeSpider(scrapy.Spider):
    name = 'cebraspe'
    allowed_domains = ['https://www.cebraspe.org.br']
    
    script ='''
    function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
    
    '''
    def start_requests(self):
        yield SplashRequest(url="https://www.cebraspe.org.br/pas/subprogramas/2019_2021/3",callback=self.parse,endpoint="execute",args={'lua_source':self.script})


    def parse(self, response):
        print(response.body)