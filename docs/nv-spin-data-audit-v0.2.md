# AVI — Spin-force Datenprüfung: S8/S10/S11 v0.2
Stand: 2026-10-09

## Verifiziert
- Dryad DOI 10.5061/dryad.4xgxd25q4 nennt **ein** ZIP-Archiv (3,28 GB) mit Messdaten und Programmcode.
- FigS8: FRA-Textdateien (vertikal/horizontal, mit/ohne Magnet).
- FigS10: Roh-Zeitreihen je Magnetabstand als HDF5, Python->Excel->Mathematica->Kraftkurve.
- FigS11: HDF5-Zeitreihen mit/ohne Magnet, PSD-Berechnung.
- HDF5-Position in Metern, Zeit in Sekunden, Geschwindigkeit in m/s; 2,44 kHz Abtastrate.
Quelle: https://datadryad.org/dataset/doi:10.5061/dryad.4xgxd25q4

## Zugriff und Auditgrenze
README öffentlich lesbar, aber individueller Download der README-Datei via Web-Werkzeug liefert 403; die Messdaten befinden sich im 3,28-GB-ZIP. Daher **keine Datenpunkte geladen, keine Kurve fitbar und keine Magnetkontrollsignifikanz ermittelt**. Vorherige Zahlen zur Ersatzkraft sind parametrisierte H0-Beispiele, keine unabhängigen Reproduktionen.

## Auswertungsablauf
1. Archiv lokal herunterladen und nur `FigS8`, `FigS10`, `FigS11` extrahieren.
2. S8-Dateiformat und Einheiten inspizieren, dann `scripts/analyze_s8.py` mit expliziter Spalten- und Einheitenauswahl laufen lassen.
3. S8 Magnet-an/aus: nicht nur Kurvenhöhe, sondern f0, Q, Basislinie und Messkalibrierung vergleichen; Magnet kann auch mechanische Steifigkeit ändern.
4. S10: Position-Spuren mit Lock-in bei dokumentierter Pulsfrequenz und Block-Bootstrap auswerten; Kraftumrechnung über gemessenes Q und Puls-Grundwelle.
5. S11: gleiche PSD-Einheiten, Segmentlänge, Fensterung, Frequenzauflösung und Laserleistung; Resonanzsignal und Schätzerunsicherheit prüfen.
6. AVI-Test nur nach erfolgreichem H0- und Kontrollvergleich zulässig. Gegenwärtiger Status: Standardphysik-kompatibel, kein AVI-Residual.

## Methodenwarnung
S8-Auswerteskript ist für rohe amplitudenproportionale lineare Magnituden vorgesehen, **nicht** dB oder komplexe FRA-Transfers. Ohne Kopfzeilenkontrolle und Kalibration darf es nicht als vollständige Replikation gelten.
