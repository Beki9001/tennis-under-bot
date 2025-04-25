"""
Tests for the data scraper module.
"""
import pytest
from src.data_scraper import get_player_stats

def test_get_player_stats_valid_input():
    """Test player stats retrieval with valid input."""
    stats = get_player_stats("Berrettini", "Giron", "clay")
    assert isinstance(stats, dict)
    assert 'player1' in stats
    assert 'player2' in stats
    assert 'form' in stats['player1']
    assert 'surface_performance' in stats['player1']

def test_get_player_stats_invalid_surface():
    """Test player stats retrieval with invalid surface."""
    with pytest.raises(ValueError):
        get_player_stats("Berrettini", "Giron", "invalid_surface")

def test_get_player_stats_timeout():
    """Test timeout handling in player stats retrieval."""
    # Implement timeout test
    pass