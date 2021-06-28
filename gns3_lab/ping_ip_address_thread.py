# import concurrent.futures
# import urllib.request

# URLS = ['http://www.foxnews.com/',
#         'http://www.cnn.com/',
#         'http://europe.wsj.com/',
#         'http://www.bbc.co.uk/',
#         'http://some-made-up-domain.com/']

# # Retrieve a single page and report the URL and contents
# def load_url(url, timeout):
#     with urllib.request.urlopen(url, timeout=timeout) as conn:
#         return conn.read()

# # We can use a with statement to ensure threads are cleaned up promptly
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     # Start the load operations and mark each future with its URL
#     future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
#     for future in concurrent.futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         try:
#             data = future.result()
#         except Exception as exc:
#             print('%r generated an exception: %s' % (url, exc))
#         else:
#             print('%r page is %d bytes' % (url, len(data)))





import concurrent.futures
import os
from  datetime import datetime
start_time = datetime.now()
ip_add_list = ['192.168.1.200', '192.168.1.201', '192.168.1.202', 
                '192.168.1.205', '192.168.1.208', '10.1.1.1']

#ping function for threadpoolexecutor submit function
def ping_result(ip,command):


    result = os.system(command +" " + ip + " -n 1")
 #   print (result)
    if result ==0:
        ping_re = 'ping successful'
    else:
        ping_re = 'ping failed'
    return ping_re
#ping function for threadpoolexecutor map function
def ping_result_map(ip):


    result = os.system('ping' +" " + ip + " -n 1")
 #   print (result)
    if result ==0:
        ping_re = 'ping successful'
    else:
        ping_re = 'ping failed'
    return ping_re
    
#threadpoolexecutor submit function example
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
  
    
    future_result ={executor.submit(ping_result, list, 'ping'): list for list in ip_add_list } 
    # print (type(result))
    # print (result)
    # future_result = {}
    # for list in ip_add_list:
    #     future_result = {executor.submit(ping_result, list, 'ping')}
    #     #print (fu_list)
    # print (future_result)

    for f in concurrent.futures.as_completed(future_result):
        print (future_result)
        ip  = future_result[f]
        data = f.result()
        print (ip)
        print (data)
    
print (datetime.now() - start_time)

##threadpoolexecutor map function example
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    
    map_result =executor.map(ping_result_map, ip_add_list)
    for list, output in zip(ip_add_list,map_result):
        print (list,output)
        





