def calculate_bmi(weight, height):
  bmi = weight / (height * height)
  return bmi
#Task1- BMI Calculator
def bmi_category(bmi):

  if bmi < 18.5:
    category = "Underweight"
  elif bmi < 25:
    category = "Normal weight"
  elif bmi < 30:
    category = "Overweight"
  else:
    category = "Obese"
  return category

# Get weight and height from user
try:
  weight = float(input("Enter your weight in kilograms (kg): "))
  height = float(input("Enter your height in meters (m): "))
except ValueError:
  print("Error: Please enter numbers for weight and height.")
  exit()

# Calculate BMI and category
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")
