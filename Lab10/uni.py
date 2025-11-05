def student_result():
    try:
        marks_obtained = float(input("Enter marks obtained: "))
        total_marks = float(input("Enter total marks: "))
        percentage = (marks_obtained / total_marks) * 100
        print(f"Percentage: {percentage:.2f}%")

        file_name = "student_result.txt"
        with open(file_name, "w") as f:
            f.write(f"Marks Obtained: {marks_obtained}\n")
            f.write(f"Total Marks: {total_marks}\n")
            f.write(f"Percentage: {percentage:.2f}%\n")
        
        print(f"Result saved successfully in '{file_name}'")

    except ValueError:
        print("Error: Please enter numeric values for marks.")
    except ZeroDivisionError:
        print("Error: Total marks cannot be zero.")
    except FileNotFoundError:
        print("Error: The result file is missing.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

student_result()