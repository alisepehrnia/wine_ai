# 🍷 Wine AI – Data Mining, Hill Climbing & MLP on Wine Quality

A collection of **data-mining and computational-intelligence** experiments on the **Wine Quality (white wine) dataset**.

The repository is organised into three independent sub-projects:

- **`wine_data_mining`** – exploratory data analysis and correlation study of the chemical attributes.
- **`wine_hill_climbing`** – a hill-climbing optimisation algorithm with mutation, implemented in Python.
- **`wine_mlp`** – two multilayer perceptron (MLP) neural network configurations, implemented in MATLAB.

> **Note:** The reports are written in **Persian (Farsi)**, while the code, file names, and repository documentation are in English.

---

# 📖 Overview

The **Wine Quality dataset** (white wine subset) contains **4,898 samples** and **12 attributes** (11 chemical properties plus one quality score).

Across the three projects, the goal is to explore, analyse, optimise, and predict wine quality using different computational intelligence techniques.

| Sub-project | Technique | Tool |
|-------------|-----------|------|
| `wine_data_mining` | Exploratory data analysis, statistics, correlations | Word / PDF Reports + Excel |
| `wine_hill_climbing` | Hill-climbing optimisation with mutation | Python |
| `wine_mlp` | Multilayer Perceptron (MLP) | MATLAB |

---

# 📂 Repository Structure

```text
wine_ai/
├── README.md
├── wine_data_mining/
│   ├── Report.docx
│   ├── Report.pdf
│   └── winequality-white.xlsx
│
├── wine_hill_climbing/
│   ├── Flowchart.vsdx
│   ├── Work Report.pdf
│   ├── hill_climbing.py
│   └── wine.xls
│
└── wine_mlp/
    ├── NN1Results/
    ├── NN2Results/
    ├── data/
    ├── report/
    │   ├── Report.docx
    │   └── Report.pdf
    └── src/
        ├── NN1_src.m
        ├── NN2_src.m
        └── data-final-white.mat
```

---

# 📊 Dataset

## Overview

The repository uses the **Wine Quality (White Wine)** dataset, originally published by the **UCI Machine Learning Repository**.

The dataset is widely used for machine learning, data mining, optimisation, and regression/classification research.

### Dataset Summary

| Property | Value |
|----------|-------|
| Dataset | White Wine Quality |
| Samples | 4,898 |
| Features | 11 |
| Target | Quality |
| Missing Values | None |
| Task | Regression / Classification |

The target variable is **Quality**, an integer score assigned by wine experts.

Depending on the project, the quality score is treated either as:

- a **regression target** (predicting an exact quality score), or
- a **classification target** (predicting quality categories).

---

## Dataset Characteristics

- 4,898 observations
- 11 continuous chemical features
- 1 integer target variable
- No missing values
- Moderate class imbalance
- Suitable for:
  - Data Mining
  - Exploratory Data Analysis
  - Machine Learning
  - Neural Networks
  - Optimisation Algorithms

---

## Feature Categories

The chemical measurements describe the physical and chemical properties of white wine samples.

These include:

- acidity measurements
- sugar content
- sulfur dioxide levels
- density
- pH
- sulphates
- alcohol percentage

Together these measurements are used to predict the perceived wine quality.

---

# 🧬 Dataset Features

The Wine Quality dataset contains **12 attributes**:

- **11 numerical chemical properties**
- **1 target quality score**

The features are:

