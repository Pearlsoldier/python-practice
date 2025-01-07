from source import daily, weekly

print(daily.forecast())
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)