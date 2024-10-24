# AI6122_Search_Engine
# Installation Guide and Usage Instructions

Welcome to the installation guide for our **Search Engine for Businesses and Reviews in New Jersey (NJ)**. This guide will help you set up the system on your machine and provide instructions on how to use it effectively.

**Note:** The data and the program are available at [Kaggle: Yelp NJ Dataset](https://www.kaggle.com/datasets/dyleslie/yelp-nj). You can also directly run `search_engine.exe` if you prefer.

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Installation Steps](#2-installation-steps)
   - [Step 1: Download the Data and Program](#step-1-download-the-data-and-program)
   - [Step 2: Install Python 3](#step-2-install-python-3)
   - [Step 3: Install Required Python Packages](#step-3-install-required-python-packages)
   - [Step 4: Prepare the Directory Structure](#step-4-prepare-the-directory-structure)
   - [Step 5: Generate the Indexes](#step-5-generate-the-indexes)
3. [Usage Instructions](#3-usage-instructions)
   - [Option 1: Keyword Search of Businesses](#option-1-keyword-search-of-businesses)
   - [Option 2: Keyword Search of Reviews](#option-2-keyword-search-of-reviews)
   - [Option 3: Geospatial Search of Businesses](#option-3-geospatial-search-of-businesses)
   - [Option 4: Review Summary](#option-4-review-summary)
     - [Sub-option 1: Plot Review Distribution](#sub-option-1-plot-review-distribution)
     - [Sub-option 2: Get User's Review Summary](#sub-option-2-get-users-review-summary)
   - [Option 5: Exit](#option-5-exit)
4. [Additional Notes](#4-additional-notes)

## 1. Prerequisites

Before setting up the system, ensure that you have the following:

- **Python 3.x** installed on your system.
- **pip** (Python package manager) installed.
- The following Python packages:
  - `whoosh`
  - `matplotlib`
  - `termcolor`
- **Data and Program:**
  - Download from [Kaggle: Yelp NJ Dataset](https://www.kaggle.com/datasets/dyleslie/yelp-nj)
    - Data Files: `nj_business.json`, `nj_review.json`
    - Program Files: `main.py`, `indexer.py`, `searcher.py`, `review_summary.py`

**Alternatively**, you can directly run the compiled executable `search_engine.exe` if you prefer not to run the source code.

## 2. Installation Steps

### Step 1: Download the Data and Program

- Visit the [Kaggle: Yelp NJ Dataset](https://www.kaggle.com/datasets/dyleslie/yelp-nj) page.
- Download the dataset and program files.
- Extract the files to a directory on your machine.

### Step 2: Install Python 3

If you don't have Python 3 installed, download it from the [official website](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

### Step 3: Install Required Python Packages

Open your terminal or command prompt and run the following commands to install the required packages:

```bash
pip install whoosh matplotlib termcolor
```

### Step 4: Prepare the Directory Structure

Ensure your project directory has the following structure:

```
your_project/
├── data/
│   ├── nj_business.json
│   └── nj_review.json
├── index/
├── main.py
├── search_engine/
    ├── __init__.py
    ├── indexer.py
    ├── review_summary.py
    └── searcher.py
```

If the `data` and `index` directories do not exist, create them:

```bash
mkdir data index
```

Place the `nj_business.json` and `nj_review.json` data files into the `data/` directory.

### Step 5: Generate the Indexes

Before using the search functionalities, you need to generate the indexes for the business and review data.

Run the `indexer.py` script:

```bash
python indexer.py
```

This script will:

- Read data from `data/nj_business.json` and `data/nj_review.json`.
- Create indexes in the `index/` directory.

**Note:** The indexing process may take several minutes, depending on the size of the data files. Progress messages and a plot showing the indexing time will be displayed during the process.

## 3. Usage Instructions

After generating the indexes, you can start using the search engine.

Run the `main.py` script:

```bash
python main.py
```

**Alternatively**, if you prefer using the executable, run `search_engine.exe`:

- On Windows: Double-click `search_engine.exe` or run it via the command prompt.
- On macOS/Linux: Make sure the executable has execute permissions and run it from the terminal.

You will see the following menu:

```
Welcome to our search engine for businesses and reviews in NJ!
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5):
```

### Option 1: Keyword Search of Businesses

- **Description:** Search for businesses based on keywords in their names.

- **Instructions:**

  1. Choose option `1`.
  2. Enter keywords or phrases when prompted.
     - **Keyword Search:** Simply enter the keywords (e.g., `Chinese Food`).
     - **Exact Phrase Search:** Enclose the phrase in double quotes (e.g., `"Chinese Food"`).
  3. Enter the number of top results to return.

- **Example:**

  ```
  Enter your choice (1-5): 1
  
  Notice: To execute a keyword search, simply enter the keywords (e.g., Chinese Food).
          To execute an exact phrase search, enclose the phrase in "" (e.g., "Chinese Food").
  
  Enter the keywords or phrase in business names: Italian Restaurant
  Enter the number of top results to return: 5
  
  Rank: 1, Score: 15.732, DocID: 123,
  Snippet: [Highlighted snippet of the business name]
  
  ... (additional results) ...
  
  Processing Time: 0.2567s
  ```

### Option 2: Keyword Search of Reviews

- **Description:** Search for reviews based on keywords in the review text.

- **Instructions:**

  1. Choose option `2`.
  2. Enter keywords or phrases when prompted.
     - Use the same format as in Option 1.
  3. Enter the number of top results to return.

- **Example:**

  ```
  Enter your choice (1-5): 2
  
  Notice: To execute a keyword search, simply enter the keywords (e.g., Chinese Food).
          To execute an exact phrase search, enclose the phrase in "" (e.g., "Chinese Food").
  
  Enter the keywords or phrase in reviews: excellent service
  Enter the number of top results to return: 10
  
  Rank: 1, Score: 12.843, DocID: 456,
  Snippet: [Highlighted snippet of the review text]
  
  ... (additional results) ...
  
  Processing Time: 0.3891s
  ```

### Option 3: Geospatial Search of Businesses

- **Description:** Search for businesses within a specified geographical area defined by latitude and longitude ranges.

- **Instructions:**

  1. Choose option `3`.
  2. Enter the minimum and maximum latitude and longitude values when prompted.
     - **Latitude Range:** Between `39.05` and `40.39`.
     - **Longitude Range:** Between `-75.55` and `-74.66`.
  3. Enter the number of top results to return.

- **Example:**

  ```
  Enter your choice (1-5): 3
  
  Notice: The geospatial area is defined by a bounding box. You need to enter the range of latitude and longitude.
  
  Enter the minimum latitude (between 39.05 and 40.39): 39.8
  Enter the maximum latitude (between 39.05 and 40.39): 40.0
  Enter the minimum longitude (between -75.55 and -74.66): -75.2
  Enter the maximum longitude (between -75.55 and -74.66): -74.9
  Enter the number of top results to return: 5
  
  Rank: 1, Score: 9.564, DocID: 789,
  Name: Cafe Delight, Latitude: 39.85, Longitude: -75.1
  
  ... (additional results) ...
  
  Processing Time: 0.3124s
  ```

### Option 4: Review Summary

- **Description:** View summaries related to user reviews.

- **Instructions:**

  1. Choose option `4`.

  2. You will see a sub-menu with two options:

     ```
     Options:
     1. Plot Review Distribution
     2. Get User's Review Summary
     Enter your choice (1 or 2):
     ```

#### Sub-option 1: Plot Review Distribution

- **Description:** Plot the distribution of the number of reviews contributed by users.

- **Instructions:**

  - Choose sub-option `1`.
  - A scatter plot will be displayed showing the distribution.
  - **Note:** Ensure that your environment supports GUI display.

- **Example:**

  ```
  Enter your choice (1 or 2): 1
  
  [A scatter plot window opens showing the distribution]
  ```

#### Sub-option 2: Get User's Review Summary

- **Description:** Get a summary of a user's reviews, including:

  - Number of reviews.
  - Bounding box of the businesses reviewed.
  - Top 10 most frequent words.
  - Top 10 most frequent phrases.
  - Three most representative sentences.

- **Instructions:**

  1. Choose sub-option `2`.
  2. Enter the user ID when prompted.
     - If the user ID does not exist, you will be provided with two random user IDs to try.
  3. The summary will be displayed in the terminal.

- **Example:**

  ```
  Enter your choice (1 or 2): 2
  
  Enter user ID: abcdef123456
  
  Summary of user abcdef123456's reviews
  
  Number of user's reviews: 5
  
  Bounding box of the businesses (Latitude, Longitude):
  Min Latitude: 39.9, Max Latitude: 40.1
  Min Longitude: -75.1, Max Longitude: -74.9
  
  Top-10 most frequent words:
  [('food', 15), ('great', 12), ('service', 10), ('place', 9), ('good', 8), ('time', 7), ('back', 6), ('restaurant', 5), ('menu', 4), ('really', 3)]
  
  Top-10 most frequent phrases:
  [(('great', 'food'), 5), (('good', 'service'), 4), (('will', 'be', 'back'), 3), (('friendly', 'staff'), 2), (('highly', 'recommend'), 1)]
  
  Three most representative sentences:
  ['The food was amazing and the service was excellent.', 'I will definitely be back!', 'One of the best restaurants in the area.']
  
  ```

### Option 5: Exit

- **Description:** Exit the search engine.

- **Instructions:**
  - Choose option `5` to exit the program.

## 4. Additional Notes

- **Data and Program Files:**
  - Ensure that all data and program files downloaded from [Kaggle](https://www.kaggle.com/datasets/dyleslie/yelp-nj) are placed in the appropriate directories.
  - The data files should be in JSON format and contain valid data as expected by the system.

- **Python Version:**
  - The scripts are compatible with **Python 3.x**. Using Python 2.x may result in errors.
  - You can check your Python version by running `python --version` in the terminal.

- **Matplotlib Plots:**
  - For options that display plots (e.g., indexing time plot in `indexer.py` and review distribution in `review_summary.py`), ensure that your environment supports GUI display.
  - If running on a headless server (without a display), you may need to configure `matplotlib` to use a non-interactive backend or save the plots to files.

- **Random User IDs:**
  - If you enter a user ID that does not exist, the system will suggest two random user IDs to try.

- **Error Handling:**
  - The system includes basic error handling for invalid inputs. Please follow the prompts carefully.

- **Re-Indexing Data:**
  - If you update the data files or need to regenerate the indexes for any reason, re-run `indexer.py`.



**Enjoy exploring businesses and reviews in New Jersey!**





# Explanation of Sample Output Obtained from the System

Below are sample outputs obtained from using the search engine system for businesses and reviews in New Jersey. Each sample includes the user inputs and the system responses, followed by explanations to help you understand how the system works.

---

## Sample 1: Keyword Search of Businesses (Keyword Search)

### User Input:

```
Welcome to our search engine for businesses and reviews in NJ!
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 1

Notice: To execute a keyword search, simply enter the keywords (e.g., Chinese Food).
        To execute an exact phrase search, enclose the phrase in "" (e.g., "Chinese Food").

Enter the keywords or phrase in business names: Chinese Food
Enter the number of top results to return: 5
```

### System Output:

```
Rank: 1, Score: 10.539775497710817, DocID: 748,
Snippet: No 1 Chinese Food

Rank: 2, Score: 10.539775497710817, DocID: 817,
Snippet: Great Taste Chinese Food

Rank: 3, Score: 10.539775497710817, DocID: 1821,
Snippet: Great Taste Chinese Food

Rank: 4, Score: 10.539775497710817, DocID: 4464,
Snippet: Great Taste Chinese Food

Rank: 5, Score: 9.426639027632504, DocID: 3873,
Snippet: Oishi Sushi Japanese & Chinese Food

Processing Time: 0.0630s
```

### Explanation:

- **Option Selected**: The user selected **Option 1**, which is the **Keyword Search of Businesses**.
- **Search Query**: The user entered the keywords **`Chinese Food`** without quotes, indicating a keyword search rather than an exact phrase search.
- **Top Results Requested**: The user requested the **top 5 results**.
- **Results**:
  - The system returned **5 business listings** that match the keywords.
  - **Rank**: Indicates the position of the result based on relevance.
  - **Score**: A numerical value representing how closely the business name matches the search terms.
  - **DocID**: The internal document ID for the business in the index.
  - **Snippet**: The name of the business, potentially with matched keywords highlighted.
- **Observations**:
  - All the top-ranked businesses have the keywords "Chinese Food" in their names.
  - The first four results have identical scores, indicating similar relevance.
  - The fifth result has a slightly lower score but still contains the keywords.

---

## Sample 2: Keyword Search of Businesses (Exact Phrase Search)

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 1

Notice: To execute a keyword search, simply enter the keywords (e.g., Chinese Food).
        To execute an exact phrase search, enclose the phrase in "" (e.g., "Chinese Food").

Enter the keywords or phrase in business names:  "Chinese Food"
Enter the number of top results to return: 5
```

### System Output:

```
Rank: 1, Score: 10.539775497710817, DocID: 748,
Snippet: No 1 Chinese Food

Rank: 2, Score: 10.539775497710817, DocID: 817,
Snippet: Great Taste Chinese Food

Rank: 3, Score: 10.539775497710817, DocID: 1821,
Snippet: Great Taste Chinese Food

Rank: 4, Score: 10.539775497710817, DocID: 4464,
Snippet: Great Taste Chinese Food

Rank: 5, Score: 9.426639027632504, DocID: 3873,
Snippet: Oishi Sushi Japanese & Chinese Food

Processing Time: 0.0330s
```

### Explanation:

- **Option Selected**: **Option 1** was selected again for a business name search.
- **Search Query**: The user entered **`"Chinese Food"`** with quotes, indicating an **exact phrase search**.
- **Top Results Requested**: The user requested the **top 5 results**.
- **Results**:
  - Similar to the previous sample, the results include businesses whose names contain the exact phrase "Chinese Food".
  - The consistent scores suggest that the exact phrase "Chinese Food" was found in the business names.
- **Observations**:
  - The results are the same as in the keyword search, indicating that in this case, the keyword and exact phrase searches yielded the same top results.
  - This suggests that the phrase "Chinese Food" is a common exact match in business names within the dataset.

---

## Sample 3: Keyword Search of Reviews (Keyword Search)

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 2

Notice: To execute a keyword search, simply enter the keywords (e.g., Chinese Food).
        To execute an exact phrase search, enclose the phrase in "" (e.g., "Chinese Food").

Enter the keywords or phrase in reviews: Chinese Food
Enter the number of top results to return: 5
```

### System Output:

```
Rank: 1, Score: 12.865171707108193, DocID: 1064,
Snippet: great place to grab Chinese food when you are craving...spicy Chinese food

Rank: 2, Score: 12.68378463311891, DocID: 135676,
Snippet: Good standard chinese food you expect in a chinese restaurant.  Did...from traditional chinese dishes this trip...Food good, place clean & staff friendly & prices good

Rank: 3, Score: 12.66294420706439, DocID: 85663,
Snippet: I wanted to like the food, but as a Chinese-American, I can tell...I've had American Chinese food that's better than this...and more authentic Chinese food

Rank: 4, Score: 12.660548098346798, DocID: 69882,
Snippet: The most honest Food was good it's basically...Chinese food.. Nothing special honestly...lol just Chinese food

Rank: 5, Score: 12.6516615279971, DocID: 1590,
Snippet: Excellent, authentic Chinese schezuan food! Even nicer is that it...Nice to have actual Chinese food close to home rather...that sweet tasting food at most quasi-Chinese restaurants

Processing Time: 0.6715s
```

### Explanation:

- **Option Selected**: The user selected **Option 2** for **Keyword Search of Reviews**.
- **Search Query**: The user entered **`Chinese Food`** without quotes for a keyword search.
- **Top Results Requested**: The top **5** results were requested.
- **Results**:
  - The system returned **5 reviews** containing the keywords "Chinese" and "Food".
  - **Scores** are slightly higher than those in the business search, possibly due to the lengthier content in reviews.
  - **Snippets**:
    - Each snippet includes portions of the review text where the keywords appear.
    - Ellipses (`...`) indicate omitted text for brevity.
- **Observations**:
  - The reviews discuss experiences with Chinese food, including opinions on authenticity, quality, and service.
  - The snippets show varied contexts in which "Chinese food" appears.

---

## Sample 4: Keyword Search of Reviews (Exact Phrase Search)

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 2

Notice: To execute a keyword search, simply enter the keywords (e.g., Chinese Food).
        To execute an exact phrase search, enclose the phrase in "" (e.g., "Chinese Food").

Enter the keywords or phrase in reviews:  "Chinese Food"
Enter the number of top results to return: 5
```

### System Output:

```
Rank: 1, Score: 12.865171707108193, DocID: 1064,
Snippet: great place to grab Chinese food when you are craving...spicy Chinese food

Rank: 2, Score: 12.68378463311891, DocID: 135676,
Snippet: Good standard chinese food you expect in a chinese restaurant.  Did...from traditional chinese dishes this trip...Food good, place clean & staff friendly & prices good

Rank: 3, Score: 12.66294420706439, DocID: 85663,
Snippet: I wanted to like the food, but as a Chinese-American, I can tell...I've had American Chinese food that's better than this...and more authentic Chinese food

Rank: 4, Score: 12.660548098346798, DocID: 69882,
Snippet: The most honest Food was good it's basically...Chinese food.. Nothing special honestly...lol just Chinese food

Rank: 5, Score: 12.6516615279971, DocID: 1590,
Snippet: Excellent, authentic Chinese schezuan food! Even nicer is that it...Nice to have actual Chinese food close to home rather...that sweet tasting food at most quasi-Chinese restaurants

Processing Time: 0.9436s
```

### Explanation:

- **Option Selected**: **Option 2** was selected again for a review search.
- **Search Query**: The user entered **`"Chinese Food"`** with quotes for an **exact phrase search**.
- **Top Results Requested**: The user requested the **top 5 results**.
- **Results**:
  - The results are identical to those from the keyword search in Sample 3.
  - This indicates that the exact phrase "Chinese Food" frequently appears in the reviews.
- **Observations**:
  - The exact phrase search did not narrow down the results further compared to the keyword search.
  - Users often mention "Chinese food" as a phrase in their reviews.

---

## Sample 5: Geospatial Search of Businesses

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 3

Notice: The geospatial area is defined by a bounding box. You need to enter the range of latitude and longitude.

Enter the minimum latitude (between 39.05 and 40.39): 39.10
Enter the maximum latitude (between 39.05 and 40.39): 40.39
Enter the minimum longitude (between -75.55 and -74.66): -75.58
Enter the maximum longitude (between -75.55 and -74.66): -74.66
Enter the number of top results to return: 5
```

### System Output:

```
Rank: 1, Score: 2.0, DocID: 0,
Name: Stomel Elliot Attorney-At-Law, Latitude: 39.915478, Longitude: -75.016973

Rank: 2, Score: 2.0, DocID: 1,
Name: Sharky's Sports Bar & Grill, Latitude: 39.6968014, Longitude: -74.9998214

Rank: 3, Score: 2.0, DocID: 2,
Name: Super Sushi Kyo Hin, Latitude: 40.0416285, Longitude: -74.8258209

Rank: 4, Score: 2.0, DocID: 3,
Name: Fresh Fruits & Salads, Latitude: 39.9466899, Longitude: -75.123327

Rank: 5, Score: 2.0, DocID: 4,
Name: America's Best Contacts & Eyeglasses, Latitude: 39.824552, Longitude: -74.929032

Processing Time: 0.2920s
```

### Explanation:

- **Option Selected**: The user selected **Option 3** for **Geospatial Search of Businesses**.
- **Bounding Box Input**:
  - **Minimum Latitude**: `39.10`
  - **Maximum Latitude**: `40.39`
  - **Minimum Longitude**: `-75.58`
  - **Maximum Longitude**: `-74.66`
- **Top Results Requested**: The user requested the **top 5 results**.
- **Results**:
  - The system returned **5 businesses** located within the specified geographical bounding box.
  - **Rank**: All results have the same score and are ranked based on their order in the index.
  - **Score**: A uniform score of `2.0` indicates that the ranking is solely based on the spatial query without additional weighting.
  - **Business Details**:
    - **Name**: The name of the business.
    - **Latitude and Longitude**: The geographical coordinates of the business.
- **Observations**:

  - The businesses returned span various industries, indicating a broad search.
  - The geographical coordinates of each business fall within the specified ranges.  

---

## Sample 6: Plot Review Distribution

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 4

Options:
1. Plot Review Distribution
2. Get User's Review Summary
Enter your choice (1 or 2): 1
```

### System Output:

![已上传的图片](https://files.oaiusercontent.com/file-G7J0zuL2A0GrcAOfMpslYwgW?se=2024-10-24T19%3A44%3A58Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D299%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dimage.png&sig=cRzRt0D%2BXthQT%2B841cRAGO/RbUu3aeyh4OwC6orTc6M%3D)

### Explanation:

- **Option Selected**: The user selected **Option 4** for **Review Summary** from the main menu.
- **Sub-option Selected**: Within the review summary options, the user selected **Option 1**, which is to **Plot Review Distribution**.
- **Results**:
  - The displayed graph is titled **"Distribution of reviews contributed by users"**.
  - The x-axis represents the **Number of reviews** contributed by users.
  - The y-axis represents the **Number of users** having a specific number of reviews.
  - Each red dot on the graph represents the count of users that have contributed a specific number of reviews. For instance, a large number of users have contributed just a few reviews, as shown by the dot at the 5-reviews mark, and there are fewer users as the number of reviews increases.
- **Observations**:
  - The graph shows a clear trend where the number of users contributing reviews decreases as the number of reviews increases. This is typical in many review systems where most users contribute only a few reviews.
  - The highest point on the left indicates that the majority of users have contributed only one review, which is common in user-generated content platforms.
- **Plot Characteristics**:
  - **Scatter Plot**: The use of a scatter plot is appropriate here as it helps to visualize the distribution of discrete counts (number of reviews) among a population (users).
  - **Data Points**: The specific counts, such as for 0, 5, 10, 15, 20, 25, 30, 35, and 40 reviews, help identify common patterns of user engagement on the platform.

---

## Sample 7: Get User's Review Summary (Invalid User ID)

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 4

Options:
1. Plot Review Distribution
2. Get User's Review Summary
Enter your choice (1 or 2): 2

Enter user ID: 001
```

### System Output:

```
User ID 001 doesn't exist, please try again.
If you're unsure about the correct ID, here are two random user IDs you can try: ['i-v015Oa8uK4JiHe0GC8mQ', 'bvqCg5gUYaNk_uWvAmFb2A']
```

### Explanation:

- **Option Selected**: The user selected **Option 4** for **Review Summary** from the main menu.
- **Sub-option Selected**: The user chose **Option 2**, which is to **Get User's Review Summary**.
- **User ID Entry**: The user entered an invalid user ID (`001`), which does not exist in the database.
- **System Response**: 
  - The system promptly informs the user that the user ID does not exist.
  - Provides a helpful suggestion by offering two alternative, random user IDs that the user can try to retrieve summaries for, enhancing user experience by reducing frustration and guiding the user towards valid queries.
- **Observations**:
  - This feature shows the robustness of the system in handling errors and guiding the user to rectify them.
  - Providing alternative IDs helps ensure that users can still engage with the system even if they initially make a mistake.

---

## Sample 8: Get User's Review Summary (Valid User ID)

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 4

Options:
1. Plot Review Distribution
2. Get User's Review Summary
Enter your choice (1 or 2): 2

Enter user ID: i-v015Oa8uK4JiHe0GC8mQ
```

### System Output:

```
Summary of user i-v015Oa8uK4JiHe0GC8mQ's reviews

Number of user's reviews: 99

Bounding box of the businesses:
[List of addresses]

Top-10 most frequent words:
[('i', 228)]
[('was', 200)]
[('you', 91)]
[('we', 87)]
[('are', ,)]
[('but', 73)]
[('my', 68)]
[('great', 66)]
[('place', 64)]
[('have', 59)]

Top-10 most frequent phrases:
[('It was', 25)]
[('in the', 17)]
[('of the', 17)]
[('and the', 16)]
[('I have', 16)]
[('is a', 15)]
[('on the', 15)]
[('I ordered', 15)]
[('There is', 14)]
[('a nice', 13)]

Three most representative sentences:
["  It's difficult to find comfortable seating during rush hours and if you are unfamiliar with where to find the food that you have no clue what you are in the mood to eat, you get pushed out if the way by shoppers"]
['Lastly, tiramisu dessert was prepared at our table, step-by-step starting was the lady fingers, drizzing them with fresh espresso, topped with thick mascarpone, sprinkled with ground cocoa, annndddd more espresso']
["I had heard some great reviews of this plac, so I looked them up, read the chef's impressive bio online, and decided to make New Year's Eve reservations on open table at the last minute"]
```

### Explanation:

- **Option Selected**: Again, **Option 4** for **Review Summary**.
- **Sub-option Selected**: **Option 2** for **User's Review Summary**.
- **User ID Entry**: A valid user ID (`i-v015Oa8uK4JiHe0GC8mQ`) is provided.
- **Results**:
  - The user has contributed **99 reviews**.
  - **Bounding Box**: Lists addresses of businesses reviewed, showcasing geographical diversity in the user's reviews.
  - **Top-10 Most Frequent Words and Phrases**: Highlights common words and phrases, offering insights into the user's writing style and frequent topics.
  - **Representative Sentences**: Provides direct examples of the user's review content, giving a snapshot of their perspectives and review contexts.
- **Observations**:
  - Detailed user review summaries like this can help in understanding individual user behavior, preferences, and their engagement with various businesses.
  - This feature is useful for market analysis, customer relationship management, and personalizing user experiences based on review patterns.

## Sample 9: Exiting the Search Engine

### User Input:

```
Options:
1. Keyword Search of Businesses
2. Keyword Search of Reviews
3. Geospatial Search of Businesses
4. Review Summary
5. Exit
Enter your choice (1-5): 5
```

### System Output:

```
Bye!
```

### Explanation:

- **Option Selected**: The user selected **Option 5**, which is to **Exit** from the main menu.
- **System Response**:
  - The system acknowledges the user's choice to exit by displaying a simple farewell message, **"Bye!"**.
- **Observations**:
  - This feature demonstrates the system's ability to terminate sessions effectively, respecting the user's intention without additional prompts or delays, thereby enhancing the user experience.
- **Process**:
  - After displaying the farewell message, the system would typically terminate the session, closing any open resources or saving necessary states as configured.

