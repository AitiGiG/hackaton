# import requests
# from bs4 import BeautifulSoup as Bs
# import csv

# url = 'https://www.mashina.kg/search/?currency=2&price_from=&price_to=&page='

# def parse(url):
#     auto_list = []

#     for i in range(1,16):
#         request = requests.get(f'{url}{i}')
#         html = Bs(request.text,'lxml')
#         auto = html.find('div', class_ = 'table-view-list').find_all('div',class_ = 'list-item')
#         for a in auto:
#             name = a.find('h2' , class_='name').text
#             price = a.find('div', class_= 'price').find('strong').text
#             img = a.find('img' , class_='lazy-image')
#             info1 = a.find('div', class_ = 'info-wrapper').find('p', class_= 'year-miles').text
#             info2 = a.find('div', class_ = 'info-wrapper').find('p', class_= 'body-type').text
#             info3 = a.find('div', class_ = 'info-wrapper').find('p', class_= 'volume').text
#             name = name.strip()
#             auto_list.append({'name' : name , 'img': img.get('data-src'),'price': price , 'info' :[info1.strip(), info2.strip(), info3.strip()]})
#     return auto_list

# def send_csv(data_url):
#     field_name = ['name' , 'img' , 'price' , 'info']
#     with open('cars.csv' , 'w') as file:
#         csv_w = csv.DictWriter(file, delimiter='|', fieldnames=field_name) 
#         for i in data_url:
#             csv_w.writerow(i)    

# data_url = parse(url)
# send_csv(data_url)

