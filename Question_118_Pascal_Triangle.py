class Solution:
    def generate(numRows):
        res = []
        for i in range(numRows):
            res.append([1]*(i+1))
        
        for line in range(2, numRows):
            inner_length = line - 1
            count = 1
            while count <= inner_length:
                res[line][count] = res[line-1][count-1] + res[line-1][count]
                count += 1
        return res

def main():
    print(Solution.generate(6))

main()