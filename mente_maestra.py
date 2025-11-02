"""
Mente Maestra: El Torneo de los Sabios
A trivia game with levels, power-ups, and social sharing features.
"""

import random
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Question:
    """Represents a trivia question."""
    question: str
    options: List[str]
    correct_answer: int  # Index of correct option
    category: str
    difficulty: int  # 1-3 (easy, medium, hard)
    hint: str = ""


@dataclass
class Sage:
    """Represents a legendary sage opponent."""
    name: str
    title: str
    specialty: str
    level: int
    description: str
    avatar: str  # Emoji or icon


@dataclass
class PowerUp:
    """Represents a power-up that can be purchased with wisdom fragments."""
    name: str
    description: str
    cost: int
    icon: str


@dataclass
class PlayerProfile:
    """Represents a player's profile and progress."""
    name: str = "Jugador"
    current_level: int = 1
    wisdom_fragments: int = 0
    total_score: int = 0
    questions_answered: int = 0
    questions_correct: int = 0
    rank: str = "Aprendiz"
    avatar_emoji: str = "🎓"
    power_ups_owned: Dict[str, int] = field(default_factory=dict)
    completed_levels: List[int] = field(default_factory=list)
    failed_questions: List[Question] = field(default_factory=list)
    
    def get_accuracy(self) -> float:
        """Calculate player's accuracy percentage."""
        if self.questions_answered == 0:
            return 0.0
        return (self.questions_correct / self.questions_answered) * 100
    
    def update_rank(self):
        """Update player rank based on wisdom fragments."""
        rank_thresholds = get_rank_thresholds()
        for rank_name, min_fragments, _ in reversed(rank_thresholds):
            if self.wisdom_fragments >= min_fragments:
                self.rank = rank_name
                break


