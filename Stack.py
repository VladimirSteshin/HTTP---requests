import requests
import datetime


def get_questions(tag, days):
    final_date = int(datetime.datetime.timestamp(datetime.datetime.now()))
    start_date = final_date - days * 86400
    settings = {'tagged': tag, 'fromdate': start_date, 'todate': final_date, 'site': 'stackoverflow.com'}
    url = 'https://api.stackexchange.com/2.3/questions'
    response = requests.get(url, params=settings)
    result = response.json()
    return len(result['items'])


print(get_questions('Python', 2))
