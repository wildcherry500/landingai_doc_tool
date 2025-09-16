# LandingAI Document Extraction Tool

Extract text and analyze documents using LandingAI's Agentic Document Extraction API. This tool processes PDFs and images, extracting structured text content and generating visual analysis of the document layout.

## 🚀 Quick Start

### 1. Setup
```bash
# Clone or download this project
cd landingai_doc_tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Get API Key
1. Go to [https://app.landing.ai/](https://app.landing.ai/)
2. Sign up/login and get your API key
3. Edit the `.env` file and replace `REPLACE_WITH_YOUR_ACTUAL_API_KEY` with your real API key

### 3. Run the Tool
```bash
# Process a specific document
python src/main.py /path/to/your/document.pdf

# Interactive mode (will prompt for file path)
python src/main.py

# Get help
python src/main.py --help
```

## 📖 Usage Options

### Command Line Arguments
```bash
# Process a specific file
python src/main.py document.pdf
python src/main.py /full/path/to/document.jpg
python src/main.py "path with spaces/document.pdf"

# Interactive mode
python src/main.py
```

### Interactive Mode
When you run the script without arguments, it enters interactive mode:
```
No file path provided. Entering interactive mode...

Enter the path to your document (or 'quit' to exit): /path/to/file.pdf
```

Type `quit`, `exit`, or `q` to exit interactive mode.

## 📁 Output Files

The tool saves output files **next to your source document**:

**For document: `/path/to/document.pdf`**
- **Extracted Text**: `/path/to/document_extracted.md` (markdown format)
- **Visualizations**: `/path/to/visualizations/` (folder with PNG images)

### Output Details
- **Text File**: Contains all extracted text in markdown format with structural annotations
- **Visualization Images**: PNG files showing AI analysis of each page with bounding boxes and detected elements

## 🎯 Supported File Types

| Type | Extensions | Notes |
|------|------------|-------|
| **PDFs** | `.pdf` | Multi-page documents |
| **Images** | `.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp` | Single page images |

## ⚙️ Configuration

The `.env` file contains configuration options:

```env
# Required: Your LandingAI API key
VISION_AGENT_API_KEY=your_actual_api_key_here

# Optional: Processing settings (defaults work for most users)
BATCH_SIZE=4
MAX_WORKERS=2
MAX_RETRIES=80
MAX_RETRY_WAIT_TIME=30
RETRY_LOGGING_STYLE=log_msg
```

## 🔧 Troubleshooting

### Common Issues

**"API key is invalid"**
- Double-check your API key in the `.env` file
- Ensure no extra spaces or characters
- Verify your LandingAI account is active

**"File does not exist"**
- Check the file path is correct
- Use quotes around paths with spaces: `"My Documents/file.pdf"`
- Ensure the file exists and you have read permissions

**"Unsupported file type"**
- Only PDF and image files are supported
- Check the file extension matches supported types

### Getting Help
```bash
python src/main.py --help
```

## 🏗️ Project Structure

```
landingai_doc_tool/
├── .env                    # API key and configuration
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
├── src/
│   └── main.py            # Main application script
└── output/                # Legacy output folder (no longer used)
```

## 📝 Examples

### Basic Usage
```bash
# Process a PDF
python src/main.py ~/Documents/report.pdf

# Process an image
python src/main.py ~/Pictures/screenshot.png
```

### Batch Processing
```bash
# Process multiple files (run separately)
python src/main.py file1.pdf
python src/main.py file2.pdf
python src/main.py file3.jpg
```

### With Spaces in Path
```bash
# Use quotes for paths with spaces
python src/main.py "/Users/john/My Documents/Important Report.pdf"
```

## 🎮 Features

✅ **Smart File Validation** - Checks file existence and supported formats  
✅ **Command Line Interface** - Easy to use with arguments or interactive mode  
✅ **Local Output** - Files saved next to source documents for easy organization  
✅ **Visual Analysis** - See exactly how AI interpreted your document  
✅ **Error Handling** - Clear error messages with troubleshooting guidance  
✅ **Multiple Formats** - Support for PDFs and common image formats 