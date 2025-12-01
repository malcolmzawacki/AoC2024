
def veggieSpacer(veggieRows = list):
    for i in range(1,len(veggieRows)):
            for j in range(1,len(veggieRows[i])-1):
                if veggieRows[i][j] == 1:
                    pass
                elif veggieRows[i][j] != veggieRows[i][j+1]:
                    veggieRows[i].insert(j+1,1)
    return veggieRows

def onOpen():
    with open("text/day12sample.txt") as f:
        text = f.read()
        veggies = list(text.splitlines())
        veggieRows = []
        for row in veggies:
            veggieRow = list(veggie for veggie in row)
            #veggieRow.append(1)
            #veggieRow.insert(0,1)
            veggieRows.append(veggieRow)
        #veggieRows = veggieSpacer(veggieRows)
        plot_dict = dict()
        for i in range(len(veggieRows)):
            for j in range(len(veggieRows[i])):
                if veggieRows[i][j] not in plot_dict.keys():
                    plot_dict.update({veggieRows[i][j] : [(i,j)]})
                else:
                    plot_dict[veggieRows[i][j]].append((i,j))
        for row in veggieRows:
            print(row)
        print(plot_dict)


import datetime
start = datetime.datetime.now()
onOpen()
print("Time: "+ str(datetime.datetime.now() - start))