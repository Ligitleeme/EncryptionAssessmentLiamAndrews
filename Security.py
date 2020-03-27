class Security:
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\n ~`!@#$%^&*()_-+=<>,.?/\|[]}{:;" #Defines symbol list for caeser cipher
    MAX_KEY_SIZE = len(SYMBOLS) #Assigns a number to amount of characters in the symbol list

    def __init_(self): 
        print("")

    def getMode(self):
        while True:
            print('Do you wish to encrypt or decrypt a message?')
            mode = input().lower()
            if mode in ['encrypt', 'e', 'decrypt', 'd']:
                return mode
            else:
                print('Enter either "encrypt" or "e" or "decrypt" or "d".')
    def getMessage(self):
        print('Enter the name of the file:')
        
        return input()

    def getKey(self):
        key = 0
        while True:
            print('Enter the key number (1-%s)' % (self.MAX_KEY_SIZE))
            key = int(input())
            if (key >= 1 and key <= self.MAX_KEY_SIZE):
                return key
    
    def CaesarEncrypt(self, mode, message, key):
        translated = ''
        for symbol in message:
            symbolIndex = self.SYMBOLS.find(symbol)
            if symbolIndex == -1:
                translated += symbol
            else:
                symbolIndex += key
                if symbolIndex >= len(self.SYMBOLS):
                    symbolIndex -= len(self.SYMBOLS)
                elif symbolIndex < 0:
                    symbolIndex += len(self.SYMBOLS)
                translated += self.SYMBOLS[symbolIndex]
        return translated
    
    def CaesarDecrypt(self, mode, message, key):
        key = -key
        translated = ''
        for symbol in message:
            symbolIndex = self.SYMBOLS.find(symbol)
            if symbolIndex == -1:
                translated += symbol
            else:
                symbolIndex += key
                if symbolIndex >= len(self.SYMBOLS):
                    symbolIndex -= len(self.SYMBOLS)
                elif symbolIndex < 0:
                    symbolIndex += len(self.SYMBOLS)
                translated += self.SYMBOLS[symbolIndex]
        return translated

    def PolySubEncryptor(self, mode):
        translated = ""
        encrypt_letter_to_num = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,"'":26,",":27,".":28,"?":29,"/":30," ":31,"A":32,"B":33,"C":34,"D":35,"E":36,"F":37,"G":38,"H":39,"I":40,"J":41,"K":42,"L":43,"M":44,"N":45,"O":46,"P":47,"Q":48,"R":49,"S":50,"T":51,"U":52,"V":53,"W":54,"X":55,"Y":56,"Z":57,"\n":58,"!":59,"@":60,"#":61,"$":62,"%":63,"^":64,"&":65,"*":66,"(":67,")":68,"-":69,"_":70,"+":71,"=":72,"0":73,"9":74,"1":75,"2":76,"3":77,"4":78,"5":79,"6":80,"7":81,"8":82,"9":83,"`":84}
        encrypt_num_to_letter = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",26:"'",27:",",28:".",29:"?",30:"/",31:" ",32:"A",33:"B",34:"C",35:"D",36:"E",37:"F",38:"G",39:"H",40:"I",41:"J",42:"K",43:"L",44:"M",45:"N",46:"O",47:"P",48:"Q",49:"R",50:"S",51:"T",52:"U",53:"V",54:"W",55:"X",56:"Y",57:"Z",58:"\n",59:"!",60:"@",61:"#",62:"$",63:"%",64:"^",65:"&",66:"*",67:"(",68:")",69:"-",70:"_",71:"+",72:"=",73:"0",74:"9",75:"1",76:"2",77:"3",78:"4",79:"5",80:"6",81:"7",82:"8",83:"9",84:"`"}
        if mode == 'e' or mode =='encrypt':
            
            displacement_word = input("Please enter your displacement word: ")
            f4 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/test.txt" , "r")
            main_body = f4.read()
            new_word = ""

            displacement_list = []
            for x in displacement_word:
                displacement_list.append(encrypt_letter_to_num[x])

            displacement_list_position_count = 0
        
            for x in main_body:
                if displacement_list_position_count == len(displacement_list):
                    displacement_list_position_count = 0
                old_value = encrypt_letter_to_num[x]
                new_value = old_value + displacement_list[displacement_list_position_count]
                while new_value > 83:
                    new_value -= 84
                new_word += encrypt_num_to_letter[new_value]
                displacement_list_position_count += 1
                translated = new_word
        return translated

    def PolySubDecryptor(self, mode): 
        translated = ""
        encrypt_letter_to_num = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,"'":26,",":27,".":28,"?":29,"/":30," ":31,"A":32,"B":33,"C":34,"D":35,"E":36,"F":37,"G":38,"H":39,"I":40,"J":41,"K":42,"L":43,"M":44,"N":45,"O":46,"P":47,"Q":48,"R":49,"S":50,"T":51,"U":52,"V":53,"W":54,"X":55,"Y":56,"Z":57,"\n":58,"!":59,"@":60,"#":61,"$":62,"%":63,"^":64,"&":65,"*":66,"(":67,")":68,"-":69,"_":70,"+":71,"=":72,"0":73,"9":74,"1":75,"2":76,"3":77,"4":78,"5":79,"6":80,"7":81,"8":82,"9":83,"`":84}
        encrypt_num_to_letter = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",26:"'",27:",",28:".",29:"?",30:"/",31:" ",32:"A",33:"B",34:"C",35:"D",36:"E",37:"F",38:"G",39:"H",40:"I",41:"J",42:"K",43:"L",44:"M",45:"N",46:"O",47:"P",48:"Q",49:"R",50:"S",51:"T",52:"U",53:"V",54:"W",55:"X",56:"Y",57:"Z",58:"\n",59:"!",60:"@",61:"#",62:"$",63:"%",64:"^",65:"&",66:"*",67:"(",68:")",69:"-",70:"_",71:"+",72:"=",73:"0",74:"9",75:"1",76:"2",77:"3",78:"4",79:"5",80:"6",81:"7",82:"8",83:"9",84:"`"}        
        if mode == 'd' or mode =='decrypt':
            
            displacement_word = input("Enter displacement word: ")
            f4 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/Polysub_Encrypted.txt" , "r")
            main_body = f4.read()
            new_word = ""

            displacement_list = []
            for x in displacement_word:
                displacement_list.append(encrypt_letter_to_num[x])

            displacement_list_position_count = 0
        
            for x in main_body:
                if displacement_list_position_count == len(displacement_list):
                    displacement_list_position_count = 0
                old_value = encrypt_letter_to_num[x]
                new_value = old_value - displacement_list[displacement_list_position_count]
                while new_value < 0:
                    new_value += 84
                new_word += encrypt_num_to_letter[new_value]
                displacement_list_position_count += 1
            translated = new_word
        return translated
        
