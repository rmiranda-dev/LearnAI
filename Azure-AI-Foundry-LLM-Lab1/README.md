# Azure AI Foundry LLM Test Project

A Python project to test and interact with Large Language Models (LLMs) in Azure AI Foundry.

## Getting Started

### Prerequisites

1. Python 3.8 or higher
2. Azure subscription with Azure AI Foundry access
3. Azure OpenAI resource deployed

### Setup Instructions

1. **Clone and navigate to the project:**
   ```powershell
   cd "01_Lab1"
   ```

2. **Create and activate a virtual environment (recommended):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Copy `.env.template` to `.env`
   - Fill in your Azure AI Foundry credentials:
     ```
     AZURE_OPENAI_API_KEY=your_actual_api_key
     AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
     AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
     ```

4. **Run the LLM test:**
   ```powershell
   python main.py
   ```

**Note:** Make sure your virtual environment is activated when running the application.

## Project Structure

```
01_Lab1/
├── main.py              # Azure AI Foundry LLM test application
├── requirements.txt     # Python dependencies (openai, python-dotenv)
├── .env.template        # Environment variables template
├── .env                 # Your actual environment variables (not in git)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Features

- ✅ Simple Azure AI Foundry LLM integration
- ✅ Minimal dependencies (only openai and python-dotenv)
- ✅ Environment-based configuration
- ✅ Error handling and user-friendly messages
- ✅ Clean, focused codebase for LLM testing

## Azure AI Foundry Setup

1. **Create Azure OpenAI Resource:**
   - Go to Azure Portal
   - Create an Azure OpenAI resource
   - Deploy a model (e.g., GPT-4)

2. **Get Credentials:**
   - Copy the API key from your Azure OpenAI resource
   - Copy the endpoint URL
   - Note your deployment name

3. **Update .env file** with your actual values

## Usage Examples

The application will:
1. Connect to your Azure AI Foundry LLM
2. Send a test prompt
3. Display the AI response
4. Show success/failure status

## Troubleshooting

- Ensure your Azure OpenAI resource is properly deployed
- Check that your API key and endpoint are correct
- Verify your deployment name matches the one in Azure
- Make sure you have sufficient quota/credits
