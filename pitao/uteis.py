def conversor():
    frase = str(input('Insere uma palavra/frase: '))
    frase = frase.upper().strip()
    comprFrase = len(frase)

    for i in range(comprFrase):
        if frase[i]=='A' or frase[i]=='Á' or frase[i]=='À' or frase[i]=='Ã' or frase[i]=='Â' or frase[i]=='Ä':
            print('𓄿 ',end='')
        elif frase[i]=='B':
            print('𓃀 ',end='')
        elif frase[i]=='C' or frase[i]=='Ç':
            print('𓎡 ',end='')
        elif frase[i]=='D':
            print('𓂧 ',end='')
        elif frase[i]=='E' or frase[i]=='É' or frase[i]=='È' or frase[i]=='Ê' or frase[i]=='Ë':
            print('𓇋 ',end='')
        elif frase[i]=='F':
            print('𓆑 ',end='')
        elif frase[i]=='G':
            print('𓎼 ',end='')
        elif frase[i]=='H':
            print('𓎛 ',end='')
        elif frase[i]=='I' or frase[i]=='Í' or frase[i]=='Ì' or frase[i]=='Î' or frase[i]=='Ï':
            print('𓇌 ',end='')
        elif frase[i]=='J':
            print('𓆓 ',end='')
        elif frase[i]=='K':
            print('𓎡 ',end='')
        elif frase[i]=='L':
            print('𓃭 ',end='')
        elif frase[i]=='M':
            print('𓅓 ',end='')
        elif frase[i]=='N' or frase[i]=='Ñ':
            print('𓈖 ',end='')
        elif frase[i]=='O' or frase[i]=='Ó' or frase[i]=='Ò' or frase[i]=='Õ' or frase[i]=='Ô' or frase[i]=='Ö':
            print('𓍯 ',end='')
        elif frase[i]=='P':
            print('𓊪 ',end='')
        elif frase[i]=='Q':
            print('𓈎 ',end='')
        elif frase[i]=='R':
            print('𓂋 ',end='')
        elif frase[i]=='S':
            print('𓋴 ',end='')
        elif frase[i]=='T':
            print('𓏏 ',end='')
        elif frase[i]=='U' or frase[i]=='Ú' or frase[i]=='Ù' or frase[i]=='Û' or frase[i]=='Ü':
            print('𓅱 ',end='')
        elif frase[i]=='V':
            print('𓆑 ',end='')
        elif frase[i]=='W':
            print('𓅱 ',end='')
        elif frase[i]=='X':
            print('𓋴 ',end='')
        elif frase[i]=='Y' or frase[i]=='Ý':
            print('𓇌 ',end='')
        elif frase[i]=='Z':
            print('𓊃 ',end='')
        elif frase[i]==' ':
            print('⠀',end='')
        else:
            print('Insira um caracter válido!!')