# My First Program

def show_menu():
    print("===== Patient Manager =====")
    print("1. Add Patient")
    print("2. Show all patients")
    print("3. Update patients")
    print("4. Delete Patient")
    print("5. Exit")
    print('')

def add_patient(patients):       
    patient_name = input("Patient name: ")
    try:
        patient_age = int(input("Patient age: "))
    except ValueError:
        print("Please enter a valid age!!")
        return
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
    try:
        del_patient_nu = int(input("Enter patient number to delete: "))
    except ValueError:
        print("Invalid Entry!!")
        return
    if del_patient_nu < 1 or del_patient_nu > len(patients):
        print("Invalid Number.") 
    else:
        print(f"{patients[del_patient_nu-1]['name']} deleted successfully!")
        del(patients[del_patient_nu-1])

def update_patient(patients):
    if not patients:
        print("No patients found!")
        return
    for index,patient in enumerate(patients,1):
        print(f"{index}. {patient['name']} ({patient['age']} years)")
        
    try:
        update_patient_nu = int(input("Enter patient number to update: ")) 
    except ValueError:
        print("Invalid Entry.")
        return
    if update_patient_nu < 1 or update_patient_nu > len(patients):
        print("Invalid Number.") 
        return
    patient_index = update_patient_nu -1
    new_name = input("New name: ")
    while True:
        try:
            new_age = int(input("New age: "))
        except ValueError:
            print("Invalid Entry.")
        else:
            break    
            
    patients[patient_index]["name"] = new_name
    patients[patient_index]["age"] = new_age
    print("\n")
    print("Patient Updated Successfully!")
    return



patients =[]
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        add_patient(patients)
        
    elif choice == '2':
        show_patients(patients)

    elif choice =='3':
            update_patient(patients)
        
    elif choice =='4':
        delete_patient(patients)    

    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Enter a Valid number.")