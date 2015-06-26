'''
Created on Jun 19, 2015
This application displays which politicians are involved in the keywords
    the user has provided
@author: 
    Sina Tuy
    Kiron Roy
    Richard Chen
    Kendra Branton
    Hong Luu
'''
import urllib2
import json
from Candidate import *
import MessageObject
from pprint import pprint

def main():
    file_in = open('sunlight.key', 'r')
    api_key = file_in.read()
    candidate_list = {}

    # no longer need file_in
    file_in.close()

    phrase = ""
    while phrase == "":
        phrase = str(raw_input("Enter phrase: "))
    url = ("http://capitolwords.org/api/1/text.json?phrase="+phrase+
           "&page=0&state=CA&start_date=2010-01-01&end_date=2015-12-12"+
           "&apikey="+api_key)  
    
    print "My api key is:", api_key
    print "My url is:", url
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(request)
    
    # no longer need opener
    opener.close()

    json_data = json.load(f)
    j_string = byteify(json_data)
#     pprint(j_string)
    
    file_out = open('sunlight-output-LongVersion.txt', 'w')
    file_out.writelines(json.dumps(j_string, indent=4, sort_keys=True))

    file_out = open('sunlight-output-ShortVersion.txt', 'w')

    for item in json_data['results']:
        if item['speaking'] != '':
            # check if candidate does not exist
            # if candidate does exist, skip this
            if candidate_list.has_key(item['bioguide_id']) == False:
                candidate = CandidateObject(item['bioguide_id'], item['speaker_first'], item['speaker_last'],item['speaker_party'])
                
                # add candidate to list of candidates if not exist
            candidate_list[item['bioguide_id']] = candidate
                
            # add message to candidate
            candidate_list.get(item['bioguide_id']).addMessage(item['speaking'], item['date'], item['title'])
            
            file_out.writelines(item['speaker_last'])
            file_out.writelines(',')
            file_out.writelines(item['speaker_first'])
            file_out.writelines('\n')
            file_out.writelines(json.dumps(item['speaking'], indent=4))
            file_out.writelines('\n\n')

    file_out.close()
    
    print(candidate_list.get('F000116').getMessage())
    
# used to get rid of that 'u' in the JSON format
def byteify(json_data):
    if isinstance(json_data, dict):
        return {byteify(key):byteify(value) for key,value in json_data.iteritems()}
    elif isinstance(json_data, list):
        return [byteify(element) for element in json_data]
    elif isinstance(json_data, unicode):
        return json_data.encode('utf-8')
    else:
        return json_data

if __name__=="__main__":
    main()