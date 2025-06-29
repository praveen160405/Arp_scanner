##car_name = "bmw"
##car_model = "2020"
##string_f = f"{car_name} {car_model}"
##output_name = f"the car is {string_f}"
##print(output_name)


##var_1  = " praveen kumar  "
##var_1 = var_1.lstrip()
##print(var_1)


##udemy_url = "https://udemy.com"
##print(udemy_url.removeprefix("https://"))

##var_name = "this is checking\"s a code"   #forward slash
##print(var_name)

##my_var = 3   +   3.0
#print(my_var)


#a, b, c = 3,5,10
#print(a,b,c)


# to define list with []
#starts with 0 index
#car_value = [4,5,6,7]
#car_name = ["bmw","honda","hyundai","audi"]
#output_1 = (car_value)
#print(*output_1)      # *is used to avoid [] in output

# -1 in list[]
#car_value = [3,4,5,6]
#car_name = ["bmw","benz","honda","audi"]
#print(car_name[-1])            # -1 always return last item in the list


# f string
#car_value = [4,5,6,7]
#car_name = ["bmw","honda","hyundai","audi"]
#add_f = f"THE CAR NAME IS: {car_name[3].upper()} and the value is :{car_value[3]}"
#print(add_f)  


# insert append del a list item
#car_value = ["bmw","audi","benz"]
#car_value.append("honda")                    # car_value.insert(1,"honda") 
#print(*car_value)
#car_value.insert(3,"india")
#print(*car_value)
#del car_value[0]
#print(*car_value)
#car_value.remove("benz")
#print(*car_value)


#popped element means remove last element from the stack 
#car_name = ["honda","vw","benz"]
#popped_car = car_name.pop()
#print(car_name)
#print(popped_car)



# to save the sort in original string
#cars = ["audi","toyato","benz","vw"]
#cars.sort(reverse=True)
#print(*cars)



# temporarly stores in string and not change the value of original string
#cars = ["audi","toyato","benz","vw"]
#print(cars)
#print(sorted(cars))

#length
#cars = ["audi","bmw","benz"]
#output = len(cars)                   #len is a function
#print(output)


#revere a string
#cars = ["audi","bmw","benz"]
#cars.reverse()
#print(cars)


#for loop
#batsmans = ["abd","virat","gayle"]
#for cricket in batsmans:
#    print(f"THESE ARE THE BATSMANS : {cricket}")
#    print(f"{cricket} he is goat \n")


#for loop in range
#car_name = list(range(3,11,3))
#print(car_name)


#range
#for i in range(1,10):
#    print(i)

#for loop in range
#my_value = []
#for new_value in range(1,11):
#    update_value = new_value ** 2
#    my_value.append(update_value)
#print(my_value)    



#slice
#cars = ["audi","bmw","honda","benz"]
#print(*cars[0:2])
#print(*cars[0:])
#print(*cars[-4:])
#print(cars[:])            # [:] it makes a exact copy of list


#my_car = ["audi","bmw","honda","benz","hyundai","swift"]
#my_friendcar = my_car
#my_car.append("new")
#print(my_car)
#print(my_friendcar)



#my_value = []
#for value in range(1,22,2):
#   new_value = value /2
#    my_value.append(new_value)
#    print(my_value)


#my_value = [3]
#my_car = ["audi","bmw","honda"]
#if (my_value[0] < 2):              # to compare values in list tuple we use index
#    print("success")
#else:
#    print("failure")

#my_value = [3,5,7,11]
#for value in my_value:
#    if(value) < 10:
#        print("success")
#    else:
#        print("failure")
        

# def function
#def function(name):
#    update_name = name
#    if(update_name == name):
#        print("same name")
#    else:
#        print("no same")
#function('praveen')



#user input
#name = input("ENTER A NAME: ")                #input()
#print(name)


#def output_name(course_name = "cybrary" , course_no = 3):
#    output_course = course_name
#    output_no = course_no
#    print(f"the course name is :{output_course} \nthe course no is: {output_no}")
#output_name()


#def car_name(car_name1 , car_value):
#    one = car_name1
#    two = car_value
#    return one , two
  
