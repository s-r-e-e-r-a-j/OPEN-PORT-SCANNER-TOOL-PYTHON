import socket 
print("################################")
print("################################")
print("OPEN PORT SCANNER TOOL")
print("################################")
print("################################")
print("")
print("") 
target_ip = input("Enter the ip address: ")
startport=int(input("Enter the start port: "))
endport=int(input("Enter the end port: ")) 
result_array=[]
print("") 
print(f"scanning {target_ip} from {startport} to {endport}")
print("")
for port in range(startport,endport+1):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result=sock.connect_ex((target_ip,port))
    if result == 0:
       print(f"port {port} is open")
       result_array.append(port)
    else: 
         print(f"port {port} is closed")
    sock.close() 
print("") 
print("")
i=0 
arraylength=len(result_array)
print("scan complete")
print("") 
print("Open Ports:")
while i < arraylength:
      print(result_array[i]) 
      i+=1
