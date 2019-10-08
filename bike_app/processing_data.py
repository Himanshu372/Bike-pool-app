import requests
import json

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

