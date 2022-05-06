from tkinter import *
from tkinter import ttk
import requests
import json
import os
os.system("cls")
roles=False
count=0
theme="dark"
#--------------------------------------FUNCIONES------------------------------------------------
def rol():
    global login
    global theme
    login=Tk()
    login.title("Login")
    login.resizable(0,0)
    login.tk.call("source", "azure.tcl")
    login.tk.call("set_theme", theme)
    Label(login).pack()
    Label(login,text="""Calculadora de\nCurrencies y Finanzas""",font=("Comic Sans MS",15)).pack()
    Label(login).pack()
    Button(login,text="Admin",font=("Comic Sans MS",15),command=cedentials).pack()
    Label(login).pack()
    Button(login,text="Invitado",font=("Comic Sans MS",15),command=invitado).pack()
    Label(login).pack()
    login.mainloop()
def cedentials():
    login.destroy()
    global admin
    global ent_0
    global wrong
    admin=Tk()
    admin.title("Login")
    admin.resizable(0,0)
    admin.tk.call("source", "azure.tcl")
    admin.tk.call("set_theme", theme)
    Label(admin).pack()
    Button(admin,text="Atras",font=("Comic Sans MS",15),command=atras).pack()
    Label(admin).pack()
    Label(admin,text="Digite la Contraseña",font=("Comic Sans MS",15)).pack()
    Label(admin).pack()    
    ent_0=Entry(admin,font=("Comic Sans MS",15),show="♣")
    ent_0.pack()
    Label(admin).pack()
    Button(admin,text="Comprobar",font=("Comic Sans MS",15),command=comprobar).pack()
    Label(admin).pack()    
    wrong=Label(admin,text="",font=("Comic Sans MS",15),fg="red")
    wrong.pack()
    Label(admin).pack()
    admin.mainloop()
def atras():
    admin.destroy()
    rol()
def comprobar():
    global roles
    if ent_0.get()=="premium":
        roles=True
        admin.destroy()
        main()
    else:
        wrong.config(text="Contraseña Incorrecta")
def invitado():
    login.destroy()
    main()
def main():
    global root
    root=Tk()
    root.title("Proyecto Final")
    root.resizable(0,0)
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", theme)
    notebook=ttk.Notebook(root)
    notebook.grid()
    pes0=ttk.Frame(notebook)
    pes1=ttk.Frame(notebook)
    pes2=ttk.Frame(notebook)
    pesh=ttk.Frame(notebook)
    if roles==True:
        pes3=ttk.Frame(notebook)
    notebook.add(pes0,text="Conversor De Moneda")
    notebook.add(pes1,text="Prestamos")
    notebook.add(pes2,text="Inversiones")
    notebook.add(pesh,text="Historial")
    if roles==True:
        notebook.add(pes3,text="Acerda De")
#--------------------------------------CONVERTIDOR DE MONEDA------------------------------------------------
    global local
    global claveDeApi
    global lactualizacion
    global combo1
    global lfecha
    global combo2
    global epes01
    global lDestinoFinal
    with open("diccionario.json","r") as j:        
        local=json.load(j)
    fechaDeActualizacion=local["date"]
    dicAbrebiaturas=local["rates"]
    listAbrebiauras=[]
    for i,j in dicAbrebiaturas.items():
        listAbrebiauras.append(i)
    if roles==True:
        l=Label(pes0,font=("Comic Sans MS",12),text="Clave de API")
        l.grid(column=0,row=1)        
        claveDeApi=Entry(pes0,font=("Comic Sans MS",12))
        claveDeApi.grid(column=1,row=1)
        btfecha=Button(pes0,background="#E94F83",font=("Comic Sans MS",12),text="Actualizar",command=actualizar)
        btfecha.grid(column=2,row=1)    
    lactualizacion=Label(pes0,font=("Comic Sans MS",12))
    lactualizacion.grid(column=1,row=2)
    l=Label(pes0,font=("Comic Sans MS",12),text="DE:")
    l.grid(column=0,row=3)
    btinfo=Button(pes0,font=("Comic Sans MS",12),background="#F9AD3B",text="Informacion de Monedas",command=infoDeMonedas,padx=50)
    btinfo.grid(column=1,row=3)
    l=Label(pes0,font=("Comic Sans MS",12),text="A:")
    l.grid(column=2,row=3)    
    combo1=ttk.Combobox(pes0,font=("Comic Sans MS",12),values=listAbrebiauras)
    combo1.grid(column=0,row=4)    
    lfecha=Label(pes0,font=("Comic Sans MS",12),text=local["date"])
    lfecha.grid(column=1,row=4)    
    combo2=ttk.Combobox(pes0,font=("Comic Sans MS",12),values=listAbrebiauras)
    combo2.grid(column=2,row=4)
    l=Label(pes0,font=("Comic Sans MS",12),text="Digite Cantidad")
    l.grid(column=0,row=5)
    l=Label(pes0,font=("Comic Sans MS",12),text="Equivalen A")
    l.grid(column=2,row=5)    
    epes01=ttk.Entry(pes0,font=("Comic Sans MS",12),validate="key",validatecommand=(pes1.register(validate_entry), "%S"))
    epes01.grid(column=0,row=6)
    btcalcular=Button(pes0,padx=30,pady=30,background="#007FFF",font=("Comic Sans MS",15),text="Calcular",command=calculoDeMoneda)
    btcalcular.grid(column=1,row=6)    
    lDestinoFinal=Label(pes0,foreground="#007FFF",font=("Comic Sans MS",13))
    lDestinoFinal.grid(column=2,row=6)
