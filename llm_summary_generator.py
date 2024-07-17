import os
import re
import sys
import json
from textwrap import indent
import pandas as pd

SOLUTIONS_FOLDER = './solutions'
EVAL_SUBSETS = ["EvoEval_combine", "EvoEval_creative", "EvoEval_subtle", 
                "EvoEval_verbose", "EvoEval_concise", "EvoEval_difficult", 
                "EvoEval_tool_use", "humaneval"]

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
    solved_min = df['solved_num'].min()
    intersection = df[df['solved_num'] == solved_min]['solved_ids'].values[0]
    for id_list in df['solved_ids'].values:
        intersection = set(intersection).intersection(set(id_list))
    tmp = pd.DataFrame({'LLM': 'Intersection', 
                        'solved_num': len(intersection), 
                        'solved_ids': [list(intersection)]})
    df = pd.concat([df, tmp])
    return df

if __name__ == "__main__":
    sol_folder = sys.argv[1]
    if len(sys.argv) > 2:
        EVAL_SUBSETS = [sys.argv[2]]
    for evoeval_subset in EVAL_SUBSETS:
        df = get_solved(sol_folder, evoeval_subset)
        df = finalize_results(df)
        print(f'{evoeval_subset}: {df["solved_num"].tail(1).values[0]}')
        df.to_csv(f'./llm_summaries/{evoeval_subset}_results.csv', index=False)

# python3 ./llm_summary_generator.py ./solutions", "EvoEval_combine


