import functools
import numpy as np
from datascience import *

most_common = lambda a: a[np.argmax([np.count_nonzero(np.equal(i, a)) for i in a])]

def payoff(p1, p2):
    p1_defect = p1.play(p2, True)
    p2_defect = p2.play(p1, False)
    
    if p1_defect and p2_defect:
        return 4, 4
    elif p1_defect and not p2_defect:
        return 0, 5
    elif not p1_defect and p2_defect:
        return 5, 0
    else:
        return 2, 2
    
def run_match(p1, p2, n=5, winner=True):
    p1.reset_history()
    p2.reset_history()
    
    p1_years = []
    p2_years = []
    
    for i in range(n):
        p1_score, p2_score = payoff(p1, p2)
        p1_years.append(p1_score)
        p2_years.append(p2_score)
        
    if winner:
        p1_mean = np.mean(p1_years)
        p2_mean = np.mean(p2_years)

        if p1_mean < p2_mean:
            return p1
        else:
            return p2
    else:
        return p1_years, p2_years
    
def determine_winner(p1, p1_mean, p2, p2_mean):
    if p1_mean < p2_mean:
        return p1
    else:
        return p2
    
def flatten_results(tbl):
    t = Table()
    t = t.with_column("player", np.append(tbl.column("p1"), tbl.column("p2")))
    t = t.with_column("score", np.append(tbl.column("p1_mean"), tbl.column("p2_mean")))
    df = t.to_df()
    df["player"] = df["player"].apply(repr)
    return df

def create_player_class(player_name, play_method):
    @functools.total_ordering
    class Player:
        def __init__(self, p=0.5):
            self.history = make_array()
            self.prob = p
            self.name = player_name
        
        def play(self, opponent, is_p1):
            """Returns True if player defects, False otherwise"""
            defect = play_method(self, opponent, is_p1)
            self.history = np.append(self.history, defect)
            return defect
        
        def reset_history(self):
            self.history = make_array()
        
        def __repr__(self):
            if player_name == "Random":
                return player_name + "({})".format(self.prob)
            return player_name
        
        def __hash__(self):
            return hash(self.name)
        
        def __eq__(self, other):
            return self.name == other.name
        
        def __lt__(self, other):
            return self.name < other.name
    
    return Player

def defector_play(self, opponent, is_p1):
    return True

Defector = create_player_class("Defector", defector_play)

def cooperator_play(self, opponent, is_p1):
    return False

Cooperator = create_player_class("Cooperator", cooperator_play)

def random_play(self, opponent, is_p1):
    return np.random.random() < self.prob

Random = create_player_class("Random", random_play)

def alternator_play(self, opponent, is_p1):
    if len(self.history) > 0:
        return not self.history.item(-1)
    else:
        return False
    
Alternator = create_player_class("Alternator", alternator_play)

def tit_for_tat_play(self, opponent, is_p1):
    if is_p1:
        if len(opponent.history) > 0 and opponent.history.item(-1):
            return True
        else:
            return False
    else:
        if len(opponent.history) > 1 and opponent.history.item(-2):
            return True
        else:
            return False
    
TitForTat = create_player_class("TitForTat", tit_for_tat_play)

def backstabber_play(self, opponent, is_p1):
    if is_p1:
        return np.sum(opponent.history) > 3
    return np.sum(opponent.history[:-1]) > 3

Backstabber = create_player_class("Backstabber", backstabber_play)

def bully_play(self, opponent, is_p1):
    if len(self.history) == 0:
        return True
    if is_p1:
        return not opponent.history[-1]
    return not opponent.history[-2]

Bully = create_player_class("Bully", bully_play)

def desperate_play(self, opponent, is_p1):
    if is_p1:
        return np.sum(np.logical_and(self.history, opponent.history)) > 0
    return np.sum(np.logical_and(self.history, opponent.history[:-1])) > 0

Desperate = create_player_class("Desperate", desperate_play)

def fool_me_once_play(self, opponent, is_p1):
    if is_p1:
        return np.sum(opponent.history) > 1
    return np.sum(opponent.history[:-1]) > 1

FoolMeOnce = create_player_class("FoolMeOnce", fool_me_once_play)

def forgiver_play(self, opponent, is_p1):
    if len(self.history) == 0:
        return False
    if is_p1:
        return np.sum(opponent.history) / len(opponent.history) > 0.1
    return np.sum(opponent.history[:-1]) / len(opponent.history[:-1]) > 0.1

Forgiver = create_player_class("Forgiver", forgiver_play)

def once_bitten_play(self, opponent, is_p1):
    if not hasattr(self, "defects_left"):
        self.defects_left = 0
    if self.defects_left > 0:
        self.defects_left -= 1
        return True
    if is_p1:
        if len(opponent.history) >= 2:
            if opponent.history[-1] and opponent.history[-2]:
                self.defects_left = 9
                return True
    else:
        if len(opponent.history) >= 3:
            if opponent.history[-2] and opponent.history[-3]:
                self.defects_left = 9
                return True
    return False

OnceBitten = create_player_class("OnceBitten", once_bitten_play)

def worse_and_worse_play(self, opponent, is_p1):
    return np.random.rand() <= len(self.history) / 1000

WorseAndWorse = create_player_class("WorseAndWorse", worse_and_worse_play)






























