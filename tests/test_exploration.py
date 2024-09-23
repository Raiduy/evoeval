import pandas as pd

df = pd.read_json("hf://datasets/evoeval/EvoEval_difficult/test.jsonl", lines=True)


print(df.columns)