#output = car_name("benz",4)
#print(output)



# creating class and object
#class car:                                    #class is defined
#    def __init__(self,car_name,car_year):    #self should be used when class is created      
#        self.car_name = car_name
#        self.car_year = car_year
#    def test(self,check):
#        print(check)
#        print(f"{self.car_name} {self.car_year}")
#class_var = car("bmw","2016")                        # class_var object is created
#class_var.test("checking")    





#class car:                                    #class is defined
#    def __init__(self,car_name,car_year):    #self should be used when class is created      
#        self.car_name = car_name
#        self.car_year = car_year
#        print(self.car_name)
#        print(self.car_year)
#    def test(self,check):
#        return check
#        print(f"{self.car_name} {self.car_year}")
#    def python_name(self):
#        print(f"{self.car_name}")
#class_var = car("bmw","2016")                        # class_var object is created
#check_name = class_var.test("checking")   
#print(check_name)
#class_var.python_name()



#class parent:
##       self.parent_age = parent_age
#class child(parent):
#    def do_this(self):
#        print(self.parent_name)
#class_var = parent("sivakumar","50")
#class_var1 = child("sivakumar","50")
#class_var1.do_this()



#reverse the words in sentence
#message = "this is a message for example"
#translation = ''
#message_length = len(message) - 1
#while message_length>=0:
#    translation = translation + message[message_length]
#    message_length = message_length-1

#print(translation)  # Output: 'olleh'

#reverse letters with strings
#vowels = "education"
#eliminate = "dctn"
#output = ''
#for new in vowels:
#    if(new not in eliminate):              
#        output = output + new              #strings are immutable so we use this
#print(output)
#reversed_output = output[::-1]            # [::-1] means [start,stop,method]  -1 reverse 1 forward
#print(reversed_output)



#reverse letters with list
#vowels = ["education"]
#eliminate = ["dctn"]
#output = ['']
#for new in vowels:
#    if(new not in eliminate):              #list are mutable so we append 
#       output.append(new)
#print(*output)
#reversed_output = output[::-1]            # [::-1] means [start,stop,method]  -1 reverse 1 forward
#print(*reversed_output)




#manipulating mac address
#sudo apt install net-tools
#sudo ifconfig eth0 down
#sudo ifconfig eth0 hw ether 00:11:22:55:33:BB
#sudo ifconfig eth0 up
#sudo ifconfig


#import subprocess
#subprocess.run(["ipconfig"], shell=True)                   # shows ip details for windows




#import subprocess                                                         #subprocess means use tor run shell commands
#if __name__ == "__main__": 
#    interface = "eth0"
#     new_mac = "22:00:11:aa:bb:cc"
#subprocess.run(["ifconfig",interface,"down"])                             #interface means wired network
#print(f"changing mac address:{interface} to new mac:{new_mac}")
#subprocess.run(["ifconfig",interface,"hw","ether",new_mac])               #hw means hardware ,ether means ethernet
#print(f"the ifconfig is up :{interface}")
#subprocess.run(["ifconfig",interface,"up"])



#changing ip address
#import subprocess
#interface = "eth0"
#ip_new = "192.168.1.0"
#subprocess.run(["ipconfig",interface,"down"])
#subprocess.run(["ipconfig",interface,ip_new,"netmask","255.255.255.0"])
#subprocess.run(["ipconfig","interface",up"])



from scapy.all import ARP, Ether, srp                   # srp-->  send recive packets 
def scan_networks(ip_range):  
    arp = ARP(pdst=ip_range)                            #pdst --> target ip
    ether_broadcast = Ether(dst="FF:FF:FF:FF:FF:FF")    #dst --> destination 
    send_packet = ether_broadcast / arp
    output = srp(send_packet, timeout=1, verbose=0)[0]
    devices = []
    for sent,received in output:
       devices.append({'ip': received.psrc, 'mac': received.hwsrc})     #psrc--> recievers  ip for arp request it is build in function
    return devices                                                      #hwsrc-->recievers  mac for arp request it is build in function
        
final_result = scan_networks("192.168.1.0/24")














        





        




