class Solution:
    def maxProfit(self, prices):
        min_price = 10000000000
        max_earn = 0
        for elem in prices:
            max_earn = max(elem - min_price, max_earn)
            min_price = min(elem, min_price)
        return max_earn


def main():
    test = [7,6,4,3,1]
    print(Solution.maxProfit(test))

main()