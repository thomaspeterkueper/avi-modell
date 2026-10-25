# AVI-MODEL-MISSPECIFICATION-0001 — Scheinresiduen durch unvollständige Modelle
Datum: 2026-10-25. **Status: numerisches BASELINE-Experiment; kein AVI-Nachweis.**

## Frage
Kann das Weglassen einer gewöhnlichen Zustandsvariablen einen überzeugenden scheinbaren Zusatzterm erzeugen?

## Daten
Wahre synthetische Dynamik: x'=v, v'=-x-0.4v+0.3h, h'=-0.5h; initial (0.7,-0.2,1). Messung: y(t)=x(t)+epsilon, epsilon~N(0,0.01²), Seed 1729. Zeiten 0..10 in 0.25-Schritten, Training t<=5, zeitlich zurückgehaltene Validierung t>5. Geschlossene Matrixexponential-Lösung scipy.linalg.expm als Vorwärtsmodell.

## Kandidaten
1. Reduziertes zweidimensionales Modell x''+gamma*x'+omega²*x=0, freie x0,v0,gamma,omega².
2. Erweitertes zweidimensionales Modell mit gefittetem exponentiell abklingendem Antrieb a*exp(-kt), freie x0,v0,gamma,omega²,a,k. Die Erweiterung dient ausschließlich als **analoges scheinbares AVI-Residual**, ist selbst aber eine gewöhnliche Standard-Dynamik; keinesfalls AVI-Fundamentalphysik.
3. Vollständige Baseline mit **bekannter wahrer** 3x3-Dynamik und durch lineare Ausgleichung angepasstem Anfangszustand. Diese Kenntnis ist bewusst ein günstiger Orakel-Vergleich und in realen Datensätzen nicht vorauszusetzen.

## Auswertung
| Modell | Trainings-RMSE | Validierungs-RMSE |
|---|---:|---:|
| Reduziert | 0.0201003 | 0.0597428 |
| Scheinzusatz | 0.0074246 | 0.0182013 |
| Vollständige Referenz | 0.0080485 | 0.0105241 |

Reproduzierbarkeit: Python, numpy, scipy; least_squares mit begrenzten Parametern, deterministischer Startpunkt und Seed. Resultate gelten nur für den gewählten Versuch und die zeitliche Aufteilung.

## Entscheidung
**PASS: Demonstration von Modellfehlanpassung.** Ein zusätzlicher Term kann den Trainingsfehler erheblich senken, ohne neue Physik zu repräsentieren. Im vorliegenden Fall generalisiert die vollständige Standardreferenz besser. Die geringfügig bessere Trainingsanpassung des Zusatzeffekts unterstreicht das Risiko flexibler Parameterisierung.

**Einschränkungen:** Die Vollmodellstruktur ist im Experiment bekannt. Extrapolation über ein einziges Zeitfenster und einen Seed ist kein belastbarer wissenschaftlicher Modellvergleich. Ergänzend nötig: mehrere Seeds, Out-of-distribution-Tests, Regularisierung, parametergleiche Kontrollen, Residuen-Autokorrelation, Bayesianische Modellprüfung, unabhängige Messkanäle.

## Konsequenz für AVI
Vor der Interpretation eines Residuums als AVI-Effekt müssen Referenzmodell-Vollständigkeit, Störgrößen, Messkalibration und Alternativerklärungen geprüft werden. Ein AVI-spezifischer Test verlangt eine unabhängige präregistrierte Kopplungs-/Residualvorhersage gegen QFT+GR, nicht lediglich einen frei fitbaren Zusatz.

Verknüpft mit AVI-OBSERVABILITY-0001/0002 und AVI→NOXIA Executable Interface.
