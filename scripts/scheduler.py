#!/bin/python

import schedule
import time
import os

def job_b1_1():
    os.system('/etc/nmon-logger/bin/nmon_helper.sh /etc/nmon-logger /var/log/nmon-logger 2>&1 | /etc/nmon-logger/bin/hec_wrapper.sh /var/log/nmon-logger/nmon_collect.log nmon_collect collect:http')
    print 'collect started'

def job_b1_2():
    os.system('/etc/nmon-logger/bin/fifo_consumer.sh 2>&1 | /etc/nmon-logger/bin/hec_wrapper.sh /var/log/nmon-logger/nmon_processing.log nmon_processing processing:http')
    print 'consumer started'

def job_b2():
    os.system('/etc/nmon-logger/bin/nmon_cleaner.sh /etc/nmon-logger /var/log/nmon-logger 2>&1 | /etc/nmon-logger/bin/hec_wrapper.sh /var/log/nmon-logger/nmon_clean.log nmon_clean clean:http')
    print 'cleaner started'

schedule.every().minute.do(job_b1_1)
schedule.every().minute.do(job_b1_2)
schedule.every(4).hours.do(job_b2)

while 1: 
    schedule.run_pending()
    time.sleep(1)
