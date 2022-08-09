import requests

cookie_url = "https://www.notams.faa.gov/dinsQueryWeb"

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}
# query_url = "https://www.notams.faa.gov/dinsQueryWeb/queryRetrievalMapAction.do' -X POST -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://www.notams.faa.gov/dinsQueryWeb/' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://www.notams.faa.gov' -H 'Connection: keep-alive' -H 'Cookie: ak_bmsc=DFCE8EBA1CE070EB6F632F3E54A2B93A~000000000000000000000000000000~YAAQhBwhF46r+V+CAQAAOK2hexBCtrc5dBfInA8lAZf9T/IupuvIcc66EQaRCSvRH4i1W5yL++YimsV0JM9mFQuDcccuZoYUzR5Yhvi8KNshFFOYV/akNb85tlpXEgZgaXuHtJXaub7aulz2eoUsaDEDG8tut0aP79zyPUOkB925QMyrOoORaEck9b79V6taRl5nw8LUtf0igD1llVxg2X0gSBdBzKroPbr7MDnHRCjiqbSd0C3B9lFbfgV3H/YeJ02wJqlPje60UnSAHuCAuyXrYmNvZ/yjf9xXlsBVU0BtfcUYN0OcncfjpzJVuqf4yATskMPVYebvyVge5uYiVXEVNZCr4DJkc7B5PPxbKI2ysrk2Hgn82Sq3RmNwrxpfSqmw0EclrsqK9RHLVbfhZHufenMEdvgGjr1sP1Ocr6IwXYV+ZR1f/9KupdtFz0XdVwPVJA1vdccU8xHKeRGxh//qfQESSA==; JSESSIONID=0000o1v5CcixzHxJ5Xj2IDf-Ct5:15hfnse1u; bm_mi=64EA2FCA31658396C01A6A2E375FFA17~YAAQhBwhF4eV+V+CAQAAzUWhexCEwncGNXjsBGYRpSKDhK8aArGcwigytvdrnmgdIs3MTJLwHqxhx81E1ASj4hiZCzyDwYUCP+jI/dLe/MmtnaLfop6HCM5XSExgJA/J6sRztLW+NDMrgOm+gSfJzFRxYbvbBTd5NGyxq80Fn2ot7HPzJQaOqAX9v77p3JGuMrlunkMS4v2AHZhmdG7R7yrRQDf1JBj6QgT83K54KKf8yzsvD5+WRVyQ+4zOa0M3KMPLDdSa2QxIfzgLuh/BXz4E4aVevJuegEig2DTtZiMzVMrfJObt55wpkQA3M6mfOEWSaH/ZXUk73dDmOoU8~1; bm_sv=1A06CB436CC58A3D92A76EA7AF61EAED~YAAQhBwhF3Sc+l+CAQAABOqkexC1Mh2ElLj6KZZ16H23TImYVmLFtPGcTghUAJ3q9f13jtICI0dUwGXZfS71rmQ7RWr+8QXvoIcsjrAn83w8JxfT/n/dx4cScKdx1xwO/sSK9MjYjGc3LafW1RSVrEHM6/+wykFrHPTal1otbOEnp9Gf9g365517Pft+VIFTgU+cJq6UqnxTu9FqssFSq+LxQta8U96YaeBut9w1Ud0lmj4Mk63YwznY+oIiTnMbbv+RQR0=~1; DINS_QUERY_DISCLAIMER=true' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'TE: trailers' --data-raw 'reportType=Report&retrieveLocId=khef+kbuf&actionType=notamRetrievalByICAOs&submit=View+NOTAMs'"

s = requests.Session()
response = s.request("GET", cookie_url, data=payload, headers=headers)

query_url = "https://www.notams.faa.gov/dinsQueryWeb/queryRetrievalMapAction.do"

query_text = "KCPS%2CKHEF"
qpayload = f"reportType=Report&retrieveLocId={query_text}&actionType=notamRetrievalByICAOs&submit=View%2BNOTAMs"
qheaders = {
    "cookie": "JSESSIONID=00007bP4u7oHs1dlIch_cw_4-Fy%3A15hfns9ka",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.notams.faa.gov/dinsQueryWeb/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.notams.faa.gov",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}

qresponse = requests.request("POST", query_url, data=qpayload, headers=qheaders)


# print(qresponse.text)

# Save the response as a file
with open(f"notams{query_text}.html", "w") as f:
    f.write(qresponse.text)
