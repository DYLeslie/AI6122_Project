from whoosh.fields import Schema, ID, TEXT, NUMERIC
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import create_in
import os
import json
import time
import matplotlib.pyplot as plt

# Define the schema for business index
business_schema = Schema(
    business_id=ID(stored=True, unique=True),
    # Perform stemming, case folding on business names, but no stopword removal
    # Store vectors to output snippets
    name=TEXT(stored=True, analyzer=StemmingAnalyzer(stoplist=None), vector=True),
    latitude=NUMERIC(stored=True, numtype=float),
    longitude=NUMERIC(stored=True, numtype=float),
)
# Define the schema for review index
review_schema = Schema(
    review_id=ID(stored=True, unique=True),
    # Perform stemming, case folding and stopword removal on review texts
    text=TEXT(stored=True, analyzer=StemmingAnalyzer(), vector=True),
)


# Generate index
def generate_index(index_dir, data_dir, schema):
    os.makedirs(index_dir, exist_ok=True)
    # Create index
    index = create_in(index_dir, schema)

    # Load data from json
    with open(data_dir, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Set checkpoints to record the indexing time
    total_docs = len(data)
    print(f"Total documents: {total_docs}")
    check_times = 1
    next_checkpoint = int(0.1 * check_times * total_docs)
    elapsed_times = []

    # Write documents to the index
    with index.writer() as writer:
        # Record the start time
        start_time = time.time()

        for i, doc in enumerate(data):
            if schema == business_schema:
                # Write businesses
                writer.add_document(
                    business_id=doc["business_id"],
                    name=doc["name"],
                    latitude=doc["latitude"],
                    longitude=doc["longitude"],
                )
            else:
                # Write reviews
                writer.add_document(
                    review_id=doc["review_id"],
                    text=doc["text"],
                )

            # Record the indexing time
            if i + 1 == next_checkpoint:
                elapsed_time = time.time() - start_time
                print(f"Indexed {check_times * 10}% in {elapsed_time:.4f} seconds")
                elapsed_times.append(elapsed_time)
                check_times += 1
                next_checkpoint = int(0.1 * check_times * total_docs)

    # Plot the indexing time
    x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.figure()
    plt.plot(x, elapsed_times, marker='o')
    plt.xlabel("Percentage of Documents Indexed (%)")
    plt.ylabel("Elapsed Time (seconds)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Generate business index
    print("Business:")
    generate_index(index_dir="../index/business", data_dir="../data/nj_business.json", schema=business_schema)
    # Generate review index
    print("Review:")
    generate_index(index_dir="../index/review", data_dir="../data/nj_review.json", schema=review_schema)
