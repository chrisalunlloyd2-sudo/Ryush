import sys
import os
sys.path.append(os.path.expanduser('~'))
import code_manager
import project_registry

# Mapping algorithms to their functional domain and Axiomatix set for the Genetic Foundry
algorithms = {
    "Linear Regression": {"tags": "regression, supervised, predictive", "area": "foundations", "axiomatix": "{linear_modelling}"},
    "Logistic Regression": {"tags": "classification, supervised, probabilistic", "area": "foundations", "axiomatix": "{probabilistic_modelling}"},
    "Decision Trees": {"tags": "classification, regression, supervised, tree", "area": "foundations", "axiomatix": "{tree_structure}"},
    "Naive Bayes": {"tags": "classification, supervised, probabilistic, text", "area": "nlp", "axiomatix": "{probabilistic_graphical_models}"},
    "K-Nearest Neighbors": {"tags": "classification, regression, supervised, non-parametric", "area": "foundations", "axiomatix": "{spatial_analysis}"},
    "Support Vector Machines": {"tags": "classification, regression, supervised, boundary", "area": "complex_boundary", "axiomatix": "{boundary_optimization}"},
    "Random Forests": {"tags": "ensemble, classification, regression, supervised", "area": "ensemble", "axiomatix": "{ensemble_learning}"},
    "Gradient Boosting": {"tags": "ensemble, supervised, gradient_descent", "area": "ensemble", "axiomatix": "{gradient_optimization}"},
    "Regularized Models": {"tags": "regression, supervised, linear, regularization", "area": "foundations", "axiomatix": "{feature_selection}"},
    "K-Means Clustering": {"tags": "unsupervised, clustering", "area": "clustering", "axiomatix": "{iterative_grouping}"},
    "Dimensionality Reduction (PCA/t-SNE)": {"tags": "unsupervised, dimensionality_reduction, preprocessing", "area": "preprocessing", "axiomatix": "{feature_space_compression}"},
    "Reinforcement Learning": {"tags": "reinforcement, agent, policy", "area": "advanced", "axiomatix": "{dynamic_policy_optimization}"},
    "Neural Networks & Deep Learning": {"tags": "deep_learning, neural_networks, non-linear", "area": "deep_learning", "axiomatix": "{universal_approximation}"}
}

def ingest():
    for name, metadata in algorithms.items():
        code = f"# Algorithm: {name}\n# Function: {metadata['tags']}"
        code_manager.add_code(name, code, metadata['tags'])
        project_registry.register_file(f"ML_ALGO:{name}", "ML", "Ryush", "Foundry", metadata['area'], metadata['axiomatix'])
    print("Machine Learning Foundations ingested into Registry and Code DB.")

if __name__ == "__main__":
    ingest()
