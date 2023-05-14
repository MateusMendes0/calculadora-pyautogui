import PySimpleGUI as sg

def removerzero(strfloat):
    a = str(strfloat)
    b = a.endswith('.0')
    if b:
        c = a[:-2]
        return int(c)
    else:
        return strfloat


sg.theme('DarkAmber')

lista = []
a = ''

resul = [
    [sg.StatusBar('0',size=(15,1),font=('Sans',20),justification='right',key='resul',tooltip='resultado')]
]
numeros = [
    [sg.Button('1',size=(6,1)),sg.Button('2',size=(6,1)),sg.Button('3',size=(6,1))],
    [sg.Button('4',size=(6,1)),sg.Button('5',size=(6,1)),sg.Button('6',size=(6,1))],
    [sg.Button('7',size=(6,1)),sg.Button('8',size=(6,1)),sg.Button('9',size=(6,1))],
    [sg.Button(',',size=(6,1),key='.'),sg.Button('0',size=(6,1)),sg.Button('C',size=(6,1))]
]

simbolos1 = [
    [sg.Text(""),sg.Button('×',size=(5,1)),sg.Button('÷',size=(5,1)),sg.Button('⌫',size=(5,1),key='del'),sg.Button('n²',size=(5,1),key='quadrado'),sg.Text('')]
]


simbolos = [
    [sg.Button('+',size=(3,2),key='+')],
    [sg.Button('-',size=(3,2))],
    [sg.Button('=',size=(3,1))],
]

layout = [
    [sg.Frame('Resultado',resul)],
    [sg.Frame('',simbolos1)],
    [sg.Frame('',numeros,),sg.Frame('',simbolos,key='sla')],
]

window = sg.Window('Calculadora',layout)


while True:
    eventos,valores = window.read()
    print((eventos,valores))

    if eventos == None or eventos == sg.WIN_CLOSED:
        break

    else:
        if eventos not in ['+','-','=','C','del','×','÷','quadrado']:
            lista.append(eventos)
            a = ''.join(lista)
            window['resul'].update(value=a)
        elif eventos in ['+','-','×','÷']:
            if '+' in a or '-' in a or '×' in a or '÷' in a:
                pass
            else:
                lista.append(' ')
                lista.append(eventos)
                lista.append(' ')
                a = ''.join(lista)
                window['resul'].update(value=a)
    if eventos == 'del':
        lena = len(a)
        indexa = a.rfind(' ')
        print(indexa+1,lena)
        if indexa+1 == lena:
            a = a[:lena - 3]
            lista = []
            lista.append(a)
            window['resul'].update(value=a)
        else:
            a = a[:lena-1]
            lista = []
            lista.append(a)
            window['resul'].update(value=a)
    if eventos == '=':
        try:
            b = a.find(' ')
            c = float(a[:b])
            d = a.rfind(' ')
            e = float(a[d:])
            print(c,e)
        except:
            e = 0
    if eventos == '=':
        if '+' in a:
            resul1 = c + e
            resul1 = removerzero(resul1)
            a = str(resul1)
            window['resul'].update(a)
            lista.clear()
            lista.append(str(resul1))

        if '-' in a[2:]:
            resul1 = c - e
            resul1 = removerzero(resul1)
            window['resul'].update(resul1)
            a = ''
            lista.clear()
            lista.append(str(resul1))

        if '×' in a:
            resul1 = c * e
            resul1 = removerzero(resul1)
            window['resul'].update(resul1)
            a = ''
            lista.clear()
            lista.append(str(resul1))

        if '÷' in a:
            resul1 = c / e
            resul1 = removerzero(resul1)
            window['resul'].update(resul1)
            a = ''
            lista.clear()
            lista.append(str(resul1))

    if eventos == 'C':
        lista.clear()
        a = ''
        window['resul'].update(value='0')
window.close()