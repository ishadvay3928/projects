import sys
import csv

def main():
    check_correct_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
       sys.exit("CSV file not found")

    output = []
    for row in data:
        disease = diagnose_disease(row["symptoms"])
        age = find_age(row["birthdate"])
        output.append({"name":row["name"], "disease": disease, "age": age})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames =["name", "disease","age"])
        writer.writerow({"name":"name", "disease": "disease","age": "age"})
        for row in output:
           writer.writerow({"name": row["name"], "disease": row["disease"],"age": row["age"]})


def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit("too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV files")


def diagnose_disease(char):
    if char in ["cold","cough","chills"]:
        return "Flu"
    elif char in ["fever","fatigue","sweating"]:
        return "Malaria"
    elif char in ["nausea","vomiting","rashes"]:
        return "Dengue"
    elif char in ["headache","dizziness","nasal congestion"]:
        return "Migraine"
    else:
        return "No Disease"


def find_age(year):
    age = 2022 - int(year)
    return "Age " + str(age)


if __name__ == "__main__":
    main()