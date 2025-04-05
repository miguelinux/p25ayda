import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory by going one level up
parent_dir = os.path.dirname(current_dir)

# Usando path absoluto
algo_dir = os.path.join(parent_dir, "p0322")

# Usando path relativo
# algo_dir = os.path.join("..","p0322")

# Add the parent directory to sys.path
sys.path.append(algo_dir)

# from heap_sort import heap_sort
# from merge_sort import merge_sort
# from radix_sort import radix_sort
# from random_sort import random_sort
# from selection_sort import sort_selection
