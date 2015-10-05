#!/usr/bin/python

import sys,httplib,time, threading

hostname = sys.argv[1]
sample_file_path = sys.argv[2]

print hostname
print sample_file_path

sample_file = open(sample_file_path,'w')
sample_file.write("URL="+hostname)

# def executeSomething():
#     current_time = time.time()
#     conn = httplib.HTTPConnection(hostname, 80)
#     conn.request("GET", "/")
#     r1 = conn.getresponse()
#     print r1.status
#     print int(current_time)
#     time.sleep(30)

# while True:
#     executeSomething()

def f():
    # do something here ...
    try:
    	current_time = time.time()
    	conn = httplib.HTTPConnection(hostname, 80)
    	conn.request("GET", "/")
    	r1 = conn.getresponse()
    	print r1.status
    	print int(current_time)
    except:
    	print "error"


    # call f() again in 30 seconds
    threading.Timer(30, f).start()

# start calling f now and every 60 sec thereafter
f()