# =========================================================
# Poprawiono nazewnictwo zmiennych
# =========================================================
class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, p_name):
        if p_name == self.p1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        if (self.p1_points < 4 and self.p2_points < 4) and (self.p1_points + self.p2_points < 6):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            score = points[self.p1_points]
            return score + "-All" if (self.p1_points == self.p2_points) else score + "-" + points[self.p2_points]
        else:
            if self.p1_points == self.p2_points:
                return "Deuce"
            score = self.p1_name if self.p1_points > self.p2_points else self.p2_name
            return (
                "Advantage " + score
                if ((self.p1_points - self.p2_points) * (self.p1_points - self.p2_points) == 1)
                else "Win for " + score
            )