| # | Attribute | Type | Description |
|---|-----------|------|-------------|
| 1 | Fixed Acidity | Numeric | Non-volatile acids (mainly tartaric acid), measured in g/dm³ |
| 2 | Volatile Acidity | Numeric | Acetic acid concentration. High values may produce vinegar-like taste |
| 3 | Citric Acid | Numeric | Citric acid content, contributing to freshness |
| 4 | Residual Sugar | Numeric | Remaining sugar after fermentation, measured in g/dm³ |
| 5 | Chlorides | Numeric | Salt content of the wine |
| 6 | Free Sulfur Dioxide | Numeric | Free SO₂ concentration, used as antimicrobial and antioxidant agent |
| 7 | Total Sulfur Dioxide | Numeric | Total SO₂ concentration including free and bound forms |
| 8 | Density | Numeric | Wine density, usually close to water density |
| 9 | pH | Numeric | Acidity/alkalinity balance of the wine |
| 10 | Sulphates | Numeric | Sulphate concentration, related to sulfur dioxide levels |
| 11 | Alcohol | Numeric | Alcohol percentage by volume |
| 12 | Quality | Integer | Target variable, sensory quality score (0–10) |

---

# 📁 Dataset Files in the Repository

The same Wine Quality dataset is stored in three different formats.

Each sub-project uses the format most suitable for its implementation.

| Format | Location | Used By |
|--------|----------|---------|
| `.xlsx` | `wine_data_mining/winequality-white.xlsx` | Excel-based exploratory analysis |
| `.xls` | `wine_hill_climbing/wine.xls` | Python hill-climbing algorithm |
| `.mat` | `wine_mlp/src/data-final-white.mat` | MATLAB neural network scripts |

No conversion is required.

Use the dataset file provided inside each project folder.

---

# 🔍 Dataset Usage Across Projects

The same data is processed differently depending on the objective of each experiment.

## Data Mining Project

The dataset is used for:

- statistical analysis
- feature distribution analysis
- correlation investigation
- visualization
- identifying relationships between chemical properties and quality

---

## Hill Climbing Project

The dataset is used as the search space for an optimisation algorithm.

The algorithm attempts to improve candidate solutions by:

- evaluating current solutions
- generating neighbouring solutions
- applying mutation
- moving toward better solutions

---

## MLP Project

The dataset is used to train artificial neural networks.

Processing includes:

- loading the MATLAB dataset file
- preparing input/output matrices
- normalisation
- neural network training
- performance evaluation

---

# 📈 Target Variable Distribution

The `Quality` attribute represents expert sensory evaluation.

The possible values are:

```
0 - 10
```

However, the dataset is not evenly distributed.

Most wine samples have quality scores around:

```
5 and 6
```

while very high or very low scores are rare.

This imbalance should be considered when interpreting:

- classification accuracy
- confusion matrices
- model performance

---

# 🔗 Feature Relationships

Several chemical attributes are correlated with each other.

Examples:

- Free sulfur dioxide and total sulfur dioxide have a strong relationship.
- Alcohol content often shows a positive relationship with quality.
- Volatile acidity often shows a negative relationship with quality.
- Density is related to sugar and alcohol content.

These relationships are important for:

- feature selection
- dimensionality analysis
- machine learning model design

---

# 🧩 Sub-project Overview

The repository contains three independent experiments:

| Folder | Main Goal |
|--------|-----------|
| `wine_data_mining` | Understand dataset characteristics and correlations |
| `wine_hill_climbing` | Apply optimisation algorithms |
| `wine_mlp` | Train neural network models |

Each project includes its own documentation, source files, and required data.

---

# 🧩 Sub-project 1 – `wine_data_mining`

## Purpose

The **wine_data_mining** project focuses on exploratory data analysis (EDA) of the Wine Quality dataset.

The objective is to understand how the chemical characteristics of white wine relate to the final quality score assigned by human experts.

The analysis is documented in a Persian-language academic report.

---

# 🔬 Analysis Performed

The project investigates the dataset from a data-mining perspective.

The main topics covered are:

- Dataset exploration
- Statistical analysis
- Feature distribution analysis
- Correlation analysis
- Relationship between chemical properties and wine quality

---

# 📊 Exploratory Data Analysis

The report includes an overview of:

- Number of samples
- Number of attributes
- Feature ranges
- Minimum and maximum values
- Average values
- Standard deviations
- Distribution of quality scores

The statistical analysis helps identify:

- dominant features
- unusual values
- possible relationships between variables

---

# 🔗 Correlation Analysis

One of the main goals of this project is studying the relationship between chemical attributes and the quality score.

The analysis includes:

## Positive Correlations

Some features tend to increase with better quality scores.

Example:

### Alcohol

Higher alcohol content generally shows a positive relationship with wine quality.

---

## Negative Correlations

Some features tend to decrease as quality improves.

Examples:

### Volatile Acidity

Higher volatile acidity is often associated with lower quality because excessive acetic acid can negatively affect taste.

### Density

Density tends to decrease as alcohol content increases, creating an indirect relationship with quality.

---

# 📈 Visualization

The project includes different visualization methods:

- Feature distribution plots
- Scatter plots
- Correlation charts
- Statistical graphs

These visualizations help understand:

- feature behaviour
- outliers
- relationships between variables

---

# 📂 Files

| File | Description |
|------|-------------|
| `Report.docx` | Complete data mining report (Persian) |
| `Report.pdf` | PDF version of the report |
| `winequality-white.xlsx` | White wine dataset in Excel format |

---

# ▶️ How to Use

This project does not contain executable source code.

To explore the project:

1. Open:

```
wine_data_mining/Report.pdf
```

to read the analysis.

2. Open:

```
wine_data_mining/winequality-white.xlsx
```

to inspect the dataset.

3. The DOCX version can be edited using:

- Microsoft Word
- LibreOffice Writer
- Google Docs

---

# 📝 Key Findings

Based on the analysis:

## Important Features

Several attributes show stronger relationships with wine quality:

- Alcohol
- Volatile Acidity
- Density

These features appear to have more influence on quality prediction.

---

## Quality Distribution

The quality labels are highly imbalanced.

Most samples belong to:

```
Quality = 5
Quality = 6
```

Few samples exist for extreme values:

```
Quality = 3
Quality = 4
Quality = 8
Quality = 9
```

This imbalance should be considered when applying machine learning algorithms.

---

## Feature Correlation

Some input variables are strongly related.

Examples:

- Free sulfur dioxide ↔ Total sulfur dioxide
- Alcohol ↔ Density
- Residual sugar ↔ Density

These correlations are important for:

- feature engineering
- model interpretation
- dimensionality reduction

---

# 🎯 Project Outcome

The data mining project provides an initial understanding of the Wine Quality dataset.

The results can be used as a foundation for:

- optimisation experiments
- machine learning models
- neural network training

---

# 🧩 Sub-project 2 – `wine_hill_climbing`

## Purpose

The **wine_hill_climbing** project applies a **hill-climbing optimisation algorithm with mutation** to the Wine Quality dataset.

The goal is to search for improved solutions by iteratively modifying candidate solutions and selecting better results.

The implementation is written in **Python**.

---

# 🧠 Algorithm Overview

## Hill Climbing

Hill climbing is a local search optimisation technique.

The algorithm starts with an initial candidate solution and repeatedly attempts to improve it.

The general process is:

1. Generate an initial solution.
2. Evaluate the current solution.
3. Create neighbouring solutions.
4. Compare neighbour performance.
5. Move to a better solution.
6. Repeat until no improvement is found.

Conceptually:

```
Current Solution
        |
        v
Generate Neighbour
        |
        v
Evaluate Fitness
        |
        v
Is Neighbour Better?
        |
   +----+----+
   |         |
 Yes        No
   |         |
Replace   Keep Current
   |
   v
Continue Search
```

---

# 🧬 Mutation Operator

Pure hill climbing can become trapped in a local optimum.

To improve exploration capability, this project introduces a mutation operator.

The mutation function:

```
modify_peridictions
```

is used to modify candidate predictions and increase search diversity.

The mutation operation helps the algorithm:

- escape local optima
- explore new regions of the search space
- avoid premature convergence

The report describes the mutation process using a mutation rate of one unit per step.

---

# ⚙️ Implementation Details