class QuestionDatabase:
    """Database of trivia questions."""
    
    def __init__(self):
        self.questions = self._initialize_questions()
    
    def _initialize_questions(self) -> List[Question]:
        """Initialize the question database."""
        questions = [
            # Historia
            Question(
                "¿En qué año cayó el Imperio Romano de Occidente?",
                ["476 d.C.", "410 d.C.", "395 d.C.", "527 d.C."],
                0, "Historia", 2,
                "Fue durante el siglo V d.C."
            ),
            Question(
                "¿Quién fue el primer presidente de los Estados Unidos?",
                ["Thomas Jefferson", "George Washington", "John Adams", "Benjamin Franklin"],
                1, "Historia", 1,
                "Su apellido es el nombre de la capital del país."
            ),
            Question(
                "¿En qué año comenzó la Segunda Guerra Mundial?",
                ["1939", "1941", "1937", "1945"],
                0, "Historia", 1,
                "Fue antes de que Estados Unidos entrara en la guerra."
            ),
            Question(
                "¿Qué civilización construyó Machu Picchu?",
                ["Los Mayas", "Los Aztecas", "Los Incas", "Los Olmecas"],
                2, "Historia", 2,
                "Esta civilización estaba ubicada en los Andes."
            ),
            
            # Ciencia
            Question(
                "¿Cuál es el planeta más grande del sistema solar?",
                ["Saturno", "Júpiter", "Neptuno", "Urano"],
                1, "Ciencia", 1,
                "Es famoso por su Gran Mancha Roja."
            ),
            Question(
                "¿Qué científico propuso la teoría de la relatividad?",
                ["Isaac Newton", "Niels Bohr", "Albert Einstein", "Stephen Hawking"],
                2, "Ciencia", 1,
                "Su fórmula más famosa es E=mc²."
            ),
            Question(
                "¿Cuál es el elemento químico más abundante en el universo?",
                ["Oxígeno", "Carbono", "Hidrógeno", "Helio"],
                2, "Ciencia", 2,
                "Es el elemento más simple, con un solo protón."
            ),
            Question(
                "¿Cuántos huesos tiene el cuerpo humano adulto?",
                ["206", "186", "216", "196"],
                0, "Ciencia", 2,
                "Es un número entre 200 y 210."
            ),
            Question(
                "¿Qué orgánulo celular es responsable de la producción de energía?",
                ["Núcleo", "Ribosoma", "Mitocondria", "Cloroplasto"],
                2, "Ciencia", 3,
                "Se le conoce como la 'central energética' de la célula."
            ),
            
            # Arte
            Question(
                "¿Quién pintó 'La Mona Lisa'?",
                ["Miguel Ángel", "Leonardo da Vinci", "Rafael", "Donatello"],
                1, "Arte", 1,
                "También fue inventor y científico renacentista."
            ),
            Question(
                "¿En qué museo se encuentra 'La noche estrellada' de Van Gogh?",
                ["Louvre", "MoMA", "Prado", "Uffizi"],
                1, "Arte", 2,
                "Está en Nueva York."
            ),
            Question(
                "¿Qué corriente artística fundó Pablo Picasso?",
                ["Surrealismo", "Cubismo", "Expresionismo", "Impresionismo"],
                1, "Arte", 2,
                "Representa objetos desde múltiples perspectivas."
            ),
            Question(
                "¿Quién esculpió 'El David'?",
                ["Leonardo da Vinci", "Donatello", "Miguel Ángel", "Bernini"],
                2, "Arte", 1,
                "También pintó la Capilla Sixtina."
            ),
            
            # Cultura General
            Question(
                "¿Cuál es el océano más grande del mundo?",
                ["Atlántico", "Índico", "Ártico", "Pacífico"],
                3, "Cultura General", 1,
                "Cubre casi un tercio de la superficie terrestre."
            ),
            Question(
                "¿Cuántos continentes hay en la Tierra?",
                ["5", "6", "7", "8"],
                2, "Cultura General", 1,
                "Incluye la Antártida."
            ),
            Question(
                "¿Cuál es la montaña más alta del mundo?",
                ["K2", "Everest", "Kilimanjaro", "Aconcagua"],
                1, "Cultura General", 1,
                "Se encuentra en el Himalaya."
            ),
            Question(
                "¿En qué país se encuentra la Torre Eiffel?",
                ["Italia", "España", "Francia", "Bélgica"],
                2, "Cultura General", 1,
                "Es la capital del país."
            ),
            
            # Lógica
            Question(
                "Si todos los gatos son animales y algunos animales vuelan, ¿qué podemos concluir?",
                ["Todos los gatos vuelan", "Algunos gatos vuelan", "Ningún gato vuela", "No se puede concluir nada"],
                3, "Lógica", 2,
                "No hay información que conecte directamente gatos con volar."
            ),
            Question(
                "¿Qué número sigue en la secuencia: 2, 4, 8, 16, ?",
                ["24", "32", "20", "30"],
                1, "Lógica", 1,
                "Cada número es el doble del anterior."
            ),
            Question(
                "Si A=1, B=2, C=3, ¿cuánto vale 'CAB'?",
                ["123", "312", "321", "231"],
                1, "Lógica", 2,
                "Escribe cada letra como su número correspondiente."
            ),
            Question(
                "¿Cuál es el siguiente número primo después de 7?",
                ["9", "10", "11", "13"],
                2, "Lógica", 2,
                "Un número primo solo es divisible por 1 y por sí mismo."
            ),
        ]
        return questions
    
    def get_questions_by_category(self, category: str, count: int = 5) -> List[Question]:
        """Get random questions from a specific category."""
        category_questions = [q for q in self.questions if q.category == category]
        return random.sample(category_questions, min(count, len(category_questions)))
    
    def get_questions_by_difficulty(self, difficulty: int, count: int = 5) -> List[Question]:
        """Get random questions of a specific difficulty."""
        difficulty_questions = [q for q in self.questions if q.difficulty == difficulty]
        return random.sample(difficulty_questions, min(count, len(difficulty_questions)))
    
    def get_random_questions(self, count: int = 5) -> List[Question]:
        """Get random questions from any category."""
        return random.sample(self.questions, min(count, len(self.questions)))


