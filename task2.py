import sys
from collections import deque

class Request:
    def __init__(self, cylinder, direction=1):
        self.cylinder = cylinder
        self.direction = direction

def read_requests(file_name):
    requests = []
    with open(file_name, 'r') as f:
        for line in f:
            requests.append(Request(int(line.strip())))
    return requests

def fcfs(requests, initial_position):
    head_movements = 0
    requests = deque(sorted(requests, key=lambda x: x.cylinder))
    requests.appendleft(Request(initial_position))
    for i in range(len(requests) - 1):
        head_movements += abs(requests[i].cylinder - requests[i+1].cylinder)
    return head_movements

def scan(requests, initial_position):
    requests = deque(sorted(requests, key=lambda x: x.cylinder))  # Convert to deque
    head_movements = 0
    current_position = initial_position
    direction = 1
    while requests or (current_position + direction < 4999 and direction == 1) or (current_position - direction > 0 and direction == -1):
        if requests and requests[0].cylinder == current_position:
            requests.popleft()
        if not requests and current_position < 4999 and direction == 1:
            current_position += 1
            continue
        if not requests and current_position > 0 and direction == -1:
            current_position -= 1
            continue
        if current_position < 4999 and direction == 1:
            next_request = next((r for r in requests if r.cylinder >= current_position), None)
            if next_request:
                head_movements += next_request.cylinder - current_position
                current_position = next_request.cylinder
                requests.popleft()
            else:
                head_movements += 4999 - current_position
                current_position = 4999
                direction = -1
        elif current_position > 0 and direction == -1:
            next_request = next((r for r in requests if r.cylinder <= current_position), None)
            if next_request:
                head_movements += current_position - next_request.cylinder
                current_position = next_request.cylinder
                requests.popleft()
            else:
                head_movements += current_position
                current_position = 0
                direction = 1
    return head_movements

def c_scan(requests, initial_position):
    requests = deque(sorted(requests, key=lambda x: x.cylinder))
    head_movements = 0
    current_position = initial_position

    while requests:
        next_request = next((r for r in requests if r.cylinder >= current_position), None)
        if next_request:
            head_movements += next_request.cylinder - current_position
            current_position = next_request.cylinder
            requests.remove(next_request)
        else:
            head_movements += 4999 - current_position
            current_position = 0
            head_movements += 4999

    return head_movements

def main():
    if len(sys.argv) != 3:
        file_name = input("Enter the file name: ")
        initial_position = int(input("Enter the initial position: "))
    else:
        file_name = sys.argv[1]
        initial_position = int(sys.argv[2])

    requests = read_requests(file_name)
    print("FCFS:")
    fcfs_head_movements = fcfs(requests, initial_position)
    print(f"Total head movements: {fcfs_head_movements}")

    print("SCAN:")
    scan_head_movements = scan(requests, initial_position)
    print(f"Total head movements: {scan_head_movements}")

    print("C-SCAN:")
    c_scan_head_movements = c_scan(requests, initial_position)
    print(f"Total head movements: {c_scan_head_movements}")

if __name__ == "__main__":
    main()