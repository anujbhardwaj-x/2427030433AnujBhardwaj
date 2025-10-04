# WAF to calculate average marks with default parameters (missing=0)
def avg_marks(m1=0, m2=0, m3=0):
    return (m1 + m2 + m3) / 3

# Example call
print("Average with all marks:", avg_marks(80, 90, 70))
print("Average with one missing:", avg_marks(80, 90))  # third taken as 0
