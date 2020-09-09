def dfs(s, res, open_, close):
    if open_ == 0 and close == 0:
        res.append(s)
    if open_ > 0:
        dfs(s+"(", res, open_-1, close)
    if open_ < close:
        dfs(s+")", res, open_, close-1)
    return
n=3
res = []
dfs("", res, n, n)
print(res)