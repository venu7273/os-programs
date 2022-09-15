from queue import Queue
def pageFaults(incomingStream, n, frames):
    print("Incoming \t pages")
    s = set()
    queue = Queue()
    page_faults = 0
    for i in range(n):
        if len(s) < frames:
            if incomingStream[i] not in s:
                s.add(incomingStream[i]) 
                page_faults += 1
                queue.put(incomingStream[i])
        else:
            if incomingStream[i] not in s:
                val = queue.queue[0]
                queue.get()
                s.remove(val)
                s.add(incomingStream[i])
                queue.put(incomingStream[i])
                page_faults += 1
        print(incomingStream[i], end="\t\t")
        for q_item in queue.queue:
            print(q_item, end="\t")
        print()
    return page_faults
print("enter the reference string:")
incomingStream = list(map(int,input().strip().split()))
n = len(incomingStream)
frames = int(input("enter the no of frames"))
page_faults = pageFaults(incomingStream, n, frames)
hits = n - page_faults
print("\nPage Faults: " + str(page_faults))
print("Hit: " + str(hits))
