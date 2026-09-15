---
id: EXT-OTA-AVI-20260915-frb-baryon-observation-channel
title: FRB-Dispersionsmaße als unabhängigen Beobachtungskanal aufnehmen
status: done
source: OTA
target: AVI
created: 2026-09-15
completed: 2026-09-15
priority: medium
sourceDocuments:
  - OTA-SCI-0092-2026-DE
---

# FRB-Dispersionsmaße als unabhängigen Beobachtungskanal aufnehmen

## Übernommener Befund

`OTA-SCI-0092-2026-DE` dokumentiert den peer-reviewten Nature-Astronomy-Befund von Sharma et al. (2026), der Dispersionsmaße von 114 lokalisierten Fast Radio Bursts als Sonde der baryonischen Materieverteilung und feedbackbedingter Unterdrückung der Materieclusterung verwendet.

## Umsetzung in AVI

Die AVI-Beobachtungs-Testmatrix wurde auf v0.2 erweitert und enthält nun:

`OBS-06 — FRB / baryonische Materieverteilung`.

Der Kanal wird als externer, physikalisch unabhängiger Constraint geführt. Er erweitert die empirische Bestimmung des Standardzustands und seiner Entwicklung, ohne als AVI-spezifische Evidenz interpretiert zu werden.

## Evidenzgrenze

FRB-Dispersionsmaße integrieren Elektronendichte entlang vergangener Lichtwege. Diese historische Integration der Beobachtungsgröße ist nicht gleichbedeutend mit einem fundamentalen Gedächtniszustand bei identischem Gegenwartszustand.

Daher folgt aus OBS-06 weder Evidenz für `xi` noch für `Phi(a)` und kein positiver Test B.

## Erfüllte Akzeptanzkriterien

- [x] FRB als eigener Beobachtungskanal in der AVI-Testmatrix geführt.
- [x] Bezug zu `OTA-SCI-0092-2026-DE` dokumentiert.
- [x] primäre Messgröße und benötigte AVI-Abbildung beschrieben.
- [x] baryonische/astrophysikalische Hauptsystematiken sichtbar gemacht.
- [x] integrierte Sichtlinieninformation von AVI-Historienabhängigkeit getrennt.
- [x] Test B bleibt eigenständig und erfordert eine messbare Observable.

## Nächster Schritt

Kein unmittelbarer AVI-Fit. Zuerst muss der dynamische Closure-Vertrag eine konkrete physikalische AVI-Wirkung und daraus eine berechenbare Observable festlegen. Erst dann ist zu entscheiden, ob OBS-06 direkt sensitiv auf diese Wirkung ist oder primär als Kontroll-/Nuisance-Kanal dient.
