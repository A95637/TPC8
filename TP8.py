def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = []
    f.readline()
    for linha in f:
            subbd=[]
            a=linha.replace("\n","")
            b=a.split(",")
            d=str(int(b[1])+1)
            b[0]=str("emd"+(str(d.zfill(5))))
            for i in range (0,13):
                if i !=1:
                    subbd.append(b[i])
            bd.append(subbd)
    return bd


def listarDataset(bd):
    p=bd.copy()
    p.sort(reverse=True, key=org)
    print("id     |Data               |Nome      | Aptidão")
    print("----------------------------------------------")
    for a in bd:
        print(a[0]+' | '+a[1]+' | '+a[3]+a[2]
                +' | '+ a[11] )
    
def org (bd):
    data=bd[1]
    return data

def consultarDataset(bd, id):
    a=0
    try:
        while bd[a][0]!=id:
            a+=1
        return bd[a][11]
    except IndexError:
        return "Erro"
    

def org2(d):
    return (d.lower())
def modalidades(d):
    modalidade=[]
    for i in d:
        if i[7] not in modalidade:
            modalidade.append(i[7])
    modalidade.sort(key=org2)


    return modalidade


def distrib(d,campo):
    ordem={"Idade":4,"Género":5,"Modalidade":7,"Clube":8, "Federado":10,"Resultado":11}
    distribuicao = {}
    for linha in d:
        if linha[ordem[campo]] in distribuicao.keys():
            distribuicao[linha[ordem[campo]]] = distribuicao[linha[ordem[campo]]] +1
        else:
            distribuicao[linha[ordem[campo]]] = 1
    return distribuicao

import matplotlib.pyplot as plt
def plotDistrib(BD,campo):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    X=[]
    Y=[]
    distribuicao=distrib(BD,campo)
    for linha in distribuicao:
            X.append(linha)
            Y.append(distribuicao[linha])
    ax.bar(X,Y)
    plt.show()
    return ()