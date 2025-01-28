# Multimodal Agent for Knowledge Integration and PDF Processing

This project integrates a multimodal assistant powered by the Gemini model, capable of interacting with users through chat and processing data from PDFs stored in a PostgreSQL database. The system utilizes a vector database for fast retrieval and embedding of knowledge, specifically from recipe PDF documents.

## Features

- **Google Gemini Model Integration**: The assistant is powered by the Gemini model, providing advanced conversational abilities.
- **PDF Knowledge Base**: PDFs can be stored and processed for knowledge extraction.
- **PostgreSQL Backend**: Data is stored and queried using PostgreSQL with pgvector for efficient vector search capabilities.
- **Interactive Chat Interface**: Users can interact with the assistant in a chat-based interface, retrieving information from PDFs and interacting with embedded knowledge.
- **Real-Time Knowledge Updates**: The knowledge base can be updated in real-time by loading and processing new PDFs.

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL database
- `.env` file with necessary API keys

### Install Dependencies

Clone this repository and install the required packages:

```bash
git clone https://github.com/PriyanshuDey23/Agentic-rag.git
```
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Ensure you have a `.env` file in the root of your project with the following content:

```bash
GOOGLE_API_KEY=your-google-api-key
```

Make sure to replace `your-google-api-key` with your actual API key from Google.

### Set Up PostgreSQL Database

Set up PostgreSQL to store vectors and assist with querying knowledge from the PDF documents.

1. Ensure your PostgreSQL server is running locally or remotely.
2. Create a database and a table for the vector storage:
   ```sql
   CREATE DATABASE ai;
   ```
3. Adjust the connection URL in the code if necessary (`db_url`).

## Usage

### Running the Application

Once the environment is set up, you can start the application:

```bash
streamlit run app.py
```

The application will start and the multimodal agent will be available for interaction.

### Cache Management

The system caches the agent initialization and knowledge base load to ensure efficient processing. You can adjust the caching mechanism or clear the cache if required.

### Interacting with the Assistant

Once the application is running, use the interface to interact with the assistant. It will load knowledge from the provided PDF and can answer questions based on the extracted information.

## Development

To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Install dependencies via `pip install -r requirements.txt`.
4. Make your changes and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
