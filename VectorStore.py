# Requisite imports
from VectorClass import VectorStore  # Importing the VectorStore class from vector_store module
import numpy as np  # Importing numpy for numerical operations

# Establish a VectorStore instance
vector_store = VectorStore()  # Creating an instance of the VectorStore class

# Define sentences
sentences = [  # Defining a list of example sentences
    "I eat mango",
    "mango is my favorite fruit",
    "mango, apple, oranges are fruits",
    "fruits are good for health",
]

# Tokenization and Vocabulary Creation
vocabulary = set()  # Initializing an empty set to store unique words
for sentence in sentences:  # Iterating over each sentence in the list
    tokens = sentence.lower().split()  # Tokenizing the sentence by splitting on whitespace and converting to lowercase
    vocabulary.update(tokens)  # Updating the set of vocabulary with unique tokens

# Assign unique indices to vocabulary words
word_to_index = {word: i for i, word in enumerate(vocabulary)}  # Creating a dictionary mapping words to unique indices

# Vectorization
sentence_vectors = {}  # Initializing an empty dictionary to store sentence vectors
for sentence in sentences:  # Iterating over each sentence in the list
    tokens = sentence.lower().split()  # Tokenizing the sentence by splitting on whitespace and converting to lowercase
    vector = np.zeros(len(vocabulary))  # Initializing a numpy array of zeros for the sentence vector
    for token in tokens:  # Iterating over each token in the sentence
        vector[word_to_index[token]] += 1  # Incrementing the count of the token in the vector
    sentence_vectors[sentence] = vector  # Storing the vector for the sentence in the dictionary

# Store in VectorStore
for sentence, vector in sentence_vectors.items():  # Iterating over each sentence vector
    vector_store.add_vector(sentence, vector)  # Adding the sentence vector to the VectorStore

# Similarity Search
query_sentence = "Mango is the best fruit"  # Defining a query sentence
query_vector = np.zeros(len(vocabulary))  # Initializing a numpy array of zeros for the query vector
query_tokens = query_sentence.lower().split()  # Tokenizing the query sentence and converting to lowercase
for token in query_tokens:  # Iterating over each token in the query sentence
    if token in word_to_index:  # Checking if the token is present in the vocabulary
        query_vector[word_to_index[token]] += 1  # Incrementing the count of the token in the query vector

similar_sentences = vector_store.find_similar_vectors(query_vector, num_results=2)  # Finding similar sentences

# Display similar sentences
print("Query Sentence:", query_sentence)  # Printing the query sentence
print("Similar Sentences:")  # Printing the header for similar sentences
for sentence, similarity in similar_sentences:  # Iterating over each similar sentence and its similarity score
    print(f"{sentence}: Similarity = {similarity:.4f}")  # Printing the similar sentence and its similarity score