def show_menu():
    print("===== Patient Manager =====")
    print("1. Add Patient")
    print("2. Show all patients")
    print("3. Exit")
    print('')

patients =[]
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        patient_name = input("Patient name: ")
        patient_age = int(input("Patient age: "))
        new_patient = {
            "name": patient_name,
            "age": patient_age
        }
        patients.append(new_patient)
        print("Patient added successfully!")
    elif choice == '2':
        print("Showing patients..")
        if not patients:
            print("No patients found.")
        else:
            for index,patient in enumerate(patients,1):
                print(f"{index}. {patient['name']} ({patient['age']} years)")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Enter a Valid number.")