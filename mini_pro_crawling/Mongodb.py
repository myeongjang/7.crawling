from pymongo import MongoClient # python, mongodb를 연동하기 위해서 bind

# creating connectioons for communicating with Mongo DB

client = MongoClient('localhost:27017') # 내컴퓨터 로컬호스트에 27017 포트와 연결
db = client.EmployeeData # db생성
collection = db.Employees # 테이블 생성 
db = client.get_database('EmployeeData') # 데이터베이스 선택
collection = db.get_collection('Employees') # 테이블 선택

# Function to insert data into mongo db
def insert():
    try:
        employeeId = input('Enter Employee id :')
        employeeName = input('Enter Name :')
        employeeAge = input('Enter age :')
        employeeCountry = input('Enter Country :')
        
        db.Employees.insert_one(
            {
                "id": employeeId,
                "name":employeeName,
                "age":employeeAge,
                "country":employeeCountry
        })
        print('\nInserted data successfully\n')
    
    except Exception as e:
        print(str(e))

# function to read records from mongo db
def read():
    try:
        empCol = db.Employees.find()
        print('\n All data from EmployeeData Database \n')
        for emp in empCol:
            print(emp)

    except Exception as e:
        print(str(e))

# Function to update record to mongo db
def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')

        db.Employees.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name":name,
                    "age":age,
                    "country":country
                }
            }
        )
        print("\nRecords updated successfully\n") 
    
    except Exception as e:
        print(str(e))

# Function to delete record from mongo db
def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id":criteria})
        print('\nDeletion successful\n')
    except Exception as e:
        print(str(e))

#def main():
if __name__ == "__main__":
    while(1):
    # chossing option to do CRUD operations
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete, 5 exit\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        elif selection == '5':
            exit(0)
        else:
