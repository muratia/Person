# coding=utf8
# importing of mysql interface and renaming it as mariadb
import mysql.connector as mariadb 
    

# Class Person
class Person():
    cursor = 0; # global variable database cursor
    sleeping = 0; #global variable that stores sleep state
    
    mariadb_connection = 0; # declaration of global variable to store the database conectivity
    
    def __init__(self): # class constructor
        self.sleeping = 0; # resetting of the awake state
        self.personalID = ""; # incialization of the variable
        self.employeeName = "";# incialization of the variable
        self.employeeJobDescription = "";# incialization of the variable
        self.employeeAddress = "";# incialization of the variable
        self.employeeCity = "";# incialization of the variable
        self.employeePhone = "";# incialization of the variable
        
    # Full construktor
    def __init__(self,  personalID= None, employeeName= None, employeeJobDescription= None, employeeAddress= None, employeeCity= None, employeePhone= None): 
        self.personalID = personalID; # passing value 
        self.employeeName = employeeName;#passing value 
        self.employeeJobDescription = employeeJobDescription;#passing value 
        self.employeeAddress = employeeAddress;#passing value 
        self.employeeCity = employeeCity;#passing value 
        self.employeePhone = employeePhone;#passing value 
        self.mariadb_connection = mariadb.connect(user='root', password='', database='flowershop'); # instatiation of the database connectivity 
        self.cursor = self.mariadb_connection.cursor(); # instatiation of the cursor and storing it on the global variable


    def insert(self): # helper method to store the data into the database
        try: # trying to execute the query
       
            self.cursor.execute("INSERT INTO employee(  "+
            " personalID, "+
            "employeeName, "+
            "employeeJobDescription,"+
            " employeeAddress, "+
            "employeeCity, "+
            "employeePhone) VALUES (%s, %s, %s, %s, %s, %s)", (
            self.personalID, 
            self.employeeName, 
            self.employeeJobDescription, 
            self.employeeAddress, 
            self.employeeCity, 
            self.employeePhone));
            self.mariadb_connection.commit(); # usually auto_commit is inactive and it is need to do committting
            print("Data are stored perfectly.");
        except ValueError:
            self.mariadb_connection.rollback(); # if there is a problem transaction fails
            print("Data are not stored.");
        return  ; 
    
    def sleep(self): # metod to start sleeping
        if(self.sleeping == 0): # checking if the person is awake
            print("Person " + self.employeeName + " is sleeping"); 
            self.sleeping = 1; # it set th value of self.sleeping implying that the person is sleeping
        else:# else
            print("Person " + self.employeeName + " is already sleeping"); 
        return;
    
    def wakeup(self):# Method to start waking up
        if(self.sleeping == 1): # it checks if the person is sleeping
            self.sleeping = 0;  # it set th value of self.sleeping implying that the person is awake
            print("Person " + self.employeeName + " is awake."); 
        else:# përndryshe
            print("Person " + self.employeeName + " is not sleeping to be woken up");
    
    def walk(self): # Method to walking
        if(self.sleeping == 0):# it checks if the person is awake
            print("Person " + self.employeeName + " is walking"); 
        else:# else
            print("Person " + self.employeeName + " can't walk he is sleeping");
        return;
    
    def run (self):# Method to start running 
        if(self.sleeping == 0):#  it checks if the person is awake
            print("Person " + self.employeeName + " is running"); 
        else:# përndryshe
            print("Person " + self.employeeName + " can't run he is sleeping");
        return;
        
# initialization of the variable p with the Person class instance
p = Person(employeeName="Ahmet");
#p.employeeName = "Ahmet"; # setting of the name
 

p.sleep(); 
p.walk();
p.wakeup();
p.walk();
p.run();
