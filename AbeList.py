class AbeList(list):
    def sort(self):
        maxv = 0
        if not self:
            return
        maxv = self[0]
        for i, val in enumerate(self[:]):
            if val < maxv:
                self[i] = maxv + 1
            else:
                maxv = val
                continue
if __name__ == "__main__":
    tl = AbeList([5,1,6,4])
    breakpoint()
    tl.sort()
    breakpoint()