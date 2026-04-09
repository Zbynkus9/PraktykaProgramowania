# =========================================================
# Rozdzielono działanie fukcji score na oddzielne funkcje i zapowniono wcześniejsze zwracanie wyniku bez sprawdzania kolejnych warunków
# Naprawiono przypisywanie nazwy gracza
# Poprawiono nazewnictwo zmiennych
# =========================================================
class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def get_tie_score(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")
        return result

    def get_advantage_or_win_score(self):
        result = ""
        p1score_advantage = self.p1points - self.p2points
        if p1score_advantage == 1:
            result = "Advantage " + self.player1_name

        elif p1score_advantage == -1:
            result = "Advantage " + self.player2_name

        elif p1score_advantage >= 2:
            result = "Win for " + self.player1_name

        else:
            result = "Win for " + self.player2_name

        return result

    def get_normal_score(self):
        result = ""
        temp_score = 0

        for i in range(1, 3):
            if i == 1:
                temp_score = self.p1points

            else:
                result += "-"
                temp_score = self.p2points

            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[temp_score]

        return result

    def score(self):

        if self.p1points == self.p2points:
            return self.get_tie_score()

        elif self.p1points >= 4 or self.p2points >= 4:
            return self.get_advantage_or_win_score()

        else:
            return self.get_normal_score()
