## crawl for 86shop ####
## def fun1 output = {'name': 分類名稱 , 'categ_url': ...}
## def fun2 input(categ_url) ---> 商品頁面的所有商品 {'product_name': 商品名稱, 'prod_url': https://www.86shop.com.tw/product?saleid=RJ00512C}
## def fun3 input(prod_url) output {......}

import requests
from bs4 import BeautifulSoup
from copy import deepcopy

def shop86_products():
    url = "https://www.86shop.com.tw/"
    resq = requests.get(url)
    soup = BeautifulSoup(resq.text, 'html.parser')
    cat_list = soup.find_all("li", class_ = "nav_menuli")

    output1= [] # 每個分類項目，與對應的url
    for n in range(3,len(cat_list)):
        categories = [x.text for x in cat_list[n].find_all("a")]
        urls = [x.get("href") for x in cat_list[n].find_all("a")]
        cats = []
        for c in range(1,len(categories)):
            k = {'cat1':categories[0], 'cat2': categories[c], 'url' : url, 'category_url': urls[c]}
            cats.append(k)
        output1 += cats

    for category in output1[0]:
        list_output = shop86_product_list(category)
        for product in list_output:
            shop86_product_info(product)

    

def shop86_product_list(category):
    url = category["url"]
    c_url = url + category["category_url"]
    resq = requests.get(c_url)
    soup = BeautifulSoup(resq.text, 'html.parser')
    page_urls = [c_url]+[url+x.get('href') for x in soup.find_all("a", class_ = 'pagination_num')[1:]]

    product_list = []
    for page_url in page_urls:
        resq = requests.get(page_url)
        soup = BeautifulSoup(resq.text, 'html.parser')
        for prod in soup.find_all("div", class_ = "bd_left"):
            category_t = deepcopy(category)
            category_t.update({'product_name' : prod.a.get("title"), 'product_url' : prod.a.get("href")})
            product_list.append(category_t)
            
    return product_list
        
def shop86_product_info(product):
    url = product["url"]
    p_url = url + product["product_url"]
    resq = requests.get(p_url)
    soup = BeautifulSoup(resq.text, 'html.parser')
    try:
        info = soup.find("div", class_ = "pr_PDInfo").get_text(separator=" \n ")
    except:
        info = ''
    product.update({'product_info' : info})
    # inser.mongodb


if __name__ == "__main__":
    shop86_products()
