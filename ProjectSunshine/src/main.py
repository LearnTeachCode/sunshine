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

def main():
    #key
    file_in = open('sunlight.key', 'r')
    #read key file
    api_key = file_in.read()
    #close file
    file_in.close()
    
    #init list
    candidate_list = {}

    #get user inputs
    phrase = str(raw_input("Enter keyword phrase:\n "))
    start_date = str(raw_input("Enter start date (e.g. 2010-01-01):\n "))
    end_date = str(raw_input("Enter start date (e.g. 2015-12-12):\n "))
    
    #setup url for request
    url = ("http://capitolwords.org/api/1/text.json?phrase=" 
        + phrase + "&page=0&state=CA&start_date=" 
        + start_date + "&end_date="
        + end_date + "&apikey=" 
        + api_key)  
    
    #print "My api key is:", api_key
    #print "My url is:", url
    
    #make request
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(request)   
    #close request
    opener.close()

    #get json response
    json_data = json.load(f)
    j_string = byteify(json_data)
    #pprint(j_string)
    
    #create file of json response for testing
    file_out = open('sunlight-output-LongVersion.txt', 'w')
    file_out.writelines(json.dumps(j_string, indent=4, sort_keys=True))
    
    #create TXT file for output
    file_out = open('sunlight-output-shortVersion-tab.txt', 'w')

    #create Objects for runtime manipulation
    for item in json_data['results']:
        #if in the JSON response, the candidate speaks
        if item['speaking'] != '':
            #check if Candidate does not exist in list
            #if Candidate does exist, skip this
            if candidate_list.has_key(item['bioguide_id']) == False:
                candidate = CandidateObject(item['bioguide_id'],
                item['speaker_first'], item['speaker_last'],
                item['speaker_party'])
                
            #add Candidate to list of candidates
            candidate_list[item['bioguide_id']] = candidate
                
            #Otherwise add Message to existing Candidate
            candidate_list.get(item['bioguide_id']).addMessage(item['speaking'], item['date'], item['title'])
            
            #write to TXT file
            file_out.writelines(item['speaker_last'])
            file_out.writelines(', ')
            file_out.writelines(item['speaker_first'])
            file_out.writelines('\t')
            file_out.writelines(json.dumps(item['speaking']))
            file_out.writelines('\n')
            
    #close files
    file_out.close()
    
    #test Object
    print(candidate_list.get('F000116').getMessage())
    
    
#used to get rid of that 'u' in the JSON format
def byteify(json_data):
    if isinstance(json_data, dict):
        return {byteify(key):byteify(value) for key,value in json_data.iteritems()}
    elif isinstance(json_data, list):
        return [byteify(element) for element in json_data]
    elif isinstance(json_data, unicode):
        return json_data.encode('utf-8')
    else:
        return json_data
    

#program entry
if __name__=="__main__":
    main()