from codeforces.contests import ContestHelper
from codeforces_api import CodeforcesParser, CodeforcesApi
import cf_base_class
import pandas as pd
import os

cf_parser = CodeforcesParser()
cf_api = CodeforcesApi()
contest_helper = ContestHelper()

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)

# Specify the database and collection
db = client['contest_database']  # Replace 'contest_database' with your database name
collection = db['contest_submissions']  # Replace 'contest_submissions' with your collection name


def create_database_and_collection():
    # Create the collection if it doesn't exist
    if 'contest_submissions' not in db.list_collection_names():
        db.create_collection('contest_submissions')


def crawl_contest_submission(contest_id):
    all_submissions = contest_helper.get_submissions(contest_id)
    for submission in all_submissions:
        # if not df.empty and (df['contest_id'] == contest['id']).any():
        #     continue

        submission_info = submission.to_dict()
        author = submission.author

        print(submission_info.keys())

        # Insert submission directly into MongoDB collection
        collection.insert_one(submission_info)


def crawl_submission_code(contest_id, submission_id):
    pass


if __name__ == '__main__':

    # Create database and collection if they don't exist
    create_database_and_collection()

    # Call the function to crawl contest submissions
    finished_contests = contest_helper.get_contests(phase='FINISHED')

    for contest in finished_contests:
        crawl_contest_submission(contest['id'])

    # Close the MongoDB connection
    client.close()
