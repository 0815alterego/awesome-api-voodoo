#   calls the psirt tropo app and informs about a sec. issue
#   call("+"+number,{network:"SMS"});
#   say(UserName+", Please join Spark Room for Response to PSIRT : "+psirt_msg)
import requests

def place_sms(number,name,psirt):
    token_number='114d274d7b276246bc496f264672f1eaf3c84f45868d4cf002147e83319284af2633a32f1c088c67ff9ec6dd'
    baseURL='https://api.tropo.com/1.0/sessions?action=create&token='
    full_url= baseURL + token_number +'&DialNumber='+number+'&UserName='+name.replace(' ','+')+'&psirt_msg='+psirt
    print(full_url)
    call = requests.get(full_url,headers={'content-type':'application/x-www-form-urlencoded'})
    print(call.status_code,call.content)

#place_sms('+49151xxxxx','Michael Dombek','CVE-2012-111')