# My First Program

def show_menu():
    print("===== Patient Manager =====")
    print("1. Add Patient")
    print("2. Show all patients")
    print("3. Delete Patient")
    print("4. Exit")
    print('')

def add_patient(patients):       
    patient_name = input("Patient name: ")
    patient_age = int(input("Patient age: "))
    new_patient = {
        "name": patient_name,
        "age": patient_age
        }
    patients.append(new_patient)
    print("Patient added successfully!")

def show_patients(patients):
    print("Showing patients..")
    if not patients:
        print("No patients found.")
    else:
        for index,patient in enumerate(patients,1):
            print(f"{index}. {patient['name']} ({patient['age']} years)")
    
def delete_patient(patients):
    for index,patient in enumerate(patients,1):
        print(f"{index}. {patient['name']} ({patient['age']} years)")      
    del_patient_nu = int(input("Enter patient number to delete: "))
    if del_patient_nu < 1 or del_patient_nu > len(patients):
        print("Invalid Number.") 
    else:
        print(f"{patients[del_patient_nu-1]['name']} deleted successfully!")
        del(patients[del_patient_nu-1])

patients =[]
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        add_patient(patients)
        
    elif choice == '2':
        show_patients(patients)
        
    elif choice =='3':
        delete_patient(patients)    

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Enter a Valid number.")