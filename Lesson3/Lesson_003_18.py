print("METHOD 1")
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
news_ticker = ""
lenght_new_list = 0

for character in headlines:
    if len(news_ticker) >= 140:
        print("breaking now!")
        break
    elif len(character) + lenght_new_list > 140:
        remain_to_use = 140 - lenght_new_list
        print("Remain to use is {}".format(remain_to_use))
        character_rem = character[ :remain_to_use - 1]
        print("adding remain {}".format(character_rem))
        news_ticker += character_rem + " "
        lenght_new_list += (len(character_rem) + 1)
    else:
        print("Adding {}.".format(character))
        news_ticker += character + " "
        lenght_new_list += (len(character) + 1)
        rest = 140 - lenght_new_list
        print("the rest is {}".format(rest))
print(news_ticker)
print(lenght_new_list)

print("METHOD 2")
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = " "
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[ :140]
        break

print(news_ticker)


print("METHOD 3")
news_ticker = " ".join(headlines)[:140]
print(news_ticker)
