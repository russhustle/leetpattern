class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.cur += 1
        del self.hist[self.cur :]
        self.hist.append(url)

    def back(self, steps: int) -> str:
        self.cur = max(self.cur - steps, 0)
        return self.hist[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, len(self.hist) - 1)
        return self.hist[self.cur]


if __name__ == "__main__":
    obj = BrowserHistory("leetcode.com")
    obj.visit("google.com")
    obj.visit("facebook.com")
    obj.visit("youtube.com")
    assert obj.back(1) == "facebook.com"
    assert obj.back(1) == "google.com"
    assert obj.forward(1) == "facebook.com"
    obj.visit("linkedin.com")
    assert obj.forward(2) == "linkedin.com"
    assert obj.back(2) == "google.com"
    assert obj.back(7) == "leetcode.com"
