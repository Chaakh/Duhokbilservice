# Duhok Bilservice

Webbplats för Duhok Bilservice, Hildedalsgatan 62, 417 05 Göteborg.

En enda sida: `index.html`. Ingen byggkedja, inga beroenden — fotot ligger i
`bilder/`, allt annat är inbakat i filen. Öppna den i en webbläsare så syns
sidan som den är.

## Publicering

Sidan ligger på GitHub Pages och uppdateras av sig själv när `main` ändras.

## build-artifact.py

Bygger en variant för förhandsvisning som Claude-artefakt: skalar bort
`<html>`/`<head>`/`<body>` och bakar in bilderna som data-URI:er. Behövs inte
för Pages — bara för att kunna dela ett utkast innan det läggs upp.

    python build-artifact.py index.html out.html

## Innan sidan sprids till kunder

Öppettider, priser och kontaktuppgifter är ännu inte bekräftade av
verkstaden. Listan över det som måste stämmas av ligger i `ATT-BEKRAFTA.md`,
som med flit hålls utanför det här publika repot.
