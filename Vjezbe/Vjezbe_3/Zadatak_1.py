#a
print(5.0-4.935) #ocekujemo 0.065, ispis je 0.06500000000000039
#razlog je sto python decimalne brojeve koji nisu oblika 1/2^n aproksimaira najblizem broju oblika 1/2^n
#b
print(0.1+0.2+0.3) #ocekujemo 0.6, ispis je 0.6000000000000001
#razlog je sto se brojevi 0.1, 0.2 i 0.3 ne mogu napisati u obliku 1/2^n osim aproksimirano pa python racuna s tim aproksimacijama
#npr broj 0.1 je 1/10 i ne moze biti oblika 1/2^n osim ako je aproksimacija jer ako zelimo zapisati 0.1 u binarnom obliku to je beskonacno dug zapis i 
#jednom kad "prekinemo" zapisivati 0 i 1 taj napisan broj nam daje aproksimaciju 
