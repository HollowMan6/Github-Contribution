# -*- coding:utf-8 -*-
# by 'hollowman6'

'''
警告：
仅供测试使用，不可用于任何非法用途！
对于使用本代码所造成的一切不良后果，本人将不负任何责任！

Warning:
For TESTING ONLY, not for any ILLEGAL USE!
I will not be responsible for any adverse consequences caused by using this code.

'''

import requests
from lxml import etree
from datetime import datetime
import json


class GithubContributions:
    def __init__(self, username):
        self.username = username.lower()
        self.noContribution = []
        self.L1Contribution = []
        self.L2Contribution = []
        self.L3Contribution = []
        self.L4Contribution = []
        self.joinTime = ""
        self.yearlyLeastContri = {}
        self.yearlyMaxContri = {}
        self.totalCount = 0
        self.getContributionStatus()

    def getJoinTime(self):
        githubAPI = "https://api.github.com/users/" + self.username
        self.joinTime = json.loads(requests.get(githubAPI).text)[
            "created_at"].split('T')[0]
        return self.joinTime

    def getContributionStatus(self):
        self.getJoinTime()
        joinTimeOb = datetime.strptime(self.joinTime, "%Y-%m-%d")
        joinYear = int(self.joinTime.split('-')[0])
        for year in range(joinYear, datetime.now().year+1):
            github = "https://github.com/" + self.username + "?tab=overview&from=" + \
                str(year) + "-01-01&to=" + str(year) + "-12-31"
            tree = etree.HTML(requests.get(github).text)
            leastContriChanged = False
            leastContri = 100000
            maxContri = 0
            overCurrentTime = False
            for gEle in tree.xpath("//*[@id='js-pjax-container']/div[2]/div/div[2]/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/div/div[1]/svg/g/g"):
                for rectEle in gEle:
                    date = rectEle.get("data-date")
                    if (datetime.strptime(date, "%Y-%m-%d") - joinTimeOb).days >= 0 and (datetime.now() - datetime.strptime(date, "%Y-%m-%d")).days >= 0:
                        level = rectEle.get("fill")
                        if level == "var(--color-calendar-graph-day-bg)":
                            self.noContribution.append(date)
                        else:
                            count = int(rectEle.get("data-count"))
                            if count > maxContri:
                                maxContri = count
                            if count < leastContri:
                                leastContri = count
                                leastContriChanged = True
                            self.totalCount += count
                            dayDetails = {"date": date, "count": count}
                            if level == "var(--color-calendar-graph-day-L1-bg)":
                                self.L1Contribution.append(dayDetails)
                            elif level == "var(--color-calendar-graph-day-L2-bg)":
                                self.L2Contribution.append(dayDetails)
                            elif level == "var(--color-calendar-graph-day-L3-bg)":
                                self.L3Contribution.append(dayDetails)
                            elif level == "var(--color-calendar-graph-day-L4-bg)":
                                self.L4Contribution.append(dayDetails)
                    elif (datetime.now() - datetime.strptime(date, "%Y-%m-%d")).days < 0:
                        overCurrentTime = True
                        break
                if overCurrentTime:
                    break
            if not leastContriChanged:
                leastContri = 0
            self.yearlyLeastContri[year] = leastContri
            self.yearlyMaxContri[year] = maxContri

        return self.noContribution, self.L1Contribution, self.L2Contribution, self.L3Contribution, self.L4Contribution


if __name__ == "__main__":
    username = input("Github UserID: ")
    github = GithubContributions(username)

    print("Join Time: " + github.joinTime)
    print("---No Contribution---")
    for date in github.noContribution:
        print(date)

    print("---L1 Contribution---")
    for details in github.L1Contribution:
        print("Date: " + details["date"] +
              " Countributions: " + str(details["count"]))

    print("---L2 Contribution---")
    for details in github.L2Contribution:
        print("Date: " + details["date"] +
              " Countributions: " + str(details["count"]))

    print("---L3 Contribution---")
    for details in github.L3Contribution:
        print("Date: " + details["date"] +
              " Countributions: " + str(details["count"]))

    print("---L4 Contribution---")
    for details in github.L4Contribution:
        print("Date: " + details["date"] +
              " Countributions: " + str(details["count"]))

    print("---Total Countributions: " + str(github.totalCount))

    joinYear = int(github.joinTime.split('-')[0])
    for year in range(joinYear, datetime.now().year+1):
        print("---"+str(year)+" Daily Min Contribution: " +
              str(github.yearlyLeastContri[year]))
        print("---"+str(year)+" Daily Max Contribution: " +
              str(github.yearlyMaxContri[year]))
