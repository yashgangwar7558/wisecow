import psutil
import logging
from datetime import datetime

logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 80.0

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_running_processes():
    processes = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name'])]
    return processes

def main():
    cpu_usage = check_cpu_usage()
    processes = check_running_processes()

    logging.info(f'CPU Usage: {cpu_usage}%')
    logging.info(f'Running Processes: {len(processes)}')

if __name__ == '__main__':
    main()
