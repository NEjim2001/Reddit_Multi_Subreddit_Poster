# Reddit Multi-Subreddit Poster

## Overview

A Python program that enables users to efficiently post content in multiple subreddits simultaneously. Leveraging the power of pandas for CSV handling and praw for Reddit API interaction, this tool streamlines the process of posting across various communities.

## Features

- **CSV Integration**: Import a list of subreddits, post titles, body text, and URLs from a CSV file.
- **Efficient Posting**: Quickly submit content to multiple subreddits without manual intervention.
- **Authentication**: Securely authenticate with Reddit using PRAW, ensuring a seamless posting experience.

# Getting Started

## Reddit Authentication using PRAW Guide
This guide provides step-by-step instructions on how to authenticate with Reddit using PRAW (Python Reddit API Wrapper).

### Prerequisites

- Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- Reddit account. If you don't have one, you can create an account on [Reddit](https://www.reddit.com/).

### Installation (Open Terminal At Project Location)

Install PRAW using pip:

```bash
pip install praw
```

### Obtaining Reddit API Credentials

1. Log into Reddit Account.
2. Go to the [Reddit Apps page](https://www.reddit.com/prefs/apps).
2. Scroll down to the "Developed Applications" section.
3. Click on the "Create App" or "Create Another App" button.
4. Fill out the required fields:
   - **name**: Your app's name (e.g., MyRedditApp).
   - **App type**: Choose "script."
   - **Description**: Brief description of your app (Optional).
   - **About Url**: Choose "script."
   - **Redirect Uri**: http://localhost:8080

5. Click on the "Create app" button.
6. Your app details will appear on the "Developed Applications" page. Note the following:
   - **client_id**: This is your app's unique identifier.
   - **client_secret**: This is your app's secret.
<img width="859" alt="Screenshot 2023-12-18 at 8 49 01 AM" src="https://github.com/NEjim2001/Reddit_Multi_Subreddit_Poster/assets/144557253/eaf31ba7-1e73-4604-ae98-b98869feab5b">

### Finish Authentication with PRAW

```bash
python refreshtoken.py
```
**Terminal**

<img width="703" alt="Screenshot 2023-12-18 at 9 54 42 AM" src="https://github.com/NEjim2001/Reddit_Multi_Subreddit_Poster/assets/144557253/52a650c3-5aa1-442d-8723-70c1db7ac02c">

## Set Up Subreddit CSV File

1. **Go to Google Sheets, make a copy, rename copy "subreddits", and fill out the information (Keep Orange Header Row)**

https://docs.google.com/spreadsheets/d/1Odn01NUtt-9CFxqdaXuben-nz8RQdGxieiDF87s6aYs/edit?usp=sharing
   - Rules:
      - Do not touch the Orange Header Row.
      - Ensure Every Post has a Title.
      - Include a Link or Body Text in Every Post (Choose one or the other).


<img width="1185" alt="Screenshot 2023-12-18 at 8 57 14 AM" src="https://github.com/NEjim2001/Reddit_Multi_Subreddit_Poster/assets/144557253/977cbc77-c503-41a9-94cc-4d0a3fcf7e3a">


2. **Download the CSV file from Google Drive:**
   - Open your Google Sheets document.
   - Navigate to the top left corner and click on "File."
   - From the dropdown menu, select "Download."
   - Choose the option "Comma Separated Values (.csv)."
<img width="587" alt="Screenshot 2023-12-18 at 8 57 47 AM" src="https://github.com/NEjim2001/Reddit_Multi_Subreddit_Poster/assets/144557253/751e06dc-4010-48aa-99ff-34cb6cfc7471">




3. **Add CSV File to user_data folder (Replace previous document)**

## Run Application

```bash
python main.py
```


# Contributing

Feel free to contribute to this guide by opening issues or pull requests.

---

