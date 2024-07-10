class Vehicle:
    def __init__(self,vehicle_id,make,model,year,category):
        self.vehicle_id=vehicle_id
        self.make=make
        self.model=model
        self.year=year
        self.category=category

class Rental_System:
    def __init__(self):
        self.list=[('100','Audi','100','1993','Sedan'),('101','FIAT','124Spider','2019','Convertible')]
        self.tuple=()
        self.dict={}

    def add_vehicle(self,vehicle_id,make,model,year,category):
        mytuple=(vehicle_id,make,model,year,category)
        myset=set(self.list)
        if mytuple not in myset:
            self.list.append(mytuple)
            myset=set(self.list)
        else:
          #  tuple=mytuple
            print('vehicle is aleady in data')
        return self.list

    def remove_vehicle(self,vehicle_id):
        for vehicle in self.list:
            if vehicle[0]==vehicle_id:
                self.list.remove(vehicle)
                break
        return self.list

    def search_vehicles(self,make_model):
        x=make_model
        output=[]
        for i in self.list:
            if x in i:
                output.append(i)
        return output

    def list_vehicles(self):
        print(self.list)

    def categorize_vehicles(self,category):
        x=category
        output=[]
        for i in self.list:
            if x in i:
                output.append(i)
        self.dict={
            category:output
        }
        print(self.dict)

rs = Rental_System()
next=''
while(next!='no'):
    ch=input("Enter choice(add,remove,search,list,categorize) vehicle:")
    if(ch == 'add vehicle'):
        vehicle_id=int(input('Enter id of vehicle:'))
        make=input('Enter make of vehicle:')
        model=input('Enter model of vehicle:')
        year=int(input('Enter year of vehicle:'))
        category=input('Enter category of vehicle:')
        print('vehicle added:',rs.add_vehicle(vehicle_id,make,model,year,category))
    elif(ch=='remove vehicle'):
        vehicle_id=int(input('Enter id of vehicle:'))
        print('After remove:',rs.remove_vehicle(vehicle_id))
    elif(ch=='search vehicle'):
        make_model=input('Enter make or model of vehicle:')
        print(rs.search_vehicles(make_model))
    elif(ch=='list vehicle'):
        rs.list_vehicles()
    elif(ch=='categorize vehicle'):
        category=input('Enter category of vehicle:')
        rs.categorize_vehicles(category)
    else :
        print('invalid choice')
    next=input('If you want to continue then yes else no:')