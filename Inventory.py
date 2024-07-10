import datetime

class Product:
  def init(self,name,category,price,quantity,expiration_date):
    self.name=name
    self.category=category
    self.price=price
    self.quantity=quantity
    self.expiration_date=datetime.datetime.strptime(expiration_date, '%d/%m/%Y').date()

  def get_expiration_date(self):
    return self.expiration_date

  def expired_product(self):
    today = datetime.date.today()
    expired_products = []
    for product in self.list:
      expiration_date_str = product[4]
      edate = datetime.datetime.strptime(expiration_date_str, '%d/%m/%Y').date()
      if edate < today:
        expired_products.append(product)
    return expired_products

  list=[
      ('Cheese','Dairy','120','70','10/06/2024'),
      ('Onion','vegetable','40','50','16/12/2024'),
      ('Milk','Dairy','75','20','15/09/2024')
       ]

  def add_product_to_inventory(self,name,category,price,quantity,expiration_date):
    mytuple=(name,category,price,quantity,expiration_date)
    self.myset=set(self.list)
    if mytuple not in self.myset:
      self.list.append(mytuple)
      self.myset=set(self.list)
    else:
      print('product is already in data')
    return self.myset

  def remove_product_from_inventory(self,name):
    for product in self.list:
            if product[0]==name:
                self.list.remove(product)
                break
    return self.list

  def search_products(self,name_category):
    x=name_category
    output=[]
    for i in self.list:
      if x in i:
        output.append(i)
    return output

  def list_all_products(self):
    return self.list

  def categorize_products(self,category):
    x=category
    output=[]
    for i in self.list:
      if x in i:
        output.append(i)
      self.dict={
            category:output
        }
      return self.dict

  def check_expired_products(self):
    expired_products = self.expired_product()
    if expired_products:
      print('Expired products:')
      for product in expired_products:
        print(f'{product[0]} - Expired on: {product[4]}')
        self.list.remove(product)
    else:
      print('No expired products found')

  def save_inventory(self,file_name):
    try:
      with open(file_name, 'w') as file:
          for product in self.list:
            file.write(f"{product[0]},{product[1]},{product[2]},{product[3]},{product[4]}\n")
    except IOError:
      print(f"Error: Could not write to file {file_name}")

  def load_inventory(self,file_name):
    try:
      with open(file_name, 'r') as file:
        for line in file:
          name, category, price, quantity, expdate = line.strip().split(',')
          product = (name, category, float(price), int(quantity), datetime.datetime.strptime(expdate, '%d/%m/%Y').date())
          self.list.append(product)
    except IOError:
      print(f"Error: Could not read file {file_name}")

p=Product()
next=''
while(next!='no'):
  ch=input('Enter choice(add,remove,search,list,category,expired)item/(save,load)inventory:')
  if(ch=='add item'):
    name=input('Enter name of product:')
    category=input('Enter category of product:')
    price=int(input('Enter price of product:'))
    quantity=int(input('Enter quantity of product:'))
    expiration_date=input('Enter expiration date of product:')
    print('Product added:',p.add_product_to_inventory(name,category,price,quantity,expiration_date))
  elif(ch=='remove item'):
    name=input('Enter name of product:')
    print('After remove:',p.remove_product_from_inventory(name))
  elif(ch=='search item'):
    name_category=input('Enter name or category of product:')
    print(p.search_products(name_category))
  elif(ch=='list item'):
    print(p.list_all_products())
  elif(ch=='category item'):
    category=input('Enter category of product:')
    print(p.categorize_products(category))
  elif(ch=='expired item'):
    p.check_expired_products()
    print('After removed expired product:',p.list_all_products())
  elif(ch=='save inventory'):
    file_name = input("Enter file name to save inventory: ")
    p.save_inventory(file_name)
    print("Inventory saved successfully.")
  elif(ch=='load inventory'):
    file_name = input("Enter file name to load inventory: ")
    p.load_inventory(file_name)
    print("Inventory loaded successfully.")
  else:
    print('Invalid choice')
  next=input('If you want to continue the yes else no:')

