from codeforces.contests import ContestHelper
from codeforces_api import CodeforcesParser,CodeforcesApi
import cf_base_class
import pandas as pd
import os
cf_parser = CodeforcesParser()
cf_api = CodeforcesApi()


def crawl_all_problem():
    ch = ContestHelper()
    finished_contests = ch.get_contests(phase='FINISHED')

    csv_filename = 'finished_contest_problems.csv'
    if os.path.isfile(csv_filename):
        # Load existing data from CSV
        df = pd.read_csv(csv_filename)
        print(f'df content {df.shape}')
    else:
        # Create an empty DataFrame if CSV doesn't exist
        df = pd.DataFrame()

    for contest in finished_contests:
        try:
            # print(contest)

            if not df.empty and (df['contest_id']==contest['id']).any():
                continue

            ret = cf_api.contest_standings(contest['id'])

            problems = ret['problems']
            problems = [p.to_dict() for p in problems]

            for p in problems:
                if df.empty:
                    df = pd.DataFrame(columns=p.keys())
                df = df.append(p, ignore_index=True)
            print(f'Done! ')
        except Exception as e:
            print(f"An error occurred: {e}")
    df.to_csv('finished_contest_problems.csv')



if __name__ == '__main__':
    crawl_all_problem()