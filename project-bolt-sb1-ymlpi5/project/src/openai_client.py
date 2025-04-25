"""
OpenAI API client for Tennis Under Bot.
Handles all interactions with the OpenAI API.
"""
import os
from typing import Dict
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables")

openai.api_key = OPENAI_API_KEY

def analyze_match(stats: Dict) -> Dict:
    """
    Analyze match statistics using OpenAI's GPT model.
    
    Args:
        stats (Dict): Match statistics including player form and surface performance
        
    Returns:
        Dict: AI analysis results including recommendation and confidence
        
    Raises:
        Exception: If API call fails or response is invalid
    """
    try:
        # Construct the prompt
        prompt = f"""
        Analyze this tennis match data and provide an Under 22.5 games recommendation:
        
        Player 1:
        - Form: {stats['player1']['form']}
        - Surface Performance: {stats['player1']['surface_performance']}%
        - Injury Status: {stats['player1']['injury_status'] or 'None'}
        
        Player 2:
        - Form: {stats['player2']['form']}
        - Surface Performance: {stats['player2']['surface_performance']}%
        - Injury Status: {stats['player2']['injury_status'] or 'None'}
        
        Provide a recommendation for Under 22.5 games with a confidence percentage.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a tennis match analyzer specializing in game total predictions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        # Extract recommendation from response
        analysis = response.choices[0].message.content
        
        # Parse confidence from analysis (assuming it's in the text)
        confidence = 75  # Default confidence
        
        return {
            'analysis': analysis,
            'confidence': confidence
        }
        
    except openai.error.OpenAIError as e:
        raise Exception(f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to analyze match: {str(e)}")