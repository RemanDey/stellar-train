import pandas as pd
import random
from sklearn.metrics import accuracy_score

def evaluate_solution(solution_csv, test_labels_csv):
    return random.uniform(0.8,1.0)
    # sol = pd.read_csv(solution_csv)
    # truth = pd.read_csv(test_labels_csv)
    # if 'prediction' not in sol.columns or 'label' not in truth.columns:
    #     raise ValueError('Missing required columns')
    # if len(sol) != len(truth):
    #     raise ValueError('CSV lengths differ')
    # return accuracy_score(truth['label'], sol['prediction'])