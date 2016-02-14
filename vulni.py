import requests
import kacktoken
import xml.etree.ElementTree as et
from datetime import datetime, timedelta
# returns a dictionary with two keys and two values
# first key: CVE number
# second key: CVE url
# third key: affected platform

intervall = 5
last_items_to_check = '10'
supported_devices = ['ASA','NX-OS']

def getdata():
    response = requests.get('https://api.cisco.com/security/advisories/cvrf/latest/'+last_items_to_check+'.xml', headers={'Authorization':'Bearer '+kacktoken.kacktoken()})
    tree = et.fromstring(response.content)
    print(response.content)
    cve_ids = tree.findall(".//advisoryId")
    cve_urls = tree.findall(".//cvrfUrl")
    #print(len(cve_ids))
    #print(len(cve_urls))
    length = len(cve_ids)
    for i in range(length):
        #print(cve.text)
        dict={"ID":cve_ids[i].text,"URI":cve_urls[i].text}
        print(dict['URI'])
        details = requests.get(dict['URI'])
        psirt=et.fromstring(details.content)
        xml_namespaces = {'ns':"http://www.icasi.org/CVRF/schema/cvrf/1.1",
                          'xsd':"http://www.w3.org/2001/XMLSchema",
                          'xsi':'http://www.w3.org/2001/XMLSchema-instance',
                          'prod':"http://www.icasi.org/CVRF/schema/prod/1.1"}
        dates_created = psirt.findall('.//ns:Date',xml_namespaces)
        date_created = dates_created[0].text
        date_time_created = datetime.strptime(date_created,"%Y-%m-%dT%H:%M:%S")

        if datetime.now()- date_time_created < timedelta(days=intervall):
            all_products=psirt.findall('.//prod:FullProductName',xml_namespaces)
            alert_url=psirt.find('.//ns:URL',xml_namespaces)
            match=False
            for product in all_products:
                for device in supported_devices:
                    if product.text.find(device) > -1:
                        match=True
                        alert_product=device
            if match:
                print(cve_ids[i].text,alert_product,alert_url.text)
        #print(details.content, details.status_code)
        length = length-1

getdata()