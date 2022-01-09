class StatSummary:
    def __init__(self, prof, ac, hp_min, hp_max, attack_bonus, dpr_min, dpr_max, save_dc):
        self.proficiency_bonus = prof
        self.armor_class = ac
        self.hit_points = range(hp_min, hp_max)
        self.attack_bonus = attack_bonus
        self.dpr = range(dpr_min, dpr_max)
        self.save_dc = save_dc