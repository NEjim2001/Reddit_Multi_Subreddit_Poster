# THINKING PROFITS
import json
import praw
import time
import pandas as pd
import glob
import sys


TIME_DELAY_SECONDS = 5

credentials = 'client_secrets.json'
with open(credentials) as f:
    creds = json.load(f)

reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

file_paths = glob.glob("user_data/*.csv")

if not file_paths:
    print("No CSV files found in the 'user_data' directory. Exiting script.")
    sys.exit()


file_path = file_paths[0]
data = pd.read_csv(file_path, header=0)

failed_post = []
for row, subreddit_data in data.iterrows():
    subreddit_name = subreddit_data.Subreddit  # Access column by name
    flair = subreddit_data.Flair
    post_title = subreddit_data['Post Title']
    body_text = subreddit_data['Body Text']
    url_link = subreddit_data['URL Link']

    subreddit = reddit.subreddit(subreddit_name)

    if pd.isna(flair):
        try:
            if pd.isna(post_title):
                raise ValueError("Must have Post Title")

            if pd.isna(body_text):
                reddit.subreddit(subreddit_name).submit(post_title, url=url_link)
                print(f"Post completed in {subreddit_name}")
            elif pd.isna(url_link):
                reddit.subreddit(subreddit_name).submit(post_title, selftext=body_text)
                print(f"Post completed in {subreddit_name}")
            else:
                raise ValueError("Either 'Body Text' or 'Url Link' must be provided.")
        except Exception as e:
            print("Error posting in " + str(e) + "Skipping...")
            failed_post.append(subreddit_name)
        time.sleep(TIME_DELAY_SECONDS)
    else:
        # List of user selectable flairs. Expect -> [{}{}{}]
        available_flairs = list(subreddit.flair.link_templates.user_selectable())
        # Find the flair_template_id for the given flair
        matching_flair = next((item for item in available_flairs if item['flair_text'] == flair), None)

        try:
            if pd.isna(post_title):
                raise ValueError("Must have Post Title")

            if matching_flair:
                flair_id = matching_flair['flair_template_id']

                if pd.isna(body_text):
                    submission = reddit.subreddit(subreddit_name).submit(post_title, url=url_link,
                                                                         flair_id=flair_id)
                    print(f"Post completed in {subreddit_name}")
                elif pd.isna(url_link):
                    submission = reddit.subreddit(subreddit_name).submit(post_title, selftext=body_text,
                                                                         flair_id=flair_id)
                    print(f"Post completed in {subreddit_name}")
                else:
                    raise ValueError("Either 'Body Text' or 'Url Link' must be provided.")
            else:
                raise Exception("Listed Flair doesn't exist")
        except Exception as e:
            print("Error posting in " + subreddit_name + " Skipping...")
            error_message = subreddit_name + " Reason: " + str(e)

            # Append additional information if the exception is related to missing flair
            if "Flair doesn't exist" in str(e):
                error_message += f"\nUser Selectable Flair: {', '.join([item['flair_text'] for item in available_flairs])}\n"

            failed_post.append(error_message)
        time.sleep(TIME_DELAY_SECONDS)


if len(failed_post) > 0:
    print(f"[Failed to post in] \n{''.join(failed_post)}")
else:
    print("[All Post Successful]")
