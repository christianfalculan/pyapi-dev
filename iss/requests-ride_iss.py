#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    ctrl = requests.get(MAJORTOM)
    # send a put with requests.put()
    ctrl1 = requests.get(MAJORTOM)
    # send a delete with requests.delete()
    ctrl2 = requests.get(MAJORTOM)
    # send a head with requests.head()
    ctrl3 = requests.get(MAJORTOM)

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()
    houston = ctrl1.json()
    launch = ctrl2.json()
    


    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)



    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

if __name__ == "__main__":
    main()

