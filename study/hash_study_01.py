participants = ["marina", "josipa", "nikola", "vinko", "filipa"]
completions = ["josipa", "filipa", "marina", "nikola"]
#return =  "vinko"
def solution(participant, completion):
    par = sorted(participant)
    com = sorted(completion)
    for i in range(len(completion)):
        if par[i] != com[i]:
            return par[i]
    return par[len(par)-1]

result = solution(participants,completions)
print(result)