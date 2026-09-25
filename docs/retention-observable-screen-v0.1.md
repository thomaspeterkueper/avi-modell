# AVI — Retention Observable Screen v0.1

**Stand:** 25. September 2026
**Status:** Messarchitektur-Screening
**Voraussetzung:** Information-Retention Screen v0.1

## 1. Ziel

Gesucht wird keine Anomalie, sondern eine Beobachtungsarchitektur, die zusätzliche Historienabhängigkeit IR-3 von bekannten Retentionsmechanismen IR-1/IR-2 unterscheiden könnte. Ein Kanal ist nur AVI-tauglich, wenn Standardphysik als explizites Nullmodell formulierbar ist und AVI vor dem Fit eine andere quantitative Relation liefert.

## 2. Kriterien

Kandidaten werden nach dimensionsloser/normierbarer Observable, unabhängiger Kontrolle des lokalen Zustands, unabhängiger Historien-/Globalinformation, Standardmodellierung von IR-1/IR-2, Wiederholbarkeit und präregistrierbarer AVI-Abweichung geprüft.

## 3. RO-1 — optische/atomare Frequenzverhältnisse

O_ij = nu_i / nu_j.

Stärken: intrinsisch dimensionslos; verschiedene Systeme besitzen verschiedene Sensitivitätskoeffizienten; moderne Vergleiche erreichen Unsicherheiten von wenigen 10^-18; etablierte Analysen testen variable fundamentale Konstanten, skalare Felder und Äquivalenzprinzipverletzungen.

Problem: Eine Abweichung ist nicht automatisch Historienretention. Bekannte Felder, Umwelt, Gravitation und Systematiken können dieselbe Messklasse beeinflussen.

**IR-3-Trennschärfe:** mittel.  
**Rolle:** stärkster lokaler Präzisionskanal, benötigt aber eine unabhängig definierte Globalvariable.

## 4. RO-2 — kontrollierte hysteretische/nicht-Markovsche Quantensysteme

Identische gegenwärtige Kontrollparameter werden bei bewusst unterschiedlicher Präparation verglichen. Dies ist ein sehr guter Blind-/Negativkontrolltest dafür, ob eine Analyse bekannte interne Zustandsinformation fälschlich als IR-3 klassifiziert.

**IR-3-Trennschärfe als Naturtest:** gering.  
**Methodischer Wert:** hoch.

## 5. RO-3 — kosmologische Fossilien

CMB, primordial erzeugte Strukturen, Nukleosynthese und großskalige Materieverteilung tragen reale Information über frühere kosmische Zustände. Diese Information ist zunächst IR-1/IR-2, weil Standardkosmologie ihre Entwicklung modelliert.

**IR-3-Trennschärfe:** gering bis mittel.  
**Rolle:** historische Referenz/Konsistenzprüfung.

## 6. RO-4 — global-context-sensitive QFT response

