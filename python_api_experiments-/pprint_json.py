
import requests
import pprint


def pretty_print_json(url):
    """
    Pretty prints out the json object and then returns it
    """
    response= requests.get(url)
    response = response.json()
    file= open("json_data.txt","w+")
    pprint.pprint(response,file)
    pprint.pprint(response)
    return response


