if __name__ == '__main__':
    print("Enter Total Process Number: ")
    total_p_no = int(input())
    total_time = 0 
    total_time_counted = 0
    proc = []
    wait_time = 0
    turnaround_time = 0
    for _ in range(total_p_no):
        print("Enter process arrival time and burst time") 
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1]
        proc.append([arrival, burst, remaining_time, 0])
        total_time += burst
    print("Enter time quantum")
    time_quantum = int(input())
    while total_time != 0:
        for i in range(len(proc)):
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                proc[i][2] = 0 
            elif proc[i][2] > 0:
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                wait_time += total_time_counted - proc[i][0] - proc[i][1]
                turnaround_time += total_time_counted - proc[i][0]
                proc[i][3] = 1 
    print("\nAvg Waiting Time is ", (wait_time * 1) / total_p_no)
    print("Avg Turnaround Time is ", (turnaround_time * 1) / total_p_no)
