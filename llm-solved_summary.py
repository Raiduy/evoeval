import os
import re
import sys
import json
from textwrap import indent
import pandas as pd

SOLUTIONS_FOLDER = './solutions'


def parse_json(path):
    counter = 0
    solved_list = []
    with open(path) as f:
        data = json.load(f)
        for problem in data['eval']:
            if(data['eval'][problem][0]['base_status'] == "pass"):
                counter += 1
                solved_list.append(problem.split('/')[-1])
        return counter, solved_list


def get_solved(sol_folder, subset):
    df = pd.DataFrame(columns=['LLM', 'solved_num', 'solved_ids'])
    for folder in os.listdir(sol_folder):
        difficult_path = os.path.join(sol_folder, folder, folder, subset)
        for path, subdirs, files in os.walk(difficult_path):
            for file in files:
                fullpath = os.path.join(path, file)
                if str(fullpath).endswith('.json'):
                    solved_num, solved_ids = parse_json(fullpath)
                    tmp = pd.DataFrame({'LLM': folder, 
                                        'solved_num': solved_num, 
                                        'solved_ids': [solved_ids]})
                    df = pd.concat([df, tmp])
        
    return df

def finalize_results(df):
    intersection = df[df['LLM'] == 'qwen-7b-1.5_temp_0.0']['solved_ids'].values[0]
    for id_list in df['solved_ids'].values:
        intersection = set(intersection).intersection(set(id_list))
    tmp = pd.DataFrame({'LLM': 'Intersection', 
                        'solved_num': len(intersection), 
                        'solved_ids': [list(intersection)]})
    print(intersection)
    print(tmp)
    df = pd.concat([df, tmp])
    print(df)
    return df

if __name__ == "__main__":
    sol_folder = sys.argv[1]
    evoeval_subset = sys.argv[2]
    df = get_solved(sol_folder, evoeval_subset)
    df = finalize_results(df)
    print(df)
    df.to_csv(f'{evoeval_subset}_results.csv', index=False)

