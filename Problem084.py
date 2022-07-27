
from random import randint, shuffle
from time import perf_counter


def round(n: float, dp: int):
    return n // (10 ** -dp) / (10 ** dp)


start = perf_counter()

codes = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
code_index_dict = {value: key for key, value in enumerate(codes)}
curr_probs = [0 for i in range(len(codes))]
prev_probs = [0 for i in range(len(codes))]
ch_cards = ["GO", "JAIL", "C1", "E3", "H2", "R1", "NR", "NR", "NU", "GB3", None, None, None, None, None, None] 
cc_cards = ["GO", "JAIL", None, None, None, None, None, None, None, None, None, None, None, None, None, None]
shuffle(ch_cards)
shuffle(cc_cards)
breaking = False
dp = 6
curr_index = 0
step_count = 1
curr_double = False
prev_double = False
prev_prev_double = False
count = 0
num_of_dice_sides = 4
while not breaking:
    # Roll
    roll1 = randint(1, num_of_dice_sides)
    roll2 = randint(1, num_of_dice_sides)
    curr_index += roll1 + roll2
    curr_index %= len(codes)
    
    # Events
    # Double roll rule
    if roll1 == roll2:
        curr_double = True
    else:
        curr_double = False
    if curr_double and prev_double and prev_prev_double:
        curr_index = code_index_dict["JAIL"]

    # G2J
    elif codes[curr_index] == "G2J":
        curr_index = code_index_dict["JAIL"]

    # CH
    elif codes[curr_index][:2] == "CH":
        ch_code = ch_cards[0]
        if ch_code in codes:
            curr_index = code_index_dict[ch_code]
        else:
            # Next railway
            if ch_code == "NR":
                if codes[curr_index] == "CH1":
                    curr_index = code_index_dict["R2"]
                elif codes[curr_index] == "CH2":
                    curr_index = code_index_dict["R3"]
                elif codes[curr_index] == "CH3":
                    curr_index = code_index_dict["R1"]
            # Next utility
            elif ch_code == "NU":
                if codes[curr_index] == "CH1" or codes[curr_index] == "CH3":
                    curr_index = code_index_dict["U1"]
                elif codes[curr_index] == "CH2":
                    curr_index = code_index_dict["U2"]
            # Go back three
            elif ch_code == "GB3":
                curr_index -= 3

        # Put card at bottom of deck
        ch_cards.insert(len(ch_cards), ch_code)
        ch_cards.remove(ch_code)

    # CC (This is simply an IF because on CH3 you can go back to CC3)
    if codes[curr_index][:2] == "CC":
        cc_code = cc_cards[0]
        if cc_code in codes:
            curr_index = code_index_dict[cc_code]

        # Put card at bottom of deck
        cc_cards.insert(len(cc_cards), cc_code)
        cc_cards.remove(cc_code)

    
    # Calculate new probabilities
    for index in range(0, len(codes)):
        if index == curr_index:
            curr_probs[index] = curr_probs[index] * (step_count - 1) + 1
        else:
            curr_probs[index] = curr_probs[index] * (step_count - 1)
        curr_probs[index] /= step_count


    # If the curr_probabilities are the same as the previous probabilities to 4.d.p then break
    breaking = True
    for index, prob in enumerate(curr_probs):
        if round(prev_probs[index], dp) != round(prob, dp):
            breaking = False
            break

    prev_probs = curr_probs.copy()
    step_count += 1
    prev_prev_double = prev_double
    prev_double = curr_double

    count += 1
    if count == 1000:
        shuffle(cc_cards)
        shuffle(ch_cards)
        count = 0


sorted_probs = [code for value, code in sorted(zip(curr_probs, codes), reverse=True)]
end = perf_counter()
elapsed_ms = (((perf_counter() - start)*100000)//1)/100
print(f"""
curr_probs: {prev_probs}
elapsed_time: {elapsed_ms}ms
maxes: {sorted_probs[:3]}
six-digit modal string: {"".join([f"{codes.index(code):02}" for code in sorted_probs[:3]])}""")