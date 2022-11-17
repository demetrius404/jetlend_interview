import requests as request
from lxml import etree

base_url = "https://jetlend.ru/borrower"
response = request.get(base_url)
if response.status_code == 200:
    tree = etree.HTML(response.text)
    count_has_attr = 0
    count_total = 0
    for e in tree.xpath(".//*"):
        # get element attr, as a sequence
        count_total += 1
        if len(e.items()) > 0:
            count_has_attr += 1
    print(response.url, count_total, count_has_attr)
    # https://jetlend.ru/borrower 1074 961
