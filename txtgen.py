import random

def generate_random_request_file(file_name, num_requests):
    with open(file_name, 'w') as file:
        for _ in range(num_requests):
            request = str(random.randint(0, 1999)) + '\n'
            file.write(request)

if __name__ == "__main__":
    file_name = "disk_requests.txt"
    num_requests = 1000
    generate_random_request_file(file_name, num_requests)