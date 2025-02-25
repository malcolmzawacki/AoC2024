
import datetime
start = datetime.datetime.now()


def construct_diskMap(text):
    diskMap = []
    for char in text:
        diskMap.append(int(char))
    return diskMap

def construct_diskIDs(diskMap):
    diskID, diskID2,whole_files,no_gaps = [],[],[],[]
    lengthCount = 0
    for i in range(len(diskMap)):
        file_chunk = []
        if i % 2 == 0:
            lengthCount+=diskMap[i]
            for j in range(diskMap[i]):
                file_chunk.append(i//2)
                diskID.append(i//2)
                diskID2.append(i//2)
            no_gaps.append(file_chunk)
        else:
            for j in range(diskMap[i]):
                diskID.append('.')
                file_chunk.append('.')
        if len(file_chunk) > 0:
            whole_files.append(file_chunk)
        diskID2.reverse()
        no_gaps.reverse()
    return diskID,diskID2,lengthCount,whole_files,no_gaps

def check_sum(diskID, diskID2,lengthCount):
    IDstring = 0
    for i in range(lengthCount):
        if type(diskID[i]) == int:
            IDstring += i*diskID[i]
        else:
           diskID.insert(i,diskID2[0])
           diskID.pop(i+1)
           IDstring += i*diskID[i]
           diskID2.pop(0)
    return IDstring,diskID,diskID2

def whole_file_compacting(whole_files, no_gaps):
    print(len(whole_files))
    print(len(no_gaps))
    i = 0
    while True:
        # get the gap index once per iteration
        try:
            gap_idx = whole_files.index(no_gaps[i])
        except ValueError:
            # if for some reason no_gaps[i] isn't in whole_files, we're done
            break

        if gap_idx == 0:
            # if that gap is at index 0, condition in 'while ...' will be falseish
            # or we can break (depending on your puzzle logic)
            break

        j = 0
        print(i)
        # keep going until we've tried positions up to the gap
        while j < gap_idx:
            if isinstance(whole_files[j][0], int):
                if j >= gap_idx - 1:
                    j = len(whole_files)
                    i += 1
                else:
                    j += 1
            else:
                # it's a gap chunk
                if len(whole_files[j]) < len(no_gaps[i]):
                    if j >= gap_idx - 1:
                        j = len(whole_files)
                        i += 1
                    else:
                        j += 1
                else:
                    diff = len(whole_files[j]) - len(no_gaps[i])
                    # store the length of the 'no_gaps[i]' chunk
                    needed = len(no_gaps[i])

                    # figure out how big the new merged gap on the right side is
                    swap = len(whole_files[gap_idx])  # 'gap_idx' instead of repeated calls
                    before = False
                    after = False
                    # if there's a gap before the chunk
                    if gap_idx - 1 >= 0 and isinstance(whole_files[gap_idx - 1][0], str):
                        swap += len(whole_files[gap_idx - 1])
                        before = True
                    # if there's a gap after the chunk
                    if gap_idx + 1 < len(whole_files) and isinstance(whole_files[gap_idx + 1][0], str):
                        swap += len(whole_files[gap_idx + 1])
                        after = True

                    swap_gap = ['.' for _ in range(swap)]

                    # replace the chunk + surrounding gaps w/ a single combined gap
                    if before:
                        if after:
                            if gap_idx < len(whole_files) - 1:
                                whole_files = (whole_files[:gap_idx - 1] + 
                                               [swap_gap] + 
                                               whole_files[gap_idx + 2:])
                            else:
                                whole_files = whole_files[:gap_idx - 1] + [swap_gap]
                        else:
                            whole_files = (whole_files[:gap_idx - 1] + 
                                           [swap_gap] + 
                                           whole_files[gap_idx + 1:])
                    else:
                        whole_files = (whole_files[:gap_idx] + 
                                       [swap_gap] + 
                                       whole_files[gap_idx + 1:])

                    # now move the file chunk into the j-th gap spot, plus leftover if any
                    if diff > 0:
                        new_gap = ['.' for _ in range(diff)]
                        whole_files = (whole_files[:j] + 
                                       [no_gaps[i]] + 
                                       [new_gap] + 
                                       whole_files[j+1:])
                        j = len(whole_files)
                        i += 1
                    else:
                        whole_files = (whole_files[:j] + 
                                       [no_gaps[i]] + 
                                       whole_files[j+1:])
                        j = len(whole_files)
                        i += 1
        # loop again, picking up the next gap
        # if i is out of range for no_gaps, break
        if i == len(no_gaps):
            break

    # build the final string

    i = 0
    print(len(whole_files))
    index = 0
    whole_files_counter = 0
    while i < len(whole_files):
        if 0 in whole_files[i] or '.' in whole_files[i]:
            print(f"SKIP {i}")
            index += len(whole_files[i])
            i+=1
        else:
            j = 0
            while j < len(whole_files[i]):
                summand = index*whole_files[i][j]
                whole_files_counter += summand
                print(f" added {index} multiplied by {whole_files[i][j]} in part {i}")
                j+=1
                index+=1
            i+=1
    print(f"DONE: found {whole_files_counter}")
    return whole_files_counter

def onOpen():
    with open("text/day9.txt") as f:
        text = f.read()
        text = "2333133121414131402"
    diskMap = construct_diskMap(text)
    #print(diskMap)
    diskID, diskID2,lengthCount,whole_files,no_gaps = construct_diskIDs(diskMap)
    whole_file_checksum = whole_file_compacting(whole_files,no_gaps)
    checksum,diskID,diskID2 = check_sum(diskID, diskID2,lengthCount)
    return checksum,diskID,diskID2, whole_file_checksum


IDstring,diskID,diskID2,whole_file_checksum = onOpen()
#print(stringcheck)
print(f" part 1 checksum is {IDstring}")
print(f" part 2 checksum is {whole_file_checksum}")
print("Time: "+ str(datetime.datetime.now() - start))
"6350726911935"