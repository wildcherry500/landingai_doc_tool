import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv
from agentic_doc.parse import parse
from agentic_doc.utils import viz_parsed_document
from agentic_doc.config import VisualizationConfig

# Load environment variables
load_dotenv()

def validate_api_key():
    """
    Validate that the API key is properly configured.
    
    Returns:
        bool: True if API key is valid, False otherwise
    """
    api_key = os.getenv('VISION_AGENT_API_KEY', '')
    
    if not api_key:
        print("Error: VISION_AGENT_API_KEY not found in environment variables.")
        print("Please add your API key to the .env file.")
        return False
    
    if api_key in ['your_api_key_here', 'REPLACE_WITH_YOUR_ACTUAL_API_KEY', 'your_actual_api_key_here']:
        print("Error: API key is still set to placeholder value.")
        print("Please replace the placeholder in .env file with your actual API key from https://app.landing.ai/")
        return False
    
    if len(api_key) < 10:  # Basic sanity check
        print("Error: API key appears to be too short. Please check your API key.")
        return False
    
    return True

def validate_file(file_path):
    """
    Validate that the file exists and is supported.
    
    Args:
        file_path (str): Path to the document to process
        
    Returns:
        bool: True if file is valid, False otherwise
    """
    path = Path(file_path)
    
    if not path.exists():
        print(f"Error: File does not exist: {file_path}")
        return False
    
    if not path.is_file():
        print(f"Error: Path is not a file: {file_path}")
        return False
    
    supported_extensions = {'.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.bmp'}
    if path.suffix.lower() not in supported_extensions:
        print(f"Error: Unsupported file type. Supported formats: {', '.join(supported_extensions)}")
        return False
    
    return True

def process_document(file_path):
    """
    Process a document using the LandingAI API.
    
    Args:
        file_path (str): Path to the document to process
        
    Returns:
        bool: True if processing was successful, False otherwise
    """
    if not validate_file(file_path):
        return False
    
    if not validate_api_key():
        return False
    
    try:
        print(f"Processing document: {file_path}")
        
        # Parse the document
        results = parse(file_path)
        
        if not results:
            print("No results returned from document processing")
            return False
        
        if len(results) == 0:
            print("Empty results returned from document processing")
            return False
            
        parsed_doc = results[0]
        
        # Print the extracted markdown
        print("\nExtracted Content (Markdown):")
        print(parsed_doc.markdown)
        
        # Save the extracted markdown to a file next to the source PDF
        source_dir = Path(file_path).parent
        output_file = source_dir / f"{Path(file_path).stem}_extracted.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(parsed_doc.markdown)
        print(f"\nExtracted text saved to: {output_file}")
        
        # Create visualizations next to the source PDF
        source_dir = Path(file_path).parent
        output_dir = source_dir / "visualizations"
        os.makedirs(output_dir, exist_ok=True)
        
        # Create visualizations with default settings
        viz_parsed_document(
            file_path,
            parsed_doc,
            output_dir=str(output_dir)
        )
        
        print(f"\nVisualizations saved to: {output_dir}")
        print("Processing completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error processing document: {str(e)}")
        
        # Provide helpful context based on error type
        error_msg = str(e).lower()
        if "api key" in error_msg:
            print("\nTroubleshooting: This appears to be an API key issue.")
            print("- Verify your API key is correct in the .env file")
            print("- Get your API key from: https://app.landing.ai/")
        elif "authentication" in error_msg or "unauthorized" in error_msg:
            print("\nTroubleshooting: Authentication failed.")
            print("- Check that your API key is valid and active")
        elif "quota" in error_msg or "limit" in error_msg:
            print("\nTroubleshooting: This may be a usage limit issue.")
            print("- Check your account usage limits at https://app.landing.ai/")
        
        return False

def get_user_input():
    """
    Get document path from user input if no command line argument provided.
    
    Returns:
        str: Path to the document file
    """
    while True:
        file_path = input("\nEnter the path to your document (or 'quit' to exit): ").strip()
        
        if file_path.lower() in ['quit', 'exit', 'q']:
            print("Exiting...")
            sys.exit(0)
            
        if file_path:
            return file_path
        
        print("Please enter a valid file path.")

def main():
    parser = argparse.ArgumentParser(
        description="Process documents using LandingAI's Agentic Document Extraction API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/main.py document.pdf
  python src/main.py /path/to/document.jpg
  python src/main.py  # Interactive mode
        """
    )
    
    parser.add_argument(
        'file_path', 
        nargs='?', 
        help='Path to the document to process (PDF, PNG, JPG, JPEG, TIFF, BMP)'
    )
    
    args = parser.parse_args()
    
    # Get file path from command line or user input
    if args.file_path:
        file_path = args.file_path
    else:
        print("No file path provided. Entering interactive mode...")
        file_path = get_user_input()
    
    # Process the document
    success = process_document(file_path)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main() 