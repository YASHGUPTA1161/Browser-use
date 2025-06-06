# import os
# import requests
# from dotenv import load_dotenv
# from pydantic import BaseModel
# from typing import List

# # Load environment variables from the .env file
# load_dotenv()

# # Retrieve the API key from environment variables
# api_key = os.getenv("OPENROUTER_API_KEY")

# # Check if API key is set
# if not api_key:
#     raise ValueError("API key is missing. Please set it in the .env file.")

# # Define the model to handle the parsed data (example model for Instagram posts)
# class Post(BaseModel):
#     caption: str
#     url: str

# class Posts(BaseModel):
#     posts: List[Post]

# # Function to make the API call to DeepSeek
# def get_response_from_deepseek(prompt: str):
#     # API endpoint for DeepSeek
#     api_url = "https://openrouter.ai/api/v1/chat/completions"
    
#     # Headers with API Key
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
    
#     # Payload to send
#     data = {
#         "model": "deepseek-r1",  # Use the relevant model, like deepseek-r1
#         "messages": [{"role": "user", "content": prompt}]
#     }
    
#     # Make the request to the API
#     try:
#         response = requests.post(api_url, headers=headers, json=data)
        
#         # Check if the response was successful
#         if response.status_code == 200:
#             return response.json()  # Return the response JSON
#         else:
#             print(f"Error during API call: Error code: {response.status_code} - {response.text}")
#             return None
#     except Exception as e:
#         print(f"Error during API call: {str(e)}")
#         return None

# # Example function to handle the API response
# def handle_api_response(data):
#     if data is not None:
#         try:
#             # Validate and parse the response using Pydantic models
#             parsed = Posts.model_validate(data)
#             print(f"Parsed Data: {parsed}")
#         except Exception as e:
#             print(f"Error parsing the response: {str(e)}")
#     else:
#         print("No data received from the API.")

# # Main function to run the workflow
# def main():
#     # Define the prompt to send to DeepSeek
#     prompt = "open Instagram and get the latest posts from a specific user"
    
#     # Call the API
#     response_data = get_response_from_deepseek(prompt)
    
#     # Handle the response
#     handle_api_response(response_data)

# if __name__ == "__main__":
#     main()

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch the API key from environment variable
API_KEY = os.getenv('GEMINI_API_KEY')

# Define the API URL
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Example request headers and payload
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Example payload for generating content (adapt based on Gemini's API documentation)
data = {
    "prompt": "Write a short story about a robot learning to love.",
    "maxOutputTokens": 100
}

def fetch_content(api_url, headers, data):
    try:
        # Send a POST request to the API
        response = requests.post(api_url, headers=headers, json=data)
        
        if response.status_code == 200:
            # Successfully got the response
            result = response.json()
            print("Generated content:", result)
        else:
            print(f"Error during API call: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Fetch content from Gemini API
fetch_content(API_URL, headers, data)
