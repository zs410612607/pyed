import time

def master_mainloop(pesys):
    log = pesys.log
    while 1:
        log.logError("Master", "Master mainloop in master_mainloop")
        time.sleep(1)