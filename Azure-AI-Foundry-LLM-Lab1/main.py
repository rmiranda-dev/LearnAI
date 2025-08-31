"""
Azure AI Foundry LLM Test Application
"""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_azure_ai_foundry_llm(user_prompt=None):
    """
    Test function to call Azure AI Foundry LLM
    """
    try:
        # Initialize Azure OpenAI client
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        
        # Use user prompt or default test prompt
        test_prompt = user_prompt or "Hello! Can you tell me about Azure AI Foundry and its capabilities?"
        
        print("🚀 Testing Azure AI Foundry LLM Connection...")
        print(f"📝 Prompt: {test_prompt}")
        print("-" * 60)
        
        # Make the API call
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4"),
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": test_prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract and display the response
        ai_response = response.choices[0].message.content
        
        print("🤖 AI Response:")
        print(ai_response)
        print("-" * 60)
        print("✅ Azure AI Foundry LLM test completed successfully!")
        
        return ai_response
        
    except Exception as e:
        print(f"❌ Error calling Azure AI Foundry LLM: {str(e)}")
        print("\n💡 Make sure you have set the following environment variables:")
        print("   - AZURE_OPENAI_API_KEY")
        print("   - AZURE_OPENAI_ENDPOINT")
        print("   - AZURE_OPENAI_DEPLOYMENT_NAME")
        print("   - AZURE_OPENAI_API_VERSION (optional, defaults to '2024-02-01')")
        return None

def main():
    """Main function to run the Azure AI Foundry LLM test."""
    print("🔧 Azure AI Foundry LLM Interactive Application")
    print("=" * 55)
    print("💡 Type 'quit', 'exit', or 'bye' to end the conversation")
    print("=" * 55)
    
    while True:
        # Get user input
        user_input = input("\n🤔 Your question: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
            print("\n👋 Goodbye! Thanks for using Azure AI Foundry LLM!")
            break
        
        # Skip empty inputs
        if not user_input:
            print("⚠️  Please enter a question or type 'quit' to exit.")
            continue
        
        # Test the LLM connection with user's question
        print(f"\n🚀 Sending your question to Azure AI Foundry...")
        response = test_azure_ai_foundry_llm(user_input)
        
        if not response:
            print("⚠️  Failed to get response. Please check your configuration.")
            break

if __name__ == "__main__":
    main()