#-------------------------------------CALCULADORA DE PRESTAMOS-------------------------------------------------
    global tipoDeInteres
    global epes11
    global epes12
    global epes13
    global r11
    global r22
    global r33
    global aviso
    global bt1
    tipoDeInteres=IntVar() 
    l=Label(pes1,font=("Comic Sans MS",12),text="Capital:")
    l.grid(column=0,row=0)
    l=Label(pes1,font=("Comic Sans MS",12),text="Periodos (Meses):")
    l.grid(column=1,row=0)
    l=Label(pes1,font=("Comic Sans MS",12),text="Tasa de Interes (%):")
    l.grid(column=2,row=0)    
    epes11=ttk.Entry(pes1,font=("Comic Sans MS",12),validate="key",validatecommand=(pes1.register(validate_entry), "%S"))
    epes11.grid(column=0,row=1)    
    epes12=ttk.Entry(pes1,font=("Comic Sans MS",12),validate="key",validatecommand=(pes1.register(validate_entry), "%S"))
    epes12.grid(column=1,row=1)    
    epes13=ttk.Entry(pes1,font=("Comic Sans MS",12),validate="key",validatecommand=(pes1.register(validate_entry), "%S"))
    epes13.grid(column=2,row=1)
    l=Label(pes1,font=("Comic Sans MS",12),text="Tipo de Interes =")
    l.grid(column=0,row=2)
    r=Radiobutton(pes1,foreground="#F7AB38",font=("Comic Sans MS",12),text="Mensual",variable=tipoDeInteres,value=1)
    r.grid(column=1,row=2)
    r=Radiobutton(pes1,foreground="#F7AB38",font=("Comic Sans MS",12),text="Efectivo Anual",variable=tipoDeInteres,value=2)
    r.grid(column=2,row=2)
    l=Label(pes1,font=("Comic Sans MS",12),text="Cuota Mensual")
    l.grid(column=0,row=3)
    l=Label(pes1,font=("Comic Sans MS",12),text="Monto Total")
    l.grid(column=1,row=3)
    l=Label(pes1,font=("Comic Sans MS",12),text="Total Intereses")
    l.grid(column=2,row=3)    
    r11=Label(pes1,foreground="#007FFF",font=("Comic Sans MS",13))
    r11.grid(column=0,row=4)    
    r22=Label(pes1,foreground="#26A0DA",font=("Comic Sans MS",13))
    r22.grid(column=1,row=4)    
    r33=Label(pes1,foreground="#E94F83",font=("Comic Sans MS",13))
    r33.grid(column=2,row=4)    
    aviso=Label(pes1,font=("Comic Sans MS",12),fg="red")
    aviso.grid(column=0,row=5)    
    bt1=Button(pes1,padx=30,pady=30,background="#007FFF",font=("Comic Sans MS",15),text="Calcular",command=calculoDePrestamo)
    bt1.grid(column=2,row=5)
