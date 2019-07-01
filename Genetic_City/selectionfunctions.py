import numpy as np

def match(participant_1, participant_2, participant_3, participant_4):
    match_array = [participant_1, participant_2, participant_3, participant_4]
    return np.argmax(match_array)
