class Solution:
    def stoneGameIX(self, stones):
        count = [0, 0, 0]

        for x in stones:
            count[x % 3] += 1

        def check(count):
            # Alice starts by taking a remainder-1 stone
            if count[1] == 0:
                return False

            count[1] -= 1

            # Number of moves we can make in the pattern
            moves = 1 + min(count[1], count[2]) * 2 + count[0]

            # If there are extra remainder-1 stones,
            # one more move can be made
            if count[1] > count[2]:
                count[1] -= 1
                moves += 1

            return moves % 2 == 1 and count[1] != count[2]

        # Try Alice starting with remainder 1
        option1 = check(count.copy())

        # Try Alice starting with remainder 2
        swapped = [count[0], count[2], count[1]]
        option2 = check(swapped)

        return option1 or option2