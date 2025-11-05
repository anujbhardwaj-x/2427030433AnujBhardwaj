try:
    basic = float(input("Enter Basic Salary: "))
    hra = float(input("Enter HRA: "))
    da = float(input("Enter DA: "))
    gross = basic + hra + da
    print(f"Gross Salary: ₹{gross:.2f}")

except ValueError:
    print("Error: Please enter valid numeric values.")
except TypeError:
    print("Error: Unsupported data type used in calculation.")
except KeyboardInterrupt:
    print("\nProcess interrupted by user.")
except Exception as e:
    print(f"Unexpected Error: {e}")