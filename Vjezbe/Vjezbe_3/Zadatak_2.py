def iteracije(N):
    zbr=5
    for i in range(N):
        zbr+=1/3
    for i in range(N):
        zbr-=1/3
    print(zbr)

iteracije(200)
iteracije(2000)
iteracije(20000)

#objasnjenje ovoga je zbog aproksimacije decimalnih brojeva koji se ne mogu zapisati u obliku 1/2^n
#  pa se svakim novim zbrajanjem/oduzimanjem
# uvodi nova aproksimacija i vrijednost odudara sve vise od ocekivane vrijednosti