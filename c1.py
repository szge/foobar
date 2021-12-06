chars = [
    "100000", # A
    "110000", # B
    "100100", # C
    "100110", # D
    "100010", # E
    "110100", # F
    "110110", # G
    "110010", # H
    "010100", # I
    "010110", # J
    "101000", # K
    "111000", # L
    "101100", # M
    "101110", # N
    "101010", # O
    "111100", # P
    "111110", # Q
    "111010", # R
    "011100", # S
    "011110", # T
    "101001", # U
    "111001", # V
    "010111", # W
    "101101", # X
    "101111", # Y
    "101011", # Z
]

# only handles a-zA-Z plus "space"
def solution(s):
    output = ""
    for letter in s:
        if letter == ' ':
            output += "000000"
        else:
            if letter.isupper():
                # if character is uppercase make sure to add the capitalization character
                output += "000001"
            output += chars[ord(letter.lower()) - 96 - 1]
        # output += " "
    return output

if __name__ == "__main__":
    print(solution("Braille"))