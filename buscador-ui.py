import main
import configuracion as conf
import tkinter as tk
from tkinter import font
from PIL import Image
from PIL import ImageTk

app = tk.Tk()
app.title("BuscadorGitHubRepos")
width = '605'
height = '560'
app.geometry(width + 'x' + height)
app.resizable(False, False)

# STATE (Credenciales)
user_state = tk.StringVar()
token_state = tk.StringVar()
# STATE (Filtros Query)
lenguaje_state = tk.StringVar()
stars_state = tk.StringVar()
forks_state = tk.StringVar()
created_state = tk.StringVar()
pushed_state = tk.StringVar()
archivedCheck_state = tk.BooleanVar()
publicCheck_state = tk.BooleanVar()
# STATE (Variables de configuración)
nRandomRepos_state = tk.IntVar()
nLapseRepos_state = tk.IntVar()
buscarEnLocalCheck_state = tk.BooleanVar()
generarListaReposCheck_state = tk.BooleanVar()
randomizarReposCheck_state = tk.BooleanVar()
clonarReposCheck_state = tk.BooleanVar()
doExcelCheck_state = tk.BooleanVar()
doCsvCheck_state = tk.BooleanVar()
scriptLapseExeCheck_state = tk.BooleanVar()

def exe():
    print("Ejecutando proceso desde buscador-UI")
    # Filtros Query:
    conf.FiltrosQuery.language = lenguaje_state.get().lower()
    conf.FiltrosQuery.stars = stars_state.get()
    conf.FiltrosQuery.forks = forks_state.get()
    conf.FiltrosQuery.created = created_state.get()
    conf.FiltrosQuery.pushed = pushed_state.get()

    if archivedCheck_state.get():
        conf.FiltrosQuery.qIs = "true"
    else:
        conf.FiltrosQuery.qIs = "false"

    if publicCheck_state.get():
        conf.FiltrosQuery.qIs = "public"
    else:
        conf.FiltrosQuery.qIs = "private"

    # Configuración
    conf.Configuracion.buscarEnLocal = buscarEnLocalCheck_state.get()
    conf.Configuracion.generarListaRepos = generarListaReposCheck_state.get()
    conf.Configuracion.randomizarListaRepos = randomizarReposCheck_state.get()
    conf.Configuracion.lapseExe = False
    conf.Configuracion.clonarRepositorios = clonarReposCheck_state.get()
    conf.Configuracion.doExcel = doExcelCheck_state.get()
    conf.Configuracion.doCsv = doCsvCheck_state.get()
    conf.Configuracion.N_RANDOM = nRandomRepos_state.get()
    conf.Configuracion.N_LAPSE_REPOS = 0
    main.exe()

def randomizarReposCheck_clicked():
    if randomizarReposCheck_state.get():
        nRandomRepos_state.set(conf.Configuracion.N_RANDOM)
        nRandomRepos.config(state=tk.NORMAL)
    else:
        nRandomRepos_state.set(0)
        nRandomRepos.config(state=tk.DISABLED)

row = 0

