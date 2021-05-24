import nmap

class Scanner:

    def __init__(self,targetIP,ports,otherarguments):
        self.targetIP = targetIP
        self.ports = ports
        self.otherarguments = otherarguments
        self.nmapscanner = nmap.PortScanner()

    def scan_target(self):
        self.nmapscanner.scan(self.targetIP,self.ports,self.otherarguments)
        for host in self.nmapscanner.all_hosts():
            print('Nmap scan report for: ',host)
            print('Host is', self.nmapscanner[host]['status']['state'])
            for protocolo in self.nmapscanner[host].all_protocols():
                print('PORT\tSTATE\tSERVICE')
                for porta in self.nmapscanner[host][protocolo]:
                    target = self.nmapscanner[host][protocolo][porta]
                    print(str(porta) + " / " + protocolo + "\t" + target['state'] + "\t" + target['name'])

h = input('Digite o endereço IP do alvo: ')
p = input('Agora, digite as portas que você pretende acessar: ')
args = input('Digite os argumentos adicionais do comando Nmap se você preferir: ')

c = Scanner(h,p,args)
c.scan_target()