#!/usr/bin/python

import sys,httplib,time, threading

hostname = sys.argv[1]
sample_file_path = sys.argv[2]

print hostname
print sample_file_path

sample_file = open(sample_file_path,'w')
sample_file.write("URL="+hostname+'\n')

def prober_function():
    # thread setup to repeat function every 30 seconds
    t = threading.Timer(30, prober_function)
    t.daemon = True
    t.start()

    # instructions to execute
    current_time = time.time()
    input_line = '' + str(int(current_time)) + ','
    try:
    	conn = httplib.HTTPConnection(hostname, 80, timeout=30)
    	conn.request("GET", "/")
        r1 = conn.getresponse()
    	input_line +=  str(r1.status)
    except:
        input_line +=  '-1'
    sample_file.write(input_line+'\n')
    sample_file.flush()
    print "."
    

# start calling function now and every 30 sec 
print "Prober running..."
prober_function()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sample_file.close()
    print ' - Prober Closed'