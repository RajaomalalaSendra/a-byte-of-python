import pickle

# create the data.data for the real
data = "data.data"

# input the sentence
sentence = input("Enter one sentence: ")
sentence = sentence.split(" ")
# store the sentence into the data.data
f = open(data, 'wb')
pickle.dump(sentence, f)
f.close()
f = open(data, 'rb')
# Load the object from the file
data = pickle.load(f)
print(data)