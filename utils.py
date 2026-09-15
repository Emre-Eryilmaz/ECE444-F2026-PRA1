class utils:
    @staticmethod
    def reversed(number: int) -> int:
        """Takes an integer and returns the digits reversed as an integer."""
        sign = -1 if number < 0 else 1
        return sign * int(str(abs(number))[::-1])

    @staticmethod
    def formatter(number: int) -> tuple[str, str]:
        """Takes an integer and returns its binary (base 2) and octal (base 8) formats."""
        return bin(number), oct(number)
