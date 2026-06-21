class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for i in range(len(emails)):
            local, domain = emails[i].split("@")
            clean_local = local.split("+")[0].replace(".","")

            res.add((clean_local, domain))
        return len(res)