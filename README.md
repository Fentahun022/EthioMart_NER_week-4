 # EthioMart: Amharic NER and Vendor Analytics Project

## Project Overview

The core business problem is the fragmented nature of Telegram e-commerce in Ethiopia. This project solves this by creating a repeatable workflow to:
1.  **Ingest** data from multiple channels in real-time.
2.  **Structure** the data by extracting key entities (Products, Prices, Locations, etc.).
3.  **Analyze** the structured data to generate actionable business intelligence.

## Key Achievements & Results

*   **High-Performance NER Model:** Successfully fine-tuned a `Davlan/afro-xlmr-base` model, achieving an **F1-score of 0.96** on a custom Amharic e-commerce dataset.
*   **End-to-End Repeatable Workflow:** Established a complete pipeline from raw data scraping (897 messages collected) to a final, structured business analysis.
*   **Vendor Analytics Engine:** Developed a "Lending Score" that combines NER-extracted data with Telegram metadata (views, post frequency) to create a powerful vendor assessment tool.

## Tech Stack

*   **Programming Language:** Python 3.10
*   **Data Ingestion:** Telethon
*   **ML/NLP Frameworks:** PyTorch, Hugging Face (Transformers, Datasets, Tokenizers)
*   **Data Manipulation:** Pandas, NumPy
*   **Model Interpretability:** SHAP
*   **Core Libraries:** seqeval, tqdm, ipywidgets


# Environment Setup
To set up the development environment for this project, follow these steps:

Clone the repository:

git clone https://github.com/Fentahun022/EthioMart_NER_week-4.git
cd EthioMart_NER_week-4


# Create and activate a virtual environment: Using venv:

For macOS/Linux
python3 -m venv venv source venv/bin/activate

# Install dependencies:

pip install -r requirements.txt

## Project Structure

The repository is organized into modular components for clarity and scalability.
EthioMart_NER_Project/
├── .gitignore
├── data/
│ ├── scraped_data.csv # Raw data collected from Telegram
│ └── preprocessed_data.csv # Cleaned data ready for analysis
│ └── labeled_data.txt # Manually labeled data in CoNLL format
├── notebooks/
│ ├── 01_Data_Ingestion_and_Preprocessing.ipynb
│ ├── 03_Model_Finetuning_and_Evaluation.ipynb
│ ├── 04_Model_Comparison_and_Interpretability.ipynb
│ └── 05_Vendor_Scorecard_Engine.ipynb
├── reports/
│ └── vendor_scorecard.csv # Final output of the project
├── saved_models/
│ └── amharic-ner-afro-xlmr/ # The fine-tuned model artifact
├── venv/ # Python virtual environment (ignored by git)
├── README.md # This file
└── requirements.txt # Project dependencies