# LOGO URJC
logoUrjcWidth = 120
logoUrjcHeight = 60
img = Image.open("imgs/logo_urjc2.png")
img = img.resize((logoUrjcWidth,logoUrjcHeight), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
widget = tk.Label(app, image=photoImg)
widget.grid(column=0, row=row)
titleAppLbl = tk.Label(app, text="BuscadorGitHubRepos", font=('Helvetica', 18, 'bold'))
titleAppLbl.grid(column=1, row=row)
f = font.Font(titleAppLbl, titleAppLbl.cget("font"))
f.configure(underline=True)
titleAppLbl.configure(font=f)
row+=1

# CREDENCIALES
credencialesLbl = tk.Label(app, text="CREDENCIALES")
credencialesLbl.grid(column=0, row=row)
f = font.Font(credencialesLbl, credencialesLbl.cget("font"))
f.configure(underline=True)
credencialesLbl.configure(font=f)
row+=1

userLbl = tk.Label(app, text="Usuario: ")
userLbl.grid(column=0, row=row)
user_state.set(conf.Configuracion.user)
user = tk.Entry(app,width=15, textvariable=user_state)
user.grid(column=1, row=row)
row+=1

tokenLbl = tk.Label(app, text="Token: ")
tokenLbl.grid(column=0, row=row)
token_state.set(conf.Configuracion.token)
token = tk.Entry(app,width=35, textvariable=token_state)
token.grid(column=1, row=row)
row+=1

# FILTROS QUERY
filtrosQueryLbl = tk.Label(app, text="FILTROS QUERY")
filtrosQueryLbl.grid(column=0, row=row)
f = font.Font(filtrosQueryLbl, filtrosQueryLbl.cget("font"))
f.configure(underline=True)
filtrosQueryLbl.configure(font=f)
row+=1

# LENGUAJE
lenguajeLbl = tk.Label(app, text="Lenguaje: ")
lenguajeLbl.grid(column=0, row=row)
lenguaje_state.set(conf.FiltrosQuery.language)
lenguaje = tk.Entry(app,width=15, textvariable=lenguaje_state)
lenguaje.grid(column=1, row=row)
row+=1

# STARS
starsLbl = tk.Label(app, text="Stars: ")
starsLbl.grid(column=0, row=row)
stars_state.set(conf.FiltrosQuery.stars)
stars = tk.Entry(app,width=15, textvariable=stars_state)
stars.grid(column=1, row=row)
row+=1

# FORKS
forksLbl = tk.Label(app, text="Forks: ")
forksLbl.grid(column=0, row=row)
forks_state.set(conf.FiltrosQuery.forks)
forks = tk.Entry(app,width=15, textvariable=forks_state)
forks.grid(column=1, row=row)
row+=1

# CREATED
createdLbl = tk.Label(app, text="Created: ")
createdLbl.grid(column=0, row=row)
created_state.set(conf.FiltrosQuery.created)
created = tk.Entry(app,width=15, textvariable=created_state)
created.grid(column=1, row=row)
row+=1

# PUSHED
pushedLbl = tk.Label(app, text="Pushed: ")
pushedLbl.grid(column=0, row=row)
pushed_state.set(conf.FiltrosQuery.pushed)
pushed = tk.Entry(app,width=15, textvariable=pushed_state)
pushed.grid(column=1, row=row)
row+=1

# ARCHIVED
archivedLbl = tk.Label(app, text="Archived ")
archivedLbl.grid(column=0, row=row)
archivedCheck_state.set(False)
archivedCheck = tk.Checkbutton(app, var=archivedCheck_state)
archivedCheck.grid(column=1, row=row)
archivedCheck.config(state=tk.DISABLED)
row+=1

# PUBLIC
publicLbl = tk.Label(app, text="Public")
publicLbl.grid(column=0, row=row)
publicCheck_state.set(True)
publicCheck = tk.Checkbutton(app, var=publicCheck_state)
publicCheck.grid(column=1, row=row)
publicCheck.config(state=tk.DISABLED)
row+=1

# VARIABLES DE CONFIGURACIÓN
configuracionLbl = tk.Label(app, text="VARIABLES DE CONFIGURACIÓN")
configuracionLbl.grid(column=0, row=row)
f = font.Font(configuracionLbl, configuracionLbl.cget("font"))
f.configure(underline=True)
configuracionLbl.configure(font=f)
row+=1

# BUSCAR REPOS EN LOCAL
buscarEnLocalReposLbl = tk.Label(app, text="Buscar repos en LOCAL")
buscarEnLocalReposLbl.grid(column=0, row=row)
#buscarEnLocalReposLbl.pack()
buscarEnLocalCheck_state.set(conf.Configuracion.buscarEnLocal)
buscarEnLocalCheck = tk.Checkbutton(app, var=buscarEnLocalCheck_state)
buscarEnLocalCheck.grid(column=1, row=row)
#buscarEnLocalCheck.pack()
row+=1

# GENERAR LISTA REPOS
generarListaReposLbl = tk.Label(app, text="Generar lista repos ('.pickle')")
generarListaReposLbl.grid(column=0, row=row)
#generarListaReposLbl.pack()
generarListaReposCheck_state.set(conf.Configuracion.generarListaRepos)
generarListaReposCheck = tk.Checkbutton(app, var=generarListaReposCheck_state)
generarListaReposCheck.grid(column=1, row=row)
#generarListaReposCheck.pack()
row+=1

# ScriptLapseExe
scriptLapseExeLbl = tk.Label(app, text="Ejecutar mediante 'ScriptLapseExe'")
#scriptLapseExeLbl.grid(column=0, row=row)
#scriptLapseExeLbl.pack()
scriptLapseExeCheck_state.set(conf.Configuracion.lapseExe)
scriptLapseExeCheck = tk.Checkbutton(app, var=scriptLapseExeCheck_state)
#scriptLapseExeCheck.grid(column=1, row=row)
#scriptLapseExeCheck.pack()
#row+=1

# Nº LAPSE REPOS
#nLapseReposLbl = tk.Label(app, text="Nº lapse repos: ")
#nLapseReposLbl.grid(column=0, row=row)
#nLapseReposLbl.pack()
nLapseRepos_state.set(conf.Configuracion.N_LAPSE_REPOS)
nLapseRepos = tk.Entry(app,width=5, textvariable=nLapseRepos_state)
#nLapseRepos.grid(column=2, row=row)
#nLapseRepos.pack()
row+=1

# RANDOMIZAR REPOSITORIOS
randomizarReposLbl = tk.Label(app, text="Randomizar repositorios")
randomizarReposLbl.grid(column=0, row=row)
#randomizarReposLbl.pack()
randomizarReposCheck_state.set(conf.Configuracion.randomizarListaRepos)
randomizarReposCheck = tk.Checkbutton(app, var=randomizarReposCheck_state, command=randomizarReposCheck_clicked)
randomizarReposCheck.grid(column=1, row=row)
#randomizarReposCheck.pack()

# Nº REPOS RANDOM
#nRandomReposLbl = tk.Label(app, text="Nº repos random: ")
#nRandomReposLbl.grid(column=0, row=row)
#nRandomReposLbl.pack()
nRandomRepos_state.set(conf.Configuracion.N_RANDOM)
nRandomRepos = tk.Entry(app,width=5, textvariable=nRandomRepos_state)
nRandomRepos.grid(column=2, row=row)
#nRandomRepos.pack()
row+=1

# CLONAR REPOSITORIOS
clonarReposLbl = tk.Label(app, text="Clonar repositorios resultantes")
clonarReposLbl.grid(column=0, row=row)
#clonarReposLbl.pack()
clonarReposCheck_state.set(conf.Configuracion.clonarRepositorios)
clonarReposCheck = tk.Checkbutton(app, var=clonarReposCheck_state)
clonarReposCheck.grid(column=1, row=row)
#clonarReposCheck.pack()
row+=1

# DO EXCEL
doExcelLbl = tk.Label(app, text="Generar Excel")
doExcelLbl.grid(column=0, row=row)
#doExcelLbl.pack()
doExcelCheck_state.set(conf.Configuracion.doExcel)
doExcelCheck = tk.Checkbutton(app, var=doExcelCheck_state)
doExcelCheck.grid(column=1, row=row)
#doExcelCheck.pack()
row+=1

# DO CSV
doCsvLbl = tk.Label(app, text="Generar Csv")
doCsvLbl.grid(column=0, row=row)
#doCsvLbl.pack()
doCsvCheck_state.set(conf.Configuracion.doCsv)
doCsvCheck = tk.Checkbutton(app, var=doCsvCheck_state)
doCsvCheck.grid(column=1, row=row)
#doCsvCheck.pack()
row+=1

# BOTÓN EJECUTAR
exeButton = tk.Button(app, text="EJECUTAR", fg="green",  command=exe)
#exeButton.pack()
exeButton.grid(column=1, row=row)
row+=1

#buscarEnLocalCheck_clicked()
randomizarReposCheck_clicked()

app.mainloop()
