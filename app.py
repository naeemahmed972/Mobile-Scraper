import requests
import logging
import json
from pages.all_links import AllLinks
from pages.all_mobiles import AllMobiles


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

main_url = 'https://www.whatmobile.com.pk/'
mobile_data = {
    "mobiles": [

    ]
}


main_page_content = requests.get(main_url).content
links = AllLinks(main_page_content)

for link in links.get_links:
    mobile_page_content = requests.get(main_url+link).content
    mobile_page = AllMobiles(mobile_page_content)
    page_mobiles = mobile_page.mobiles

    for mobile in page_mobiles:
        print(mobile)
        if mobile.price != None:
            mobile_data["mobiles"].append(
                {
                    "name": mobile.name,
                    "price": mobile.price,
                    "link": main_url + (mobile.link).replace("/", '')
                }
            )


# print(mobile_data)
data_json = json.dumps(mobile_data)
print(data_json)

with open("mobile_data.json", "w+") as json_file:
    json_file.write(data_json)






# books = page.books

# # for book in books:
# #     print(book)


# # Going through all pages
# for page_num in range(1, page.page_count):
#     url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
#     page_content = requests.get(url).content
#     page = AllBooks(page_content)
#     books.extend(page.books)


# # print(books)