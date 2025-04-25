"""
Module for evaluating tennis match data and generating betting recommendations.
"""
from typing import Dict, Tuple
from openai_client import analyze_match

def evaluate_match(stats: Dict, odds: Tuple[float, float]) -> Dict:
    """
    Evaluate match data and generate Under 22.5 games recommendation.
    
    Args:
        stats (Dict): Player statistics and form data
        odds (Tuple[float, float]): Match odds for both players
        
    Returns:
        Dict: Evaluation results including confidence percentage
    """
    try:
        # Get AI analysis
        ai_analysis = analyze_match(stats)
        
        # Combine AI analysis with basic stats
        evaluation = {
            'form_comparison': f"{stats['player1']['form']} - {stats['player2']['form']}",
            'surface_advantage': 'Player 1 better' if stats['player1']['surface_performance'] > stats['player2']['surface_performance'] else 'Player 2 better',
            'injury_status': 'None',
            'confidence': ai_analysis['confidence'],
            'ai_recommendation': ai_analysis['analysis']
        }
        
        return evaluation
        
    except Exception as e:
        raise Exception(f"Failed to evaluate match data: {str(e)}")