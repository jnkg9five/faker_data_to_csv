#Python program to use faker lib to generated fake data and then store in csv file with field columns.

from faker import Faker
import csv

def fill_data_csv(data, filename="user_data.csv"):
    #Create specified header
    header = ['Name','Phone','Email','Job','Company']

    #Write to csv file
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        #Populate the header if file is empty
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

def gen_rand_data(fake, size):
    #generate random data user faker lib
    name = fake.name() 
    phone_number = fake.phone_number()
    email = fake.email()
    job = fake.job()
    company = fake.company() 
    
    #print("Dataset Index: ", size)

    #print random generated data to output
    #print("Name: ", name)
    #print("Phone Number: ", phone_number)
    #print("Email: ", email)
    #print("Job: ", job)    
    #print("Company: ", company)

    return {'Name': name, 'Phone': phone_number, 'Email': email, 'Job': job, 'Company': company}

def main():
    #make faker instance
    fake = Faker()

    #take in value of the data set size to store in csv
    set_size = int(input("What is the data set size to be generated? "))

    for size in range(set_size):
        rand_data = gen_rand_data(fake, size)   
        fill_data_csv(rand_data)

    print("Generated data has been written into user_data.csv with header.")

if __name__ == "__main__":
    main()    