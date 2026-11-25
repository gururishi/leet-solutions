class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for i in range (len(words)):
            if words[i].startswith('$') and words[i][1:].isdigit():
                price = int(words[i][1:])
                new_price = price*(100-discount)/100
                words[i] = f"${new_price:.2f}"
        return " " .join(words)