import pandas as pd
import requests
from bs4 import BeautifulSoup

import time
from tqdm import tqdm

def get_auto(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    auto_block = soup.find('div', class_='page page_type_listing')
    auto_url = auto_block.find_all('a', class_='Link ListingItemTitle__link')
    #print(auto_url)
    return [link.attrs['href'] for link in auto_url]

def get_all_links():
    brand = ['VOLVO']
    cars_link_list = []
    start_time = time.time()
    for car in tqdm(brand):
        for page in tqdm(range(1,4)):
            try:
                car_link_into_list = get_auto(f'https://auto.ru/cars/{car}/used/?page={page}')
                cars_link_list.extend(car_link_into_list)
                time.sleep(1)
                #print(f"Brand: {car} Page: {page}")
                #print("--- %s seconds ---" % (time.time() - start_time))
            except AttributeError:
                print("'NoneType' object has no attribute 'find_all'")
                pass
    return cars_link_list

def get_data_auto(url):
    
    response = requests.get(url)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'lxml')
    
    if soup.find('div', class_='CardSold__title'):
        return 0
    else:
        try:
            #выведем цену
            cost_attribute = soup.find('div', class_='InfoPopup InfoPopup_theme_plain InfoPopup_withChildren PriceUsedOffer__price')
            cost = cost_attribute.find('span', class_='OfferPriceCaption__price')
            cost = cost.text.replace('\xa0', '').replace('₽', '')

            #выведем брэнд и модель
            url_name_model = url.split('/')
            brand = url_name_model[6]
            model_name = url_name_model[7]

            #выведем год выпуска
            soup = BeautifulSoup(response.text, 'html.parser')
            modelDate_attribute = soup.find('ul', class_='CardInfo')
            modelDate = modelDate_attribute.find('a', class_='Link Link_color_black').text

            #выведем пробег
            mileage_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_kmAge')
            mileage = mileage_attribute.find_all('span', class_='CardInfoRow__cell')[1].text
            mileage = mileage.replace('\xa0', '').replace('км', '')

            #выведем тип кузова
            bodyType_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_bodytype')
            bodyType = bodyType_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем цвет авто
            color_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_color')
            color = color_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем цвет авто
            color_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_color')
            color = color_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем характеристики двигателя
            engine_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_engine')
            engine_attr = engine_attribute.find_all('span', class_='CardInfoRow__cell')[1].text.split('/')
            engineDisplacement = engine_attr[0].replace(' л ', '')
            enginePower = engine_attr[1].replace('\xa0', '').replace('л.с.', '').replace(' ', '')
            fuelType = engine_attr[2].replace(' ', '')

            #выведем тип коробки
            vehicleTransmission_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_transmission')
            vehicleTransmission = vehicleTransmission_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем тип привода
            drive_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_drive')
            drive = drive_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем расположение руля
            wheel_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_wheel')
            wheel = wheel_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем состояние
            state_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_state')
            state = state_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем количество владельцев
            ownersCount_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_ownersCount')
            ownersCount = ownersCount_attribute.find_all('span', class_='CardInfoRow__cell')[1].text.replace('\xa0', ' ')

            #выведем тип ПТС
            pts_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_pts')
            pts = pts_attribute.find_all('span', class_='CardInfoRow__cell')[1].text

            #выведем статус прохождения таможни
            customs_attribute = soup.find('li', class_='CardInfoRow CardInfoRow_customs')
            customs = customs_attribute.find_all('span', class_='CardInfoRow__cell')[1].text
        except AttributeError:
            print('Could not parse url')
            pass
        except UnboundLocalError:
            print('Could not parse url')
            pass
            
    
        return {'cost':cost, 
                'brand':brand, 
                'model_name':model_name, 
                'modelDate':modelDate, 
                'mileage':mileage, 
                'bodyType':bodyType, 
                'color':color, 
                'engineDisplacement':engineDisplacement, 
                'enginePower':enginePower, 
                'fuelType':fuelType, 
                'vehicleTransmission':vehicleTransmission, 
                'drive':drive, 
                'wheel':wheel, 
                'state':state, 
                'ownersCount':ownersCount, 
                'pts':pts, 
                'customs':customs}

def create_df():
    get_all_url =  get_all_links()
    lst_data = []
    for url in tqdm(get_all_url):
        try:
            #print(url)
            auto_data = get_data_auto(url)
            #print(auto_data)
            lst_data.append(auto_data)
            time.sleep(1)
        except AttributeError:
            print('Could not parse url')
            pass
        except UnboundLocalError:
            print('Could not parse url')
            pass
    return lst_data

    
auto_list_data = create_df()


for i in auto_list_data:
    if i == 0:
        auto_list_data.remove(i)
df = pd.DataFrame(auto_list_data)
df.to_csv('auto_ru_data.csv', encoding='utf-8', index=False)
df


data = pd.read_csv('auto_ru_data.csv')
data



