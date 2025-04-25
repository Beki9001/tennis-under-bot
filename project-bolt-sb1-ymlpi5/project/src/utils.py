"""
Utility functions for the Tennis Under Bot.
"""
from typing import Tuple, Dict

def parse_message(message: str) -> Tuple[str, str, str, Tuple[float, float]]:
    """
    Parse incoming message to extract match details.
    
    Args:
        message (str): Raw message text
        
    Returns:
        Tuple[str, str, str, Tuple[float, float]]: Parsed player names, surface, and odds
        
    Raises:
        ValueError: If message format is invalid
    """
    try:
        # Split players and details
        players, surface, odds = [part.strip() for part in message.split(',')]
        
        # Extract player names
        player1, player2 = [name.strip() for name in players.split('vs')]
        
        # Parse odds
        odds1, odds2 = [float(odd.strip()) for odd in odds.split('-')]
        
        return player1, player2, surface.lower(), (odds1, odds2)
        
    except Exception:
        raise ValueError("Invalid message format. Please use: Player1 vs Player2, surface, odds1 - odds2")

def format_response(evaluation: Dict) -> str:
    """
    Format evaluation results into a readable response.
    
    Args:
        evaluation (Dict): Evaluation results
        
    Returns:
        str: Formatted response message
    """
    return (
        f"Form: {evaluation['form_comparison']}\n"
        f"Surface: {evaluation['surface_advantage']}\n"
        f"Injury: {evaluation['injury_status']}\n"
        f"Recommendation: Under 22.5 → {evaluation['confidence']}% safety"
    )