class SageDatabase:
    """Database of legendary sages."""
    
    def __init__(self):
        self.sages = self._initialize_sages()
    
    def _initialize_sages(self) -> List[Sage]:
        """Initialize the sage database."""
        return [
            Sage(
                name="Sócrates",
                title="El Filósofo Inquisidor",
                specialty="Lógica",
                level=1,
                description="Maestro de la lógica y el pensamiento crítico. Te desafiará con preguntas que requieren razonamiento.",
                avatar="🧙‍♂️"
            ),
            Sage(
                name="Cleopatra",
                title="La Reina del Nilo",
                specialty="Historia",
                level=2,
                description="Conocedora de grandes imperios y civilizaciones. Pondrá a prueba tu conocimiento histórico.",
                avatar="👑"
            ),
            Sage(
                name="Leonardo da Vinci",
                title="El Genio Renacentista",
                specialty="Arte",
                level=3,
                description="Artista, inventor y científico. Te enfrentará con preguntas sobre arte y creatividad.",
                avatar="🎨"
            ),
            Sage(
                name="Marie Curie",
                title="La Pionera de la Ciencia",
                specialty="Ciencia",
                level=4,
                description="Primera mujer en ganar un Premio Nobel. Te desafiará con conocimientos científicos.",
                avatar="🔬"
            ),
            Sage(
                name="Confucio",
                title="El Maestro de la Sabiduría",
                specialty="Cultura General",
                level=5,
                description="Filósofo y pensador oriental. Te pondrá a prueba con conocimientos de cultura general.",
                avatar="🏮"
            ),
            Sage(
                name="El Gran Consejo",
                title="Los Maestros Supremos",
                specialty="Todas",
                level=6,
                description="El desafío final. Los mejores sabios se reúnen para la prueba definitiva de tu conocimiento.",
                avatar="🏛️"
            ),
        ]
    
    def get_sage_by_level(self, level: int) -> Optional[Sage]:
        """Get sage for a specific level."""
        for sage in self.sages:
            if sage.level == level:
                return sage
        return None


class PowerUpSystem:
    """Manages power-ups and their effects."""
    
    def __init__(self):
        self.power_ups = {
            "vision_futuro": PowerUp(
                name="Visión del Futuro",
                description="Revela una pista para la pregunta actual",
                cost=10,
                icon="🔮"
            ),
            "eco_pasado": PowerUp(
                name="Eco del Pasado",
                description="Te permite repetir una pregunta fallada anteriormente",
                cost=15,
                icon="⏮️"
            ),
            "escudo_sabio": PowerUp(
                name="Escudo del Sabio",
                description="Protege tu racha si fallas una pregunta",
                cost=20,
                icon="🛡️"
            ),
            "duplicador": PowerUp(
                name="Duplicador de Fragmentos",
                description="Duplica los fragmentos ganados en la siguiente pregunta correcta",
                cost=25,
                icon="✨"
            ),
        }
    
    def get_power_up(self, power_up_id: str) -> Optional[PowerUp]:
        """Get a specific power-up."""
        return self.power_ups.get(power_up_id)
    
    def get_all_power_ups(self) -> List[PowerUp]:
        """Get all available power-ups."""
        return list(self.power_ups.values())
    
    def get_power_up_id(self, power_up: PowerUp) -> Optional[str]:
        """Get the ID of a power-up."""
        for power_up_id, pu in self.power_ups.items():
            if pu == power_up:
                return power_up_id
        return None


