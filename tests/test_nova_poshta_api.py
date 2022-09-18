from requests import Response
from Utils.checking import Checking
from Utils.api import Nova_poshta_api

"""Create, update and delete location"""

class Test_searh_settlements():

    def test_search_settlements_get_cities(self):

        print('Method POST')
        result_post: Response = Nova_poshta_api.search_settlements()
        check_post = result_post.json()
        data = check_post.get('data')[0]
        address = data.get('Addresses')[0]
        ref = address.get ('DeliveryCity')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_value(result_post, "success", True)


        print('Method POST')
        result_post: Response = Nova_poshta_api.get_cities(ref)
        Checking.check_status_code(result_post, 200)
        Checking.check_json_value(result_post, "success", True)