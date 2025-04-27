def calculate_bmi(weight, height):
    """Calculate BMI using weight in kg and height in meters"""
    return weight / (height ** 2)

def counter_controlled_bmi():
    print("\n=== Counter-Controlled BMI Calculator ===")
    try:
        counter = int(input("Enter how many times you want to calculate BMI: "))
        for i in range(counter):
            print(f"\nCalculation {i+1} of {counter}")
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in meters: "))
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi:.2f}")
            
            # BMI Categories
            if bmi < 18.5:
                print("Category: Underweight")
            elif 18.5 <= bmi < 25:
                print("Category: Normal weight")
            elif 25 <= bmi < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")
    except ValueError:
        print("Please enter valid numbers!")

def sentinel_controlled_bmi():
    print("\n=== Sentinel-Controlled BMI Calculator ===")
    while True:
        try:
            weight = float(input("\nEnter weight in kg (or 0 to exit): "))
            if weight == 0:
                print("Exiting BMI calculator...")
                break
                
            height = float(input("Enter height in meters: "))
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi:.2f}")
            
            # BMI Categories
            if bmi < 18.5:
                print("Category: Underweight")
            elif 18.5 <= bmi < 25:
                print("Category: Normal weight")
            elif 25 <= bmi < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")
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