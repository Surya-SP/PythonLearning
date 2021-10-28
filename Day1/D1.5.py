#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
print("Welcome to band name generator.")
city = input("Enter your city: \n")
pet_name = input("Enter your pet's name: \n")
band_name = (city+" "+pet_name)
print("Band name could be: "+band_name)