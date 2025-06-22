

# EthioMart: Amharic NER and Vendor Analytics Project

This project aims to build an end-to-end data intelligence system for EthioMart. It involves scraping e-commerce data from Ethiopian Telegram channels, processing it, and fine-tuning a Named Entity Recognition (NER) model to extract key business entities like Products, Prices, and Locations.

The ultimate goal is to use this structured data to power a centralized e-commerce platform and a FinTech Vendor Scorecard for micro-lending decisions.

## Interim Submission (Tasks 1 & 2)

This repository currently contains the completed work for the initial phase of the project: Data Ingestion and Data Labeling




### Project Structure

EthioMart_NER_Project/
├── .gitignore
├── data/
│ ├── scraped_data.csv (Raw data collected from Telegram)
│ └── preprocessed_data.csv (Cleaned data ready for labeling/analysis)
│ └── labeled_data.txt (Manually labeled data in CoNLL format)
├── notebooks/
│ └── 01_Data_Ingestion_and_Preprocessing.ipynb
├── venv/ (Virtual environment files - ignored by git)
├── README.md
└── requirements.txt


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


# Configure Telegram API Credentials
Before you can scrape data, you must provide your own Telegram API credentials.
Obtain your api_id and api_hash from my.telegram.org.
Open the notebooks/01_Data_Ingestion_and_Preprocessing.ipynb file.
Find the section marked --- Telegram Scraper --- and replace the placeholder values for api_id, api_hash, and phone with your own credentials.

api_id = 12345678
api_hash = 'YOUR_API_HASH'
phone = '+251...'