#------------------------------------CALCULADORA DE INVERSION--------------------------------------------------
    ipoDeinversion=IntVar() 
    global inversion
    global annos
    global tasain
    global ri1
    global ri2
    global ri3
    l1=Label(pes2,font=("Comic Sans MS",12),text="invertir:")
    l1.grid(column=0,row=0)
    l2=Label(pes2,font=("Comic Sans MS",12),text="Periodos (años):")
    l2.grid(column=1,row=0)
    l3=Label(pes2,font=("Comic Sans MS",12),text="Tasa de Interes (%):")
    l3.grid(column=2,row=0)    
    inversion=ttk.Entry(pes2,font=("Comic Sans MS",12),validate="key",validatecommand=(pes2.register(validate_entry), "%S"))
    inversion.grid(column=0,row=1)    
    annos=ttk.Entry(pes2,font=("Comic Sans MS",12),validate="key",validatecommand=(pes2.register(validate_entry), "%S"))
    annos.grid(column=1,row=1)    
    tasain=ttk.Entry(pes2,font=("Comic Sans MS",12),validate="key",validatecommand=(pes2.register(validate_entry), "%S"))
    tasain.grid(column=2,row=1)
    l5=Label(pes2,font=("Comic Sans MS",12),text="Mensual")
    l5.grid(column=0,row=3)
    l6=Label(pes2,font=("Comic Sans MS",12),text="Anual")
    l6.grid(column=1,row=3)
    l7=Label(pes2,font=("Comic Sans MS",12),text="Ganancia")
    l7.grid(column=2,row=3)    
    ri1=Label(pes2,fg="#26A0DA",font=("Comic Sans MS",13))
    ri1.grid(column=0,row=4)    
    ri2=Label(pes2,fg="#26A0DA",font=("Comic Sans MS",13))
    ri2.grid(column=1,row=4)    
    ri3=Label(pes2,fg="forest green",font=("Comic Sans MS",13))
    ri3.grid(column=2,row=4)
    aviso=Label(pes2,font=("Comic Sans MS",12),fg="red")
    aviso.grid(column=0,row=5)
    btc=Button(pes2,padx=30,pady=30,bg="#007FFF",font=("Comic Sans MS",15),text="Calcular",command=calculodeinversion)
    btc.grid(column=2,row=5)
#------------------------------------Historial--------------------------------------------------
    global table
    global count
    fr1=Frame(pesh)
    fr1.grid(column=0,row=0)
    fr2=Frame(pesh)
    fr2.grid(column=1,row=0)
    fr3=Frame(pesh)
    fr3.grid(column=2,row=0)
    Label(fr1,text="Leyenda").pack()
    Label(fr1,text="P = Prestamo\nM = Periodos\n% = Tasa de Interes\n*Mes = Pagos por Mes\nMT = Monto Total\nTI = Intereses Totales\nI = Inversion\nGM = Ganancia Mensual\nGA = Ganancia Anual\nGT = Ganancia Total").pack()
    Label(fr2,text="Historial").pack()    
    table=ttk.Treeview(fr2)
    table["columns"]=("Evento")
    table.column("#0",width=0,stretch=NO)
    table.column("Evento",anchor=CENTER,width=450)
    table.heading("#0",text="",anchor=CENTER)
    table.heading("Evento",text="Evento",anchor=CENTER)
    table.pack()    
    with open("historial.txt", "r") as tf:
        lines = tf.read().split(',')
    for line in lines:
        table.insert(parent="",index="end",iid=count,text="",values=(line))
        count=count+1
