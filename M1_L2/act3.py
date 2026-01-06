from colorama import Fore, Style
# String Operations

first_name = "Jyotirmoy"
last_name = "Deb"
example = "Yahoo"

print("First Name : ", first_name)
print("Last Name : ", last_name)
print("Full Name: ", first_name+" "+last_name)
print("String Multiplied : ", (example+"!..")*3)

text_sample = "Python"

print("First Letter",text_sample[0])
print("First Three letters : ", Fore.GREEN + str(text_sample[0:3]))
print("Word Length : ", Fore.CYAN + str(len(text_sample)))
print("last Letter: ", Fore.BLUE +str(text_sample[len(text_sample) -1]))

