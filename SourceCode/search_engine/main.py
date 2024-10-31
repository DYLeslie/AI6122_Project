from search_engine.searcher import keyword_search, geospatial_search
from search_engine.review_summary import plot_review_distribution, user_review_summary
import os
import sys


# Get the absolute path of index
# Path of index differs depending on different running environments
def get_index_dir(relative_path):
    # Program is running as an exe
    try:
        base_path = sys._MEIPASS
    # Program is running as a Python script
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


business_index_dir = get_index_dir("index/business")
review_index_dir = get_index_dir("index/review")
business_data_dir = get_index_dir("data/nj_business.json")
review_data_dir = get_index_dir("data/nj_review.json")


# Interact with users through the command line interface
def interface():
    print("Welcome to our search engine for businesses and reviews in NJ!")

    while True:
        print("Options:")
        print("1. Keyword Search of Businesses")
        print("2. Keyword Search of Reviews")
        print("3. Geospatial Search of Businesses")
        print("4. Review Summary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        print()

        # Keyword search of businesses and reviews
        if choice == "1" or choice == "2":
            # Users can choose keyword search or phrase search
            # Phrase search will match the entire phrase
            print("Notice: To execute a keyword search, simply enter the keywords (e.g., Chinese Food).")
            print("        To execute an exact phrase search, enclose the phrase in \"\" (e.g., \"Chinese Food\").\n")

            if choice == "1":
                keywords = input("Enter the keywords or phrase in business names: ")
            else:
                keywords = input("Enter the keywords or phrase in reviews: ")
            top_n = int(input("Enter the number of top results to return: "))
            print()

            if choice == "1":
                outputs, elapsed_time = keyword_search(business_index_dir, "name", keywords, top_n)
            else:
                outputs, elapsed_time = keyword_search(review_index_dir, "text", keywords, top_n)
            for output in outputs:
                print(f"Rank: {output['rank']}, Score: {output['score']}, DocID: {output['docID']},")
                print(f"Snippet: {output['snippet']}\n")
            if len(outputs) == 0:
                print("No results found.\n")
            print(f"Processing Time: {elapsed_time:.4f}s\n")

        # Geospatial search of businesses
        elif choice == "3":
            print("Notice: The geospatial area is defined by a bounding box. You need to enter the range of latitude "
                  "and longitude.\n")

            min_lat = float(input("Enter the minimum latitude (between 39.05 and 40.39): "))
            max_lat = float(input("Enter the maximum latitude (between 39.05 and 40.39): "))
            min_lon = float(input("Enter the minimum longitude (between -75.55 and -74.66): "))
            max_lon = float(input("Enter the maximum longitude (between -75.55 and -74.66): "))
            top_n = int(input("Enter the number of top results to return: "))
            print()

            outputs, elapsed_time = geospatial_search(business_index_dir, min_lat, max_lat, min_lon, max_lon, top_n)
            for output in outputs:
                print(f"Rank: {output['rank']}, Score: {output['score']}, DocID: {output['docID']},")
                print(f"Name: {output['name']}, Latitude: {output['latitude']}, Longitude: {output['longitude']}\n")
            if len(outputs) == 0:
                print("No results found.\n")
            print(f"Processing Time: {elapsed_time:.4f}s\n")

        # Present the summary of reviews
        elif choice == "4":
            print("Options:")
            print("1. Plot Review Distribution")
            print("2. Get User's Review Summary")
            sub_choice = input("Enter your choice (1 or 2): ")
            print()

            if sub_choice == "1":
                # Plot the distribution map
                plot_review_distribution(review_data_dir)
            elif sub_choice == "2":
                # Get user's review summary
                user_id = input("Enter user ID: ")
                print()
                user_review_summary(review_data_dir, business_data_dir, user_id)
            else:
                print("Invalid choice. Please enter a number between 1 and 2.\n")

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    interface()
