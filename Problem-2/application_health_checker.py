import requests
import logging
from datetime import datetime

logging.basicConfig(filename='application_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = 'http://wisecom.com'  
UP_STATUS_CODES = [200] 

def check_application_health():
    try:
        response = requests.get(URL)
        if response.status_code in UP_STATUS_CODES:
            logging.info(f'Application is UP. Status code: {response.status_code}')
            return 'UP'
        else:
            logging.warning(f'Application is DOWN. Status code: {response.status_code}')
            return 'DOWN'
    except requests.exceptions.RequestException as e:
        logging.error(f'Error checking application health: {e}')
        return 'DOWN'

def main():
    status = check_application_health()
    print(f'Application status: {status}')

if __name__ == '__main__':
    main()
