def show_messages(messages,sent_messages):
    
    while len(messages) != 0:
        msg =  messages.pop()
        print(f"Showing message : {msg}")
        sent_messages.append(msg)

messages = ["msg1", "msg2", "msg3", "msg4", "msg5"]
sent_messages = []
show_messages(messages=messages, sent_messages=sent_messages)

print("original messages : " ,messages)
print("Sent messages : ", sent_messages)