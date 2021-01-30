# 获取指定Github账户的日贡献历史

[![last-commit](https://img.shields.io/github/last-commit/HollowMan6/Github-Contribution)](../../graphs/commit-activity)
![Python package](https://github.com/HollowMan6/Github-Contribution/workflows/Python%20package/badge.svg)

[![Followers](https://img.shields.io/github/followers/HollowMan6?style=social)](https://github.com/HollowMan6?tab=followers)
[![watchers](https://img.shields.io/github/watchers/HollowMan6/Github-Contribution?style=social)](../../watchers)
[![stars](https://img.shields.io/github/stars/HollowMan6/Github-Contribution?style=social)](../../stargazers)
[![forks](https://img.shields.io/github/forks/HollowMan6/Github-Contribution?style=social)](../../network/members)

[![Open Source Love](https://img.shields.io/badge/-%E2%9D%A4%20Open%20Source-Green?style=flat-square&logo=Github&logoColor=white&link=https://hollowman6.github.io/fund.html)](https://hollowman6.github.io/fund.html)
[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/HollowMan6/Github-Contribution.svg)](../../archive/master.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/HollowMan6/Github-Contribution.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/Github-Contribution/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/HollowMan6/Github-Contribution.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/Github-Contribution/context:python)

(English version is down below)

[Python库依赖](../../network/dependencies)

安装好Python3运行环境和依赖后，运行`python Github_Contribution.py`，输入Github账户信息，你就可以获得打印版的贡献信息。

另外，你还可以将[Github_Contribution.py](Github_Contribution.py)放到你的项目目录下，作为包导入：

```python
from Github_Contribution import GithubContributions

username = input("Github UserID: ")
github = GithubContributions(username)
```

类GithubContributions包含属性username，为用户ID；joinTime为Github账户创建日期，格式为`%Y-%m-%d`，为字符串类型；totalCount为总贡献数，整型数字；yearlyLeastContri和yearlyMaxContri分别为每年最小最大日贡献数，为字典类型，键为整型年份，值为整型的单日极值贡献数量。noContribution为list型，存放无贡献的日期；L1Contribution、L2Contribution、L3Contribution、L4Contribution分别存放第一、二、三、四级贡献的日期和具体贡献数量，为字典类型组成的list，单个字典中键date存放日期，count存放数量。

**警告**：

***仅供测试使用，不可用于任何非法用途！***

***对于使用本代码所造成的一切不良后果，本人将不负任何责任！***

# Get Contribution History on Days for Specified Github Account

[Python Dependencies](../../network/dependencies)

After installing the running environment and dependencies of Python3, run `python Add_Github_Contribution_History.py`, enter your Github user ID, you can get printed version of your contribution history on days.

In addition, you can put [Github_Contribution.py](Github_Contribution.py) in your project directory and import it as a package:

```python
from Github_Contribution import GithubContributions

username = input("Github UserID: ")
github = GithubContributions(username)
```

The class `GithubContributions` contains the attribute `username`, which is the user ID; `joinTime`, which is the creation date of GitHub account, in the format of `%Y-%m-%d`, which is the string type; `totalCount`, which is the total number of contributions in integer number; `yearlyLeastContri` and `yearlyMaxContri`, which separately stores the minimum and maximum daily number of contributions each year, and which is the dictionary type; the key, which is the integer year, and the value is the single day extreme number of contributions. `noContribution` is a list type, which stores the date of no contribution; `L1Contribution`, `L2Contribution`, `L3Contribution` and `L4Contribution` store the date and specific contribution quantity of the first, second, third and fourth level contribution respectively, which is a list of dictionary types, and in a single dictionary key date stores the date and count stores the quantity.

**Warning**:

***For TESTING ONLY, not for any ILLEGAL USE!***

***I will not be responsible for any adverse consequences caused by using this code.***
