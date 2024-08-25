#Python program to use faker lib to generated fake data and then store in csv file with field columns.

from faker import Faker
import csv

def gen_rand_data(fake, size):
    #generate random data user faker lib
    name = fake.name() 
    phone_number = fake.phone_number()
    email = fake.email()
    job = fake.job()
    company = fake.company() 
    
    #print("Dataset Index: ", size) Debug print segment

    #print random generated data to output
    #print("Name: ", name)
    #print("Phone Number: ", phone_number)
    #print("Email: ", email)
    #print("Job: ", job)    
    #print("Company: ", company)

    return {'Name': name, 'Phone': phone_number, 'Email': email, 'Job': job, 'Company': company} #return these values to be used at sort_key

def fill_data_csv(data, filename):
    #Create specified header
    header = ['Name','Phone','Email','Job','Company']

    #Write to csv file
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        #Populate the header if file is empty
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

def sort_csv(filename, sort_key, reverse=False):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        
    #Sort data by the key used sorted method
    sort_data = sorted(data, key=lambda x: x[sort_key], reverse=reverse)

    #Write sorted data to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(sort_data)

def main():
    #make faker instance
    fake = Faker()

    #take in value of the data set size to store in csv
    set_size = int(input("What is the data set size to be generated? "))
    name_csv = str(input("Name the output csv file: "))

    for size in range(set_size):
        rand_data = gen_rand_data(fake, size)   
        fill_data_csv(rand_data, name_csv)

    sort_csv(name_csv, sort_key='Name') #sort alphabetically by name

    print("Generated data has been written into user_data.csv with header.")

if __name__ == "__main__":
    main()    