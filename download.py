from datetime import datetime,timedelta
import requests

# Only Query API User can generate Token, Query API access is paid extra even for Admins
Token = 'PUT YOUR TOKEN HERE'
Headers = {'token': Token, 'Content-Type': 'application/json'}

def download_log(DS_ID,filename):
    url = 'https://app.datorama.com/services/dynamiclz/{}/statistics'.format(DS_ID)
    body = {
      "pageSize": 1000,
      "pageNumber": 1
    }
    
    res = requests.post(url=url,headers=Headers,json=body)
    if res.status_code==200:
      start = 0
      for i in res.json()['data']:
        if i['startExecutionTime']>start and i['status'] == 'SUCCESS':
            start = i['startExecutionTime']
            log_id = i['id']
        else:pass
    else:
      print('Error')
    url_d ='https://app.datorama.com/v1/data-stream-stats/dynamic/{}/download'.format(log_id)
    
    resp = requests.get(url=url_d,headers=Headers)
    url_content = resp.content
    csv_file = open('{}.csv'.format(filename), 'wb')
 
    csv_file.write(url_content)
    csv_file.close()      

# download_log(1234567, 'MyFile')
download_log(NUMERIC ID OF DATASTREAM, 'PUT YOUR FILENAME HERE')
