import csv

def main():
    info = get_info()
    save_to_csv(info)
    print(f"Name: {info['name']} \nAge: {info['age']} \nContact: {info['contact']}", end='')


def get_info():
    info = {}
    info["name"] = input("Name: ")
    info["age"] = int(input("Age: "))
    info["contact"] = input("Contact Details: ")
    return info


def save_to_csv(info):
    with open("info_organizer.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([info["name"], info["age"], info["contact"]])


if __name__ == "__main__":
    main()
