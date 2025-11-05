try:
    lst = [int(x) for x in input("Enter integers separated by space: ").split()]
    index = int(input("Enter index to access: "))
    print(f"Element at index {index}: {lst[index]}")

except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter valid integers for list and index.")
except TypeError:
    print("Error: List contains incompatible data types.")
except Exception as e:
    print(f"Unexpected Error: {e}")