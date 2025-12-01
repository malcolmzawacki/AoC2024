import datetime
start = datetime.datetime.now()
with open("text/day7.txt") as f:
    text = f.read().split("\n")
    test_values, samples, candidates, count = [], [], [], 0
    for row in text:
        target_str, numbers_str = row.split(': ')
        test_values.append(int(target_str))
        samples.append([int(x) for x in numbers_str.split()])

for i in range(len(test_values)):
    candidates.append([samples[i][0]])
    samples[i].pop(0)
    for j in range(len(samples[i])):
        candidate_copy = []
        for k in range(len(candidates[i])):
            mult_test,add_test = candidates[i][k] * samples[i][j], candidates[i][k] + samples[i][j]
            if add_test <= test_values[i]:
                candidate_copy.insert(0,add_test)
            if mult_test <= test_values[i]:
                candidate_copy.insert(0,mult_test)
        candidates[i] = candidate_copy.copy()
        if j == len(samples[i]) - 1:
            if test_values[i] in candidates[i]:
                count+= test_values[i]

print(count)
print("Time: "+ str(datetime.datetime.now() - start))