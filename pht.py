import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class HealthTracker:
    def __init__(self):
        self.user_data = {}

    def create_profile(self):
        # Get user information (e.g., name, age, height, weight)
        self.user_data['name'] = input("Enter your name: ")
        self.user_data['age'] = int(input("Enter your age: "))
        self.user_data['height'] = float(input("Enter your height (in cm): "))
        self.user_data['weight'] = float(input("Enter your weight (in kg): "))

    def track_metric(self):
        # Select metric to track (e.g., weight, blood pressure, blood glucose)
        metric = input("Select metric to track: ")
        value = float(input("Enter value: "))
        self.user_data[metric] = value

    def set_goal(self):
        # Set goal for specific metric (e.g., weight loss)
        metric = input("Select metric for goal: ")
        goal_value = float(input("Enter goal value: "))
        self.user_data[f"{metric}_goal"] = goal_value

    def view_progress(self):
        # Display progress toward goals
        print("Progress:")
        for metric, value in self.user_data.items():
            if metric.endswith("_goal"):
                print(f"{metric[:-5]}: {value}")

    def visualize_data(self):
        # Simple data visualization using matplotlib
        plt.plot(self.user_data['weight'])
        plt.xlabel("Time")
        plt.ylabel("Weight (kg)")
        plt.show()

def main():
    tracker = HealthTracker()
    while True:
        print("1. Create Profile")
        print("2. Track Metric")
        print("3. Set Goal")
        print("4. View Progress")
        print("5. Visualize Data")
        print("6. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            tracker.create_profile()
        elif choice == "2":
            tracker.track_metric()
        elif choice == "3":
            tracker.set_goal()
        elif choice == "4":
            tracker.view_progress()
        elif choice == "5":
            tracker.visualize_data()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