class GameSession:
    """Manages a single game session."""
    
    def __init__(self, player: PlayerProfile, level: int):
        self.player = player
        self.level = level
        self.current_question_index = 0
        self.questions: List[Question] = []
        self.score = 0
        self.streak = 0
        self.active_power_ups: Dict[str, bool] = {}
        self.completed = False
        self.sage: Optional[Sage] = None
    
    def start_level(self, questions: List[Question], sage: Sage):
        """Start a new level with questions."""
        self.questions = questions
        self.sage = sage
        self.current_question_index = 0
        self.score = 0
        self.streak = 0
        self.completed = False
    
    def get_current_question(self) -> Optional[Question]:
        """Get the current question."""
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None
    
    def answer_question(self, answer_index: int, use_duplicator: bool = False) -> Dict:
        """Process an answer and return results."""
        question = self.get_current_question()
        if not question:
            return {"error": "No hay pregunta actual"}
        
        is_correct = answer_index == question.correct_answer
        fragments_earned = 0
        
        if is_correct:
            # Calculate fragments based on difficulty and streak
            base_fragments = question.difficulty * 5
            streak_bonus = self.streak * 2
            fragments_earned = base_fragments + streak_bonus
            
            # Apply duplicator if active
            if use_duplicator:
                fragments_earned *= 2
                self.active_power_ups["duplicador"] = False
            
            self.score += fragments_earned
            self.streak += 1
            self.player.questions_correct += 1
        else:
            # Reset streak unless shield is active
            if not self.active_power_ups.get("escudo_sabio", False):
                self.streak = 0
            else:
                self.active_power_ups["escudo_sabio"] = False
            
            # Add to failed questions for "eco del pasado"
            self.player.failed_questions.append(question)
            if len(self.player.failed_questions) > 10:
                self.player.failed_questions.pop(0)
        
        self.player.questions_answered += 1
        self.current_question_index += 1
        
        # Check if level is completed
        if self.current_question_index >= len(self.questions):
            self.completed = True
            self.player.wisdom_fragments += self.score
            # Level is completed regardless of last answer, mark as complete
            if self.level not in self.player.completed_levels:
                self.player.completed_levels.append(self.level)
                self.player.current_level = max(self.player.current_level, self.level + 1)
            self.player.update_rank()
        
        return {
            "correct": is_correct,
            "fragments_earned": fragments_earned,
            "streak": self.streak,
            "completed": self.completed,
            "total_score": self.score,
        }
    
    def use_power_up(self, power_up_id: str) -> bool:
        """Activate a power-up if player has it."""
        if power_up_id in self.player.power_ups_owned:
            if self.player.power_ups_owned[power_up_id] > 0:
                self.player.power_ups_owned[power_up_id] -= 1
                self.active_power_ups[power_up_id] = True
                return True
        return False
    
    def get_hint(self) -> Optional[str]:
        """Get hint for current question if vision del futuro is active."""
        if self.active_power_ups.get("vision_futuro", False):
            question = self.get_current_question()
            if question:
                self.active_power_ups["vision_futuro"] = False
                return question.hint
        return None


def get_rank_thresholds() -> List[tuple]:
    """Get centralized rank thresholds.
    
    Returns:
        List of tuples (rank_name, min_fragments, max_fragments)
    """
    return [
        ("Aprendiz", 0, 30),
        ("Estudiante", 30, 75),
        ("Erudito", 75, 150),
        ("Sabio", 150, 300),
        ("Gran Sabio", 300, 500),
        ("Maestro Supremo", 500, 10000),
    ]


def get_share_text(player: PlayerProfile) -> str:
    """Generate text for social media sharing."""
    return f"""🧠 Mente Maestra: El Torneo de los Sabios 🧠

{player.avatar_emoji} {player.name}
🏆 Rango: {player.rank}
⭐ Fragmentos de Sabiduría: {player.wisdom_fragments}
🎯 Precisión: {player.get_accuracy():.1f}%
📊 Nivel Actual: {player.current_level}

¡Únete al torneo y demuestra tu sabiduría!
#MenteMaestra #TorneoDeLosSabios"""


def get_rank_emoji(rank: str) -> str:
    """Get emoji for player rank."""
    rank_emojis = {
        "Aprendiz": "🎓",
        "Estudiante": "📚",
        "Erudito": "🎭",
        "Sabio": "🧙",
        "Gran Sabio": "🧙‍♂️",
        "Maestro Supremo": "👑",
    }
    return rank_emojis.get(rank, "🎓")
