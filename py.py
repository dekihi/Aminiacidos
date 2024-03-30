
def traducaoRnaH(tricar):
    
   lista = [] 
   traducaoRnaH = []
   lista.append([tricar[:3], tricar[3:6], tricar[6:9]])
   rnaAminoacido = {
       'UUU': 'Phe',
       'CUU': 'Leu',
       'UUA': 'Leu',
       'AAG': 'Lisina',
       'UCU': 'Ser',
       'UAU': 'Tyr',
       'CAA': 'Gln'
   }
   
   for i in lista:
       for rna in i:
           
           for r, aminoacido in rnaAminoacido. items():
               if rna == r:
                   traducaoRnaH.append(aminoacido)
                   
   return traducaoRnaH

while True:
    
    trincarRNA = input('Digite: ').upper().strip()
    esp = '-'
    
    if trincarRNA == '':
        break
    
    else:
        if traducaoRnaH(trincarRNA):
            traducaoRnaHmsg = traducaoRnaH(trincarRNA)
            
            for i, valor in enumerate(traducaoRnaHmsg):
                 print(valor,end='')
                 print()