The algorithm is implemented in:

```
hill_climbing.py
```

The script:

- loads the Wine Quality dataset
- generates candidate solutions
- evaluates solution quality
- applies mutation
- performs iterative optimisation

---

# 📂 Files

| File | Description |
|------|-------------|
| `hill_climbing.py` | Python implementation of hill-climbing algorithm |
| `wine.xls` | Dataset used by the Python program |
| `Flowchart.vsdx` | Algorithm flowchart created with Microsoft Visio |
| `Work Report.pdf` | Detailed Persian report explaining the method |

---

# ▶️ How to Run

## Requirements

Install Python 3.x.

Navigate to the project directory:

```bash
cd wine_hill_climbing
```

Run:

```bash
python hill_climbing.py
```

---

# 📁 Dataset Location

The script expects:

```
wine.xls
```

to exist in the same directory.

Project structure:

```text
wine_hill_climbing/
├── hill_climbing.py
└── wine.xls
```

If the dataset location is changed, update the path inside:

```
hill_climbing.py
```

---

# 📊 Algorithm Flowchart

A complete flowchart of the optimisation algorithm is included:

```
Flowchart.vsdx
```

The flowchart describes:

- initialization
- solution generation
- fitness evaluation
- mutation
- iteration process
- termination condition

The file can be opened using:

- Microsoft Visio

or imported into:

- diagrams.net (draw.io)

---

# 📖 Report Contents

The Persian report includes:

## Problem Definition

Description of:

- optimisation objective
- dataset usage
- search strategy

---

## Algorithm Design

Explanation of:

- hill-climbing loop
- neighbour generation
- evaluation function
- acceptance criteria

---

## Mutation Strategy

Discussion of:

- mutation purpose
- mutation rate
- avoiding local optimum problems

---

## Results

The report analyses:

- convergence behaviour
- obtained solutions
- optimisation performance

---

# 🎯 Project Outcome

This project demonstrates the application of computational intelligence techniques beyond traditional machine learning.

Instead of directly training a predictive model, the approach uses optimisation methods to search for improved solutions.

The project provides practical experience with:

- local search algorithms
- heuristic optimisation
- mutation strategies
- computational intelligence concepts

---

# 🧩 Sub-project 3 – `wine_mlp`

## Purpose

The **wine_mlp** project applies **Multilayer Perceptron (MLP)** neural networks to the Wine Quality dataset.

The objective is to train and evaluate artificial neural networks capable of predicting wine quality based on chemical properties.

Two different neural network configurations are implemented and compared.

The implementation is developed using **MATLAB**.

---

# 🧠 Neural Network Overview

A Multilayer Perceptron (MLP) is a feed-forward artificial neural network consisting of:

- Input layer
- One or more hidden layers
- Output layer

The network learns the relationship between:

```
Chemical Properties
        |
        v
Neural Network
        |
        v
Wine Quality Prediction
```

---

# 🏗️ Network Configurations

The project contains two independent MLP implementations.

---

## NN1 – First Configuration

Source file:

```
src/NN1_src.m
```

This script defines the first neural network configuration.

It includes:

- network architecture
- training parameters
- data preparation
- training process
- performance evaluation

Results are stored in:

```
NN1Results/
```

---

## NN2 – Second Configuration

Source file:

```
src/NN2_src.m
```

The second implementation uses a different neural network configuration.

Possible differences include:

- number of hidden neurons
- network structure
- training parameters
- optimisation settings

Results are stored in:

```
NN2Results/
```

---

# 📂 Files

| File / Folder | Description |
|---------------|-------------|
| `src/NN1_src.m` | MATLAB source code for MLP configuration 1 |
| `src/NN2_src.m` | MATLAB source code for MLP configuration 2 |
| `src/data-final-white.mat` | Preprocessed MATLAB dataset |
| `NN1Results/` | Results generated by first network |
| `NN2Results/` | Results generated by second network |
| `report/Report.docx` | MLP project report (Persian) |
| `report/Report.pdf` | PDF version of report |
| `data/` | Additional supporting data files |

