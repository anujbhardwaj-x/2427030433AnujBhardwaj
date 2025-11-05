try:
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
            
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied. Cannot access the file.")
except UnicodeDecodeError:
    print("Error: The file contains unreadable characters.")
except Exception as e:
    print(f"Unexpected Error: {e}")