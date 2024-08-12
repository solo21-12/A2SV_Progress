class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        game = deque(list(senate))
        count = Counter(senate)

        while len(game) > 1:

            cur = game.popleft()
            game.append(cur)

            if count[cur] == len(game):
                break

            if cur == "R":
                game.remove("D")
                count["D"] -= 1
            else:
                game.remove("R")
                count["R"] -= 1

        return "Radiant" if game[0] == "R" else "Dire"
