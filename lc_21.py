def maximumOddBinaryNumber(s: str) -> str:
    ones_count = s.count("1")
    zeros_count = len(s) - ones_count

    return "1" * (ones_count - 1) + "0" * zeros_count + "1"
s = "0101"
print(maximumOddBinaryNumber(s))
