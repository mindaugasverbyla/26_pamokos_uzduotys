
import os
from datetime import datetime

def zurnalo_irasas(zinute):
    zurnalo_katalogas = "projects/logs"
    zurlano_dokumentas = zurnalo_katalogas+'/zurnalas.log'
    if not os.path.exists(zurnalo_katalogas):
        os.makedirs(zurnalo_katalogas)
    with open(zurlano_dokumentas, "a") as zurnalas:
        zurnalas.write(f"{datetime.now()} - {zinute}\n")

pagrindinis_katalogas = "projects"
kelias = pagrindinis_katalogas
if not os.path.exists(kelias):
    os.mkdir(pagrindinis_katalogas)
    zurnalo_irasas(f"Katalogas sukurtas: {kelias}")

vidiniai_katalogai = ["data", "scripts", "logs"]

for katalogas in vidiniai_katalogai:
     kelias = pagrindinis_katalogas+'/'+katalogas
     if not os.path.exists(kelias):
        os.mkdir(kelias)
        zurnalo_irasas(f"Katalogas sukurtas: {kelias}")

# Kuriam README
kelias = pagrindinis_katalogas+'/README.md'
turinys = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"

if not os.path.exists(kelias):
    with open(kelias, "w") as file:
        file.write(turinys)
        zurnalo_irasas(f"Dokumentas sukurtas: {kelias}")

for katalogas in vidiniai_katalogai:
    kelias = pagrindinis_katalogas+'/'+katalogas
    if os.path.exists(kelias):
        print(f"Katalogas egzistuoja: {kelias}: {os.path.exists(kelias)}")

kelias = pagrindinis_katalogas+'/README.md'
print(f"README.md egzistuoja: {kelias}: {os.path.exists(kelias)}")