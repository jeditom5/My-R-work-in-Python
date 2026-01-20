import psutil, shutil, time
THRESHOLD = 100 * 1024 * 1024  # 100MB
def healthcheck():
    psutil.cpu_percent()
    time.sleep(1)
    while True:
        if(psutil.cpu_percent() > 80.0):
           ## TODO send email
           print('Error - CPU usage is over 80%')
        if(psutil.virtual_memory().available <= THRESHOLD):
            ## TODO send email
            print('Error - Available memory is less than 100MB')
        diskstats = shutil.disk_usage('~/supplier-data')
        if((diskstats.free/diskstats.total)*100.0 <= 20.0):
            ## TODO send email
            print('Error - Available disk space is less than 20%') 
        del diskstats  
        time.sleep(60)