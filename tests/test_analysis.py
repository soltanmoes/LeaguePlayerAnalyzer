from analysis import calculate_win_rate, calculate_match_kda, calculate_overall_kda, group_by_champ
import pytest

def test_win_rate():
    participants = [
        {"win": True},
        {"win": False},
        {"win": True},
        {"win": True},
        {"win": False}
    ]

    result = calculate_win_rate(participants)

    assert result == 60.0


def test_empty_participants():
    participants = []

    result = calculate_win_rate(participants)

    assert result is None


def test_match_kda():
    participants = [
        {"kills": 10, "assists": 0, "deaths": 0},
        {"kills": 7, "assists": 2, "deaths": 10},
        {"kills": 2, "assists": 3, "deaths": 1000},
        {"kills": 10, "assists": 2, "deaths": 0},
    ]

    result = calculate_match_kda(participants)

    assert result == pytest.approx([10.0, 0.9, 0.005, 12.0])


def test_overall_kda():
    participants = [
        {"kills": 10, "assists": 0, "deaths": 0},
        {"kills": 7, "assists": 2, "deaths": 10},
        {"kills": 2, "assists": 3, "deaths": 1000},
        {"kills": 10, "assists": 2, "deaths": 0},
    ]

    result = calculate_overall_kda(participants)

    assert result == pytest.approx(36 / 1010)

def test_empty_overall_kda():
    assert calculate_overall_kda([]) is None

def test_zero_deaths_overall_kda():
    participants = [
        {"kills": 10, "assists": 5, "deaths": 0}
    ]

    assert calculate_overall_kda(participants) == 15.0

def test_group_by_champ():
    participants = [
        {"championName": "Ahri", "win": True, "kills": 10, "deaths": 2, "assists": 5},
        {"championName": "Ahri", "win": True, "kills": 7, "deaths": 3, "assists": 9},
        {"championName": "Yasuo", "win": False, "kills": 4, "deaths": 8, "assists": 3}
    ]

    assert group_by_champ(participants) == { 
        "Ahri": [
            {"championName": "Ahri", "win": True, "kills": 10, "deaths": 2, "assists": 5},
            {"championName": "Ahri", "win": True, "kills": 7, "deaths": 3, "assists": 9}
        ],
        "Yasuo": [
            {"championName": "Yasuo", "win": False, "kills": 4, "deaths": 8, "assists": 3}
        ]
    }