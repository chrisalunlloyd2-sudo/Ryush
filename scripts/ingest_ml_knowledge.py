import sys
import os
sys.path.append(os.path.expanduser('~'))
import code_manager

algorithms = {
    "Linear Regression": "Supervised Learning, finding best-fitting straight line for continuous predictions (house prices, sales). Baseline for complex models.",
    "Logistic Regression": "Classification, mapping probabilities between 0 and 1 via sigmoid function. Ideal for spam filtering/churn.",
    "Decision Trees": "Flowchart-based predictive modeling. High interpretability, handles categorical/numerical data, prone to overfitting.",
    "Random Forests": "Ensemble learning. 'Wisdom of crowds', reduces overfitting by averaging multiple trees. Robust/accurate.",
    "Support Vector Machines": "Optimal boundary seekers, finding maximum margin between classes. Excellent for high-dimensional, small-to-medium data.",
    "Naive Bayes": "Fast probabilistic classification. Uses Bayes' theorem. Lightning-fast, perfect for text classification (spam, sentiment).",
    "K-means Clustering": "Unsupervised learning. Grouping similar data points together without labels. Segmenting customers/anomalies."
}

def ingest():
    for name, desc in algorithms.items():
        code = f"# Algorithm: {name}\n# Description: {desc}"
        code_manager.add_code(name, code, "machine_learning, algorithm, predictive_modeling, supervised, unsupervised")
    print("Machine Learning Foundations ingested.")

if __name__ == "__main__":
    ingest()
