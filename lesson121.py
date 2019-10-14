# fruits = {"apple": 5, "pineapple": 15, "orange": 36, "bananas": 2}


# print(fruits.keys())
# print(fruits.values())
# for i in fruits.values():
# 	print(i, end=" ")
# for key in fruits.keys():
# 	if fruits[key] > 5:
# 		print(key)
# ISTC = {"Gor Smbatyan" : 26, "David Grigoryan": 26, "Vardges Hivhannisyan": 26, "Artur Altunyan": 23, "Artur Ananyan": 29}
# print(ISTC)
# ISTC["Artur Altunyan"] = 280
# print(ISTC)
# ISTC["Artur Ananyan"] = 444
# del ISTC["Gor Smbatyan"]
# print(ISTC)

# fruits = {"apple": 5, "pineapple": 15, "orange": 36, "bananas": 2}
# print(fruits.items())

# for (name, kg) in fruits.items():
# 	print(name, "is", kg, "In store")


# classes = {"Math": ["David", "Lucy", "Dana"],
# 			"Physics": ["Adison", " Benjamin"]}
# print("studenys in math class", classes["Math"])
# classes["Math"].append("Artur")
# print("Student in math class", classes["Math"])

# Art = {"age": 35, "Nation" : 'Armenian', "status": "single"}
# Arth = {"age": 36, "Nation": "Arm", "status": "married"}

# classes = {"Artur": Art, "Arthur": Arth}
# for age in classes.keys():
# 	print(classes["Artur"])
# 	print(classes["Arthur"])

text = "Text messages are used for personal family business and social purposes Governmental and non-governmental organizations use text messaging for communication between colleagues In the 2010s, the sending of short informal messages has become an accepted part of many cultures, as happened earlier with emailing.[1] This makes texting a quick and easy way to communicate with friends, family and colleagues, including in contexts where a call would be impolite or inappropriate (e.g., calling very late at night or when one knows the other person is busy with family or work activities). Like e-mail and voicemail, and unlike calls (in which the caller hopes to speak directly with the recipient), texting does not require the caller and recipient to both be free at the same moment; this permits communication even between busy individuals. Text messages can also be used to interact with automated systems, for example, to order products or services from e-commerce websites, or to participate in online contests. Advertisers and service providers use direct text marketing to send messages to mobile users about promotions, payment due dates, and other notifications instead of using postal mail, email, or voicemail."
word_dict = {}

text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("(", "")
text = text.replace(")", "")
text = text.split(" ")
# print(text)

for word in text:
 	if word in word_dict.keys():
 		word_dict[word] += 1
 	else:
 		word_dict[word] = 1
for (word, amount) in word_dict.items():
	if amount > 2:
		print(word, ":", amount)
