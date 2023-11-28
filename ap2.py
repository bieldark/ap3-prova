class Question:
    def __init__(self, prompt, answer, points, correct_feedback, incorrect_feedback):
        self.prompt = prompt
        self.answer = answer
        self.points = points
        self.correct_feedback = correct_feedback
        self.incorrect_feedback = incorrect_feedback


class Puzzle:
    def __init__(self, description, solution, points, correct_feedback, incorrect_feedback):
        self.description = description
        self.solution = solution
        self.points = points
        self.correct_feedback = correct_feedback
        self.incorrect_feedback = incorrect_feedback


def introduction():
    print("Bem-vindo, explorador espacial! Você embarcou em uma missão épica em busca de conhecimento nos confins do universo.")
    print("Nesta jornada, você encontrará desafios intelectuais e quebra-cabeças intrigantes para provar sua destreza e aprender mais sobre o cosmos.")
    print("Acumule pontos respondendo a perguntas e resolvendo quebra-cabeças enquanto explora as estrelas!")
    print("Vamos começar!\n")


def run_quiz(questions, puzzles):
    score = 0
    introduction()

    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer:
            print(
                f"{question.correct_feedback} Você ganhou {question.points} pontos.\n")
            score += question.points
        else:
            print(f"{question.incorrect_feedback}\n")

    print(f"Você marcou um total de {score} pontos.\n")

    for puzzle in puzzles:
        user_solution = input(puzzle.description + "\nSua resposta: ")
        if user_solution == puzzle.solution:
            print(f"{puzzle.correct_feedback} Você ganhou {puzzle.points} pontos.\n")
            score += puzzle.points
        else:
            print(f"{puzzle.incorrect_feedback}\n")

    print(f"Sua pontuação final é {score} pontos.\n")

    if score == sum([question.points for question in questions]) + sum([puzzle.points for puzzle in puzzles]):
        print("Parabéns! Você acertou todas as perguntas e quebra-cabeças. Você é um verdadeiro mestre do conhecimento!")
    else:
        print("Obrigado por explorar o universo em busca de conhecimento!")


if __name__ == "__main__":
    # Defina perguntas e quebra-cabeças
    questions = [
        Question("Qual é a capital do Brasil?\n(a) São Paulo\n(b) Rio de Janeiro\n(c) Brasília\n", "c", 10,
                 "Resposta correta! Brasília é a capital do Brasil.", "Resposta incorreta. A capital do Brasil é Brasília."),
        Question("Quantos planetas existem em nosso sistema solar?\n(a) 7\n(b) 9\n(c) 8\n", "c", 20,
                 "Correto! Existem 8 planetas em nosso sistema solar.", "Resposta errada. Nosso sistema solar possui 8 planetas."),
        Question("Qual é o símbolo químico para o oxigênio?\n(a) Ox\n(b) O\n(c) O2\n", "b", 15,
                 "Você acertou! 'O' é o símbolo químico do oxigênio.", "Errado. O símbolo químico do oxigênio é 'O'."),
        Question("Quem escreveu 'Dom Quixote'?\n(a) Miguel de Cervantes\n(b) Gabriel García Márquez\n(c) Paulo Coelho\n", "a", 25,
                 "Isso mesmo! Miguel de Cervantes é o autor de 'Dom Quixote.", "Incorreto. O autor de 'Dom Quixote' é Miguel de Cervantes."),
        Question("Qual é a fórmula química da água?\n(a) H2O2\n(b) CO2\n(c) H2O\n", "c", 15,
                 "Correto! A fórmula química da água é H2O.", "Errado. A fórmula química da água é H2O.")
    ]

    puzzles = [
        Puzzle("Resolva o quebra-cabeça: 3 * 4 = ?", "12", 10,
               "Bom trabalho! A resposta correta é 12.", "Resposta incorreta. O resultado correto é 12."),
        Puzzle("Resolva o quebra-cabeça: 7 + 8 = ?", "15", 15,
               "Ótimo! 7 + 8 é igual a 15.", "Errado. A resposta correta é 15."),
        Puzzle("Resolva o quebra-cabeça: Qual é o resultado de 2^3?\n(a) 4\n(b) 6\n(c) 8\n",
               "c", 20, "Você acertou! 2^3 é igual a 8.", "Incorreto. A resposta correta é 8."),
        Puzzle("Resolva o quebra-cabeça de lógica: Se 5 + 3 = 28, 9 + 1 = 810, então 6 + 3 = ?",
               "63", 25, "Excelente! A resposta é 63.", "Errado. A solução é 63.")
    ]

    run_quiz(questions, puzzles)
