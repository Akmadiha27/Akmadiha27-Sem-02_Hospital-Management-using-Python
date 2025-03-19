class Hospital:
    def __init__(self, name, city, beds, price, rating, reviews):
        self.name = name
        self.city = city
        self.beds = beds
        self.price = price
        self.rating = rating
        self.reviews = reviews

    def display(self):
        print(f"\nHospital Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Total Beds: {self.beds}")
        print(f"Price per Bed: ${self.price:.2f}")
        print(f"Rating: {self.rating}")
        print(f"Reviews: {self.reviews}\n")


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Patient Name: {self.name}, Age: {self.age}")


def sort_by_price(hospitals):
    return sorted(hospitals, key=lambda x: x.price)


def sort_by_name(hospitals):
    return sorted(hospitals, key=lambda x: x.name)


def sort_by_rating(hospitals):
    return sorted(hospitals, key=lambda x: x.rating * x.reviews, reverse=True)


def sort_by_beds(hospitals):
    return sorted(hospitals, key=lambda x: x.beds, reverse=True)


def hospitals_in_city(hospitals, city):
    found = [h for h in hospitals if h.city.lower() == city.lower()]
    if not found:
        print(f"No hospitals found in {city}")
    for h in found:
        h.display()


# Sample hospital data
hospitals = [
    Hospital("Hospital A", "X", 100, 250.0, 4.5, 100),
    Hospital("Hospital B", "Y", 150, 200.0, 4.2, 80),
    Hospital("Hospital C", "X", 200, 180.0, 4.0, 120),
    Hospital("Hospital D", "Z", 80, 300.0, 4.8, 90),
    Hospital("Hospital E", "Y", 120, 220.0, 4.6, 110),
]

# Sample patient data
patients = {
    "Hospital A": [Patient("Amar", 35), Patient("Manish", 45), Patient("Atul", 28)],
    "Hospital B": [Patient("Elvish", 62), Patient("Debolina", 18), Patient("Shruti", 55)],
    "Hospital C": [Patient("Zafar", 50), Patient("Rahul", 30), Patient("Priya", 40)],
    "Hospital D": [Patient("Amir", 22), Patient("Asif", 38), Patient("Prince", 60)],
    "Hospital E": [Patient("Aditya", 28), Patient("Aman", 48), Patient("Sahil", 33)],
}

while True:
    print("\n*********** Hospital Management System Menu ***********")
    print("1. Display All Hospital Data")
    print("2. Display Patients Data")
    print("3. Sort Hospitals by Bed Price (Ascending)")
    print("4. Sort Hospitals by Available Beds (Descending)")
    print("5. Sort Hospitals by Name (Ascending)")
    print("6. Sort Hospitals by Rating and Reviews (Descending)")
    print("7. Display Hospitals in a Specific City")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for h in hospitals:
            h.display()

    elif choice == "2":
        for hospital, patient_list in patients.items():
            print(f"\nPatients in {hospital}:")
            for p in patient_list:
                p.display()

    elif choice == "3":
        sorted_hospitals = sort_by_price(hospitals)
        print("\nHospitals sorted by price (Ascending):")
        for h in sorted_hospitals:
            h.display()

    elif choice == "4":
        sorted_hospitals = sort_by_beds(hospitals)
        print("\nHospitals sorted by available beds (Descending):")
        for h in sorted_hospitals:
            h.display()

    elif choice == "5":
        sorted_hospitals = sort_by_name(hospitals)
        print("\nHospitals sorted by name (Ascending):")
        for h in sorted_hospitals:
            h.display()

    elif choice == "6":
        sorted_hospitals = sort_by_rating(hospitals)
        print("\nHospitals sorted by rating and reviews (Descending):")
        for h in sorted_hospitals:
            h.display()

    elif choice == "7":
        city = input("Enter city name: ")
        hospitals_in_city(hospitals, city)

    elif choice == "8":
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
