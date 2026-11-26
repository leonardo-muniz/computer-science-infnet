def teams(candidates, k):

    if k == 0: return [""]

    if len(candidates) < k: return []

    primeiro = candidates[0]

    com_primeiro = [
        primeiro + " " + t if t else primeiro
        for t in teams(candidates[1:], k - 1)
    ]

    sem_primeiro = teams(candidates[1:], k)

    return com_primeiro + sem_primeiro