import scrapy


class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table = child
                break
        for row in table.xpath('//tr'):
            try:
                print(row.xpath('td//text()')[0].extract())
            except IndexError:
                pass
