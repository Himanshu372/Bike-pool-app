import requests
import json
import math
import re
from bike_app.constants import MAPQUEST_URL





def get_location(loc_string):
    '''

    :param loc_string:
    :return:
    '''
    # try:
    loc_list = [i for i in re.split('\s|,', loc_string) if len(i) > 0]
    country = loc_list.pop()
    state = loc_list.pop()
    city = loc_list.pop()
    street = '+'.join(loc_list)
    get_mapquest_url = MAPQUEST_URL + '&street={}'.format(street) + '&city={}'.format(city) + '&state={}'.format(state) + '&country={}'.format(country)
    get_mapquest_response = requests.get(get_mapquest_url)
    if get_mapquest_response.status_code == 200:
        response_text_dict = json.loads(get_mapquest_response.text)
        loc_results = response_text_dict['results'][0]['locations']
        if len(loc_results) == 1:
            return loc_results[0]['latLng']['lat'], loc_results[0]['latLng']['lng']
    # except:
    #     return None


def cal_haversine_distance(cord_1, cord_2):
    '''

    :param cord_1:
    :param cord_2:
    :return:
    '''
    R = 6371
    lat_1, long_1 = float(cord_1.split(',')[0].strip('()\ ')), float(cord_1.split(',')[1].strip('()\ '))
    lat_2, long_2 = float(cord_2.split(',')[0].strip('()\ ')), float(cord_2.split(',')[1].strip('()\ '))
    del_lat = math.radians(abs(lat_1 - lat_2))
    del_long =  math.radians(abs(long_1 - long_2))
    a = pow(math.sin(del_lat / 2), 2) + math.cos(long_1) * math.cos(long_2) * pow(math.sin(del_long / 2), 2)
    c = 2 * math.atan2(pow(a, .5), pow((1 - a), .5))
    distance = R * c
    return distance

