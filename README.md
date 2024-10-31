# AI6122_Search_Engine
# Installation Guide and Usage Instructions

## Table of Contents
1. [Running Yelp Data Analysis on Google Colab](#1-running-yelp-data-analysis-on-google-colab)
2. [Running Comprehensive Text Analysis on Google Colab](#2-running-comprehensive-text-analysis-on-google-colab)
3. [Installation Guide and Usage Instructions of Search Engine](#3-installation-guide-and-usage-instructions-of-search-engine)
4. [Comparison Results Analysis Tool](#4-comparison-results-analysis-tool)

## 1. Running Yelp Data Analysis on Google Colab

The analysis notebook, `Yelp_NJ.ipynb`, is designed to process and analyze Yelp data, which may include tasks like cleaning, exploring, and visualizing Yelp review data to uncover trends and insights about businesses, reviews, and customer sentiment. Yelp data analysis offers valuable insights into customer behavior, business trends, and regional preferences. With Google Colab, users can easily run this analysis in a cloud environment, leveraging Colab's free GPU and TPUs for faster processing. 

### 1. Requirements

- **Google Account**: Required to access Google Colab.
- **Google Colab**: No installations are required on your local machine as all processing is done in Colab's cloud environment.
- **Dataset**: The dataset should be uploaded or available in the correct path within Colab to avoid path issues.

The required packages for the analysis (such as `pandas`, `numpy`, and `matplotlib`) are pre-installed on Google Colab. However, additional libraries may be installed as specified in the notebook.

### 2. Setup

1. **Upload the Notebook to Colab**: Open [Google Colab notebook](https://colab.research.google.com/drive/1xc-yvFelBFmcRKR-bjgMOQnkB4wVjBQf?usp=sharing) and upload the `Yelp_NJ.ipynb` file.

2. **Upload or Mount Data**:
   - If your dataset is stored locally, upload it directly into the Colab session by navigating to Files > Upload.
   - Alternatively, if you are working with a dataset on Google Drive, mount your Google Drive to access the data directly. Run the following code cell in Colab to mount your drive:

     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```

3. **File Paths**: Ensure that all file paths in the notebook are updated according to your Colab environment (e.g., `/content/drive/MyDrive/...` if using Google Drive).

### 3. Running the Notebook

To execute the notebook:

1. Start by running cells sequentially from the beginning. The notebook's cells are designed to perform:
   - **Data Import**: Loads the Yelp data from the specified source.
   - **Data Preprocessing**: Cleans and organizes the data.
   - **Exploratory Data Analysis (EDA)**: Visualizes trends, distributions, and patterns in Yelp reviews.

2. **Save Outputs**: You can save results or visualizations by downloading them from Colab or saving them to Google Drive.

### Expected Output
1. Baisc Statistics
```Shell
Total number of businesses: 8536

Top 10 business categories:
categories
Restaurants                  3341
Food                         1717
Shopping                     1228
Beauty & Spas                 819
Home Services                 741
Pizza                         717
Automotive                    682
Sandwiches                    602
Health & Medical              595
Event Planning & Services     570
Name: count, dtype: int64

Business rating statistics:
count    8536.000000
mean        3.459114
std         0.960938
min         1.000000
25%         3.000000
50%         3.500000
75%         4.000000
max         5.000000
Name: stars, dtype: float64

Review count statistics per business:
count    8536.000000
mean       29.268627
std        49.686376
min         5.000000
25%         7.000000
50%        13.000000
75%        29.000000
max       709.000000
Name: review_count, dtype: float64

Total number of reviews: 260897

Review distribution by star ratings:
stars
1     51506
2     22838
3     25853
4     50209
5    110491
Name: count, dtype: int64

Average review length: 570.44 characters

Review distribution by year:
year
2005        3
2006      101
2007      384
2008      988
2009     2045
2010     4076
2011     7047
2012     9865
2013    14410
2014    19752
2015    26961
2016    29271
2017    31698
2018    33873
2019    33889
2020    21988
2021    23416
2022     1130
Name: count, dtype: int64

Top 10 users with the most interactions:
                      user_id  total_votes
427    -G7Zkl1wIWBBmD0KRy_sCw        15360
60813  aaEr2-3Qaa4jo9rkjiqibA         5341
46859  SeWsQoYPbQuMAqfRNNS6Jg         5210
24410  ET8n-r7glWYqZhuR6GcdNw         4880
77594  lRRuTimITgwzoXLIM3g9qw         3959
99626  zUk_Ww2q1At1QSyRbUjIGQ         3887
38188  N8ITUUDRBpo1hTNDvk1byA         3733
40365  OXlfFHsM15JYh_lvat2w2w         3488
27867  GcdYgbaF75vj7RO6EZhPOQ         2844
94195  w6OPX0bAyxIFKWkGDJrtGA         2554
```
![image](https://github.com/user-attachments/assets/b0230c7d-d171-43a5-9bed-9f857c3e4344)
![image](https://github.com/user-attachments/assets/02b5f257-1d95-4743-9a8d-77d21045384a)
![image](https://github.com/user-attachments/assets/a54c3bf2-6a43-41a7-87fd-0b63d85fef6b)
![image](https://github.com/user-attachments/assets/7c45665d-a0f5-4daf-9d47-7f5641a7934b)

2. Tokenization & Stemming
```Shell
Selected Business IDs: ['9X2rQUHO_ka0k7tu7wr_7g', 'O2l31-gVCX2R9yRTtGPyaQ']，9X2rQUHO_ka0k7tu7wr_7g - Number of words before stemming: 1433
9X2rQUHO_ka0k7tu7wr_7g - Number of words after stemming: 1175
O2l31-gVCX2R9yRTtGPyaQ - Number of words before stemming: 845
O2l31-gVCX2R9yRTtGPyaQ - Number of words after stemming: 743
```
![image](https://github.com/user-attachments/assets/fd8993d9-df84-497a-bf0e-4940e41c9094)
![image](https://github.com/user-attachments/assets/a9555cce-6017-421d-a7d2-99aa665a0bfb)
![image](https://github.com/user-attachments/assets/3b5fa1ba-b048-4252-b4f0-abf31e5cff9e)
![image](https://github.com/user-attachments/assets/1092da21-2bc6-4c37-bd11-bf9d860e16f4)
![image](https://github.com/user-attachments/assets/d64a30f1-1e5e-4f05-be71-ea31129cdfa1)
![image](https://github.com/user-attachments/assets/27a6b65c-64d9-416f-9654-05415c282883)
![image](https://github.com/user-attachments/assets/b1f482c3-fde9-4652-89eb-039186dc35b3)
![image](https://github.com/user-attachments/assets/3c651b2a-a453-4bc6-ba70-395e7b7889d2)
![image](https://github.com/user-attachments/assets/49cc4438-0a6c-42d6-bc5c-006f108acd40)
![image](https://github.com/user-attachments/assets/31845f26-2f4e-4972-b905-2255e2390573)
![image](https://github.com/user-attachments/assets/fcc90b25-b1be-4787-9b38-0839decdcd80)
![image](https://github.com/user-attachments/assets/6aa0cd42-186f-4f9b-82c4-e7975210821a)
![image](https://github.com/user-attachments/assets/43c9d604-937c-4eca-a39f-461730ca3ff9)
![image](https://github.com/user-attachments/assets/25a94db9-f061-41e3-bbb9-3f12b25789ff)
![image](https://github.com/user-attachments/assets/8a6468c4-a5fe-4590-a1ee-048af82b6110)
![image](https://github.com/user-attachments/assets/a4da7fa0-f0fd-40c7-a68f-f0a824f6f2df)
![image](https://github.com/user-attachments/assets/f20af904-c68a-43a0-8edf-243295ae5b4c)
![image](https://github.com/user-attachments/assets/1de5a954-45f4-4545-8be1-3d681034c633)
![image](https://github.com/user-attachments/assets/341427c8-d564-4894-8b84-d4756aacb17b)
![image](https://github.com/user-attachments/assets/243b5b4b-1ed4-4ab2-b10f-4f6c211f2679)
![image](https://github.com/user-attachments/assets/d79c619d-4a4a-43b5-9a13-3058172d6f4b)
![image](https://github.com/user-attachments/assets/3884ad2f-3ede-4519-a748-956a3b6241c0)


![image](https://github.com/user-attachments/assets/42f835be-c275-4fb0-85cd-faecf802b050)

![image](https://github.com/user-attachments/assets/090c1133-97e3-444f-bc27-44b3af843163)

![image](https://github.com/user-attachments/assets/1f21f9b0-2f84-466e-a2b8-8fee0f2d4798)

![image](https://github.com/user-attachments/assets/a9010695-e608-4de1-8e58-cefca9370bb8)

![image](https://github.com/user-attachments/assets/001f7f6c-d483-4711-89ab-9bd9f08dc566)

![image](https://github.com/user-attachments/assets/54a8e6b3-7488-4e59-b27d-d56cb9311eb6)


## 2. Running Comprehensive Text Analysis on Google Colab
This guide explains how to run a comprehensive text analysis script on Google Colab. The script analyzes multiple text files (from StackOverflow, Reddit, news articles, and patents) for readability, structural elements, sentiment, and use of technical terms. This process provides insights into the writing style differences across these text types. You can start by opening this [Google Colab notebook](https://colab.research.google.com/drive/1xc-yvFelBFmcRKR-bjgMOQnkB4wVjBQf?usp=sharing).

### Instructions

#### Step 1: Prepare and Upload Text Files to Google Drive
1. Organize the files you want to analyze:
  - Ensure all text files are in `.txt` or `.pdf` format.
  - Files should cover each of the four types: StackOverflow, Reddit, news articles, and patents, ideally two files per category.
2. Upload all files to Google Drive:
  - Create a folder named `TextFiles` in your Google Drive’s main directory.
  - Place all `.txt` and `.pdf` files in this `TextFiles` folder.

#### Step 2: Set Up Google Colab

``1. Open Google Colab in your web browser.
2. Create a new notebook by going to File > New Notebook.

#### Step 3: Install Dependencies and Mount Google Drive

Copy and paste the following code into the first cell to install necessary libraries and mount Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')

!pip install pdfplumber
!pip install textblob
!pip install textstat
import nltk
nltk.download('punkt')  # Downloads the punkt tokenizer from NLTK
```

#### Step 4: Run the Analysis Code

1. In a new cell, paste the main analysis code provided.
2. Ensure the code points to the correct directory (`/content/drive/MyDrive/TextFiles`).
3. Run this cell to start the analysis on all uploaded files.

### Expected Output

Upon running, the code will analyze all files in the `TextFiles` folder. For each file, it will output details on readability, structural elements, sentiment, and uppercase word usage. The output will display results sequentially for each of the 8 files, with clear section separators, as shown below:

```markdown
==================================================
Analyzing: stackoverflow1.txt
==================================================

Complexity and Readability:
- Number of sentences      : 28
- Number of words          : 680
- Average sentence length  : 25.64 words
- Unique words ratio       : 0.46
- Flesch-Kincaid score     : 12.60

Structural Elements:
- Bullet points            : 0
- Code blocks              : 0
- Numbered items           : 0

Sentiment Analysis:
- Polarity (emotion)       : 0.20 (range -1 to 1)
- Subjectivity             : 0.41 (range 0 to 1)

Uppercase Words Analysis:
- Uppercase words count    : 21
- Uppercase words ratio    : 0.03

Sample Sentences:
- Enterprise 2024.7:
- Empower your subject matter experts to contribute
This release introduces Subject Matter Expert (SME) Auto-Assign to the Stack Overflow for Teams experience so expert knowledge is automatically captured, verified, and distributed to users.

==================================================
```

The analysis will continue similarly for all 8 files, covering the four text categories.

**Notes**
- The analysis is designed to run through all uploaded files in one go, providing comprehensive results for each file.
- Each text file’s results will display sentence and word counts, readability scores, sentiment analysis, uppercase usage, and example sentences.
- The code is designed for English-language text analysis; adjustments may be needed for other languages.

## 3. Installation Guide and Usage Instructions of Search Engine
Welcome to the installation guide for our **Search Engine for Businesses and Reviews in New Jersey (NJ)**. This guide will help you set up the system on your machine and provide instructions on how to use it effectively.

**Note:** The data and the program are available at [Kaggle: Yelp NJ Dataset](https://www.kaggle.com/datasets/dyleslie/yelp-nj).  Also, we provide two different application versions: `search_engine.exe` for Windows and `search_engine` for macOS.

### Prerequisites

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

### Installation Steps

#### Step 1: Download the Data and Program

- Visit the [Kaggle: Yelp NJ Dataset](https://www.kaggle.com/datasets/dyleslie/yelp-nj) page.
- Download the dataset and program files.
- Extract the files to a directory on your machine.

#### Step 2: Install Python 3

If you don't have Python 3 installed, download it from the [official website](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

#### Step 3: Install Required Python Packages

Open your terminal or command prompt and run the following commands to install the required packages:

```bash
pip install whoosh matplotlib termcolor
```

#### Step 4: Prepare the Directory Structure

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

#### Step 5: Generate the Indexes

Before using the search functionalities, you need to generate the indexes for the business and review data.

Run the `indexer.py` script:

```bash
python indexer.py
```

This script will:

- Read data from `data/nj_business.json` and `data/nj_review.json`.
- Create indexes in the `index/` directory.

**Note:** The indexing process may take several minutes, depending on the size of the data files. Progress messages and a plot showing the indexing time will be displayed during the process.


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

#### Option 1: Keyword Search of Businesses

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

#### Option 2: Keyword Search of Reviews

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

#### Option 3: Geospatial Search of Businesses

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

#### Option 4: Review Summary

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

#### Option 5: Exit

- **Description:** Exit the search engine.

- **Instructions:**
  - Choose option `5` to exit the program.
 
## 4. Comparison Results Analysis Tool

The **Comparison Results Analysis Tool** is a command-line application designed to help users quickly filter and analyze sentences extracted from reviews containing comparative statements. This tool enables users to filter comparisons by type, specific keywords, subjects, or display specific rows within a selected range. The tool provides easy access to comparison data, such as determining positive or negative sentiment and identifying subjects in the comparisons.

### Features

- **View Positive Comparisons:** Display all positive comparisons.
- **View Negative Comparisons:** Display all negative comparisons.
- **Filter by Keyword:** Search for comparisons that contain a specific keyword.
- **Filter by Subject:** Find all comparisons involving a specific subject.
- **Display Row Range:** View comparisons within a specified row range.

### Usage Guide

Upon running the script, a menu will appear with several options:

```plaintext
==================================================
          🔍 Comparison Results Analysis Tool
==================================================
Options:
   1️⃣  View all positive comparisons
   2️⃣  View all negative comparisons
   3️⃣  Filter by keyword (e.g., 'better than')
   4️⃣  Filter by subject (e.g., 'pizza')
   5️⃣  Display a range of rows (e.g., rows 10 to 20)
   6️⃣  Exit
==================================================
Select an option (1-6):
```
### Option Descriptions
1. View all positive comparisons: Displays the first 10 positive comparisons in a tabular format.![image](https://github.com/user-attachments/assets/0ed68145-6aee-44b8-a1b8-a2438f75263d)
2. View all negative comparisons: Displays the first 10 negative comparisons in a tabular format.![image](https://github.com/user-attachments/assets/32f91c35-8874-4d42-94a3-7486def5c63e)
3. Filter by keyword: The tool prompts for a keyword.
Example: Enter `not as` to see all comparisons containing this phrase.![image](https://github.com/user-attachments/assets/3893aeaa-1265-4116-9798-b8fea12cc7b1)
4. Filter by subject: The tool prompts for a subject.
Example: Enter `pizza` to display all comparisons where either `subject_a` or `subject_b` is "pizza".![image](https://github.com/user-attachments/assets/d96cd7bc-0c93-4304-9a8e-6ca0fd325b26)
5. Display a range of rows: The tool prompts for a start and end row number.
Example: Enter `10` and `20` to display rows from 10 to 20 in the dataset.![image](https://github.com/user-attachments/assets/bf4e853f-f859-4947-90fd-2092f4018745)
6. Exit: Closes the application with a goodbye message.![image](https://github.com/user-attachments/assets/139edc05-4a61-4fb0-ae90-7e4db735c8df)
---


# Explanation of Sample Output Obtained from Search Engine System

Below are sample outputs obtained from using the search engine system for businesses and reviews in New Jersey. Each sample includes the user inputs and the system responses, followed by explanations to help you understand how the system works.

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

![Distribution of reviews contributed by users](https://i.postimg.cc/fRKNWhHh/Figure-1.png)

### Explanation:

- **Option Selected**: The user selected **Option 4** for **Review Summary** from the main menu.
- **Sub-option Selected**: Within the review summary options, the user selected **Option 1**, which is to **Plot Review Distribution**.
- **Results**:
  - The displayed graph is Distribution of reviews contributed by users.
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

