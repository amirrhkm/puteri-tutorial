import bmi_calculator_tracer

# Store the latest session data
last_counter = None
last_counter_data = None
last_sentinel_data = None

def calculate_bmi(weight, height):
    """Calculate BMI using weight in kg and height in meters"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def counter_controlled_bmi():
    global last_counter, last_counter_data, last_sentinel_data
    print("\n=== Counter-Controlled BMI Calculator ===")
    try:
        counter = int(input("Enter how many times you want to calculate BMI: "))
        last_counter = counter
        counter_data = []
        for i in range(counter):
            print(f"\nCalculation {i+1} of {counter}")
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in meters: "))
            bmi = calculate_bmi(weight, height)
            classification = classify_bmi(bmi)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {classification}")
            counter_data.append((weight, height, bmi, classification))
        last_counter_data = counter_data
        # After the loop, update the truth table
        bmi_calculator_tracer.write_markdown_truth_table(
            counter=last_counter,
            counter_data=last_counter_data,
            sentinel_data=last_sentinel_data
        )
    except ValueError:
        print("Please enter valid numbers!")

def sentinel_controlled_bmi():
    global last_counter, last_counter_data, last_sentinel_data
    print("\n=== Sentinel-Controlled BMI Calculator ===")
    sentinel_data = []
    while True:
        try:
            weight = float(input("\nEnter weight in kg (or 0 to exit): "))
            if weight == 0:
                sentinel_data.append((0, None, None, None))
                last_sentinel_data = sentinel_data
                # After the loop, update the truth table
                bmi_calculator_tracer.write_markdown_truth_table(
                    counter=last_counter,
                    counter_data=last_counter_data,
                    sentinel_data=last_sentinel_data
                )
                print("Exiting BMI calculator...")
                break
            height = float(input("Enter height in meters: "))
            bmi = calculate_bmi(weight, height)
            classification = classify_bmi(bmi)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {classification}")
            sentinel_data.append((weight, height, bmi, classification))
        except ValueError:
            print("Please enter valid numbers!")

def main():
    while True:
        print("\nBMI Calculator Program")
        print("1. Counter-Controlled Loop")
        print("2. Sentinel-Controlled Loop")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            counter_controlled_bmi()
        elif choice == "2":
            sentinel_controlled_bmi()
        elif choice == "3":
            print("Thank you for using BMI Calculator!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 