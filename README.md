# BDScore: An Empirical Study on Bias in Disease Diagnosis by Large Language Models

![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

This repository contains medical examination datasets and model outputs for analyzing diagnostic bias across four key dimensions in AI models.

## 📂 Dataset Structure
    .
    ├── calc_bdscore.py # Core script for computing 4-dimension BDScores
    ├── idd_prompts.py # All IDD debiasing prompts
    ├── medical_exam_data/ # Medical exam dataset, model outputs and bdscores
    │ ├── medical_exam.xlsx/ # Medical exam dataset
    │ │
    │ ├── pre_idd/ # Pre-debiasing outputs
    │ │ ├── model_results/ # Raw model predictions
    │ │ │ ├── gpt4_result.xlsx
    │ │ │ ├── chatgpt_result.xlsx
    │ │ │ └── ...
    │ │ │
    │ │ └── bdscores/ # Pre-IDD bias scores
    │ │ │ ├── age_scores/
    │ │ │ │ ├── gpt4_agescore.xlsx
    │ │ │ ├── gender_scores/
    │ │ │ ├── severity_scores/
    │ │ │ ├── repeat_scores/
    │ │
    │ └── post_idd/ # Post-debiasing outputs
        │ ├── model_results/ # Debiased predictions
        │ └── bdscores/ # Post-IDD bias scores
    │
    ├── README.md

## 🛠️ Usage

### 1. Calculating BDScores

python calc_bdscore.py 

### 2. Using IDD Prompts
The idd_prompts.py contains all prompts used for debiasing across four dimensions.