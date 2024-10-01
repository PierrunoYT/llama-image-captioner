import gradio as gr
import requests
import json
import os
import base64

# Read the API key from the Windows environment variable
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set. Please set it using the 'setx' command.")

YOUR_SITE_URL = "https://your-site-url.com"
YOUR_APP_NAME = "Image Captioning App"

def caption_image(image):
    # Convert image to base64
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    image_url = f"data:image/jpeg;base64,{encoded_string}"

    payload = {
        "model": "meta-llama/llama-3.2-90b-vision-instruct",
        "messages": [
            {
                "role": "system",
                "content": "You are an advanced AI capable of analyzing images. Your task is to provide detailed, accurate, and concise descriptions of the images presented to you. Focus on the main elements, colors, actions, and overall composition. If there are any notable or unusual aspects, mention those as well."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Please describe this image in detail."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": YOUR_SITE_URL,
                "X-Title": YOUR_APP_NAME,
            },
            json=payload
        )

        response.raise_for_status()  # Raise an exception for bad status codes

        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            caption = result['choices'][0]['message']['content']
            return caption
        else:
            return f"Error: Unexpected response format. Full response: {json.dumps(result, indent=2)}"
    
    except requests.exceptions.RequestException as e:
        return f"Error making request: {str(e)}"
    except json.JSONDecodeError:
        return f"Error decoding JSON response. Raw response: {response.text}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="filepath"),
    outputs="text",
    title="Detailed Image Captioning",
    description="Upload an image to get a detailed description."
)

# Launch the app
iface.launch(share=True)