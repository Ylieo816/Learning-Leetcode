# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

class UnionFind:
    def __init__(self, l):
        self.lst = list(range(l))

    def find(self, id):
        # find the root of value for id
        if id != self.lst[id]:
            self.lst[id] = self.find(self.lst[id])
        return self.lst[id]

    def union(self, child, parent):
        # current value will save the root value
        self.lst[self.find(child)] = self.find(parent)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uionFind = UnionFind(len(accounts))

        own = {}
        for i, (name, *emails) in enumerate(accounts):
            # *email is used to save the rest of variable
            # e.g. [a, *b, c] = [1,2,3,4,5], b will be 2, 3, 4
            for email in emails:
                if email in own:
                    uionFind.union(i, own[email])
                own[email] = i

        answer = collections.defaultdict(list)
        for email, owner in own.items():
            # list and append email to correspond index
            answer[uionFind.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in answer.items()]