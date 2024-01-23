def main():
    n = int(input())
    count = 0
    start = 1
    
    while count < n:
        end = start + 2
        print(f"{start} {start + 1} {end} PUM")
        start = end + 2
        count += 1

if __name__ == "__main__":
    main()
