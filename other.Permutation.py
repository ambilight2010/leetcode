class Example(object):
    def permutation(self, s):
        # 全排列
        def recursive(a, i, result):
            if i == len(a):
                result.append(''.join(a))
                return
            for j in range(i, len(a)):
                a[i], a[j] = a[j], a[i]
                recursive(a, i + 1, result)
                a[i], a[j] = a[j], a[i]

        result = []
        recursive(list(s), 0, result)
        return result

    def permutation_unduplicated(self, s):
        # 去重的全排列
        def recursive(a, i, result):
            if i == len(a):
                result.append(''.join(a))
                return
            for j in range(i, len(a)):
                # 第 1 个非重复出现的字符才进行
                invalid_flag = False
                for k in range(i, j):
                    if a[j] == a[k]:
                        invalid_flag = True
                if invalid_flag:
                    continue
                a[i], a[j] = a[j], a[i]
                recursive(a, i + 1, result)
                a[i], a[j] = a[j], a[i]

        result = []
        recursive(list(s), 0, result)
        return result

    def lexicographical_permutation(self, s):
        # 字典序法, https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        s = list(s)
        i, j = len(s) - 1, len(s) - 1
        while s[i-1] >= s[i] and i > 0: i -= 1
        if i == 0: return None
        while s[i-1] >= s[j] and j > i: j -= 1
        s[i-1], s[j] = s[j], s[i-1]
        s[i:] = s[: i-1: -1]
        return ''.join(s)

    def permutation_unrecursive(self, s):
        # 非递归的（去重）全排列
        result = []
        s = ''.join(sorted(list(s)))
        while s:
            result.append(s)
            s = self.lexicographical_permutation(s)
        return result

    def combination(self, s):
        # 组合
        def recursive(a, i, n, tmp, result):
            if n == 0:
                result.append(''.join(tmp))
                return
            if i == len(a): return
            tmp.append(a[i])
            recursive(a, i + 1, n - 1, tmp, result)
            tmp.pop(-1)
            recursive(a, i + 1, n, tmp, result)

        result = []
        for n in range(1, len(s) + 1):
            recursive(list(s), 0, n, [], result)
        return result

    def combination_bitmap(self, s):
        return [''.join([s[i] for i in range(len(s)) if bits & (1 << i)]) for bits in range(1, 1 << len(s))]

    def n_queen_recursive(self, n):
        # N 皇后递归
        def recursive(i):
            nonlocal c, count
            if i == n:
                count += 1
                return
            for j in range(n):
                valid = True
                for k in range(i):
                    if c[k] == j or i - k == abs(j - c[k]):
                        valid = False
                        break
                if valid:
                    c[i] = j
                    recursive(i + 1)

        c = [-1 for i in range(n)]
        count = 0
        recursive(0)
        return count

    def n_queen_nonrecursive(self, n):
        c = [-1 for i in range(n)]
        count = 0
        i, j = 0, 0
        while i < n:
            while j < n:
                valid = True
                for k in range(i):
                    if c[k] == j or i - k == abs(j - c[k]):
                        valid = False
                        break
                if valid:
                    c[i] = j
                    j = 0
                    break
                else:
                    j += 1
            if c[i] == -1:
                if i == 0:
                    break
                else:
                    i -= 1
                    j = c[i] + 1
                    c[i] = -1
                    continue
            if i == n - 1:
                j = c[i] + 1
                c[i] = -1
                count += 1
            else:
                i += 1
        return count

    def pick_num(self, m, n):
        # 从 1...n 中任取数使得和为 m，输出所有可能
        def recursive(a, tmp, i, result, cur_sum):
            if i == len(a):
                if sum(tmp) == m:
                    result.append(tmp[:])
                return
            if a[i] + cur_sum > m:
                return
            tmp.append(a[i])
            recursive(a, tmp, i + 1, result, cur_sum + a[i])
            tmp.pop(-1)
            recursive(a, tmp, i + 1, result, cur_sum)

        result = []
        recursive(list(range(n+1)), [], 0, result, 0)
        return result


print(Example().permutation('123'))
print(Example().permutation('122'))
print(Example().permutation_unduplicated('123'))
print(Example().permutation_unduplicated('122'))
print(Example().permutation_unduplicated('221'))
print(Example().lexicographical_permutation('123'))
print(Example().lexicographical_permutation('122'))
print(Example().lexicographical_permutation('321'))
print(Example().permutation_unrecursive('123'))
print(Example().permutation_unrecursive('122'))
print(Example().permutation_unrecursive('221'))
print(Example().combination('123'))
print(Example().combination_bitmap('123'))
print(Example().n_queen_recursive(8))
print(Example().n_queen_nonrecursive(8))
print(Example().pick_num(10, 5))
