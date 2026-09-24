# AVI — QFT Response Gate v0.1

**Stand:** 24. September 2026
**Status:** kritischer Referenztest
**Pfad:** O2 / Q4 — globale Kontextseparation über lokale Feldkorrelationen

## 1. Gate-Frage

Können zwei Raumzeiten/Feldkonfigurationen mit lokal gleicher klassischer Geometrie, aber unterschiedlichem globalem Kontext eine unterschiedliche lokale dimensionslose Übergangs- oder Detektorantwort erzeugen?

Antwort aus etablierter QFT in gekrümmter Raumzeit:

    JA.

Dies ist ein Architektur- und Nullmodell-Ergebnis, keine AVI-Evidenz.

## 2. Standard-QFT-Mechanismus

Für einen Unruh-DeWitt-artigen Zweiniveaudetektor mit Energielücke Ω ist die Antwort in führender Ordnung durch die entlang der Weltlinie ausgewertete Zweipunktfunktion des Feldes bestimmt:

    F(Ω) =
      ∫ dτ dτ'
      χ(τ) χ(τ')
      exp[-i Ω(τ-τ')]
      W(x(τ),x(τ'))

mit Schaltfunktion χ und Wightman-Funktion W.

Damit gilt schematisch:

    global geometry/topology/boundary data
      -> quantum state / W(x,x')
      -> detector response F(Ω).

Eine lokale klassische Krümmungsmessung muss die globale Information daher nicht vollständig enthalten, während eine lokale quantenmechanische Response sie über Feldkorrelationen dennoch tragen kann.

## 3. Direkte Referenzfälle

### R1 — quotient/topologisch nichttriviale flache Raumzeiten

Langlois (2006) berechnet Übergangsraten von inertialen und beschleunigten Detektoren in Quotienten des Minkowski-Raums unter diskreten Isometrien. Die globale Identifikation verändert die Feldkorrelationen und damit die Detektorantwort, obwohl die lokale flache Geometrie erhalten sein kann.

### R2 — kompakte Raumdimension

Chiou (2016) untersucht einen Unruh-DeWitt-Detektor in flacher Raumzeit mit kompakter Raumdimension. Die Kompaktifizierung erzeugt bevorzugte globale Strukturen und verändert Anregungs-/Abregungsraten abhängig von Bewegung und Beschleunigung.

### R3 — lokal gleiche Geometrie, global unterschiedliche Struktur

Smith und Mann (2016) zeigen an lokal flachen, topologisch nichttrivialen Raumzeiten, dass lokale Detektorstatistiken und Detektorkorrelationen von der globalen Raumzeitstruktur abhängen können.

Cong et al. (2020) zeigen einen verwandten Effekt für einen Detektor im Inneren einer dünnen Materieschale: Die Response kann globale Struktur unterscheiden, obwohl der Detektor während des endlichen Messintervalls klassisch keinen Lichtsignal-Rundweg zur Schale absolvieren kann.

### R4 — kompakte Milne-Kosmologie

Wilkinson und Louko (2025) analysieren einen inertialen Detektor in einer expandierenden Milne-Kosmologie mit kompakten räumlichen Schnitten. Die Response hängt unter anderem von Umfangsparameter, Alter bei Einschalten, Geschwindigkeit, Randbedingung und bei untwisted fields vom Nullmodenzustand ab.

### R5 — toroidale Raumzeit

Kajuri und Siddh (2026, Preprint) untersuchen vierdimensionale Minkowski-Raumzeit mit zwei periodisch identifizierten Raumrichtungen, also R × T². Die globale Topologie hinterlässt Signaturen in Feldkorrelationen und Detektor-Übergangsraten. Dieser aktuelle Preprint bestätigt die fortdauernde Relevanz des Referenzproblems, ist aber nicht peer-reviewed.

## 4. Dimensionslose Observable

Für AVI ist eine absolute Anregungswahrscheinlichkeit weniger geeignet als eine normierte Response.

Geeignete Standard-QFT-Referenzgrößen sind beispielsweise

    R_AB(Ω) = F_A(Ω) / F_B(Ω)

für zwei kontrollierte globale Kontexte A/B,

oder für einen stationären Detektor ein Verhältnis von Anregungs- und Abregungsraten

    D(Ω) = Γ_up(Ω) / Γ_down(Ω).

Diese Größen sind dimensionslos. Im thermischen KMS-Fall kann D mit einer Temperatur-/Gap-Kombination verknüpft sein; außerhalb stationärer Situationen muss die konkrete Definition einschließlich Schaltfunktion und Messdauer explizit angegeben werden.

## 5. Test B-GQFT

Wir definieren den Standardreferenztest:

    local classical geometry_A = local classical geometry_B
    detector microphysics_A = detector microphysics_B
    trajectory_A = trajectory_B locally
    switching_A = switching_B
    field theory_A = field theory_B
    G_global,A != G_global,B

und berechnen

    W_A != W_B

sowie daraus

    F_A(Ω) != F_B(Ω).

Dieser Test ist in bekannten QFT-Modellen erfüllbar.

Damit ist die Kette

    G_global -> Q_correlations -> local response

nicht nur konzeptionell möglich, sondern explizit berechenbar.

## 6. Wichtige Kausalitätsgrenze

Das Ergebnis darf nicht als überlichtschnelle Informationsübertragung interpretiert werden.

Der Quantenzustand beziehungsweise die Korrelationsstruktur ist Teil der globalen Vorbereitung des Feldzustands. Eine Änderung entfernter Randbedingungen kann nicht beliebig instantan als kontrollierbares Signal an einen lokalen Detektor übertragen werden. Mikrokausalität und die konkrete Zustandspräparation bleiben zu respektieren.

Für AVI folgt daraus:

> Ein globaler Kontext kann lokale Response mitbestimmen; daraus folgt keine dynamische Fernwirkung ohne Träger und kausale Zustandsentwicklung.

## 7. Ergebnis für AVI

    Q4 Response Gate: PASS AS STANDARD-QFT REFERENCE

Das ist stärker als das vorige Architecture Gate:

- lokale klassische Geometrie kann gleich sein;
- globale Struktur kann verschieden sein;
- Wightman-/Korrelationsstruktur kann verschieden sein;
- lokale Übergangsresponse kann verschieden sein;
- der Unterschied ist standardtheoretisch berechenbar.

Damit besitzt AVI-B-G einen realen Nullkanal.

## 8. Gleichzeitig ein negatives Ergebnis

Gerade weil Standard-QFT den Mechanismus bereits liefert, darf AVI nicht behaupten:

    globale Struktur -> lokale Response

sei seine neue Vorhersage.

Das wäre keine neue Theorie.

Ein AVI-spezifischer Beitrag muss deshalb als Residuum relativ zu einer vollständig spezifizierten Standard-QFT-Vorhersage definiert werden.

## 9. Residualformulierung

Für Messkanal k:

    r_k =
      ln O_k,obs
      - ln O_k,QFT+GR

Eine AVI-Erweiterung darf nur dann eingeführt werden, wenn sie vor der Datenanpassung eine gemeinsame Struktur für mehrere Kanäle festlegt, zum Beispiel

    r_k^AVI =
      λ X_global ΔS_k · n

wobei X_global nicht nachträglich aus demselben Residuum definiert werden darf.

Die frühere Variable ξ kann nur dann physikalisch mehr als eine QFT-Hilfsgröße sein, wenn

    ξ_AVI != ξ_QFT-derived

operational definiert und durch eine unabhängige Relation bestimmt wird.

## 10. Konsequenz für das bisherige C_i-Modell

Die bisherige Form

    ln(C_i/C_j) = λ ξ ΔS_ij · n

bleibt als phenomenologischer Testansatz brauchbar, aber ξ darf nicht einfach "die lokale Wightman-Funktion" bedeuten.

Saubere Zerlegung:

    O_ij,pred =
      O_ij,QFT+GR
      × C_ij,AVI

mit

    C_ij,AVI -> 1

im AVI-Nullfall.

Damit werden bekannte QFT-Response-Effekte im Referenzmodell absorbiert, statt als AVI-Signal fehlinterpretiert zu werden.

## 11. Neuer Engpass

Der Carrier ist nicht mehr das Hauptproblem. Standard-QFT liefert bereits einen Carrier:

    Q = field correlation structure.

Der neue Engpass ist die **zusätzliche AVI-Relation**.

AVI muss nun beantworten:

1. Welche globale Größe X_global ist unabhängig definiert?
2. Warum ist ihre Wirkung nicht bereits in W_QFT enthalten?
3. Welche gemeinsame, sparsame Kopplung zu mehreren Systemsignaturen folgt?
4. Welche zwei Experimente/Beobachtungskanäle unterscheiden AVI von QFT+GR?

Ohne diese vier Punkte sollte das Modell nicht weiter parametrisiert werden.

## 12. Nächster Gate-Test: Residual-Space Gate

Vor neuen Fitparametern wird geprüft, ob überhaupt ein logisch sauberer Residualraum existiert.

Drei Möglichkeiten:

### RS1 — keine zusätzliche Relation nötig

Alle global-context-abhängigen lokalen Response-Effekte folgen aus QFT+GR.

Dann ist O2 als AVI-Mechanismus redundant.

### RS2 — effektive universelle Relation

Mehrere physikalisch verschiedene lokale Systeme zeigen nach vollständiger Standardmodellierung eine gemeinsame Abhängigkeit von einer unabhängig gemessenen globalen Größe.

Dann wäre ein AVI-artiger phänomenologischer Residualtest sinnvoll.

### RS3 — neue fundamentale Physik

Eine zusätzliche Relation benötigt einen neuen Freiheitsgrad oder eine Modifikation von QFT/GR.

Dann verlässt AVI den minimalistischen O2-Referenzpfad und muss als konkrete Erweiterung formuliert werden.

## 13. Entscheidung

Der Q4-Pfad wird nicht verworfen, aber seine Rolle ändert sich:

    vorher: möglicher AVI-Carrier
    jetzt: etablierter Standard-QFT-Carrier und zwingendes Nullmodell.

Der nächste Schritt ist daher **kein weiterer Carrier-Screen**, sondern das Residual-Space Gate.

## 14. Epistemischer Status

- **[R]** Unruh-DeWitt-Response hängt von der Wightman-/Korrelationsfunktion entlang der Detektorweltlinie ab.
- **[R]** Es existieren peer-reviewte Modelle, in denen global unterschiedliche, lokal gleiche oder lokal nicht unterscheidbare klassische Geometrien verschiedene Detektorantworten erzeugen.
- **[R]** Diese Effekte sind Standard-QFT und keine AVI-Evidenz.
- **[H]** Ein zusätzlicher AVI-Beitrag könnte als präregistriertes Residuum relativ zu QFT+GR existieren.
- **[D]** Ein AVI-Modell, das lediglich bekannte global-context-sensitive QFT-Response neu benennt, ist redundant.

## 15. Referenzen

- P. Langlois, *Causal particle detectors and topology*, Annals of Physics 321 (2006) 2027–2070, DOI 10.1016/j.aop.2006.01.013.
- L. Smith, R. B. Mann, *Spacetime structure and vacuum entanglement*, Phys. Rev. D 93, 044001 (2016).
- D.-W. Chiou, *Response of the Unruh-DeWitt detector in flat spacetime with a compact dimension*, 2016.
- W. Cong et al., *Quantum distinction of inertial frames: Local versus global*, Phys. Rev. D 101, 104060 (2020).
- T. R. Perche, E. Martín-Martínez, *Geometry of spacetime from quantum measurements*, Phys. Rev. D 105, 066011 (2022).
- A. S. Wilkinson, J. Louko, *Local quantum detection of the cosmological expansion: Unruh-DeWitt detectors in spatially compact Milne cosmology*, Phys. Rev. D 111, 025008 (2025).
- N. Kajuri, S. Siddh, *Unruh-DeWitt Detector Response in Toroidal Spacetime*, arXiv:2604.21118 (2026), preprint.
