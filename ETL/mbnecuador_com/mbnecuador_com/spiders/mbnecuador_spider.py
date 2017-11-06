import scrapy
import re

class MbnecuadorSpider(scrapy.Spider):
    name = "Mbnecuador"
    
    start_urls = [
        'http://mbnecuador.com/mbnecuador/releases-2/',
    ]

    def parse(self, response):
        for artista in response.css('article.col-1-4'):
            
            nombre = artista.css('footer h2 a::text').extract_first()
            
            #delete whitespace and upper
            nombre  = re.sub(' +',' ',nombre.strip().upper())

            categoria  = artista.css('footer div.cat a::text').extract_first()
            
            if categoria is not None:
                categoria = re.sub(' +',' ',categoria.strip().upper())

            yield {
                
                'nombre': nombre,
                'url': artista.css('footer h2 a::attr(href)').extract_first(),
                'categoria': categoria,
                'categoria_url': artista.css('footer div.cat a::attr(href)').extract_first(),
                'imagen_url': artista.css('img::attr(src)').extract_first(),
                'duplicado':0
            }

            next_page = response.css('div.wp-pagenavi a.nav-next::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)