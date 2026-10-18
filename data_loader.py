import csv
import numpy as np

def load_data(path):
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        grade_cols = ["math",  "physics", "english"]
        records = []
        for row in reader:
            for subject in grade_cols:
                try:
                    row[subject] = float(row[subject])
                except (ValueError, TypeError):
                    row[subject] = None

            records.append(row)

        return records


def fill_missing(records, subject):
    values = [record[subject] for record in records if record[subject] is not None]

    mean_val = np.mean(np.array(values))
    for record in records:
        if record[subject] is None:
            record[subject] = mean_val

    return records

def remove_bad_records(records):
    grade_cols = ["math",  "physics", "english"]
    valid_records = []
    for record in records:
        invalid = False
        for subject in grade_cols:
            if record[subject] is None:
                invalid = True
                break

        if not invalid:
            valid_records.append(record)

    return valid_records


def remove_duplicates(records):
    unique_records = []

    for record in records:
        if record not in unique_records:
            unique_records.append(record)

    return unique_records

if __name__ == "__main__":
    records = load_data("data/students.csv")
    records = fill_missing(records, "physics")
    records = remove_bad_records(records)
    records = remove_duplicates(records)
    print(len(records))
    print(records)