---

# 🔄 Data Preprocessing

Before training the neural networks, the dataset is prepared for MATLAB processing.

Typical preprocessing steps include:

- loading dataset
- separating input features and target values
- normalization/scaling
- preparing training and testing data

The processed dataset is stored as:

```
data-final-white.mat
```

---

# ▶️ How to Run

## Requirements

Install:

- MATLAB

---

## Run NN1

Open MATLAB and navigate to:

```text
wine_mlp/src/
```

Run:

```matlab
NN1_src
```

---

## Run NN2

Run:

```matlab
NN2_src
```

---

# 📊 Results

Each network has its own results folder:

```
NN1Results/
```

and

```
NN2Results/
```

These folders may contain:

- performance metrics
- training outputs
- graphs
- figures
- evaluation results

The results can be compared to determine which network configuration performs better.

---

# 📖 Report Contents

The Persian report explains:

## Network Architecture

Including:

- input layer
- hidden layers
- output layer
- neuron configuration

---

## Training Process

Including:

- learning algorithm
- training parameters
- epochs
- learning rate
- activation functions

---

## Performance Evaluation

The report discusses:

- prediction results
- error measurements
- comparison between NN1 and NN2

Possible evaluation metrics include:

- Mean Squared Error (MSE)
- accuracy
- confusion matrix
- prediction performance

---

# 🎯 Project Outcome

This project demonstrates how artificial neural networks can model complex relationships between wine chemical properties and quality scores.

The comparison between two MLP configurations provides insight into:

- neural network architecture selection
- parameter tuning
- impact of network design on prediction performance

---

# 🔬 Machine Learning Approach Summary

The three repository projects represent three different computational approaches:

| Project | Approach |
|---------|----------|
| `wine_data_mining` | Understanding and analysing data |
| `wine_hill_climbing` | Optimisation and search |
| `wine_mlp` | Supervised neural network learning |

Together, they demonstrate different areas of computational intelligence.

---

# 🛠️ Tools & Technologies

The repository combines several tools and programming environments.

| Sub-project | Language / Tool | Description |
|-------------|-----------------|-------------|
| Data Mining | Microsoft Word / PDF / Excel | Exploratory analysis and statistical investigation |
| Hill Climbing | Python 3.x | Optimisation algorithm implementation |
| MLP Neural Networks | MATLAB | Artificial neural network training and evaluation |
| Flowchart | Microsoft Visio | Algorithm design documentation |
| Documentation | Word / PDF | Academic reports written mainly in Persian |

---

# 🚀 Getting Started

This section explains how to run and explore all sub-projects.

---

# 📋 Prerequisites

## Python Environment

Required for:

```
wine_hill_climbing
```

Install:

- Python 3.x

Verify installation:

```bash
python --version
```

---

## MATLAB

Required for:

```
wine_mlp
```

Recommended:

- MATLAB with Neural Network Toolbox

---

## Document Readers

Required for viewing reports:

- Microsoft Word
- LibreOffice Writer
- PDF Reader

---

## Optional Tools

For viewing the algorithm flowchart:

- Microsoft Visio

or:

- diagrams.net (draw.io)

---

# 📚 Recommended Reading Order

For understanding the complete project, follow this order:

---

## 1. Data Mining Analysis

Open:

```
wine_data_mining/Report.pdf
```

Purpose:

- understand the dataset
- study feature relationships
- analyse correlations

This provides the foundation for the following projects.

---

## 2. Hill Climbing Optimisation

Open:

```
wine_hill_climbing/Work Report.pdf
```

Purpose:

- understand the optimisation approach
- study the search algorithm
- learn about mutation strategy

---

## 3. Neural Network Prediction

Open:

```
wine_mlp/report/Report.pdf
```

Purpose:

- understand MLP architecture
- compare neural network approaches
- review prediction performance

---

