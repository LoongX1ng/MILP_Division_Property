# Algorithm 2 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS


from sbox import Sbox

if __name__ == "__main__":
    # PRESENT Sbox
    cipher = "Ascon"  # "PRESENT"
    sbox = [0x4, 0xB, 0x1F, 0x14, 0x1A, 0x15, 0x9, 0x2, 0x1B, 0x5, 0x8, 0x12, 0x1D, 0x3, 0x6, 0x1C, 0x1E, 0x13, 0x7,
            0xE, 0x0, 0xD, 0x11, 0x18, 0x10, 0xC, 0x1, 0x19, 0x16, 0xA, 0xF, 0x17]  # [0xc, 0x5, 0x6, 0xb, 0x9, 0x0,
    # 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

    present = Sbox(sbox)

    filename = cipher + "_DivisionTrails.txt"

    present.PrintfDivisionTrails(filename)
