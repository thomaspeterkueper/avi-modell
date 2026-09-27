# AVI — Core Formalization v0.2

**Stand:** 27. September 2026
**Status:** formaler Kernvertrag; v0.2 nach Core Stress-Test
**Voraussetzung:** Core Invariant Reconstruction Gate v0.1

## 1. Ziel

Diese Fassung formalisiert den minimalen AVI-Kern ohne ξ, Φ, Memory-Kernel, X_global oder konkrete neue Kopplung. Sie definiert keinen neuen physikalischen Mechanismus. Sie legt fest, wann eine Behauptung zusätzlicher Zustands- oder Historieninformation überhaupt zulässig wird.

## 2. Objekte

Sei M_std das vollständig spezifizierte Standardmodell für den betrachteten Testbereich.

Der relevante Standardzustand am Vergleichszeitpunkt t* sei

    Ω = (Y, B, G, C),

mit Y = lokale/interne Standardfreiheitsgrade, B = relevante Rand-/Anfangsbedingungen, G = relevante globale/topologische/Quantenzustandsinformation und C = Messkanal, Apparat, Umgebung, Selektion und Response.

Diese Zerlegung ist funktional, nicht ontologisch fundamental.

## 3. Daten und Rekonstruktion

Für Beobachtungsdaten D gilt

    R_M : D -> P(Ω | D, M_std).

Die Rekonstruktion ist im Allgemeinen eine Verteilung über Zustände. Eine Punktschätzung Ω_hat darf sie nur ersetzen, wenn gezeigt wird, dass die verlorene Zustandsunsicherheit für die Zielobservable vernachlässigbar ist.

## 4. Standard-Prädiktor

    P_std(O | D, M_std)
      = integral dΩ P_std(O | Ω, M_std) P(Ω | D, M_std).

Alle relevanten Korrelationen zwischen Komponenten von Ω müssen erhalten bleiben.

## 5. Zwei Ebenen der Zustandsäquivalenz

### 5.1 Q-bezogene prädiktive Äquivalenz

Zwei Fälle A und B sind bezüglich einer vorab definierten Observablenfamilie Q prädiktiv äquivalent,

    Ω_A ~_Q Ω_B,

genau dann, wenn für alle q in Q gilt

    P_std(q | Ω_A, M_std) = P_std(q | Ω_B, M_std).

Diese Relation ist observablenbezogen und darf nicht als vollständige physikalische Zustandsidentität interpretiert werden.

### 5.2 Starke Standardzustandsäquivalenz

Für starke Same-State-/History-Tests definieren wir

    Ω_A ≡_std Ω_B

nur dann, wenn alle unter M_std für die getestete Dynamik relevanten lokalen/internen Zustandsgrößen Y, Randdaten B, globalen Daten G und Kanalzustände C gleich sind oder ihre verbleibende Unsicherheit explizit gemeinsam marginalisiert wird.

Damit gilt

    ≡_std  =>  ~_Q

für korrekt spezifiziertes M_std und Q, aber nicht notwendig umgekehrt.

Ein Strong History Test verlangt ≡_std. Die schwächere Relation ~_Q dient Vorhersage- und Messdesignfragen.

## 6. Rekonstruktionsäquivalenz ist schwächer

Aus ähnlichen Rekonstruktionsverteilungen folgt nicht automatisch Ω_A ~_Q Ω_B. Ebenso begründen verschiedene Samples aus P(Ω|D,M) keine physikalische Historienseparation.

## 7. Closure

M_std ist für Q im getesteten Bereich geschlossen, wenn die beobachteten Q-Daten mit der posterior-prädiktiven Standardverteilung vereinbar sind und keine präregistrierte gemeinsame Residualstruktur verbleibt, die durch fehlende Standardzustands-, Kanal- oder Modellinformation erklärt werden muss.

    D_Q compatible with P_std(Q | D_control, M_std).

D_control bezeichnet Daten zur Rekonstruktion/Kontrolle von Ω. Wo möglich sollen Ziel- und Kontrolldaten getrennt sein.

## 8. Closure-Defekt

Ein Closure-Defekt ist zunächst eine statistische Größe, keine neue Ontologie. Für eine präregistrierte Teststatistik T:

    Δ_cl = T(D_Q, P_std(Q | D_control, M_std)).

Mögliche T sind kalibrierte posterior-predictive Statistiken, Likelihood-Ratio-artige Größen, z-Scores oder multivariate Residualstatistiken.

    Δ_cl != 0 does not imply new physical state.

## 9. Multi-Channel Closure

Für physikalisch verschiedene Kanäle k:

    r_k = T_k(D_k, P_std(O_k | D_control, M_std))
    r = (r_1, ..., r_n).

Zu prüfen sind gemeinsame präregistrierte Struktur, Kovarianz, Look-elsewhere-Effekte, Modellmissspezifikation, verbleibende Unsicherheit in Ω und unabhängige Replikation.

## 10. Erweiterungszulässigkeit Ω -> (Ω,Z)

Eine Erweiterung wird erst zugelassen, wenn alle Gates erfüllt sind:

**E1 Standard completeness:** relevante Standardzustands- und Kanalunsicherheit modelliert oder marginalisiert.

**E2 Robust closure defect:** Defekt bleibt unter plausiblen Standardmodellvarianten bestehen und ist nicht auf eine einzelne Rekonstruktion oder einen einzelnen Kanal beschränkt.

