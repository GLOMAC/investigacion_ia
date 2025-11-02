"""
Tests for Mente Maestra game logic
"""

import pytest
from mente_maestra import (
    Question, Sage, PowerUp, PlayerProfile,
    QuestionDatabase, SageDatabase, PowerUpSystem, GameSession,
    get_share_text, get_rank_emoji
)


class TestPlayerProfile:
    """Test PlayerProfile class."""
    
    def test_player_creation(self):
        """Test creating a new player."""
        player = PlayerProfile(name="Test Player")
        assert player.name == "Test Player"
        assert player.current_level == 1
        assert player.wisdom_fragments == 0
        assert player.rank == "Aprendiz"
    
    def test_accuracy_calculation(self):
        """Test accuracy calculation."""
        player = PlayerProfile()
        assert player.get_accuracy() == 0.0
        
        player.questions_answered = 10
        player.questions_correct = 7
        assert player.get_accuracy() == 70.0
    
    def test_rank_update(self):
        """Test rank updates based on wisdom fragments."""
        player = PlayerProfile()
        
        player.wisdom_fragments = 10
        player.update_rank()
        assert player.rank == "Aprendiz"
        
        player.wisdom_fragments = 50
        player.update_rank()
        assert player.rank == "Estudiante"
        
        player.wisdom_fragments = 100
        player.update_rank()
        assert player.rank == "Erudito"
        
        player.wisdom_fragments = 200
        player.update_rank()
        assert player.rank == "Sabio"
        
        player.wisdom_fragments = 350
        player.update_rank()
        assert player.rank == "Gran Sabio"
        
        player.wisdom_fragments = 600
        player.update_rank()
        assert player.rank == "Maestro Supremo"


class TestQuestionDatabase:
    """Test QuestionDatabase class."""
    
    def test_database_initialization(self):
        """Test that database initializes with questions."""
        db = QuestionDatabase()
        assert len(db.questions) > 0
    
    def test_get_questions_by_category(self):
        """Test retrieving questions by category."""
        db = QuestionDatabase()
        questions = db.get_questions_by_category("Historia", 3)
        assert len(questions) <= 3
        assert all(q.category == "Historia" for q in questions)
    
    def test_get_questions_by_difficulty(self):
        """Test retrieving questions by difficulty."""
        db = QuestionDatabase()
        questions = db.get_questions_by_difficulty(1, 3)
        assert len(questions) <= 3
        assert all(q.difficulty == 1 for q in questions)
    
    def test_get_random_questions(self):
        """Test retrieving random questions."""
        db = QuestionDatabase()
        questions = db.get_random_questions(5)
        assert len(questions) <= 5


class TestSageDatabase:
    """Test SageDatabase class."""
    
    def test_database_initialization(self):
        """Test that database initializes with sages."""
        db = SageDatabase()
        assert len(db.sages) == 6
    
    def test_get_sage_by_level(self):
        """Test retrieving sage by level."""
        db = SageDatabase()
        sage = db.get_sage_by_level(1)
        assert sage is not None
        assert sage.level == 1
        assert sage.name == "Sócrates"
    
    def test_final_sage(self):
        """Test final sage (Gran Consejo)."""
        db = SageDatabase()
        sage = db.get_sage_by_level(6)
        assert sage is not None
        assert sage.name == "El Gran Consejo"
        assert sage.specialty == "Todas"


class TestPowerUpSystem:
    """Test PowerUpSystem class."""
    
    def test_power_up_retrieval(self):
        """Test retrieving power-ups."""
        system = PowerUpSystem()
        vision = system.get_power_up("vision_futuro")
        assert vision is not None
        assert vision.name == "Visión del Futuro"
        assert vision.cost == 10
    
    def test_all_power_ups(self):
        """Test getting all power-ups."""
        system = PowerUpSystem()
        power_ups = system.get_all_power_ups()
        assert len(power_ups) == 4


class TestGameSession:
    """Test GameSession class."""
    
    def test_game_creation(self):
        """Test creating a game session."""
        player = PlayerProfile(name="Test")
        game = GameSession(player, 1)
        assert game.level == 1
        assert game.score == 0
        assert game.streak == 0
    
    def test_answer_correct_question(self):
        """Test answering a question correctly."""
        player = PlayerProfile()
        game = GameSession(player, 1)
        
        question = Question(
            "Test question?",
            ["A", "B", "C", "D"],
            1, "Test", 1, "hint"
        )
        game.start_level([question], Sage("Test", "Test", "Test", 1, "Test", "🧙"))
        
        result = game.answer_question(1)  # Correct answer
        
        assert result["correct"] is True
        assert result["fragments_earned"] > 0
        assert result["streak"] == 1
        assert player.questions_correct == 1
        assert player.questions_answered == 1
    
    def test_answer_wrong_question(self):
        """Test answering a question incorrectly."""
        player = PlayerProfile()
        game = GameSession(player, 1)
        
        question = Question(
            "Test question?",
            ["A", "B", "C", "D"],
            1, "Test", 1, "hint"
        )
        game.start_level([question], Sage("Test", "Test", "Test", 1, "Test", "🧙"))
        
        result = game.answer_question(0)  # Wrong answer
        
        assert result["correct"] is False
        assert result["fragments_earned"] == 0
        assert result["streak"] == 0
        assert player.questions_correct == 0
        assert player.questions_answered == 1
        assert len(player.failed_questions) == 1
    
    def test_streak_bonus(self):
        """Test that streak provides bonus fragments."""
        player = PlayerProfile()
        game = GameSession(player, 1)
        
        questions = [
            Question("Q1", ["A", "B"], 0, "Test", 1, ""),
            Question("Q2", ["A", "B"], 0, "Test", 1, ""),
        ]
        sage = Sage("Test", "Test", "Test", 1, "Test", "🧙")
        game.start_level(questions, sage)
        
        result1 = game.answer_question(0)  # Correct
        result2 = game.answer_question(0)  # Correct
        
        # Second answer should have more fragments due to streak
        assert result2["fragments_earned"] > result1["fragments_earned"]
    
    def test_power_up_usage(self):
        """Test using power-ups."""
        player = PlayerProfile()
        player.power_ups_owned["vision_futuro"] = 1
        
        game = GameSession(player, 1)
        
        # Use the power-up
        success = game.use_power_up("vision_futuro")
        assert success is True
        assert player.power_ups_owned["vision_futuro"] == 0
        assert game.active_power_ups.get("vision_futuro") is True
    
    def test_level_completion(self):
        """Test level completion."""
        player = PlayerProfile()
        game = GameSession(player, 1)
        
        question = Question("Q", ["A", "B"], 0, "Test", 1, "")
        sage = Sage("Test", "Test", "Test", 1, "Test", "🧙")
        game.start_level([question], sage)
        
        result = game.answer_question(0)  # Correct answer
        
        assert result["completed"] is True
        assert game.completed is True
        assert 1 in player.completed_levels
        assert player.current_level == 2


class TestUtilityFunctions:
    """Test utility functions."""
    
    def test_get_share_text(self):
        """Test social media share text generation."""
        player = PlayerProfile(name="Test Player")
        player.wisdom_fragments = 100
        player.current_level = 3
        
        text = get_share_text(player)
        
        assert "Test Player" in text
        assert "100" in text
        assert "3" in text
    
    def test_get_rank_emoji(self):
        """Test rank emoji retrieval."""
        assert get_rank_emoji("Aprendiz") == "🎓"
        assert get_rank_emoji("Maestro Supremo") == "👑"
        assert get_rank_emoji("Unknown") == "🎓"  # Default


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
