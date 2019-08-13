from bs4 import BeautifulSoup
import sys
sys.path.insert(0, '/home/mcsadmin/webServer/scraper')
from time import time
from nzxscraper.scrape_data import get_browser, list_companies, scrape_company, printProgressBar
from nzxscraper.save_data_sql import *
from nzxscraper.environment import DEBUG, downloadDirectory, COMPANIES
import shutil
from nzxscraper import logger

def run_scraper_module():
    startTime = time()
    browser = get_browser()

    try:
        stockTickersList = list_companies(browser)

        # Initialise the array which is  going to store Stock class objects
        stockDataArray = []

        # For each ticker in the list, find the link to the respective summary page
        stockIteration = 0
        printProgressBar(stockIteration, len(stockTickersList))
        for stock in stockTickersList :
            stockData = scrape_company(browser, stock)
            stockDataArray.append(stockData)
            stockIteration += 1
            printProgressBar(stockIteration, len(stockTickersList))
        logger.info("Scraping complete")

        save_data(stockDataArray)
    finally:
        browser.quit()
        # logger.info("Temporary files deleted")
        # shutil.rmtree(downloadDirectory)

        if DEBUG: endTime = time()
        # logger.info("That took a total of: " + str(round(endTime-startTime)) + " seconds.")
        # logger.info(str(round((endTime-startTime)/COMPANIES)) + " seconds per company.")

run_scraper_module()
