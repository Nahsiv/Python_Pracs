from multiprocessing import Process

def numsqr(num=2):
    print(num ** 2)

def main():
    procs = []

    for i in range(5):
        procs.append(Process(target=numsqr))

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

if __name__ == '__main__':
    main()
