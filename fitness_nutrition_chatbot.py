import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to lemmatize text
def lemmatize_text(text):
    words = nltk.word_tokenize(text.lower())
    return ' '.join([lemmatizer.lemmatize(word) for word in words])

# Load the knowledge base
with open("fitness_nutrition_kb.json", "r") as f:
    knowledge_base = json.load(f)

# Extract questions and answers from the knowledge base
questions = [lemmatize_text(qa["question"]) for qa in knowledge_base["questions_answers"]]
answers = [qa["answer"] for qa in knowledge_base["questions_answers"]]

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the vectorizer with the questions from the knowledge base
tfidf_matrix = tfidf_vectorizer.fit_transform(questions)

# Function to get an answer based on a user query
def get_answer(query, threshold=0.3):
    # Convert the user's query into a TF-IDF vector
    normalized_query = lemmatize_text(query)
    query_vector = tfidf_vectorizer.transform([normalized_query])

    # Calculate the cosine similarity between the query vector and the knowledge base
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)

    # Find the highest similarity and its index
    best_match_index = np.argmax(cosine_similarities)
    highest_similarity = cosine_similarities[0, best_match_index]

    # If the highest similarity is below the threshold, return a default response
    if highest_similarity < threshold:
        return "Sorry, I didn't quite understand your question. Can you rephrase or ask something else?"

    # Return the corresponding answer if it passes the threshold
    return answers[best_match_index]

# Function to interact with the chatbot
def run_chatbot():
    print("Welcome to the Fitness & Nutrition Chatbot! Ask me a question. Type 'quit', 'exit', or 'bye' to leave.")

    while True:
        user_query = input("\nYou: ")

        # Check for exit statements
        if user_query.lower() in ["quit", "exit", "bye","thanks"]:
            print("Chatbot: Goodbye! Take care and stay healthy!")
            break
        
        # Check for greeting
        if any(greet in user_query.lower() for greet in ["hi", "hello", "hey", "howdy"]):
            print("Chatbot: Hello! How can I help you today?")
            continue  # Move on to the next iteration after greeting

        answer = get_answer(user_query)
        print(f"Chatbot: {answer}")

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