G_global -> W(x,x') -> local response.

Der Mechanismus ist bereits Standard-QFT und daher zwingendes Nullmodell jeder AVI-Behauptung über global-to-local coupling.

**IR-3-Trennschärfe:** gering.  
**Rolle:** Nullmodell.

## 7. RO-5 — unabhängige kosmologische Expansions-/Distanzkanäle

SNe Ia, BAO, cosmic chronometers, standard sirens, strong-lensing time delays und ergänzend FRB-basierte Struktur-/Baryoninformation besitzen unterschiedliche Abhängigkeiten von Kalibration, Astrophysik, Geometrie und integrierter Expansionsgeschichte.

Mehrere unabhängige Wege können dieselbe Hintergrundbeschreibung testen und Degeneranzen/Systematiken brechen. Unterschiedliche historische Sensitivität ist jedoch noch kein starker Test B.

**IR-3-Trennschärfe:** mittel als Konsistenzarchitektur.  
**Rolle:** bester kosmologischer Multi-Channel-Referenzsatz.

## 8. RO-6 — Cross-Domain-Kombination

Die stärkste zukünftige Architektur kombiniert einen lokalen dimensionslosen Kanal mit unabhängig bestimmter kosmologischer Information:

local: O_ij = nu_i/nu_j  
global: X_cos aus kosmologischen Proben.

Nullhypothese:
O_ij folgt QFT+GR/SM nach Entfernung bekannter lokaler Kopplungen.

AVI-Testhypothese:
delta ln O_ij = lambda K_ij X_cos

mit vorab definiertem X_cos, unabhängig bestimmtem K_ij, einem gemeinsamen lambda, mehreren Transitionspaaren und keiner nachträglichen Auswahl.

**IR-3-Trennschärfe:** potentiell hoch.  
**Status:** noch keine AVI-Hypothese, weil X_cos nicht physikalisch ausgewählt ist.

## 9. Rollen

- lokaler Präzisionssensor: RO-1
- methodische Negativkontrolle: RO-2
- historische Standardreferenz: RO-3
- global-to-local Nullmodell: RO-4
- kosmologische unabhängige Referenz: RO-5
- eigentliche AVI-Testarchitektur: RO-6

Keiner dieser Kanäle liefert derzeit IR-3-Evidenz.

## 10. Test R — Retention Relation

Gegeben sind vollständig modellierte lokale Standardzustände L, eine unabhängig beobachtete globale/kosmologische Variable X und mehrere lokale dimensionslose Responsekanäle O_k.

H0: O_k = O_k,std(L)

gegen

H_R: ln(O_k/O_k,std) = lambda K_k X.

Dieser Test behauptet nicht, zwei identische Universen mit verschiedener Vergangenheit zu erzeugen. Er testet eine reproduzierbare relationale Kopplung zwischen unabhängiger globaler Information und lokalen Responsekanälen.

## 11. Schutzregeln

1. X wird nicht aus lokalen Residuen konstruiert.
2. K_k wird nicht auf Residuen optimiert.
3. Ein einziges lambda gilt kanalübergreifend.
4. Mindestens zwei physikalisch verschiedene lokale Kanäle sind erforderlich.
5. Standardfelder und Umweltkopplungen werden explizit modelliert.
6. Nullresultate bleiben im Test.
7. Kosmologische Unsicherheit in X wird propagiert.
8. Ein positives Test-R-Ergebnis wäre zunächst eine neue empirische Relation, kein Beweis kosmischen Gedächtnisses.

## 12. Aktuelle Messrealität

Optische Frequenzvergleiche von Al+, Yb und Sr erreichten 2026 Gesamtunsicherheiten von höchstens etwa 3.2 × 10^-18. Uhren werden bereits als Sensoren für hypothetische skalare Felder, Variationen fundamentaler Konstanten und Äquivalenzprinzipverletzungen untersucht.

Diese Empfindlichkeit ist **keine AVI-Grenze**, solange AVI keine konkrete Kopplung definiert.

## 13. Entscheidung

Retention Observable Screen:

- measurable architectures = YES
- IR-3 discriminator in principle = YES
- AVI-specific driver X = NOT DEFINED
- AVI data fit = BLOCKED

Wir besitzen damit eine experimentell sinnvolle Form, ohne xi oder Phi ontologisch vorauszusetzen.

## 14. Nächster Gate-Test

Es folgt ein **Global-Driver Screen** für X.

Kandidaten müssen unabhängig messbar, dimensionslos/natürlich normierbar, physikalisch klar und präregistrierbar sein. Sie dürfen nicht bloß Zeit/Rotverschiebung umbenennen oder bereits vollständig der lokale QFT/GR-Carrier sein.

Zu prüfen:
- Expansionsform q(a) bzw. -d ln H/dN;
- dimensionslose Dichteanteile Omega_i(a);
- global/topologische diskrete Information;
- unabhängig rekonstruierte integrierte Expansionsgrößen;
- keine frei geformten History-Kernel.

## 15. Epistemischer Status

- **[R]** Präzisionsuhren liefern extrem genaue dimensionslose Frequenzverhältnisse und werden für Tests neuer Physik verwendet.
- **[R]** Kosmologische Proben besitzen komplementäre Abhängigkeiten von Expansionsgeschichte und Systematiken.
- **[D]** Eine Cross-Domain-Architektur kann IR-3 prinzipiell besser von lokalen Standardmechanismen trennen als ein einzelner Kanal.
- **[H]** Eine gemeinsame AVI-Relation zwischen unabhängigem globalem X und lokalen Frequenzverhältnissen könnte existieren.
- **[I]** Keine der betrachteten Beobachtungen ist Evidenz für eine solche Relation.
