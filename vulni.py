import requests
import kacktoken
import xml.etree.ElementTree as et
# returns a dictionary with two keys and two values
# first key: CVE number
# second key: CVE url
# third key: affected platform
def getdata():
    response = requests.get('https://api.cisco.com/security/advisories/cvrf/latest/10.xml', headers={'Authorization':'Bearer '+kacktoken.kacktoken()})
    tree = et.fromstring(response.content)
    cve_ids = tree.findall(".//advisoryId")
    cve_urls = tree.findall(".//cvrfUrl")
    #print(len(cve_ids))
    #print(len(cve_urls))
    length = len(cve_ids)
    for i in range(length):
        #print(cve.text)
        dict={"ID":cve_ids[i].text,"URI":cve_urls[i].text}
        length = length-1

getdata()