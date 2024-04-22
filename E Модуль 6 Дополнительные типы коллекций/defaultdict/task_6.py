from collections import defaultdict as di


def best_sender(messages, senders):
    res = di(int)
    for k, v in zip(senders, messages):
        res[k] = res.get(k, 0) + len(v.split())
    return sorted(res.items(), key=lambda x: (x[1], x[0]))[-1][0]


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))
