from queue import Queue
import threading, socket
class DNSlister:

    def __init__(self,target,threads):
        self.threads = threads
        self.t4rg3t = target
        self.lock = threading.Lock()
        self.q = Queue()

    def bruteforce(self):
        while not self.q.empty():
            DNS = self.q.get() + "." + self.t4rg3t
            try:
                IP = socket.gethostbyname(DNS)
                self.lock.acquire()
                print(DNS + ":\t" + IP)
            except socket.gaierror:
                pass
            else:
                self.lock.release()
            self.q.task_done()

    def callthreads(self):
        with open("wordlist") as list:
            while True:
                name = list.readline().strip("\n")
                if not name:
                    break
                self.q.put(name)
        for i in range(self.threads):
            t = threading.Thread(target=self.bruteforce)
            t.daemon = True
            t.start()
        self.q.join()

    def main(self):
        self.callthreads()
        print('Mapeamento completo!')

c = DNSlister(target='google.com',threads=1000)
c.main()
