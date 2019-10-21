
characteristics={"hair_color": {"black": "CCAGCAATCGC","brown": "GCCAGTGCCG","blonde":"TTAGCTATCGC"},
                 "facial_shape":{"square":"GCCACGG","round":"ACCACAA","oval":"AGGCCTCA"},
                 "eye_color": {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"},
                 "gender": {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"},
                 "race":{"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}
}

suspects={ "Eva":{"gender":"female", "race":"white","hair_color":"blonde","eye_color":"blue","facial_shape":"oval"},""
"Larisa":{"gender":"female","race":"white","hair_color":"brown","eye_color":"brown","facial_shape":"oval"},
"Matej":{"gender":"male","race":"white","hair_color":"black","eye_color":"blue","facial_shape":"oval"},
"Miha":{"gender":"male","race":"white","hair_color":"brown","eye_color":"green","facial_shape":"square"}}

criminal={}

print( "***** Welcome to CSI FORENSICS PROGRAM *****")
print( "Analyzing suspects data ...")

with open("dna.txt","r") as dna_file:
  dna_list=dna_file.read()

  for c in characteristics:
      for k, v in characteristics[c].items():
         if v in dna_list:
            criminal[c]=k

  for s in suspects:
     l_item= suspects[s].items()
     equales= set(l_item) & set (criminal.items())
     if len(equales)==5:
         print("This suspect--> ",s," is the real criminal who ate the ice cream!!")
         break






