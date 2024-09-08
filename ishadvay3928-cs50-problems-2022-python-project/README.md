# Medical Diagnosis System

#### Video Demo: <https://youtu.be/DOx4C3oXwBw>

#### Description:
The Medical Diagnosis System is a simple Python program that allows users to diagnose diseases based on symptoms and calculate the age of patients using their birthdate. The program takes input from a CSV file containing patient information, including symptoms and birthdate, and outputs the diagnosis results to another CSV file.

## Features
- Read patient data from a CSV file.
- Diagnose diseases based on symptoms.
- Calculate patient age using birthdate.
- Write diagnosis results to a CSV file.

## Installation
1. Clone the repository: `git clone [repository_url]`
2. Navigate to the project directory: `cd medical-diagnosis-system`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Prepare a CSV file with patient information, including symptoms and birthdate.
2. Run the program with the following command: `python main.py input_file.csv output_file.csv`
   - Replace `input_file.csv` with the path to your input CSV file.
   - Replace `output_file.csv` with the desired name and path for the output CSV file.
3. The program will diagnose the diseases based on the symptoms and calculate the patient's age.
4. The diagnosis results, including the patient's name, disease, and age, will be written to the output CSV file.

## Example
Suppose we have an input CSV file named `patients.csv` with the following structure:

| name   | symptoms              | birthdate |
|--------|-----------------------|-----------|
| John   | fever, headache       | 1990      |
| Emily  | cough, fatigue        | 1985      |
| Sarah  | nausea, vomiting, fever | 2002      |

To run the program and generate the diagnosis results, use the following command:

```
python main.py patients.csv diagnosis_results.csv
```

The program will diagnose the diseases based on the symptoms and calculate the ages of the patients. The diagnosis results will be written to the `diagnosis_results.csv` file.

## Testing
The code includes a set of unit tests to ensure the correctness of some functions. The tests are implemented using the pytest framework. To run the tests, use the following command:

```
pytest test.py
```

## Contributions
Contributions to the Medical Diagnosis System are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).