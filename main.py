class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls = 0
        self.out = False

    def add_runs(self, r):
        self.runs += r
        self.balls += 1

    def wicket(self):
        self.out = True
        self.balls += 1


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = [Player(p) for p in players]
        self.total_runs = 0
        self.wickets = 0
        self.overs = 0
        self.balls_in_over = 0
        self.striker_index = 0
        self.non_striker_index = 1
        self.next_player_index = 2

    def rotate_strike(self):
        self.striker_index, self.non_striker_index = self.non_striker_index, self.striker_index

    def add_ball(self, outcome):
        striker = self.players[self.striker_index]

        if outcome == "W":
            striker.wicket()
            self.wickets += 1
            print(f"WICKET! {striker.name} is out.")

            if self.next_player_index < len(self.players):
                self.striker_index = self.next_player_index
                self.next_player_index += 1
            else:
                print("All players are out!")
                return "ALL_OUT"

        else:
            runs = int(outcome)
            striker.add_runs(runs)
            self.total_runs += runs

            # Rotate strike for 1,3,5 runs
            if runs % 2 == 1:
                self.rotate_strike()

        self.balls_in_over += 1

        # If over completed
        if self.balls_in_over == 6:
            self.overs += 1
            self.balls_in_over = 0
            self.rotate_strike()
            print(f"--- Over {self.overs} completed ---")

        return "OK"

    def summary(self):
        print("\n========== MATCH SUMMARY ==========")
        print(f"Team: {self.name}")
        print(f"Score: {self.total_runs}/{self.wickets} in {self.overs}.{self.balls_in_over} overs\n")

        print("Player Scorecard:")
        for p in self.players:
            status = "out" if p.out else "not out"
            print(f"{p.name}: {p.runs} ({p.balls}) - {status}")


class Match:
    def __init__(self, team_name, players):
        self.team = Team(team_name, players)

    def start(self):
        print("\n===== Cricket Scoring Started =====")
        print("Enter: 0 1 2 3 4 5 6 for runs, W for wicket, Q to quit\n")

        while True:
            ball = input("Ball outcome: ").upper()

            if ball == "Q":
                break

            if ball not in ["0","1","2","3","4","5","6","W"]:
                print("Invalid input!")
                continue

            status = self.team.add_ball(ball)

            if status == "ALL_OUT":
                break

        print("\n===== Innings Completed =====")
        self.team.summary()


# -----------------------------
# MAIN PROGRAM
# -----------------------------
players = ["Player1", "Player2", "Player3", "Player4", "Player5",
           "Player6", "Player7", "Player8", "Player9", "Player10", "Player11"]

match = Match("Team A", players)
match.start()






