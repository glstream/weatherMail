import requests
import json
url = 'https://quotes.rest/qod'



res = requests.get(url)
resData = res.json()


try: 
    resData['contents']['quotes']
    data = resData['contents']['quotes']
except Exception as e:
    data = [{u'category': u'inspire', u'permalink': u'https://theysaidso.com/quote/74RZL1_lOJ5uScr4h8ntCgeF/napoleon-hill-effort-only-fully-releases-its-reward-after-a-person-refuses-to-qu', u'tags': [u'effort', u'inspire'], u'quote': u'Effort only fully releases its reward after a person refuses to quit.', u'author': u'Napoleon Hill', u'length': u'69', u'background': u'https://theysaidso.com/img/bgs/man_on_the_mountain.jpg', u'date': u'2018-12-23', u'title': u'Inspiring Quote of the day', u'id': u'74RZL1_lOJ5uScr4h8ntCgeF'}]


# if  is None:
#      data = resData['contents']['quotes']
# else: 
#     



# try: 
#     resData["error"]

#     if resCode == 429:
#         print("There was an issue using canned quote")
#         data = [{u'category': u'inspire', u'permalink': u'https://theysaidso.com/quote/74RZL1_lOJ5uScr4h8ntCgeF/napoleon-hill-effort-only-fully-releases-its-reward-after-a-person-refuses-to-qu', u'tags': [u'effort', u'inspire'], u'quote': u'Effort only fully releases its reward after a person refuses to quit.', u'author': u'Napoleon Hill', u'length': u'69', u'background': u'https://theysaidso.com/img/bgs/man_on_the_mountain.jpg', u'date': u'2018-12-23', u'title': u'Inspiring Quote of the day', u'id': u'74RZL1_lOJ5uScr4h8ntCgeF'}]

# #data = 
# except Exception as e: 
#     print("There was an error: \n"+str(e))

# 

# quote = data[0]["quote"]

# author = data[0]["author"]

# print(quote)
# print(author)

print(data)