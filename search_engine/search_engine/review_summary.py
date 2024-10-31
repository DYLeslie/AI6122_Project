import json
import matplotlib.pyplot as plt
from collections import Counter
import re
import random


# Create business_id to latitude and longitude mapping
def load_business_info(business_data_dir):
    with open(business_data_dir, "r", encoding="utf-8") as f:
        business_data = json.load(f)

    business_info = {}
    for business in business_data:
        business_info[business["business_id"]] = (business["latitude"], business["longitude"])

    return business_info


# Mapping the distribution of user-contributed comments
def plot_review_distribution(review_data_dir):
    with open(review_data_dir, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    user_review_counts = {}
    for review in review_data:
        user_id = review["user_id"]
        user_review_counts[user_id] = user_review_counts.get(user_id, 0) + 1

    # Count the number of users with specific numbers of comments
    specific_counts = [0, 5, 10, 15, 20, 25, 30, 35, 40]
    user_count_per_review = [sum(1 for count in user_review_counts.values() if count == n) for n in specific_counts]

    plt.figure()
    plt.scatter(specific_counts, user_count_per_review, color='red', marker='o')
    plt.xlabel("Number of reviews")
    plt.ylabel("Number of users having particular numbers of reviews")
    plt.title("Distribution of reviews contributed by users")
    plt.grid(True)
    plt.show()


# Generate a summary of user comments
def user_review_summary(review_data_dir, business_data_dir, user_id):
    with open(review_data_dir, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    # Load Merchant Latitude and Longitude Information
    business_info = load_business_info(business_data_dir)

    # Get all comments from this user
    user_reviews = [review for review in review_data if review["user_id"] == user_id]

    if not user_reviews:
        random_user_ids = random.sample([review["user_id"] for review in review_data], 2)
        print(f"User ID {user_id} doesn't exist, please try again.")
        print(f"If you're unsure about the correct ID, here are two random user IDs you can try: {random_user_ids}\n")
        return

    # Numbers of comments
    review_count = len(user_reviews)

    # Bounding box
    latitudes = []
    longitudes = []
    for review in user_reviews:
        business_id = review["business_id"]
        if business_id in business_info:
            latitude, longitude = business_info[business_id]
            latitudes.append(latitude)
            longitudes.append(longitude)

    min_latitude, max_latitude = min(latitudes), max(latitudes)
    min_longitude, max_longitude = min(longitudes), max(longitudes)


    # Top-10 words
    words = []
    for review in user_reviews:
        text = review["text"]
        words += [word.lower() for word in re.findall(r'\w+', text) if word.lower() not in get_stopwords()]

    word_freq = Counter(words).most_common(10)

    # Top-10 phrases
    phrases = extract_common_phrases(user_reviews, top_n=10)

    # Top-3 sentences
    representative_sentences = select_representative_sentences(user_reviews)

    print(f"Summary of user {user_id}'s reviews")
    print(f"\nNumber of user's reviews: {review_count}")
    print(f"\nBounding box of the businesses (Latitude, Longitude):")
    print(f"Min Latitude: {min_latitude}, Max Latitude: {max_latitude}")
    print(f"Min Longitude: {min_longitude}, Max Longitude: {max_longitude}")
    print(f"\nTop-10 most frequent words:")
    for word in word_freq:
        print(f"{[word]}")
    print(f"\nTop-10 most frequent phrases:")
    for phrase in phrases:
        print(f"{[phrase]}")
    print(f"\nThree most representative sentences:")
    for representative_sentence in representative_sentences:
        print(f"{[representative_sentence]}")
    print()

    return {
        "review_count": review_count,
        "word_freq": word_freq,
        "phrases": phrases,
        "representative_sentences": representative_sentences
    }


# List of stopwords
def get_stopwords():
    return {"the", "and", "is", "in", "it", "this", "that", "of", "to", "a", "for", "on", "with"}


# Get common phrases
def extract_common_phrases(reviews, top_n=10):
    phrases = []
    for review in reviews:
        text = review["text"]
        phrases += re.findall(r'\b\w+\s\w+\b|\b\w+\s\w+\s\w+\b', text)

    phrase_freq = Counter(phrases).most_common(top_n)
    return phrase_freq


# Get Top-3 sentences
def select_representative_sentences(reviews):
    sentences = []
    for review in reviews:
        text = review["text"]
        # Assume all the sentences end with . or ! or ? or \n
        sentences += re.split(r'[.!?(\n)]', text)

    # Pick up the longest sentence
    representative_sentences = sorted(sentences, key=len, reverse=True)[:3]
    return representative_sentences

