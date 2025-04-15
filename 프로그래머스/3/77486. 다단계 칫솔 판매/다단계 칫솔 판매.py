def solution(enroll, referral, seller, amount):

    money = { x : 0 for x in ["-"]+enroll}
    member = {enr : ref for enr, ref in zip(enroll,referral)}

    for name,cash in zip(seller,amount):
        cash*=100
        money[name] += cash
        while name != "-" and cash > 0:
            money[name] -= cash//10
            name = member[name]
            money[name] += cash//10
            cash//=10

    return [money[x] for x in enroll]