#------------------------------------ACERCA DE--------------------------------------------------
    l=Label(pes3,font=("Comic Sans MS",9),text="""
    Python 3 , VS Code
    Softwere desarrollado por:
    Raul Ortega (tacho7913@gmail.com)

    Tema Azure desarrollado por:
    rdbende
    rdbende@gmail.com""")
    l.grid(column=0,row=0)
    l=Label(pes3,text="""
    Agradecimientos a

    Universidad Castro Carazo

    Profesor:
    Steven Arias
    IN1013""")
    l.grid(column=1,row=0)
    l=Label(pes3,font=("Comic Sans MS",9),text="""
    Servicio de Currencies por:
    https://fixer.io/
    Cada API esta limitada a 100 intentos por mes

    (Publica): dd44405658a1e71fd1d896a14a76f32d
    (Raul): e8b61c6dcd13207be4cd1e80461dc65d
    (Sebas): 420c3d5fb0dd29ab3257169cd74b2727
    (David): 43ba788a96d885a0d13f4a2676ceb4af""")
    l.grid(column=2,row=0)
    Button(pes3,padx=30,pady=30,bg="#26A0DA",font=("Comic Sans MS",12),text="Tema Light",command=light).grid(column=0,row=1)
    Button(pes3,padx=30,pady=30,bg="#900815",font=("Comic Sans MS",12),text="Tema Dark",command=dark).grid(column=2,row=1)

    root.mainloop()
def validate_entry(text):
    return text.isnumeric()
def actualizar():
    api = claveDeApi.get()
    try:
        res_a = requests.get("http://data.fixer.io/api/latest",params={"access_key": api})
        dato_a = res_a.json()
        prueba=dato_a["success"]
        if prueba==True:
            with open("diccionario.json","w") as j:
                json.dump(dato_a,j)
            lactualizacion.config(text="Actualizacion Exitosa",fg="green")
            lfecha.config(text=local["date"])
        else:
            lactualizacion.config(text="Error de Peticion",fg="red")
    except:
        lactualizacion.config(text="Error de Conexion",fg="red")
def calculoDeMoneda():
    global count
    combobase=combo1.get()
    combodestino=combo2.get()
    cantidad=epes01.get()
    cantidad=float(cantidad)
    rate_a = local["rates"][combobase]
    rate_b = local["rates"][combodestino]
    rate = round((rate_b / (rate_a)), 4)
    resultadoFinal=rate*cantidad
    resultadoFinal=float(resultadoFinal)
    resultadoFinal=round(resultadoFinal,2)
    lDestinoFinal.config(text=f'{(resultadoFinal):,}')
    actual=f'"-{cantidad} {combo1.get()} = -{resultadoFinal} {combo2.get()}"'
    historial = open("historial.txt","a")
    historial.write(str(actual))
    historial.write(",")
    historial.close()
    table.insert(parent="",index="end",iid=count,text="",values=(actual))
    count=count+1
