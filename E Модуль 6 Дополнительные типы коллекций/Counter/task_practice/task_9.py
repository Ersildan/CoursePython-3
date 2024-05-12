from collections import Counter


def print_bar_chart(data, mark):
    mx = len(data) if data == str else len(max(data, key=len))
    for i in Counter(data).most_common():
        print(f"{i[0].ljust(mx)} |{i[1] * mark}")


print_bar_chart('beegeek', '+')
languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')
