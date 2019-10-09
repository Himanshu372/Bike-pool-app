import requests
import json
import math

MAPQUEST_URL = 'http://www.mapquestapi.com/geocoding/v1/address?key=SsRGOwY10OEkejYJYB2ACoaUiNtDDoIv'



def get_location(loc_string):
    '''

    :param loc_string:
    :return:
    '''
    try:
        get_mapquest_url = MAPQUEST_URL + '&location={}'.format(loc_string)
        get_mapquest_response = requests.get(get_mapquest_url)
        if get_mapquest_response.status_code == 200:
            response_text_dict = json.loads(get_mapquest_response.text)
            loc_results = response_text_dict['results'][0]['locations']
            if len(loc_results) == 1:
                return loc_results[0]['latLng']['lat'], loc_results[0]['latLng']['lng']
    except:
        return None


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