**E3 Independent definition:** Z wird unabhängig vom Zielresiduum definiert.

**E4 Dynamics:** Z besitzt eine wohldefinierte Dynamik oder Zustandsregel.

**E5 Predictive relation:** vor dem Ziel-Datenfit folgt eine quantitative P_ext(O|Ω,Z,M_ext), die sich von P_std unterscheidet.

**E6 Sparse cross-channel structure:** keine unabhängigen Rettungsparameter pro Kanal.

**E7 Null embedding:** es existiert ein klarer Grenzfall M_ext -> M_std.

**E8 Falsification region:** mögliche Daten können M_ext innerhalb seines zulässigen Parameterraums verwerfen.

## 11. Historieninformation

Eine Historie H ist operational relevant, wenn mindestens eine Bedingung gilt:

1. H ist in Ω(t*) physikalisch kodiert;
2. H beeinflusst die gegenwärtige Prädiktion durch eine etablierte nicht-Markovsche Dynamik;
3. eine zugelassene Erweiterung Z trägt Information über H und erfüllt E1–E8.

Andernfalls ist H für die gegenwärtige Observable operational redundant.

## 12. Strong History Test

Benötigt werden A und B mit

    Ω_A ≡_std Ω_B
    H_A != H_B.

Unter Standard closure gilt P_std(Q|Ω_A)=P_std(Q|Ω_B). Ein reproduzierbarer Unterschied wäre ein Closure-Defekt.

Die Reihenfolge bleibt:

    detect defect
      -> audit Ω and M_std
      -> test reconstruction/channel completeness
      -> identify missing carrier/dynamics
      -> only then consider extension Z.

Der Strong History Test ist ein Discovery-Test auf Zustands-/Modellunvollständigkeit, kein direkter AVI-Nachweis.

## 13. Fünf Axiome in formaler Kurzform

**A1 — Completeness before extension**

    extension Z admissible only after E1 and E2.

**A2 — Reconstruction is not ontology**

    R(D) = P(Ω|D,M)
    uncertainty[R] != physical Z.

**A3 — History requires a present carrier**

    H relevant to O(t*) only if
    H -> Ω(t*) or H -> admissible dynamics -> O(t*).

**A4 — Same-state claims require strong standard-state equivalence**

    strong same state := Ω_A ≡_std Ω_B.

Die schwächere Relation Ω_A ~_Q Ω_B bedeutet nur gleiche Standardvorhersage für Q und genügt nicht für den Strong History Test.

**A5 — Extension requires independent predictive closure**

    Z defined independently
      + dynamics
      + preregistered P_ext
      + null embedding
      + falsification region.

## 14. Minimaler Workflow

    1. define Q and M_std
    2. define Ω
    3. reconstruct P(Ω|D_control,M_std)
    4. compute posterior predictive distribution
    5. preregister T
    6. evaluate Δ_cl
    7. audit standard closure
    8. only if E1-E2 pass: propose Z
    9. require E3-E8 before calling it an AVI extension.

## 15. Konsequenz für bestehende AVI-Symbole

- ξ: kein Core-Symbol; möglicher zukünftiger Spezialfall von Z.
- Φ: kein Core-Symbol; historischer Modellkandidat.
- W: kein Core-Symbol; nur zulässig, falls konkrete Dynamik ihn erfordert.
- X_global: Standardinformation, Kontrollvariable oder zukünftiger Prädiktor je nach physikalischer Definition; nicht automatisch AVI.
- S_i/n_a: spezielle Erweiterungsmodelle, nicht Core.
- Test B: wird im Core als Strong History Test/Closure-Test neu interpretiert.

## 16. Falsifikationslogik

Der Core behauptet nicht, dass Z existiert. Kein Closure-Defekt ist daher kein Scheitern des Frameworks, sondern ein negatives Ergebnis für die getestete Zusatzhypothese.

Ein dauerhaftes Muster, in dem alle scheinbaren Historieneffekte nach Zustandsvervollständigung verschwinden, schwächt die wissenschaftliche Motivation für zusätzliche AVI-Ontologie.

Ein Closure-Defekt bestätigt AVI nicht; er öffnet nur E3–E8.

## 17. Ergebnis

**Core Formalization v0.2: PASS AFTER STRESS-TEST PATCH.**

Der AVI-Kern besitzt jetzt einen zustandsraumneutralen mathematischen Vertrag mit Ω, D, R_M, P_std, der prädiktiven Relation ~_Q, der starken Standardzustandsrelation ≡_std, Δ_cl und dem Erweiterungsgate Ω -> (Ω,Z).

Er enthält bewusst keine neue Naturkonstante und keinen behaupteten neuen Freiheitsgrad.

## 18. Nächster Gate-Test

Es folgt ein **Core Stress-Test v0.1** mit mindestens vier bekannten Klassen:

1. Hysterese/interne Zustandsvariablen;
2. offene nicht-Markovsche Quantensysteme;
3. globale/topologische QFT-Kontexte;
4. kosmologische Rekonstruktionsunsicherheit einschließlich OTA-SCI-0093/0094.

Der Core besteht nur, wenn er diese Fälle korrekt als Standardzustand, Rekonstruktionsproblem oder etablierte Dynamik klassifiziert und keine falschen Z-Erweiterungen erzeugt.