def infoDeMonedas():
    ventana_info=Toplevel(root)
    ventana_info.title("Informacion de Monedas")
    info=Label(ventana_info,text="""
    Monedas disponibles
    Fixer API viene con soporte para 170 monedas mundiales, incluidos metales preciosos y Bitcoin.
    Encuentre a continuación una lista completa de los símbolos disponibles.""")
    info.grid(column=1,row=0)
    info=Label(ventana_info,text="""
    AED	United Arab Emirates Dirham
    AFN	Afghan Afghani
    ALL	Albanian Lek
    AMD	Armenian Dram
    ANG	Netherlands Antillean Guilder
    AOA	Angolan Kwanza
    ARS	Argentine Peso
    AUD	Australian Dollar
    AWG	Aruban Florin
    AZN	Azerbaijani Manat
    BAM	Bosnia-Herzegovina Convertible Mark
    BBD	Barbadian Dollar
    BDT	Bangladeshi Taka
    BGN	Bulgarian Lev
    BHD	Bahraini Dinar
    BIF	Burundian Franc
    BMD	Bermudan Dollar
    BND	Brunei Dollar
    BOB	Bolivian Boliviano
    BRL	Brazilian Real
    BSD	Bahamian Dollar
    BTC	Bitcoin
    BTN	Bhutanese Ngultrum
    BWP	Botswanan Pula
    BYR	Belarusian Ruble
    BYN	New Belarusian Ruble
    BZD	Belize Dollar
    CAD	Canadian Dollar
    CDF	Congolese Franc
    CHF	Swiss Franc
    CLF	Chilean Unit of Account (UF)
    CLP	Chilean Peso
    CNY	Chinese Yuan
    COP	Colombian Peso
    CRC	Costa Rican Colón
    CUC	Cuban Convertible Peso
    CUP	Cuban Peso
    CVE	Cape Verdean Escudo
    CZK	Czech Republic Koruna
    DJF	Djiboutian Franc
    DKK	Danish Krone""")
    info.grid(column=0,row=1)
    info=Label(ventana_info,text="""
    DOP	Dominican Peso
    DZD	Algerian Dinar
    EGP	Egyptian Pound
    ERN	Eritrean Nakfa
    ETB	Ethiopian Birr
    EUR	Euro
    FJD	Fijian Dollar
    FKP	Falkland Islands Pound
    GBP	British Pound Sterling
    GEL	Georgian Lari
    GGP	Guernsey Pound
    GHS	Ghanaian Cedi
    GIP	Gibraltar Pound
    GMD	Gambian Dalasi
    GNF	Guinean Franc
    GTQ	Guatemalan Quetzal
    GYD	Guyanaese Dollar
    HKD	Hong Kong Dollar
    HNL	Honduran Lempira
    HRK	Croatian Kuna
    HTG	Haitian Gourde
    HUF	Hungarian Forint
    IDR	Indonesian Rupiah
    ILS	Israeli New Sheqel
    IMP	Manx pound
    INR	Indian Rupee
    IQD	Iraqi Dinar
    IRR	Iranian Rial
    ISK	Icelandic Króna
    JEP	Jersey Pound
    JMD	Jamaican Dollar
    JOD	Jordanian Dinar
    JPY	Japanese Yen
    KES	Kenyan Shilling
    KGS	Kyrgystani Som
    KHR	Cambodian Riel
    KMF	Comorian Franc
    KPW	North Korean Won
    KRW	South Korean Won
    KWD	Kuwaiti Dinar
    KYD	Cayman Islands Dollar
    KZT	Kazakhstani Tenge""")
    info.grid(column=1,row=1)
    info=Label(ventana_info,text="""
    LAK	Laotian Kip
    LBP	Lebanese Pound
    LKR	Sri Lankan Rupee
    LRD	Liberian Dollar
    LSL	Lesotho Loti
    LTL	Lithuanian Litas
    LVL	Latvian Lats
    LYD	Libyan Dinar
    MAD	Moroccan Dirham
    MDL	Moldovan Leu
    MGA	Malagasy Ariary
    MKD	Macedonian Denar
    MMK	Myanma Kyat
    MNT	Mongolian Tugrik
    MOP	Macanese Pataca
    MRO	Mauritanian Ouguiya
    MUR	Mauritian Rupee
    MVR	Maldivian Rufiyaa
    MWK	Malawian Kwacha
    MXN	Mexican Peso
    MYR	Malaysian Ringgit
    MZN	Mozambican Metical
    NAD	Namibian Dollar
    NGN	Nigerian Naira
    NIO	Nicaraguan Córdoba
    NOK	Norwegian Krone
    NPR	Nepalese Rupee
    NZD	New Zealand Dollar
    OMR	Omani Rial
    PAB	Panamanian Balboa
    PEN	Peruvian Nuevo Sol
    PGK	Papua New Guinean Kina
    PHP	Philippine Peso
    PKR	Pakistani Rupee
    PLN	Polish Zloty
    PYG	Paraguayan Guarani
    QAR	Qatari Rial
    RON	Romanian Leu
    RSD	Serbian Dinar
    RUB	Russian Ruble
    RWF	Rwandan Franc
    SAR	Saudi Riyal
    SBD	Solomon Islands Dollar""")
    info.grid(column=2,row=1)
    info=Label(ventana_info,text="""
    SCR	Seychellois Rupee
    SDG	Sudanese Pound
    SEK	Swedish Krona
    SGD	Singapore Dollar
    SHP	Saint Helena Pound
    SLL	Sierra Leonean Leone
    SOS	Somali Shilling
    SRD	Surinamese Dollar
    STD	São Tomé and Príncipe Dobra
    SVC	Salvadoran Colón
    SYP	Syrian Pound
    SZL	Swazi Lilangeni
    THB	Thai Baht
    TJS	Tajikistani Somoni
    TMT	Turkmenistani Manat
    TND	Tunisian Dinar
    TOP	Tongan Paʻanga
    TRY	Turkish Lira
    TTD	Trinidad and Tobago Dollar
    TWD	New Taiwan Dollar
    TZS	Tanzanian Shilling
    UAH	Ukrainian Hryvnia
    UGX	Ugandan Shilling
    USD	United States Dollar
    UYU	Uruguayan Peso
    UZS	Uzbekistan Som
    VEF	Venezuelan Bolívar Fuerte
    VND	Vietnamese Dong
    VUV	Vanuatu Vatu
    WST	Samoan Tala
    XAF	CFA Franc BEAC
    XAG	Silver (troy ounce)
    XAU	Gold (troy ounce)
    XCD	East Caribbean Dollar
    XDR	Special Drawing Rights
    XOF	CFA Franc BCEAO
    XPF	CFP Franc
    YER	Yemeni Rial
    ZAR	South African Rand
    ZMK	Zambian Kwacha (pre-2013)
    ZMW	Zambian Kwacha
    ZWL	Zimbabwean Dollar""")
    info.grid(column=3,row=1)
