#!/usr/bin/env python
"""
Demo script for Mente Maestra game
This script demonstrates the key features of the game without requiring Streamlit.
"""

from mente_maestra import (
    QuestionDatabase, SageDatabase, PowerUpSystem,
    GameSession, PlayerProfile, get_share_text, get_rank_emoji
)


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def demo_player_profile():
    """Demonstrate player profile features."""
    print_header("🎓 PLAYER PROFILE DEMO")
    
    player = PlayerProfile(name="Demo Player", avatar_emoji="🧙")
    print(f"\n{player.avatar_emoji} Player: {player.name}")
    print(f"🏆 Rank: {player.rank}")
    print(f"⭐ Wisdom Fragments: {player.wisdom_fragments}")
    print(f"📊 Current Level: {player.current_level}/6")
    print(f"🎯 Accuracy: {player.get_accuracy():.1f}%")
    
    # Simulate progression
    player.wisdom_fragments = 100
    player.update_rank()
    print(f"\n✨ After earning 100 fragments...")
    print(f"🏆 New Rank: {player.rank}")
    
    return player


def demo_question_database():
    """Demonstrate question database."""
    print_header("📚 QUESTION DATABASE DEMO")
    
    db = QuestionDatabase()
    print(f"\n✓ Total questions available: {len(db.questions)}")
    
    # Show questions by category
    categories = set(q.category for q in db.questions)
    print(f"✓ Categories: {', '.join(categories)}")
    
    # Get sample questions
    print("\n--- Sample History Questions ---")
    history_qs = db.get_questions_by_category("Historia", 2)
    for i, q in enumerate(history_qs, 1):
        print(f"\n{i}. {q.question}")
        for j, opt in enumerate(q.options):
            marker = "✓" if j == q.correct_answer else " "
            print(f"   [{marker}] {chr(65+j)}) {opt}")
        print(f"   💡 Hint: {q.hint}")
    
    return db


def demo_sage_database():
    """Demonstrate sage database."""
    print_header("🧙 SAGE DATABASE DEMO")
    
    db = SageDatabase()
    print(f"\n✓ Total sages: {len(db.sages)}")
    
    print("\n--- All Sages ---")
    for sage in db.sages:
        print(f"\n{sage.avatar} Level {sage.level}: {sage.name}")
        print(f"   Title: {sage.title}")
        print(f"   Specialty: {sage.specialty}")
        print(f"   {sage.description}")
    
    return db


def demo_power_up_system():
    """Demonstrate power-up system."""
    print_header("💫 POWER-UP SYSTEM DEMO")
    
    system = PowerUpSystem()
    power_ups = system.get_all_power_ups()
    
    print(f"\n✓ Available power-ups: {len(power_ups)}")
    
    for pu in power_ups:
        print(f"\n{pu.icon} {pu.name}")
        print(f"   Description: {pu.description}")
        print(f"   Cost: {pu.cost} fragments")
    
    return system


def demo_game_session():
    """Demonstrate a complete game session."""
    print_header("🎮 GAME SESSION DEMO")
    
    # Setup
    player = PlayerProfile(name="Demo Player")
    qdb = QuestionDatabase()
    sdb = SageDatabase()
    
    # Get first sage
    sage = sdb.get_sage_by_level(1)
    print(f"\n{sage.avatar} Challenge: {sage.name}")
    print(f"Title: {sage.title}")
    print(f"Specialty: {sage.specialty}")
    
    # Get questions
    questions = qdb.get_questions_by_category(sage.specialty, 3)
    print(f"\n✓ Loaded {len(questions)} questions")
    
    # Start game
    game = GameSession(player, 1)
    game.start_level(questions, sage)
    
    print("\n--- Playing Game ---")
    
    # Simulate answering questions
    for i, question in enumerate(questions, 1):
        print(f"\n📝 Question {i}/{len(questions)}")
        print(f"Category: {question.category} | Difficulty: {'⭐' * question.difficulty}")
        print(f"\n{question.question}")
        
        for j, opt in enumerate(question.options):
            print(f"   {chr(65+j)}) {opt}")
        
        # Simulate answering (sometimes correct, sometimes wrong)
        answer = question.correct_answer if i % 2 == 1 else (question.correct_answer + 1) % len(question.options)
        
        result = game.answer_question(answer)
        
        if result['correct']:
            print(f"\n✅ Correct! +{result['fragments_earned']} fragments")
            print(f"🔥 Streak: {result['streak']}")
        else:
            print(f"\n❌ Wrong! Correct answer: {question.options[question.correct_answer]}")
        
        print(f"📊 Total Score: {result['total_score']}")
    
    if game.completed:
        print("\n🎉 LEVEL COMPLETED!")
        print(f"✨ Total fragments earned: {game.score}")
        print(f"📊 New wisdom fragments: {player.wisdom_fragments}")
        print(f"🏆 New rank: {player.rank}")
    
    return player


def demo_social_sharing():
    """Demonstrate social sharing."""
    print_header("📱 SOCIAL SHARING DEMO")
    
    player = PlayerProfile(name="Champion Player")
    player.wisdom_fragments = 350
    player.current_level = 5
    player.questions_answered = 50
    player.questions_correct = 42
    player.update_rank()
    
    share_text = get_share_text(player)
    
    print("\n--- Share Text ---")
    print(share_text)
    
    print("\n✓ Ready to share on social media!")


def main():
    """Run all demos."""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║        🧠 MENTE MAESTRA: EL TORNEO DE LOS SABIOS 🧠       ║")
    print("║                                                            ║")
    print("║                    FEATURE DEMONSTRATION                   ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    # Run all demos
    demo_player_profile()
    demo_question_database()
    demo_sage_database()
    demo_power_up_system()
    player = demo_game_session()
    demo_social_sharing()
    
    print_header("✅ DEMO COMPLETE")
    print("\nAll features demonstrated successfully!")
    print("\nTo play the full game, run: streamlit run app.py")
    print("Then navigate to the '🧠 Mente Maestra' section.")
    print()


if __name__ == "__main__":
    main()
