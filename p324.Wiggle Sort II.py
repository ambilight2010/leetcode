class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.wiggleSort_sort(nums)


    def wiggleSort_sort(self, nums):
        """
        O(nlogn)

        0 1 2 3 4 5 6 7
        S S S M M L L L

        =>

        3   2   1   0
          7   6   5   4
        M   S   S   S
          L   L   L   M

        =>

        3 7 2 6 1 5 0 4
        M L S L S L S M
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def wiggleSort_On(self, nums):
        """
        O(n)

        Virtual Indexing:
            (n = 10)
            Accessing A(0) actually accesses nums[1].
            Accessing A(1) actually accesses nums[3].
            Accessing A(2) actually accesses nums[5].
            Accessing A(3) actually accesses nums[7].
            Accessing A(4) actually accesses nums[9].
            Accessing A(5) actually accesses nums[0].
            Accessing A(6) actually accesses nums[2].
            Accessing A(7) actually accesses nums[4].
            Accessing A(8) actually accesses nums[6].
            Accessing A(9) actually accesses nums[8].

        Three-way Partitioning:
            output => [L ... L] [M ... M] [S ... S]

        =>

        A: 0 1 2 3 4 5 6 7 8 9
           L L L L M M M S S S
        N: 1 3 5 7 9 0 2 4 6 8

        =>

        N: 0 1 2 3 4 5 6 7 8 9
           M L M L S L S L S M
        A: 5 0 6 1 7 2 8 3 9 4
        """
        def A(i):
            return (1+2*i) % (n|1)

        def nth_element(nth):
            def partion(l, r, a):
                mid = a[l]
                i, j = l, r
                while i < j:
                    while i < j and a[i] <= mid: i += 1
                    while i < j and a[j] > mid: j -= 1
                    if i < j: a[i], a[j] = a[j], a[i]
                a[l], a[i] = a[i], a[l]
                return i

            def helper(l, r, k, a):
                if l >= r: return
                middle = partion(l, r, a)
                if middle - l == k: return
                elif middle - l > k: helper(l, middle - 1, k, a)
                else: helper(middle + 1, r, k - (middle - l + 1), a)

            helper(0, n - 1, nth, nums)

        n = len(nums)
        nth_element(n // 2)
        mid = nums[n // 2]
        i, j, k = 0, 0, n-1
        while j <= k:
            if nums[A(j)] > mid:
                nums[A(i)], nums[A(j)] = nums[A(j)], nums[A(i)]
                i += 1
                j += 1
            elif nums[A(j)] < mid:
                nums[A(j)], nums[A(k)] = nums[A(k)], nums[A(j)]
                k -= 1
            else:
                j += 1
