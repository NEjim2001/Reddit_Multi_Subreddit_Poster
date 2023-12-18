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

### Finish Authentication with PRAW

```bash
python refreshtoken.py
```

## Set Up Subreddit CSV File

1. **Go to Google Sheets, make a copy, rename "subreddits", and Fill out Information**

https://docs.google.com/spreadsheets/d/1Odn01NUtt-9CFxqdaXuben-nz8RQdGxieiDF87s6aYs/edit?usp=sharing


2. **Download the CSV file from Google Drive:**
   - Open your Google Sheets document.
   - Navigate to the top left corner and click on "File."
   - From the dropdown menu, select "Download."
   - Choose the option "Comma Separated Values (.csv)."


3. **Add CSV File to user_data folder (Replace previous document)**

## Run Application

```bash
python main.py
```


# Contributing

Feel free to contribute to this guide by opening issues or pull requests.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