# ⚡ Quick Run Reference

## Python Hill Climbing

Navigate to:

```bash
cd wine_hill_climbing
```

Run:

```bash
python hill_climbing.py
```

Required file:

```
wine.xls
```

---

## MATLAB MLP

Navigate inside MATLAB:

```matlab
cd wine_mlp/src
```

Run first configuration:

```matlab
NN1_src
```

or second configuration:

```matlab
NN2_src
```

---

# 🗂️ Complete Workflow

The recommended workflow is:

```
Wine Dataset
      |
      v
Data Mining Analysis
      |
      v
Feature Understanding
      |
      +----------------+
      |                |
      v                v
Hill Climbing       MLP Neural Network
Optimisation        Prediction
      |                |
      v                v
Search Results     Model Results
```

---

# 🔬 Experimental Philosophy

The repository demonstrates three different computational intelligence viewpoints:

## Data Understanding

The data mining stage answers:

- What features exist?
- How are they distributed?
- Which attributes influence quality?

---

## Optimisation

The hill-climbing stage explores:

- How can solutions be improved?
- How can search algorithms escape local optima?

---

## Learning

The MLP stage investigates:

- How can a neural network learn the relationship between inputs and quality?
- How does architecture affect prediction performance?

---

# 📌 Project Requirements Summary

| Component | Requirement |
|-----------|-------------|
| Dataset Analysis | Excel + PDF/Word reader |
| Python Algorithm | Python 3.x |
| Neural Networks | MATLAB |
| Flowchart | Visio or draw.io |
| Reports | PDF viewer |

---

# 📝 Notes & Caveats

This section contains important information about the repository structure, implementation details, and limitations.

---

# 🌐 Language Information

The repository contains both English and Persian content.

## English Content

The following items are written in English:

- source code
- file names
- folder names
- repository documentation

---

## Persian Content

The following documents are written in Persian (Farsi):

- data mining report
- hill climbing report
- MLP report

The reports were created for academic coursework purposes.

---

# 📌 Dataset Duplication

The Wine Quality dataset exists in multiple formats:

```
.xlsx
.xls
.mat
```

This is intentional.

Each sub-project uses the format most convenient for its environment.

| Format | Used By |
|--------|---------|
| `.xlsx` | Excel-based data analysis |
| `.xls` | Python implementation |
| `.mat` | MATLAB neural network |

No dataset conversion is required.

---

# ⚠️ Quality Score Imbalance

The target variable:

```
Quality
```

is not evenly distributed.

Most samples belong to:

```
Quality = 5
Quality = 6
```

Extreme quality scores are uncommon:

```
Quality = 3
Quality = 4
Quality = 8
Quality = 9
```

---

## Impact on Machine Learning

This imbalance may affect:

- classification accuracy
- model evaluation
- confusion matrices
- prediction reliability

A model may achieve good overall accuracy while performing poorly on rare quality classes.

Possible improvements:

- resampling techniques
- class balancing
- weighted loss functions
- regression-based prediction

---

# 📊 Results Folder Information

The MLP results folders:

```
NN1Results/
NN2Results/
```

may contain:

- training graphs
- performance plots
- output files
- evaluation metrics

The exact content depends on the MATLAB execution environment and generated results.

---

# 🔧 Implementation Notes

## Hill Climbing

The hill-climbing implementation is a heuristic optimisation approach.

Important characteristics:

- local search behaviour
- neighbour-based improvement
- mutation-based exploration

Because it is a heuristic algorithm:

- results may depend on initial conditions
- different runs may produce different outcomes
- parameter tuning can affect performance

---

## MLP Neural Networks

The MLP implementation depends on:

- MATLAB version
- installed toolboxes
- training parameters
- random initialization

For reproducible experiments:

- use the same MATLAB environment
- keep the same random seed when possible
- compare models using identical datasets

---

# 🔍 Academic Scope

This repository represents an academic collection of experiments covering:

