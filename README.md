# booksCrawl

This is a pure Python scrapy project based on a book website. This was a joy to work on because I learned how to play around with the LinkExtractors.

LinkExtractors is such a sexy feature in the framework. You write the rules you want the crawl to follow and ..  WALA!! magic.

I programmed the crawl to follow a set of rules such as what links are allowed to be crawled, followed and where the parseback occurs. 

I extracted the: Title, Price, Avalability and url from the site successfully by yielding into a dictionary and storing it into a CSV file.
