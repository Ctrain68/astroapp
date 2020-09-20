from datetime import datetime 
import socket
import json
import urllib.request

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

# print(local_ip)

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print(external_ip)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# class Api_location:
#     def __init__(self, url):
#         pass
    
#     def get_word_from_api(self, ):
#         request = 
        
   
    
    
# class File_handler:
#      def write_word_to_file(....):
         
# class Word:
#     def ...
    
    
# main:
#     user input?
    
# if:
#     get_word_from_api
#     write word to file:
# # else:
#     find_wird_in_fi