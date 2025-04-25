"""
Tests for the AI evaluator module.
"""
import pytest
from src.ai_evaluator import evaluate_match

def test_evaluate_match_valid_input():
    """Test match evaluation with valid input."""
    stats = {
        'player1': {'form': 'Good', 'surface_performance': 75.0, 'injury_status': None},
        'player2': {'form': 'Medium', 'surface_performance': 65.0, 'injury_status': None}
    }
    odds = (1.22, 4.20)
    
    result = evaluate_match(stats, odds)
    assert isinstance(result, dict)
    assert 'confidence' in result
    assert isinstance(result['confidence'], (int, float))
    assert 0 <= result['confidence'] <= 100

def test_evaluate_match_missing_data():
    """Test match evaluation with missing data."""
    stats = {
        'player1': {'form': None, 'surface_performance': None, 'injury_status': None},
        'player2': {'form': None, 'surface_performance': None, 'injury_status': None}
    }
    odds = (1.22, 4.20)
    
    with pytest.raises(Exception):
        evaluate_match(stats, odds)