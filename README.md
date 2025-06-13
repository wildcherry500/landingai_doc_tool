# LandingAI Document Extraction Project

This project uses LandingAI's Agentic Document Extraction API to process and extract information from documents.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following content:
```
VISION_AGENT_API_KEY=your_api_key_here
BATCH_SIZE=4
MAX_WORKERS=2
MAX_RETRIES=80
MAX_RETRY_WAIT_TIME=30
RETRY_LOGGING_STYLE=log_msg
```

## Project Structure

```
landingai_help/
├── .env                    # API key and configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── src/                   # Source code directory
│   └── main.py           # Main script
└── output/               # Directory for saving results
    ├── groundings/       # For saving grounding images
    └── visualizations/   # For saving visualization outputs
```

## Usage

1. Get your API key from LandingAI
2. Add your API key to the `.env` file
3. Run the main script:
```bash
python src/main.py
```

## Features

- Document extraction from PDFs and images
- Automatic handling of large documents
- Visualization of extracted content
- Error handling and retries
- Configurable processing parameters 