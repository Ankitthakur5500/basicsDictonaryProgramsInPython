#Dictionary and counter in Python to find winner of election


from collections import Counter
votes =['johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john'] 
vote_count=Counter(votes)
print(vote_count)
max_votes=max(vote_count.values())
print(max_votes)
for x in vote_count.keys():
        if vote_count[x]==max_votes:
            print(x)