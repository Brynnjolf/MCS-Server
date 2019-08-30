from main.models import *
from datetime import datetime
import json

def save_json_data(payload):
        payloadJSON = json.loads(payload)
        for scrapeDate, scrapeData in payloadJSON.items():
            for companyKey, companyValue in scrapeData.items():
                if companyKey != 'Date':
                    companyModel = Company(ticker= companyKey, name= companyValue['Summary']['Name'], sector= companyValue['Profile']['\nBusiness Description\n'])
                    #print(companyKey, companyValue['Summary']['Name'], companyValue['Profile']['\nBusiness Description\n'])
                    for companyDataKey, companyDataValue in companyValue.items():
                        if companyDataKey == "Summary":
                            for summaryKey, summaryValue in companyDataValue.items():
                                # print(summaryKey, summaryValue)
                                pass
                        if companyDataKey == "Directors":
                            for directorName, roleName in companyDataValue.items():
                                # print(directorName, roleName)
                                pass
                        if companyDataKey == "Ratio":
                            for ratioKey, ratioValue in companyDataValue.items():
                                # print(ratioKey, ratioValue)
                                pass
                        if companyDataKey == "FinancialProfile":
                            # print(companyDataValue['Year'])
                            for statementKey, statementValue in companyDataValue['Data'].items():
                                # print(statementKey)
                                pass
                        if companyDataKey == "Profile":
                            for profileKey, profileValue in companyDataValue.items():
                                # print(profileKey, profileValue)
                                pass
                        if companyDataKey == "HistoricalPrices":
                            for date, priceData in companyDataValue.items():
                                # print(date, priceData)
                                pass
                        if companyDataKey == "HistoricalDividends":
                            divList = []
                            # Entry.objects.bulk_create([
                            # Entry(headline="Django 1.0 Released"),
                            # Entry(headline="Django 1.1 Announced"),
                            # Entry(headline="Breaking: Django is awesome")
                            # ])

                            for date, dividend in companyDataValue.items():
                                # print(date, dividend)
                                divList.append(Dividends(date = date, ticker = companyModel, dividends = dividend))
                            Dividends.objects.bulk_create(divList)
