class ClassStatSummary:
    def __init__(self, prof, ac, hp_min, hp_max, attack_bonus, dpr_min, dpr_max, save_dc):
        self.proficiency_bonus = prof
        self.armor_class = ac
        self.hit_points = range(hp_min, hp_max)
        self.attack_bonus = attack_bonus
        self.dpr = range(dpr_min, dpr_max)
        self.save_dc = save_dc

class IndividualStatSummary:
    def __init__(self, prof, ac, hp, attack_bonus, dpr, save_dc):
        self.proficiency_bonus = prof
        self.armor_class = ac
        self.hit_points = hp
        self.attack_bonus = attack_bonus
        self.dpr = dpr
        self.save_dc = save_dc
    
    # TODO check if monster is member of CR by adjustment (due to abnormal AC or Attack Bonus / Save DC)
    
    def is_defensive_member_of(self, class_stat_summary):
        return self.hit_points in class_stat_summary.hit_points and abs(self.armor_class - class_stat_summary.armor_class) < 2:


    def is_offensive_member_of(self, class_stat_summary):
        # TODO check if monster relies more on attack bonus or save DC
        return self.dpr in class_stat_summary.dpr and abs(self.attack_bonus - class_stat_summary.attack_bonus) < 2:

