from classes import StatSummary

# TODO Add stat summaries for CR 5+
CR_TO_STAT_SUMM_LOOKUP = {
    0: StatSummary(2, 13, 1, 6, 3, 0, 1, 13),
    0.125: StatSummary(2, 13, 7, 35, 3, 2, 3, 13),
    0.25: StatSummary(2, 13, 36, 49, 3, 6, 8, 13),
    1: StatSummary(2, 13, 71, 85, 3, 9, 14, 13),
    2: StatSummary(2, 13, 86, 100, 3, 15, 20, 13),
    3: StatSummary(2, 13, 101, 115, 4, 21, 26, 13),
    4: StatSummary(2, 14, 116, 130, 5, 27, 32, 14)
}