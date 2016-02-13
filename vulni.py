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
    cve_number = tree.findall(".//cve")
    cve_url = tree.findall(".//cvrfUrl")
    for cve in cve_number:
        print(cve.)
getdata()