from Utils.http_methods import Http_methods

"""Testing nova poshta"""
base_url = "https://api.novaposhta.ua/v2.0/json/" # base url
api_key = "50110018387dc4f7bc677621dbf28030"
city_name = "Київ"

class Nova_poshta_api():

    """method to search settlements"""
    @staticmethod
    def search_settlements():
        json_to_search_settlements = {"apiKey": api_key, "modelName": "Address",
                                     "calledMethod": "searchSettlements",
                                     "methodProperties": {"CityName" : city_name,
                                                          "Limit" : "10", "Page" : "1"}}
        result_post = Http_methods.post(base_url, json_to_search_settlements)
        print(result_post.text)
        return result_post

    """method to get cities"""

    @staticmethod
    def get_cities(ref):
        json_to_get_cities = {"apiKey": api_key, "modelName": "Address", "calledMethod": "getCities",
                                      "methodProperties": {"Ref" : ref, "Page" : "1", "FindByString" : city_name,
                                                           "Limit" : "10"}}
        result_post = Http_methods.post(base_url, json_to_get_cities)
        print(result_post.text)
        return result_post