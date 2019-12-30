

from pprint_json import pretty_print_json
import pprint

def get_my_information():
    data= pretty_print_json("http://ip-api.com/json/")
    for key,val in data.items():
        pprint.pprint(str(key)+":"+str(val))


if __name__=="__main__":
    get_my_information()