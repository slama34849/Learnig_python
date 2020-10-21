import random

my_vocab = {
             "replenish": "fill (something) up again.", 
             "dissipate": "disappear or cause to disappear",
             "copacetic": "in excellent order.\ne.g - he said to tell you everything is copacetic",
             "hypothetically": "by imagining a possibility rather than reality; as a hypothesis.\ne.g - we talked hypothetically about how cool it would be if we moved"
             }


user_request = input("Please enter a word or choose the index number to get definition: ")

def my_dictionary(user_request):
	if user_request != "list" or user_request != "random":	
		while user_request in my_vocab.keys():
			print(my_vocab[user_request])
			break
		else: 
		 	print("This word doesn't exist. Contact Surya to add the word")

my_dictionary(user_request)



if user_request == "list":
	for a,b in my_vocab.items():
	  print(a)



if user_request == "random":
	lis = ([i for i in my_vocab.keys()])
	vocab_len = len(lis)
	vocab_ran = random.randint(0, vocab_len - 1)
	random_choice = lis[vocab_ran]
	print(f'{random_choice} means\n' + my_vocab[random_choice])







# random_vocab()



#Things to add
# be able to append data in dict 