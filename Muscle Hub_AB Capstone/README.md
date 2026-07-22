# Muscle Hub A/B Test Analysis

A data analysis project completed as part of Codecademy's Python Data Science path, exploring an A/B test conducted by a fictional fitness studio, Muscle Hub.

## Project Overview

Muscle Hub ran an A/B test to see whether adding a short fitness quiz to their sign-up flow would increase the number of visitors who become members. This project uses Python and pandas to explore, clean, and analyze the resulting data, then draws conclusions about the quiz's effect on conversion.

## Objectives

- Combine and clean data from multiple sources (visits, fitness tests, applications, purchases)
- Determine what percentage of visitors take a fitness test
- Compare conversion rates between the A group (no quiz) and B group (quiz)
- Use a chi-square test to check whether the difference in conversion is statistically significant
- Visualize results with matplotlib

## Tools & Libraries

- Python 3
- pandas
- numpy
- matplotlib
- scipy (`chi2_contingency`)

## Files

| File | Description |
|------|--------------|
| `muscle_hub.ipynb` | Jupyter notebook containing the full analysis |
| `visits.csv` | Visitor sign-up data |
| `fitness_tests.csv` | Fitness test completion data |
| `applications.csv` | Membership application data |
| `purchases.csv` | Membership purchase data |

## Key Findings

- A summary of the fitness test completion rate, application rate, and purchase rate is included in the notebook.
- The chi-square test results indicate whether the quiz had a statistically significant effect on conversion to membership.

## How to Run

1. Clone or download this repository.
2. Install the required libraries: `pip install pandas numpy matplotlib scipy`.
3. Open `muscle_hub.ipynb` in Jupyter Notebook or JupyterLab.
4. Run all cells to reproduce the analysis.

## Acknowledgments

This project is part of Codecademy's Data Scientist career path.
