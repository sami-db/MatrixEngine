import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
from Method.MethodGauss import inversion_gauss
from Method.MethodLaplace import *
from Matrice.Matrice import generer_matrice_aleatoire

 # definition du theme tkinter  pour le design
def configurer_theme():
    style = ttk.Style()
    style.theme_use('clam')

    couleur_fond = '#2D2D2D' 
    couleur_texte = '#E0E0E0'  
    couleur_primaire = '#3C3F41'  
    couleur_secondaire = '#5C93D1' 

    style.configure('.', background=couleur_fond, foreground=couleur_texte, font=('Helvetica', 10))
    style.configure('TButton', background=couleur_primaire, foreground=couleur_texte, borderwidth=1)
    style.configure('TProgressbar', background='lime', troughcolor=couleur_fond, bordercolor='black', lightcolor=couleur_secondaire, darkcolor=couleur_secondaire)
    style.map('TButton', background=[('active', couleur_secondaire)], foreground=[('active', couleur_texte)])
    
    style.configure('TScrolledText', background='white', foreground=couleur_texte)
    style.configure('TEntry', fieldbackground='white', foreground=couleur_fond)


# lancer le test (on utilise des threads séparer
# pour exeuter plusieurs fonctions en parallèle)
def run_tests():
    def task():
        btn_start['state'] = 'disabled'
        temps_max = int(entry_temps_max.get())  # on recup le temps saisi pas le user dans le text area (tentry)
        progress['value'] = 0
        set_text(txt_resultats, "", clear=True)

        def update_progression(etape, etapes_totales):
            valeur_progression = (etape / etapes_totales) * 100
            progress['value'] = valeur_progression
            fenetre.update_idletasks()
            insert_text(txt_resultats, f"Progression: Étape {etape}/{etapes_totales} complétée.\n")

        etapes_totales = 3
        try:
            update_progression(1, etapes_totales)
            n_gauss, temps_gauss = trouver_taille_max_gauss(update_progression, 2, temps_max)

            n_laplace, temps_laplace = trouver_taille_max_laplace(update_progression, 3, temps_max)
            
            # affichage des resultats dans un tableau

            insert_text(txt_resultats, "--- Résultats de la comparaison des temps de calcul ---\n")
            insert_text(txt_resultats, "| Méthode         | Taille maximale | Temps (s)   |\n")
            insert_text(txt_resultats, "|-----------------|-----------------|-------------|\n")
            insert_text(txt_resultats, f"| Gauss           | {n_gauss:<15}| {temps_gauss:<10.2f}|\n")
            insert_text(txt_resultats, f"| Laplace         | {n_laplace:<15}| {temps_laplace:<10.2f}|\n")
            insert_text(txt_resultats, "-------------------------------------------------------\n")

            message_base = "Étape 1: Recherche avec la méthode de Gauss : OK\nÉtape 2: Recherche avec la méthode de Laplace : OK\nÉtape 3: Affichage des résultats : OK"
            set_text(txt_loading, message_base, clear=True)

        finally:
            btn_start['state'] = 'normal'

    threading.Thread(target=task).start()

# insère le texte dans le text area
def insert_text(widget, texte):
    widget.config(state=tk.NORMAL)
    widget.insert(tk.END, texte)
    widget.config(state=tk.DISABLED)

# remplace le texete dans le text area
def set_text(widget, texte, clear=False):
    widget.config(state=tk.NORMAL)
    if clear:
        widget.delete('1.0', tk.END)
    widget.insert(tk.END, texte)
    widget.config(state=tk.DISABLED)

# methode de Gauss (temps_max = temps saisi par l'utilisateur)
def trouver_taille_max_gauss(update_progression, etape, temps_max):
    message_base = "Étape 1: Recherche avec la méthode de Gauss"
    insert_text(txt_loading, f"{message_base}...\n")
    n = 1
    debut_recherche = time.time()
    while True:
        animation_texte = message_base + "." * (n % 4) + "\n"
        set_text(txt_loading, animation_texte, clear=True)

        matrice = generer_matrice_aleatoire(n)
        inversion_gauss(matrice)
        temps_ecoule = time.time() - debut_recherche
        if temps_ecoule > temps_max:
            insert_text(txt_resultats, f"Taille maximale trouvée: {n - 1}\n\n")
            update_progression(etape, 3)
            return n - 1, temps_ecoule
        n += 1

