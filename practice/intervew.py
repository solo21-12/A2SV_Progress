def matching(players, trainers):
    players.sort()
    trainers.sort()

    player, trainer = 0, 0
    maxMatching = 0

    while player < len(players) and trainer < len(trainers):
        if players[player] <= trainers[trainer]:
            player += 1
            maxMatching += 1

        trainer += 1

    return maxMatching


print(matching([1, 1, 1], [10]))


def solution(nums):

    if len(nums) <= 4:
        return 0

    nums.sort()

    return min(

        (nums[-1] - nums[3]),
        (nums[-2] - nums[2]),
        (nums[-3] - nums[1]),
        (nums[-4] - nums[0])
    )


print(solution([5,3,2,4]))