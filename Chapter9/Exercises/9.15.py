from lottery_v2 import Lottery

count = 0
flag = True
lottery_ticket = Lottery()
winning_combo = lottery_ticket.show_winning_combo()
userroll = lottery_ticket.you_rolled()

while flag:
    for i in range(len(userroll)):
        if userroll[i] != winning_combo[i]:
            count += 1
            userroll = lottery_ticket.you_rolled()
            continue
    flag = False
    
print(f"Count : {count}")
        