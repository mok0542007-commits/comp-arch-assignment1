def ror_step(bits):
    """One ROR step: LSB moves to the MSB position, the rest shift right."""
    lsb = bits[-1]
    return lsb + bits[:-1], lsb


def rcr_step(bits, cf):
    """One RCR step: old CF enters the MSB, the LSB becomes the new CF."""
    lsb = bits[-1]
    return cf + bits[:-1], lsb


def ror(bits, n):
    print("=== ROR (Rotate Right without Carry) ===")
    print(f"Original : {bits}")
    result = bits
    for i in range(1, n + 1):
        result, out = ror_step(result)
        print(f"Step {i}   : LSB out = {out}  ->  {result}")

    # Manual method: last n bits move to the front
    manual = bits[-n:] + bits[:-n]
    print(f"Result   : {result}")
    print(f"Manual   : {manual}")
    print("Status   :", "VERIFIED" if result == manual else "MISMATCH")
    print()


def rcr(bits, n, cf):
    print("=== RCR (Rotate Right through Carry) ===")
    print(f"Original : {bits}   CF = {cf} (initial)")
    result = bits
    for i in range(1, n + 1):
        old_cf = cf
        result, cf = rcr_step(result, cf)
        print(f"Step {i}   : LSB out = {cf}, old CF = {old_cf}  ->  {result}   CF = {cf}")

    # Manual method: treat CF + 8 bits as a 9-bit ring, rotate right by n
    ring = cf_initial = None
    ring = None
    ring = None
    return result, cf


def rcr_with_check(bits, n, cf_start):
    print("=== RCR (Rotate Right through Carry) ===")
    print(f"Original : {bits}   CF = {cf_start} (initial)")
    result, cf = bits, cf_start
    for i in range(1, n + 1):
        old_cf = cf
        result, cf = rcr_step(result, cf)
        print(f"Step {i}   : LSB out = {cf}, old CF = {old_cf}  ->  {result}   CF = {cf}")

    # Manual method: 9-bit ring (CF + byte), rotate right by n
    ring = cf_start + bits
    ring = ring[-n:] + ring[:-n]
    manual_cf, manual_byte = ring[0], ring[1:]

    print(f"Result   : {result}   final CF = {cf}")
    print(f"Manual   : {manual_byte}   final CF = {manual_cf}")
    print("Status   :", "VERIFIED" if (result, cf) == (manual_byte, manual_cf) else "MISMATCH")
    print()


number = "11010101"

# a) ROR by 3
ror(number, 3)

# b) RCR by 3 (initial CF not given, so CF = 0 is assumed; CF = 1 shown for comparison)
rcr_with_check(number, 3, "0")
rcr_with_check(number, 3, "1")