- Data Mining
- Computational Intelligence
- Optimisation Algorithms
- Artificial Neural Networks

It is intended primarily for:

- learning
- research demonstrations
- coursework evaluation

---

# 🚀 Possible Extensions

Future improvements could include:

## Additional Machine Learning Models

Examples:

- Decision Trees
- Random Forest
- Support Vector Machines
- Gradient Boosting
- XGBoost

---

## Improved Optimisation Methods

Examples:

- Genetic Algorithms
- Particle Swarm Optimisation
- Simulated Annealing
- Ant Colony Optimisation

---

## Advanced Neural Networks

Examples:

- Deep Neural Networks
- Convolutional Neural Networks
- Recurrent Neural Networks
- Transformer-based models

---

## Better Data Processing

Possible improvements:

- feature selection
- dimensionality reduction
- PCA analysis
- outlier handling
- advanced feature engineering

---

# 🤝 Contributing

This repository is an academic and experimental project.

Contributions are welcome.

Possible contribution areas:

- adding new machine learning models
- improving optimisation algorithms
- tuning neural network architectures
- improving documentation
- adding visualization tools

---

## Contribution Workflow

1. Fork the repository.
2. Create a new branch.

Example:

```bash
git checkout -b feature/new-model
```

3. Add your improvements.
4. Commit changes.

Example:

```bash
git commit -m "Add new prediction model"
```

5. Push the branch.

```bash
git push origin feature/new-model
```

6. Open a Pull Request.

---

# 📄 License

No explicit license is currently specified for this repository.

If you intend to reuse, modify, or redistribute the code or documentation, please contact the repository owner for permission and usage terms.

---

# 🙏 Acknowledgements

This project was developed using several academic resources, datasets, and software tools.

---

# 🍷 Dataset

The Wine Quality dataset was originally introduced by:

**P. Cortez, A. Cerdeira, F. Almeida, T. Matos, J. Reis**

Title:

> Modeling wine preferences by data mining from physicochemical properties

The dataset is publicly available through the:

**UCI Machine Learning Repository**

The dataset has been widely used in:

- machine learning research
- regression problems
- classification experiments
- data mining studies

---

# 👨‍🏫 Academic References

The project reports were prepared as part of academic coursework.

Referenced courses include:

- Advanced Data Mining  
- Computational Intelligence  

---

# 🧰 Software Tools Used

This repository uses:

## Programming Languages

- Python
- MATLAB

---

## Data Analysis Tools

- Microsoft Excel
- MATLAB data processing tools

---

## Documentation Tools

- Microsoft Word
- PDF generation tools

---

## Diagram Tools

- Microsoft Visio

---

# 📌 Final Repository Summary

This repository demonstrates three different approaches for analysing and predicting wine quality.

| Area | Project | Main Technique |
|------|---------|----------------|
| Data Analysis | `wine_data_mining` | Exploratory Data Mining |
| Optimisation | `wine_hill_climbing` | Hill Climbing + Mutation |
| Machine Learning | `wine_mlp` | Multilayer Perceptron Neural Networks |

Together, these experiments demonstrate the application of computational intelligence methods to a real-world chemical dataset.

---

# 🏁 Conclusion

The Wine Quality dataset provides an excellent example of how different computational approaches can be applied to the same problem.

The repository progresses through three major stages:

```
Understanding Data
        |
        v
Optimising Solutions
        |
        v
Learning Predictive Models
```

The combination of:

- statistical analysis,
- optimisation algorithms,
- and neural networks

provides a complete practical introduction to computational intelligence workflows.

---

# ⭐ Project Highlights

✔ Real-world dataset analysis  
✔ Exploratory data mining  
✔ Correlation and statistical investigation  
✔ Heuristic optimisation algorithm  
✔ Mutation-based search improvement  
✔ MATLAB neural network implementation  
✔ Comparison of different computational approaches  
✔ Academic documentation and reports  

---

# 📚 End of README

Thank you for exploring this project.