def calculoDePrestamo():
    global count
    try:
        cantidadDelPrestamo=int(epes11.get())
        cantidadDePeriodos=int(epes12.get())
        tasa=int(epes13.get())
        tasaDeInteres=tasa/100
        opcion=tipoDeInteres.get()
        if opcion==1:
            cuotaMensual=round((tasaDeInteres*cantidadDelPrestamo)/(1-(1+tasaDeInteres)**-cantidadDePeriodos),2)
            monto_total=round(cuotaMensual*cantidadDePeriodos,2)
            intereses=round(monto_total-cantidadDelPrestamo,2)
            r11.config(text=f'{(cuotaMensual):,}')
            r22.config(text=f'{(monto_total):,}')
            r33.config(text=f'{(intereses):,}')
            aviso.config(text="")
            actual=f'"-P:{cantidadDelPrestamo} -M:{cantidadDePeriodos} -%:{tasa} Mensual = -*Mes:{cuotaMensual} -MT:{monto_total} -TI:{intereses}"'
            historial = open("historial.txt","a")
            historial.write(str(actual))
            historial.write(",")
            historial.close()
            table.insert(parent="",index="end",iid=count,text="",values=(actual))
            count=count+1
        elif opcion==2:
            tasaAnual=((1+tasaDeInteres)**(1/12))-1
            cuotaMensual=round((tasaAnual*cantidadDelPrestamo)/(1-(1+tasaAnual)**-cantidadDePeriodos),2)
            monto_total=round(cuotaMensual*cantidadDePeriodos,2)
            intereses=round(monto_total-cantidadDelPrestamo,2)
            r11.config(text=f'{(cuotaMensual):,}')
            r22.config(text=f'{(monto_total):,}')
            r33.config(text=f'{(intereses):,}')
            aviso.config(text="")
            actual=f'"-P:{cantidadDelPrestamo} -M:{cantidadDePeriodos} -%:{tasa} Anual = -*Mes:{cuotaMensual} -MT:{monto_total} -TI:{intereses}"'
            historial = open("historial.txt","a")
            historial.write(str(actual))
            historial.write(",")
            historial.close()
            table.insert(parent="",index="end",iid=count,text="",values=(actual))
            count=count+1
    except:
        aviso.config(text="Datos Faltantes",fg="red")
def calculodeinversion():
    global count
    try:
        i=int(inversion.get())
        tasa2=int(tasain.get())/100
        t=int(annos.get())
        mes= t*12
        mensual=i*tasa2
        ganancia=mensual*mes
        anual=ganancia/t
        ri1.config(text=f'{(mensual):,}')
        ri2.config(text=f'{(anual):,}')
        ri3.config(text=f'{(ganancia):,}')
        aviso.config(text="")
        actual=f'"-I:{i} -M:{t} -%:{tasa2} = -GM:{mensual} -GA:{anual} -GT:{ganancia}"'
        historial = open("historial.txt","a")
        historial.write(str(actual))
        historial.write(",")
        historial.close()
        table.insert(parent="",index="end",iid=count,text="",values=(actual))
        count=count+1
    except:
        aviso.config(text="Datos Faltantes",fg="red")
def light():
    global theme
    theme="light"
    root.destroy()
    main()
def dark():
    global theme
    theme="dark"
    root.destroy()
    main()
#-----------------------------------------------------------------------------------------------
rol()