# methode de Laplace (temps_max = temps saisi par l'utilisateur)
def trouver_taille_max_laplace(update_progression, etape, temps_max):
    message_base = "Étape 1: Recherche avec la méthode de Gauss : OK\nÉtape 2: Recherche avec la méthode de Laplace"
    insert_text(txt_loading, f"{message_base}...")
    n = 1
    debut_recherche = time.time()
    while True:
        animation_texte = message_base + "." * (n % 4) + "\n"
        set_text(txt_loading, animation_texte, clear=True)

        matrice = generer_matrice_aleatoire(n)
        determinant_laplace(matrice)
        temps_ecoule = time.time() - debut_recherche
        if temps_ecoule > temps_max:
            insert_text(txt_resultats, f"Taille maximale trouvée: {n - 1}\n\n")
            update_progression(etape, 3)
            return n - 1, temps_ecoule
        n += 1




# créer l'interface tkinter
fenetre = tk.Tk()
fenetre.title("MatrixEngine for Gauss & Laplace")

# appliquer le theme
configurer_theme()

# ajouter les elements dans l'interface graphique
cadre = ttk.Frame(fenetre, padding="30 15 30 15")
cadre.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
fenetre.columnconfigure(0, weight=1)
fenetre.rowconfigure(0, weight=1)

# titre
titre_projet = ttk.Label(cadre, text="Comparaison des méthodes Gauss et Laplace pour l'inversion de matrice", font=("TkDefaultFont", 16))
titre_projet.grid(row=0, column=0, columnspan=4, pady=3, sticky=tk.N)

# noms
label_participant = ttk.Label(cadre, text="Sami - Antoine")
label_participant.grid(row=1, column=1, columnspan=2, pady=(5, 30), sticky=tk.N)

# espacement pour séparer l'entête du corps
vide = ttk.Label(cadre, text="")
vide.grid(row=1, column=2, columnspan=2, pady=3, sticky=tk.N)

# Label et text input pour saisir le temps max 
label_temps_max = ttk.Label(cadre, text="Temps max (s):")
label_temps_max.grid(row=3, column=1, columnspan=1, padx=5, sticky=tk.E)

entry_temps_max = ttk.Entry(cadre)
entry_temps_max.grid(row=3, column=2, padx=5, sticky=tk.W)
entry_temps_max.insert(0, "300")  # Valeur par défaut

# bouton start
btn_start = ttk.Button(cadre, text="Lancer le test", command=run_tests)
btn_start.grid(row=4, column=1, columnspan=2, pady=10, padx=5, sticky=tk.EW)

# bar de progression
progress = ttk.Progressbar(cadre, orient=tk.HORIZONTAL, length=100, mode='determinate')
progress.grid(row=5, column=0, columnspan=4, pady=20, sticky=tk.EW)

# text area pour afficher etape
txt_loading = scrolledtext.ScrolledText(fenetre, undo=True, width=70, height=3)
txt_loading.grid(row=6, column=0, sticky=(tk.EW))
txt_loading.config(state=tk.DISABLED)

# text area pour afficher résultats
txt_resultats = scrolledtext.ScrolledText(fenetre, undo=True, width=70, height=15)
txt_resultats.grid(row=7, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))
txt_resultats.config(state=tk.DISABLED)

# centrer les éléments
for i in range(4):
    cadre.columnconfigure(i, weight=1)
fenetre.rowconfigure(0, weight=1)

fenetre_width = fenetre.winfo_reqwidth()
fenetre_height = fenetre.winfo_reqheight()
position_right = int(fenetre.winfo_screenwidth() / 2 - fenetre_width / 2)
position_down = int(fenetre.winfo_screenheight() / 2 - fenetre_height / 2)
fenetre.geometry("+{}+{}".format(position_right, position_down))

fenetre.mainloop()