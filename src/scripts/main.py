import requests
from bs4 import BeautifulSoup
import csv



class TableScraper:
    results = []
    
    
    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):
        #print(html)
        
        content = BeautifulSoup(html, 'lxml') #here we are creating the content variable that would store the first version of the entire content
        table = content.find('table')
        #print(table)

        rows = table.findAll('tr')#extracting the rows
        #print(rows)

        

        self.results.append([header.text for header in rows[0].findAll('th')])#extracting the columns
        print(self.results)
                

        for row in  rows:
            
            self.results.append([data.text for data in row.findAll('td')])#Extracting all the data from the rows

        for one in self.results:#After appending all the data printing the result
          print(one)

    def to_csv(self):#Creating a csv file containing the entire data
        with open('table.csv','w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.results)
        

    def run(self):
        response = self.fetch('https://rera.cgstate.gov.in/Approved_project_List.aspx')
        self.parse(response.text)
        self.to_csv()
        
        

if __name__=='__main__':
    scraper = TableScraper()
    scraper.run() 