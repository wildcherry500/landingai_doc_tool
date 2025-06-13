landing-ai / agentic-doc <!-- text, from page 0 (l=0.053,t=0.042,r=0.335,b=0.077), with ID 51301cd0-e220-4cea-a697-02f7688cdf39 -->

- ![inline figure: magnifying glass icon]
- ![inline figure: inbox tray icon]

![inline figure: circular profile photo of a person in a tan hat and brown jacket] <!-- text, from page 0 (l=0.814,t=0.042,r=0.948,b=0.079), with ID 814dc921-1d7b-43fc-8f69-22e1f76590bb -->

< Code  Issues  6  Pull requests  3  Discussions <!-- text, from page 0 (l=0.060,t=0.086,r=0.547,b=0.110), with ID 17c8e300-c457-4f5b-9d1c-da1753fed3fb -->

- ◦ Actions
- ◦ Projects
- ◦ Security <!-- marginalia, from page 0 (l=0.562,t=0.086,r=0.857,b=0.110), with ID fe597463-007f-492a-8ae8-5a73b65df290 -->

Insig <!-- marginalia, from page 0 (l=0.870,t=0.088,r=0.947,b=0.110), with ID 440f7a9d-f3bc-4df3-b78d-541beb4603fa -->

Summary : This image shows three square buttons, each containing a different icon: an eye, a branching network, and a yellow star. The icons are simple line drawings, and only the star is filled with colour.

photo:
Scene Overview :
  • Three square buttons are arranged horizontally.
  • The first button contains an eye icon (outline).
  • The second button contains a branching network or fork icon (outline).
  • The third button contains a five-pointed star icon, filled with yellow.

Technical Details :
  • All buttons have rounded corners and a light grey border.
  • Only the star icon is filled with colour; the other two are outlined in grey.
  • No text labels or additional UI elements are present.

Spatial Relationships :
  • The buttons are evenly spaced in a single row.
  • All icons are centred within their respective buttons.

Analysis :
  • The icons likely represent common actions: "view" (eye), "fork" or "branch" (network), and "favourite" or "starred" (star).
  • The yellow fill on the star suggests it is selected or active, while the others are inactive. <!-- figure, from page 0 (l=0.052,t=0.122,r=0.187,b=0.158), with ID a0c4f6bc-421b-4689-a0fd-afdc13dbc557 -->

Python library for Agentic Document Extraction from LandingAI <!-- text, from page 0 (l=0.054,t=0.162,r=0.529,b=0.187), with ID a643dd1a-86e5-4462-b6df-fa1c5dcfc58c -->

[landing.ai/agentic-document-extraction](landing.ai/agentic-document-extraction)  
Apache-2.0 license  
622 stars   66 forks   13 watching   Branches   Activity   Custom properties   Tags <!-- text, from page 0 (l=0.051,t=0.193,r=0.723,b=0.276), with ID ee11d069-6e26-4082-93eb-0d2fb577d9de -->

🌐 Public repository <!-- text, from page 0 (l=0.053,t=0.277,r=0.208,b=0.301), with ID 4ccc0288-61af-4cb0-b99b-91afaf58c13e -->

5 Branches: 5

0 Tags: 0 <!-- text, from page 0 (l=0.054,t=0.320,r=0.962,b=0.358), with ID 80459e4e-5c2b-4c1b-a5de-0a8422d76c1d -->

