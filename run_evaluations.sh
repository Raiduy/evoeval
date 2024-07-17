#!/bin/bash

declare -a categories=("EvoEval_combine" "EvoEval_creative" "EvoEval_subtle" 
                        "EvoEval_verbose" "EvoEval_concise" "EvoEval_difficult" 
                        "EvoEval_tool_use" "humaneval")

for category in "${categories[@]}"
do
    for llm in ./solutions/*/*/ ; do
        [ -L "${llm%/}" ] && continue
        #echo "$llm"
        #echo "$category"
        python3 ./evoeval/evaluate.py --dataset "$category" --samples "$llm$category/"
    done
done


