from datetime import date

lst = sorted([date.fromisoformat(input()) for i in range(int(input()))])

print(*[i.strftime('%d/%m/%Y') for i in lst], sep='\n')
