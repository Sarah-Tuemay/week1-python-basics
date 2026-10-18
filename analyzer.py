import numpy as np
import data_loader


def get_scores(records):
    subjects = ['math', 'physics', 'english']
    arr = []
    for record in records:
        person = []

        for sub in subjects:
            person.append(record[sub])

        arr.append(person)

    return np.array(arr)


def subject_averages(scores):
    return scores.mean(axis=0)


def top_student(records,scores):
    idx = scores.mean(axis=1).argmax()
    return records[idx]["name"]


def pass_rate(scores, threshold = 50):
    avg = scores.mean(axis=1)
    avg = avg[avg >= threshold]

    return float((len(avg)/len(scores)) * 100)


if __name__ == "__main__":
    records = data_loader.load_clean_data("data/students.csv")
    scores = get_scores(records)
    avg = pass_rate(scores, 85)
    print(f"Top student: {top_student(records, scores)}")
    print(avg)
    print(subject_averages(scores))

