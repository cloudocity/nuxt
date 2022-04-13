games = int(input())
results = {}
for n in range(games):
    line = input()
    #print(line)
    line = line.split(";")
   # print(line)
    for i in range(0,3,2):
        if line[i] not in results:
            results[line[i]] = [1, 0, 0, 0, 0]
        else:
            results[line[i]][0] += 1
   # print('222',line[i])
    #print('!!!',line[0],line[3],line[2])
    #print('results', results)
    #print('line',line[1] , line[3])
    if int(line[1]) > int(line[3]):
        results[line[0]][1] += 1
        results[line[2]][3] += 1
        #print('win1', results)
    elif int(line[1]) == int(line[3]):
        results[line[0]][2] += 1
        results[line[2]][2] += 1
        #print('win2', results)
    else:
        results[line[0]][3] += 1
        results[line[2]][1] += 1
        #print('win3', results)
#print(results.items())
for team, res in results.items():
    res[4] = res[1]*3 + res[2]
    print(team+":", res[0], res[1], res[2], res[3], res[4])