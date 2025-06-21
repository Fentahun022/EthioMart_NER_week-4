# EthioMart: Amharic NER for E-Commerce Consolidation

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

# This project develops a complete workflow for building an Amharic Named Entity Recognition (NER) system. The system is designed for EthioMart, a platform aiming to centralize Ethiopia's Telegram-based e-commerce activities by extracting key business entities (Products, Prices, Locations) from vendor posts.

The project also includes a Vendor Analytics Engine that uses the extracted data and post metadata to create a "Lending Score," helping EthioMart identify promising vendors for micro-lending opportunities.
## Project Overview

The primary goal is to create a repeatable pipeline that:
1.  Ingests real-time data from multiple Amharic e-commerce Telegram channels.
2.  Preprocesses and labels the unstructured text data.

## Key Features

- **Data Ingestion:** A robust Python scraper using `Telethon` to fetch data from public Telegram channels.
- **Data Labeling:** A manually labeled, high-quality dataset in CoNLL format, tailored for e-commerce entities.