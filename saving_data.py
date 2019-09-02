from main.models import *
from datetime import datetime
import json

def save_json_data(payload):
        payloadJSON = json.loads(payload)
        for scrapeDate, scrapeData in payloadJSON.items():
            for companyKey, companyValue in scrapeData.items():
                if companyKey != 'Date':
                    companyModel = Company(ticker= companyKey, name= companyValue['Summary']['Name'], sector= companyValue['Profile']['\nBusiness Description\n'])
                    companyModel.save()
                    #print(companyKey, companyValue['Summary']['Name'], companyValue['Profile']['\nBusiness Description\n'])
                    for companyDataKey, companyDataValue in companyValue.items():
                        if companyDataKey == "Summary":
                            summaryList = []
                            for summaryKey, summaryValue in companyDataValue.items():
                                # print(summaryKey, summaryValue)
                                pass
                                
                        if companyDataKey == "Directors":
                            directorList = []
                            for directorName, roleName in companyDataValue.items():
                                # print(directorName, roleName)
                                directorList.append(
                                    Directors(
                                        date = scrapeDate.replace('/','-'),
                                        ticker = companyModel,
                                        director_name = directorName,
                                        director_role = roleName
                                    )
                                )
                            Directors.objects.bulk_create(directorList, ignore_conflicts = True)
                            print("Saved director information for ", companyKey)
                        if companyDataKey == "Ratio":
                            ratioList = []
                            # ratioList.append(
                            #     Ratios(
                            #         class Ratios(models.Model):
                            #         date = scrapeDate.replace('/','-'),
                            #         ticker = companyModel
                            #         market_cap = companyDataValue['\nOverview\n'],
                            #         price_equity = companyDataValue['\nOverview\n'],
                            #         EPS = companyDataValue['\nOverview\n'],
                            #         NTA = companyDataValue['\nOverview\n'],
                            #         DPS = companyDataValue['\nOverview\n'],
                            #         beta_value = companyDataValue['\nOverview\n'],
                            #         price_NTA = companyDataValue['\nOverview\n'],
                            #         Net_yield = companyDataValue['\nOverview\n'],
                            #         Sharpe = companyDataValue['\nOverview\n'],
                            #         debt_equity = companyDataValue['\nOverview\n'],
                            #         current = companyDataValue['\nOverview\n'],
                            #         ROE = companyDataValue['\nOverview\n'],
                            #         ROA = companyDataValue['\nOverview\n'],
                            #         quick_ratio = companyDataValue['\nOverview\n'],
                            #     )
                            # )

                        if companyDataKey == "FinancialProfile":
                            # print(companyDataValue['Year'])
                            for statementKey, statementValue in companyDataValue['Data'].items():
                                # print(statementKey)
                                pass
                        if companyDataKey == "Profile":
                            profileList = []
                            # print(profileKey, profileValue)
                            profileList.append(
                                CompanyProfile(
                                    ticker = companyModel,
                                    date = scrapeDate.replace('/','-'),
                                    overview = companyDataValue['\nOverview\n'],
                                    performance = companyDataValue['\nPerformance\n'],
                                    outlook = companyDataValue['\nOutlook\n'],
                                    description = companyDataValue['\nBusiness Description\n']
                                )
                            )
                            CompanyProfile.objects.bulk_create(profileList, ignore_conflicts= True)
                            print("Saved profile data for ", companyKey)
                        if companyDataKey == "HistoricalPrices":
                            priceList = []
                            for date, priceData in companyDataValue.items():
                                # print(date, priceData)
                                priceList.append(
                                    Price(
                                        date = date,
                                        ticker = companyModel,
                                        price = priceData['Last'],
                                        capital_adjusted = priceData['Capital Adjusted'],
                                        volume_traded = priceData['Volume Traded'],
                                        value_traded = priceData['Dollar Value Traded'],
                                        number_of_trades = priceData['Trades'],
                                        price_change = priceData['Change']))
                            Price.objects.bulk_create(priceList, ignore_conflicts= True)
                            print("Saved price data for ", companyKey)
                        if companyDataKey == "HistoricalDividends":
                            divList = []
                            for date, dividend in companyDataValue.items():
                                # print(date, dividend)
                                divList.append(
                                    Dividends(
                                        date = date,
                                        ticker = companyModel,
                                        dividends = dividend))
                            Dividends.objects.bulk_create(divList, ignore_conflicts= True)
                            print("Saved dividend data for ", companyKey)
