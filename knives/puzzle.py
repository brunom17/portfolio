from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # If A is a knight, the statement must be true
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave, the statement must be false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statement_A = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, statement_A),
    Implication(AKnave, Not(statement_A))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_different = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, A_same),
    Implication(AKnave, Not(A_same)),
    Implication(BKnight, B_different),
    Implication(BKnave, Not(B_different))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# A could have said "I am a knight" or "I am a knave"
A_said_knight = Biconditional(AKnight, AKnight) 
A_said_knave = Biconditional(AKnight, AKnave)
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # One of these two was actually said by A
    Or(A_said_knight, A_said_knave),

    # B says: A said "I am a knave" => A_said_knave is what B claims
    Implication(BKnight, A_said_knave),
    Implication(BKnave, Not(A_said_knave)),

    # B also says: "C is a knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
