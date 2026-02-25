import os
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "titanic.csv")

df = pd.read_csv(file_path)

def run_query(question: str):
    question = question.lower()

    # 1️⃣ Percentage of male passengers
    if "percentage" in question and "male" in question:
        total = len(df)
        males = len(df[df["Sex"] == "male"])
        percentage = (males / total) * 100
        return f"Approximately {percentage:.2f}% of passengers were male."

    # 2️⃣ Histogram of passenger ages
    elif "histogram" in question and "age" in question:
        plt.figure()
        df["Age"].dropna().hist(bins=20)
        plt.xlabel("Age")
        plt.ylabel("Count")
        plt.title("Histogram of Passenger Ages")

        image_path = os.path.join(BASE_DIR, "age_histogram.png")
        plt.savefig(image_path)
        plt.close()

        return {
            "text": "Here is the histogram of passenger ages.",
            "image": image_path
        }

    # 3️⃣ Average ticket fare
    elif "average" in question and "fare" in question:
        avg_fare = df["Fare"].mean()
        return f"The average ticket fare was {avg_fare:.2f}."

    # 4️⃣ Embarked port count
    elif "embark" in question:
        counts = df["Embarked"].value_counts()
        return counts.to_string()

    else:
        return "Sorry, I can only answer questions about age, fare, gender percentage, and embarkation."