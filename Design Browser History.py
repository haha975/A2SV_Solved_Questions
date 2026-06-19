class BrowserHistory:

    def __init__(self, homepage: str):
        self.app=[]
        self.homepage=homepage
        self.app.append(homepage)
        self.pos=0
        

    def visit(self, url: str) -> None:
        self.app=self.app[:self.pos+1]
        self.homepage=url
        self.app.append(url)
        self.pos+=1
        

    def back(self, steps: int) -> str:
        lenn=self.pos
        if lenn==0 or lenn-steps<0:
            self.pos=0
            self.homepage = self.app[0]
            return self.homepage
        else:
            self.pos=lenn-steps
            self.homepage=self.app[self.pos]
            return self.homepage
        

    def forward(self, steps: int) -> str:
        leng=self.pos
        if leng==len(self.app)-1 or leng+steps>len(self.app)-1:
            self.pos=len(self.app)-1
            self.homepage = self.app[-1]
            return self.homepage
        else:
            self.pos=leng+steps
            self.homepage=self.app[self.pos]
            return self.homepage
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
