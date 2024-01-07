import scrapy
import os 
from os.path import dirname
import sqlite3

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, 'source-EXPLOIT-DB.html')

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    #start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]
    start_urls = [f"file://{url}"]
    
    def parse(self, response):
        ## Setup database
        connection = sqlite3.connect('vuln.db')
        table = 'CREATE TABLE vulns (exploit TEXT, cve TEXT)'
        cursor = connection.cursor()
        cursor.execute(table)

        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table = child
                break
        
        # Actual data too much, just save the first 100 rows of data for the sake of eg. 
        count = 0 
        
        for row in table.xpath('//tr'):
            if count > 100:
                break
            try:
                # extract relavant data and insert them into the table
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                cursor.execute('INSERT INTO VULNS (exploit, cve) VALUES(?, ?)', (exploit_id, cve_id))
                connection.commit()
                count += 1
                
                #print(row.xpath('td//text()')[0].extract())
            except IndexError:
                pass
