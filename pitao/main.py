import sys
import uteis

def main():
    op=0
    while op!=1 or op!=2:
        print('--------------------------------')
        print('          CONVERTGLIFO          ')
        print('    conversor de hieróglifos    ')
        print('--------------------------------')
        print('1- Converter de letras para hieróglifos')
        print('2- Sair')
        op = int(input('opção -> '))

        if op==1:
            uteis.conversor()
            print('\n'); 
            main()
        elif op==2:
            sys.exit('volte sempre :D')
        else:
            print('Insira uma opção válida!!')

main()