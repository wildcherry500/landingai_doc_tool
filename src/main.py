import os
from dotenv import load_dotenv
from agentic_doc.parse import parse
from agentic_doc.utils import viz_parsed_document
from agentic_doc.config import VisualizationConfig

# Load environment variables
load_dotenv()

def process_document(file_path):
    """
    Process a document using the LandingAI API.
    
    Args:
        file_path (str): Path to the document to process
    """
    try:
        # Parse the document
        results = parse(file_path)
        
        if not results:
            print("No results returned from document processing")
            return
        
        parsed_doc = results[0]
        
        # Print the extracted markdown
        print("\nExtracted Content (Markdown):")
        print(parsed_doc.markdown)
        
        # Create visualizations
        output_dir = "output/visualizations"
        os.makedirs(output_dir, exist_ok=True)
        
        # Create visualizations with default settings
        images = viz_parsed_document(
            file_path,
            parsed_doc,
            output_dir=output_dir
        )
        
        print(f"\nVisualizations saved to: {output_dir}")
        
    except Exception as e:
        print(f"Error processing document: {str(e)}")

def main():
    # Example usage
    document_path = "path/to/your/document.pdf"  # Replace with your document path
    process_document(document_path)

if __name__ == "__main__":
    main() 