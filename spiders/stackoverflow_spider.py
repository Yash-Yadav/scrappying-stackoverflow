import scrapy
import datetime

class StackOverflowSpider(scrapy.Spider):
  name = "stackoverflow"

  def start_requests(self):
    urls = [
      'https://stackoverflow.com/questions/tagged/python'
    ]

    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)
  
  def parse(self, response):
    filename = "test.html"

    with open(filename, 'ab') as f:
      questions = response.xpath('//*[@class="fs-body3 grid--cell fl1 mr12 sm:mr0 sm:mb12"]/text()').get().strip()
      questions = questions[:-13]
      date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      output = questions + "|" + date + "\n"
      f.write(output.encode())