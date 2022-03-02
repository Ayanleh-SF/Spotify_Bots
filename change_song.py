"""
	Change la musique jouée sur spotify
	Entrée : str(<nom de la musique>)
	Sortie : None	
"""
import psutil
from pywinauto import Desktop
from pywinauto.application import Application


def find_pid():
	for proc in psutil.process_iter():
		if proc.name() == "Spotify.exe":
			for k,v in proc.as_dict().items():
				if k == "cmdline" and v[0] == "Spotify.exe":
					spotify_pid = proc.as_dict()["pid"]

	return spotify_pid


def change(music_name):
	app = Application(backend="uia").connect(process=find_pid())

	search_entry = app.top_window().child_window(title="Artistes, titres ou podcasts", control_type="Edit")

	if search_entry.exists() == False:
		app.top_window().child_window(best_match="Rechercher").invoke()

	app.top_window().child_window(title="Artistes, titres ou podcasts", control_type="Edit").set_text(text=music_name)
	
	app.top_window().child_window(title="Résultats de la recherche de titres", control_type="Table").child_window(best_match="Plus d'options pour", control_type="MenuItem").invoke()

	app.top_window().child_window(title="Ajouter à la file d'attente", control_type="MenuItem").invoke()

	app.top_window().child_window(title="Suivant", control_type="Button").click()

	app.top_window().minimize()


change("runaway") # Entrer le nom de la musique souhaitée
