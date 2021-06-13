import netmiko
import csv
new_row = []
rowlsrc = []
rowldst = []



#below is the sample script for how to covert list to csv file
# data = [
#     ['Dan', 42],
#     ['Cordelia', 33],
#     ['Sammy', 52]
# ]


# with open('outputdata.csv', 'w') as outfile:
#     mywriter = csv.writer(outfile)
#     # manually add header

#     mywriter.writerow(['name', 'age'])
#     for d in data:
#         mywriter.writerow(d)

cisco_device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.201",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    "port": 22
}
new_row = []
rowls =[]
wordls =[]
net_connect = netmiko.ConnectHandler(**cisco_device)
net_connect.enable()
output = net_connect.send_command("show ip accounting")
print (type(output))
with open('ip_accounting.txt','wt') as file:
    file.write(output +'\n')



with open('ip_accounting.txt','rt') as file:
    for line in file:
        for wordls in line.split('         '):
            
                new_row.append(wordls)
                if len(new_row) > 2:
                    if '\n' in new_row[-1]:
                        rowlsrc.append(new_row[0])
                        rowldst.append(new_row[1])
                        print (rowlsrc,rowldst)
                        print ("start new row")
                        new_row.clear()
i = 0
with open("ip_accountings.csv",'w') as outfile:
    write = csv.writer(outfile)
    while i < len(rowldst):
        write.writerow([rowlsrc[i],rowldst[i]])
        i =i+1

                
                
                
                