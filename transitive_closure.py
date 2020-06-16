def transitive_closure(n, g):

    def dfs(s, v):
        tc[s][v]=1
        for nei in g[v]:
            if tc[s][nei]==0:
                dfs(s, nei)

    tc = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dfs(i,i)
    return tc


g = {
    0: [1,2],
    1: [2],
    2: [0,3],
    3: []
}

print(transitive_closure(4, g))