- Landing AI Bot [skip ci] chore(release): agentic-doc 0.2.7 5905e32 · 2 days ago
- • .github/workflows feat: enable integration tests (#26) 2 months ago
- • agentic_doc feat: change output name for extrac… 2 days ago
- • tests feat: change output name for extrac… 2 days ago
- • .flake8 Initial implementation 3 months ago
- • .gitignore Initial implementation 3 months ago
- • LICENSE Initial commit 3 months ago
- • README.md feat: change output name for extrac… 2 days ago
- • poetry.lock feat: update connectors and style (#… 2 weeks ago
- • pyproject.toml [skip ci] chore(release): agentic-doc… 2 days ago <!-- text, from page 0 (l=0.057,t=0.364,r=0.942,b=0.694), with ID 378378a6-765e-423d-840d-710272a441b7 -->

README   Apache-2.0 license <!-- text, from page 0 (l=0.069,t=0.712,r=0.347,b=0.736), with ID b5ce5139-4d49-4873-a379-29bfdc20fe2f -->

- ![inline micro-figure: pencil icon] 
- ![inline micro-figure: bulleted list icon] <!-- text, from page 0 (l=0.863,t=0.714,r=0.931,b=0.736), with ID 87746494-cb00-44e0-ba53-62a620d1557e -->

# Agentic Document Extraction – Python Library <!-- text, from page 0 (l=0.158,t=0.785,r=0.844,b=0.823), with ID 32d4d623-6a93-420c-a80f-cf44694ec414 -->

CI passing  VisionAgent <!-- text, from page 0 (l=0.336,t=0.835,r=0.534,b=0.857), with ID 96141935-8cf4-4f87-aa5b-60dacd80f6fa -->

<table>
  <tr>
    <td style="background-color:#555;color:#fff;">pypi package</td>
    <td style="background-color:#97CA00;color:#fff;">0.2.4</td>
  </tr>
</table> <!-- marginalia, from page 0 (l=0.539,t=0.835,r=0.667,b=0.856), with ID 825c2f4d-2e8d-4880-a345-5caf2da33663 -->

Web App · Discord · Blog · Docs <!-- marginalia, from page 0 (l=0.376,t=0.870,r=0.629,b=0.895), with ID 150f3a2e-21d8-4fd5-9976-030550f258c2 -->

## Overview

The LandingAI **Agentic Document Extraction** API pulls structured data out of visually complex documents—think tables, pictures, and charts—and returns a hierarchical JSON with exact element locations. <!-- text, from page 0 (l=0.084,t=0.033,r=0.896,b=0.118), with ID 5f33c3d8-1000-4712-9310-84fe11b872db -->

- **Long-document support** – process 100+ page PDFs in a single call
- **Auto-retry / paging** – handles concurrency, time-outs, and rate limits
- **Helper utilities** – bounding-box snippets, visual debuggers, and more <!-- text, from page 0 (l=0.089,t=0.125,r=0.648,b=0.224), with ID 3570071a-14d2-46e0-988b-3b57b23c4cf3 -->

- 📦 **Batteries-included install**: `pip install agentic-doc` – nothing else needed → see [Installation](https://github.com/agentic-ai/agentic-doc#installation)
- 🗂 **All file types**: parse PDFs of *any* length, single images, or URLs → see [Supported Files](https://github.com/agentic-ai/agentic-doc#supported-files)
- 🦾 **Long-doc ready**: auto-split & parallel-process 1000+ page PDFs, then stitch results → see [Parse Large PDF Files](https://github.com/agentic-ai/agentic-doc#parse-large-pdf-files)
- 🧬 **Structured output**: returns hierarchical JSON plus ready-to-render Markdown → see [Result Schema](https://github.com/agentic-ai/agentic-doc#result-schema)
- 🖼 **Ground-truth visuals**: optional bounding-box snippets and full-page visualizations → see [Save Groundings as Images](https://github.com/agentic-ai/agentic-doc#save-groundings-as-images)
- 🏃‍♂️ **Batch & parallel**: feed a list; library manages threads & rate limits (`BATCH_SIZE`, `MAX_WORKERS`) → see [Parse Multiple Files in a Batch](https://github.com/agentic-ai/agentic-doc#parse-multiple-files-in-a-batch)
- 🛡 **Resilient**: exponential-backoff retries for 408/429/502/503/504 and rate-limit hits → see [Automatically Handle API Errors and Rate Limits with Retries](https://github.com/agentic-ai/agentic-doc#automatically-handle-api-errors-and-rate-limits-with-retries)
- 🛠 **Drop-in helpers**: `parse_documents`, `parse_and_save_documents`, `parse_and_save_document` → see [Main Functions](https://github.com/agentic-ai/agentic-doc#main-functions)
- ⚙️ **Config via env / .env**: tweak parallelism, logging style, retry caps—no code changes → see [Configuration Options](https://github.com/agentic-ai/agentic-doc#configuration-options)
- 🛰 **Raw API ready**: advanced users can still hit the REST endpoint directly → see the [API Docs](https://github.com/agentic-ai/agentic-doc#api-docs) <!-- text, from page 0 (l=0.086,t=0.237,r=0.892,b=0.600), with ID 6263bd90-100e-4b59-8d53-3439fb6d61f6 -->

# Quick Start

## Installation

    pip install agentic-doc <!-- text, from page 0 (l=0.085,t=0.611,r=0.312,b=0.726), with ID f3e63bf5-4131-46ec-882c-d7ebc4bf2289 -->

- Requirements
- Python version 3.9, 3.10, 3.11 or 3.12
- LandingAI agentic AI API key (get the key here) <!-- text, from page 0 (l=0.088,t=0.750,r=0.476,b=0.829), with ID f75fad67-e703-48bb-87ca-f551f9d3f220 -->

Set the API Key as an Environment Variable

After you get the LandingAI agentic AI API key, set the key as an environment variable (or put it in a `.env` file): <!-- text, from page 0 (l=0.086,t=0.841,r=0.901,b=0.899), with ID 7a83171f-ec4f-4072-be21-184433d1bc9b -->

export VISION_AGENT_API_KEY=<your-api-key> <!-- marginalia, from page 0 (l=0.102,t=0.915,r=0.463,b=0.937), with ID 9319173a-985d-4ea3-8f7e-7b763df1efaf -->

 <!-- marginalia, from page 0 (l=0.871,t=0.913,r=0.899,b=0.934), with ID 2c4b4896-ce04-4233-afb0-532fab12a631 -->

Supported Files <!-- text, from page 0 (l=0.088,t=0.032,r=0.249,b=0.057), with ID 057da544-5ff0-4ade-b284-4fd8f0c55a18 -->

- The library can extract data from:

  - • PDFs (any length)
  - • Images that are supported by OpenCV-Python (i.e. the  cv2  library)
  - • URLs pointing to PDF or image files <!-- text, from page 0 (l=0.090,t=0.065,r=0.626,b=0.164), with ID 1d53701a-b287-4789-bb01-92c61bf8f5db -->

# Basic Usage

## Extract Data from One Document

Run the following script to extract data from one document and return the results in both markdown and structured chunks. <!-- text, from page 0 (l=0.088,t=0.177,r=0.857,b=0.283), with ID 7659f405-afc4-47ba-a77d-6f0cc70f67c2 -->

from agentic_doc.parse import parse

# Parse a local file
result = parse("path/to/image.png")
print(result[0].markdown)  # Get the extracted data as markdown
print(result[0].chunks)    # Get the extracted data as structured chunks of content

# Parse a document from a URL
result = parse("https://example.com/document.pdf")
print(result[0].markdown)

# Legacy approach (still supported)
from agentic_doc.parse import parse_documents
results = parse_documents(["path/to/image.png"])
parsed_doc = results[0] <!-- text, from page 0 (l=0.099,t=0.302,r=0.905,b=0.536), with ID 886a1d7e-179c-4521-a6cb-7b48934cb829 -->

**Extract Data from Multiple Documents**

Run the following script to extract data from multiple documents. <!-- text, from page 0 (l=0.088,t=0.564,r=0.571,b=0.614), with ID 80aa784d-ab58-40bf-81e3-502cae29873a -->

from agentic_doc.parse import parse

# Parse multiple local files
file_paths = ["path/to/your/document1.pdf", "path/to/another/document2.pdf"]
results = parse(file_paths)
for result in results:
    print(result.markdown) <!-- text, from page 0 (l=0.100,t=0.632,r=0.902,b=0.747), with ID 0bac9103-17fc-4477-b628-57b8e24c78d6 -->

# Parse and save results to a directory
results = parse(file_paths, result_save_dir="path/to/save/results")
result_paths = []
for result in results:
    result_paths.append(result.result_path)
# result_paths: ["path/to/save/results/document1_20250313_070305.json", ...] <!-- text, from page 0 (l=0.101,t=0.757,r=0.741,b=0.853), with ID 5827ed78-2127-4cc4-9e53-6afc24287217 -->

Using field extraction

from pydantic import BaseModel, Field
from agentic_doc.parse import parse <!-- text, from page 0 (l=0.088,t=0.881,r=0.897,b=0.955), with ID d8e5858a-4881-4179-8ad6-b0378085a725 -->

class ExtractedFields(BaseModel):
    employee_name: str = Field(description="the full name of the employee")
    employee_ssn: str = Field(description="the social security number of the employee")
    gross_pay: float = Field(description="the gross pay of the employee")
    employee_address: str = Field(description="the address of the employee") <!-- text, from page 0 (l=0.102,t=0.047,r=0.831,b=0.132), with ID d813649b-2fed-4435-9f85-7f15679c1074 -->

results = parse("mydoc.pdf", extraction_model=ExtractedFields)
fields = results[0].extraction
print(fields.employee_name) <!-- text, from page 0 (l=0.103,t=0.138,r=0.625,b=0.191), with ID c134f414-0a64-4530-9d9d-7d29c831cf9f -->

**Extract Data Using Connectors**

The library now supports various connectors to easily access documents from different sources: <!-- text, from page 0 (l=0.088,t=0.216,r=0.802,b=0.267), with ID 4be67ebc-cdda-42bb-972b-75b70576fac7 -->

Google Drive Connector

Prerequisites: Follow the Google Drive API Python Quickstart tutorial first to set up your credentials. <!-- text, from page 0 (l=0.088,t=0.280,r=0.856,b=0.331), with ID 4b0ad56b-7bd6-4a22-b5ad-507613af0521 -->

The Google Drive API quickstart will guide you through:

1. Creating a Google Cloud project
2. Enabling the Google Drive API
3. Setting up OAuth 2.0 credentials <!-- text, from page 0 (l=0.090,t=0.341,r=0.500,b=0.436), with ID f8a43f11-b601-4f6d-9cdf-8c17183acbf6 -->

After completing the quickstart tutorial, you can use the Google Drive connector as follows: <!-- text, from page 0 (l=0.088,t=0.446,r=0.761,b=0.467), with ID d640de1a-e315-4d1c-a077-41b97a7e0f9c -->

from agentic_doc.parse import parse
from agentic_doc.connectors import GoogleDriveConnectorConfig <!-- text, from page 0 (l=0.103,t=0.484,r=0.898,b=0.522), with ID 69585c8e-f243-421c-83d6-501eb3afd01e -->

# Using OAuth credentials file (from quickstart tutorial)
config = GoogleDriveConnectorConfig(
    client_secret_file="path/to/credentials.json",
    folder_id="your-google-drive-folder-id"  # Optional
) <!-- text, from page 0 (l=0.106,t=0.533,r=0.583,b=0.612), with ID 9019c431-a335-4aed-a06a-c269dec0a0fd -->

# Parse all documents in the folder
results = parse(config)

# Parse with filtering
results = parse(config, connector_pattern="*.pdf") <!-- text, from page 0 (l=0.105,t=0.624,r=0.524,b=0.704), with ID 148f0dac-2213-4c6d-b345-5d5708378f04 -->

Amazon S3 Connector

from agentic_doc.parse import parse
from agentic_doc.connectors import S3ConnectorConfig

config = S3ConnectorConfig(
  bucket_name="your-bucket-name",
  aws_access_key_id="your-access-key",  # Optional if using IAM roles
  aws_secret_access_key="your-secret-key",  # Optional if using IAM roles
  region_name="us-east-1"
) <!-- text, from page 0 (l=0.089,t=0.731,r=0.900,b=0.914), with ID 573660c4-7936-43a7-bbae-5405fc7d6d91 -->

# Parse all documents in the bucket
results = parse(config) <!-- text, from page 0 (l=0.103,t=0.923,r=0.404,b=0.957), with ID 12de646b-0912-43a6-8ba9-e4cab2387af1 -->

# Parse documents in a specific prefix/folder
results = parse(config, connector_path="documents/") <!-- text, from page 0 (l=0.100,t=0.047,r=0.544,b=0.084), with ID 0d507981-c1e8-432d-84a3-c1d17e03b602 -->

Local Directory Connector

from agentic_doc.parse import parse
from agentic_doc.connectors import LocalConnectorConfig

config = LocalConnectorConfig()

# Parse all supported documents in a directory
results = parse(config, connector_path="/path/to/documents")

# Parse with pattern filtering
results = parse(config, connector_path="/path/to/documents", connector_pattern="*.pdf")

# Parse all supported documents in a directory recursively (search subdirectories as well)
config = LocalConnectorConfig(recursive=True)
results = parse(config, connector_path="/path/to/documents") <!-- text, from page 0 (l=0.086,t=0.108,r=0.918,b=0.368), with ID bb44fb96-2357-44a5-85fc-904e2020e77a -->

URL Connector

from agentic_doc.parse import parse
from agentic_doc.connectors import URLConnectorConfig

config = URLConnectorConfig(
    headers={"Authorization": "Bearer your-token"},  # Optional
    timeout=60  # Optional
)

# Parse document from URL
results = parse(config, connector_path="https://example.com/document.pdf") <!-- text, from page 0 (l=0.086,t=0.391,r=0.910,b=0.590), with ID 19735d79-3ae1-42f3-9a5c-6db03682312a -->

Raw Bytes Input <!-- text, from page 0 (l=0.089,t=0.614,r=0.211,b=0.634), with ID 9ff64f52-ce57-4a30-838b-db818395fad9 -->

from agentic_doc.parse import parse

# Load a PDF or image file as bytes
with open("document.pdf", "rb") as f:
    raw_bytes = f.read()

# Parse the document from bytes
results = parse(raw_bytes) <!-- text, from page 0 (l=0.102,t=0.651,r=0.420,b=0.781), with ID 625ac49e-606d-4401-bfa6-259f97d3f911 -->

You can also parse image bytes: <!-- text, from page 0 (l=0.091,t=0.801,r=0.334,b=0.822), with ID 72135500-7660-43f1-ac19-c3a3e8d9efff -->

with open("image.png", "rb") as f:
    image_bytes = f.read()

results = parse(image_bytes) <!-- text, from page 0 (l=0.102,t=0.842,r=0.395,b=0.909), with ID 8bca8690-b2de-41d2-ae51-909831132be1 -->

This is useful when documents are already loaded into memory (e.g., from an API response or uploaded via a web interface). The parser will auto-detect the file type from the bytes. <!-- text, from page 0 (l=0.087,t=0.032,r=0.892,b=0.076), with ID 101a69fe-3734-40e7-bef9-31bda7a53d8d -->

## Why Use It?

- **Simplified Setup:** No need to manage API keys or handle low-level REST calls.
- **Automatic Large File Processing:** Splits large PDFs into manageable parts and processes them in parallel.
- **Built-In Error Handling:** Automatically retries requests with exponential backoff and jitter for common HTTP errors.
- **Parallel Processing:** Efficiently parse multiple documents at once with configurable parallelism. <!-- text, from page 0 (l=0.088,t=0.089,r=0.916,b=0.239), with ID 4338bc68-51a1-4e46-b5b5-56251fef57e2 -->

## Main Features

With this library, you can do things that are otherwise hard to do with the Agentic Document Extraction API alone. This section describes some of the key features this library offers. <!-- text, from page 0 (l=0.087,t=0.253,r=0.873,b=0.335), with ID 67f6d0fc-eed1-4778-8cc7-653b00f55208 -->

## Parse Large PDF Files

**A single REST API call can only handle up to certain amount of pages at a time** (see rate limits). This library automatically splits a large PDF into multiple calls, uses a thread pool to process the calls in parallel, and stitches the results back together as a single result. <!-- text, from page 0 (l=0.089,t=0.350,r=0.893,b=0.441), with ID d6d8ac7e-a75a-47fc-b348-f334e7a7ea42 -->

We've used this library to successfully parse PDFs that are 1000+ pages long. <!-- text, from page 0 (l=0.090,t=0.450,r=0.661,b=0.472), with ID 1a3037b9-ecc5-463f-a061-78dff08c84cf -->

## Parse Multiple Files in a Batch

You can parse multiple files in a single function call with this library. The library processes files in parallel. <!-- text, from page 0 (l=0.091,t=0.487,r=0.855,b=0.540), with ID 0d41cf03-ce90-4068-811f-0fc57d901a8c -->

**NOTE:** You can change the parallelism by setting the `batch_size` setting. <!-- text, from page 0 (l=0.093,t=0.549,r=0.655,b=0.572), with ID c8ec0fde-5a3a-44ec-9ba1-c23824749f60 -->

## Save Groundings as Images

The library can extract and save the visual regions (groundings) of the document where each chunk of content was found. This is useful for visualizing exactly what parts of the document were extracted and for debugging extraction issues. <!-- text, from page 0 (l=0.088,t=0.587,r=0.898,b=0.676), with ID e211be11-b5fd-4a61-ad33-3b1ce21033d0 -->

Each grounding represents a bounding box in the original document, and the library can save these regions as individual PNG images. The images are organized by page number and chunk ID. <!-- text, from page 0 (l=0.090,t=0.688,r=0.895,b=0.727), with ID 1599af07-4d5e-409c-98c6-bd2681d2357f -->

Here's how to use this feature: <!-- text, from page 0 (l=0.091,t=0.738,r=0.319,b=0.757), with ID 4ed57e6b-9edd-432a-9dc2-0988124e5754 -->

from agentic_doc.parse import parse_documents

# Save groundings when parsing a document
results = parse_documents(
    ["path/to/document.pdf"],
    grounding_save_dir="path/to/save/groundings"
) <!-- text, from page 0 (l=0.106,t=0.779,r=0.507,b=0.889), with ID 068bc044-6fb1-442d-9294-80d5286da4a6 -->

# The grounding images will be saved to:
# path/to/save/groundings/document_TIMESTAMP/page_X/CHUNK_TYPE_CHUNK_ID_Y.png
# Where X is the page number, CHUNK_ID is the unique ID of each chunk,
# and Y is the index of the grounding within the chunk <!-- text, from page 0 (l=0.105,t=0.902,r=0.745,b=0.965), with ID 64e88088-cb5e-4123-a817-fa616312b94d -->

# Each chunk's grounding in the result will have the image_path set
for chunk in results[0].chunks:
    for grounding in chunk.grounding:
        if grounding.image_path:
            print(f"Grounding saved to: {grounding.image_path}") <!-- text, from page 0 (l=0.101,t=0.047,r=0.670,b=0.132), with ID 47fb9c02-399b-4ba6-a442-d3bca8c0a600 -->

This feature works with all parsing functions: `parse_documents`, `parse_and_save_documents`, and `parse_and_save_document`. <!-- text, from page 0 (l=0.089,t=0.149,r=0.818,b=0.191), with ID 8cc5004f-7650-4268-b82a-66946c6674b6 -->

## Visualize Parsing Result
The library provides a visualization utility that creates annotated images showing where each chunk of content was extracted from the document. This is useful for: <!-- text, from page 0 (l=0.087,t=0.205,r=0.902,b=0.332), with ID e5edc0d0-8398-417a-81ea-70ec9a95a1f3 -->

Here's how to use the visualization feature:

from agentic_doc.parse import parse
from agentic_doc.utils import viz_parsed_document
from agentic_doc.config import VisualizationConfig <!-- text, from page 0 (l=0.087,t=0.341,r=0.900,b=0.435), with ID 1815bcb9-cce4-4b2e-b3b4-145d70d3644e -->

# Parse a document
results = parse("path/to/document.pdf")
parsed_doc = results[0] <!-- text, from page 0 (l=0.103,t=0.443,r=0.439,b=0.494), with ID 244bde8d-85c9-463a-97f7-f7f099d8b855 -->

# Create visualizations with default settings
# The output images have a PIL.Image.Image type
images = viz_parsed_document(
    "path/to/document.pdf",
    parsed_doc,
    output_dir="path/to/save/visualizations"
) <!-- text, from page 0 (l=0.103,t=0.505,r=0.503,b=0.614), with ID 9412eac0-d33d-4ed0-b392-3ca3ead30665 -->

# Or customize the visualization appearance
viz_config = VisualizationConfig(
    thickness=2,  # Thicker bounding boxes
    text_bg_opacity=0.8,  # More opaque text background
    font_scale=0.7,  # Larger text
    # Custom colors for different chunk types
    color_map={
        ChunkType.TITLE: (0, 0, 255),  # Red for titles
        ChunkType.TEXT: (255, 0, 0),  # Blue for regular text
        # ... other chunk types ...
    }
) <!-- text, from page 0 (l=0.103,t=0.626,r=0.618,b=0.814), with ID cc109b3f-56c7-4bc8-abb7-0f67b8342ede -->

images = viz_parsed_document(
    "path/to/document.pdf",
    parsed_doc,
    output_dir="path/to/save/visualizations",
    viz_config=viz_config
) <!-- text, from page 0 (l=0.104,t=0.825,r=0.483,b=0.921), with ID 5363b890-0dc5-4ca3-9ec6-9e3ad734f0c0 -->

# The visualization images will be saved as: <!-- marginalia, from page 0 (l=0.104,t=0.932,r=0.476,b=0.952), with ID 92f3c9e3-8c8e-450b-b08c-8891f50516e0 -->

# path/to/save/visualizations/document_viz_page_X.png
# Where X is the page number <!-- text, from page 0 (l=0.104,t=0.033,r=0.551,b=0.066), with ID 98fce883-5e7e-4c59-9759-e92f22925fd3 -->

- Bounding boxes around each extracted chunk
- Chunk type and index labels
- Different colors for different types of content (titles, text, tables, etc.)
- Semi-transparent text backgrounds for better readability <!-- text, from page 0 (l=0.089,t=0.088,r=0.635,b=0.208), with ID 6702b839-b0c8-41b8-9598-48b2560eb87a -->

Automatically Handle API Errors and Rate Limits with Retries

The REST API endpoint imposes rate limits per API key. This library automatically handles the rate limit error or other intermittent HTTP errors with retries. <!-- text, from page 0 (l=0.088,t=0.221,r=0.899,b=0.294), with ID e9435dfa-414d-49fc-8eaf-944c72b166b3 -->

For more information, see Error Handling and Configuration Options. <!-- text, from page 0 (l=0.089,t=0.304,r=0.595,b=0.326), with ID 60444664-1b59-413f-9aab-4349bc63d6d3 -->

# Error Handling

This library implements a retry mechanism for handling API failures:

- • Retries are performed for these HTTP status codes: 408, 429, 502, 503, 504.
- • Exponential backoff with jitter is used for retry wait time.
- • The initial retry wait time is 1 second, which increases exponentially.
- • Retry will stop after `max_retries` attempts. Exceeding the limit raises an exception and results in a failure for this request.
- • Retry wait time is capped at `max_retry_wait_time` seconds.
- • Retries include a random jitter of up to 10 seconds to distribute requests and prevent the thundering herd problem. <!-- text, from page 0 (l=0.088,t=0.341,r=0.902,b=0.570), with ID fb557ce8-7434-4c46-9f5f-c4a52ece0954 -->

Parsing Errors

If the REST API request encounters an unrecoverable error during parsing (either from client-side or server-side), the library includes an errors field in the final result for the affected page(s). Each error contains the error message, error_code and corresponding page number. <!-- text, from page 0 (l=0.087,t=0.587,r=0.906,b=0.677), with ID 2f69e7e1-450b-4c13-9087-c1782d38aecf -->

## Configuration Options

The library uses a [Settings](https://) object to manage configuration. You can customize these settings either through environment variables or a `.env` file: <!-- text, from page 0 (l=0.088,t=0.693,r=0.905,b=0.775), with ID b581f95e-6ee9-4583-b88b-fb85bd25d49b -->

Below is an example  .env  file that customizes the configurations:

# Number of files to process in parallel, defaults to 4
BATCH_SIZE=4
# Number of threads used to process parts of each file in parallel, defaults to 5.
MAX_WORKERS=2
# Maximum number of retry attempts for failed intermittent requests, defaults to 100
MAX_RETRIES=80
# Maximum wait time in seconds for each retry, defaults to 60
MAX_RETRY_WAIT_TIME=30 <!-- text, from page 0 (l=0.089,t=0.787,r=0.899,b=0.953), with ID 6cc4db3c-bb2a-439b-bec8-7e32c2dd582f -->

# Logging style for retry, defaults to log_msg
RETRY_LOGGING_STYLE=log_msg <!-- text, from page 0 (l=0.103,t=0.032,r=0.495,b=0.069), with ID c7bdb115-ac73-4b11-bcbe-5fd487183c2d -->

## Max Parallelism

The maximum number of parallel requests is determined by multiplying `BATCH_SIZE` × `MAX_WORKERS`.

> **NOTE:** The maximum parallelism allowed by this library is 100. <!-- text, from page 0 (l=0.088,t=0.094,r=0.837,b=0.180), with ID c3f292dc-9f21-4296-bd7b-f03d961c90c7 -->

Specifically, increasing `MAX_WORKERS` can speed up the processing of large individual files, while increasing `BATCH_SIZE` improves throughput when processing multiple files. <!-- text, from page 0 (l=0.090,t=0.189,r=0.876,b=0.230), with ID 7841958b-401e-4350-85f9-02b81c8c1d08 -->

**NOTE:** Your job's maximum processing throughput may be limited by your API rate limit. If your rate limit isn't high enough, you may encounter rate limit errors, which the library will automatically handle through retries. <!-- text, from page 0 (l=0.094,t=0.237,r=0.878,b=0.297), with ID fd91130f-ad80-43cb-b061-b1ef475160db -->

The optimal values for MAX_WORKERS and BATCH_SIZE depend on your API rate limit and the latency of each REST API call. For example, if your account has a rate limit of 5 requests per minute, and each REST API call takes approximately 60 seconds to complete, and you're processing a single large file, then MAX_WORKERS should be set to 5 and BATCH_SIZE to 1. <!-- text, from page 0 (l=0.090,t=0.307,r=0.881,b=0.383), with ID 8c6f924a-e7ee-47c9-8397-d36c4acb2528 -->

You can find your REST API latency in the logs. If you want to increase your rate limit, schedule a time to meet with us here. <!-- text, from page 0 (l=0.089,t=0.394,r=0.892,b=0.433), with ID 422d2324-61f8-4c6e-a5bc-2d1e8db9ae0b -->

Set RETRY_LOGGING_STYLE

The RETRY_LOGGING_STYLE setting controls how the library logs the retry attempts.

- • log_msg : Log the retry attempts as a log messages. Each attempt is logged as a separate message. This is the default setting.
- • inline_block : Print a yellow progress block ('█') on the same line. Each block represents one retry attempt. Choose this if you don't want to see the verbose retry logging message and still want to track the number of retries that have been made.
- • none : Do not log the retry attempts. <!-- text, from page 0 (l=0.089,t=0.449,r=0.907,b=0.634), with ID cab661e5-4b0e-4d66-b30f-70357710c90d -->

- **API Key Errors:**  
  Ensure your API key is correctly set as an environment variable.
- **Rate Limits:**  
  The library automatically retries requests if you hit the API rate limit. Adjust `BATCH_SIZE` or `MAX_WORKERS` if you encounter frequent rate limit errors.
- **Parsing Failures:**  
  If a document fails to parse, an error chunk will be included in the result, detailing the error message and page index.
- **URL Access Issues:** If you're having trouble accessing documents from URLs, check that the URLs are publicly accessible and point to supported file types (PDF or images). <!-- text, from page 0 (l=0.089,t=0.651,r=0.908,b=0.929), with ID 41760097-65c8-49fe-a1b1-5f91f39fa4dc -->

Note on include_marginalia and include_metadata_in_markdown <!-- text, from page 0 (l=0.090,t=0.943,r=0.786,b=0.967), with ID ef6232f9-81d9-4bf8-b6ee-ed19c661ba23 -->

- `include_marginalia`: If True, the parser will attempt to extract and include marginalia (footer notes, page number, etc.) from the document in the output.
- `include_metadata_in_markdown`: If True, the output markdown will include metadata. <!-- text, from page 0 (l=0.098,t=0.033,r=0.908,b=0.096), with ID ddb143ef-0cf4-45ae-8a33-2a5a87bbd49a -->

Both parameters default to True. You can set them to False to exclude these elements from the output. <!-- text, from page 0 (l=0.088,t=0.105,r=0.846,b=0.130), with ID fed891cc-def7-4dcb-83d2-314a17ba2290 -->

Example: Using the new parameters <!-- text, from page 0 (l=0.089,t=0.141,r=0.375,b=0.162), with ID 764f29f6-e39d-42ed-b6c7-796ba67c0787 -->

from agentic_doc.parse import parse <!-- text, from page 0 (l=0.104,t=0.176,r=0.904,b=0.204), with ID 87b91d67-0921-4932-9e52-f6e0f0d46751 -->

## Releases
No releases published <!-- text, from page 0 (l=0.056,t=0.279,r=0.192,b=0.326), with ID 2b142a14-5b88-44b9-9d86-453a6545dd4b -->

Packages

No packages published <!-- text, from page 0 (l=0.057,t=0.349,r=0.198,b=0.395), with ID cd659f54-f2c6-40b8-8b11-ae98c2164a7f -->

Summary : This image shows a horizontal row of 11 circular profile icons representing contributors to a project, as typically seen in collaborative platforms.

photo:  
Scene Overview : 
  • Main subject is a row of 11 circular contributor avatars.
  • Each avatar is distinct, with a mix of photographic portraits, abstract icons, and stylised illustrations.
  • The avatars are arranged in a single horizontal line, each partially overlapping the next.
  • The background is white, and the heading "Contributors 11" appears above the row.

Technical Details : 
  • No scale bar or magnification.
  • No on-image UI elements except for the contributor icons and the heading.
  • Some avatars are photographs of people, while others are stylised or abstract images.

Spatial Relationships : 
  • All avatars are equally sized and aligned horizontally.
  • The arrangement suggests equal status among contributors, with no hierarchy implied by position.

Analysis : 
  • The image visually communicates the collaborative nature of the project by displaying all contributors together in a uniform, recognisable format.
  • The mix of photographic and abstract avatars suggests a diverse group of contributors, possibly with different roles or levels of anonymity. <!-- figure, from page 0 (l=0.052,t=0.419,r=0.505,b=0.483), with ID 29ba8a8d-f87f-40e2-bbea-56709b1fec4f -->

Languages <!-- text, from page 0 (l=0.057,t=0.502,r=0.149,b=0.520), with ID 7ab5594f-c0d6-449f-bba7-2d19641df479 -->

● Python 100.0% <!-- text, from page 0 (l=0.061,t=0.542,r=0.177,b=0.562), with ID 1e703d77-ca49-4c6e-8d98-bdf58564f0e4 -->