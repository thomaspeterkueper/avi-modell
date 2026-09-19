# AVI — Test B: Determinismus-Gate v0.1

**Stand:** 19. September 2026  
**Status:** kritischer Modelltest  
**Betroffene Variante:** AVI-B0.1

## 1. Frage

Kann die aktuelle AVI-B0.1-Konstruktion zwei standardphysikalisch zulässige kosmologische Historien A und B besitzen, die am selben Vergleichspunkt denselben **vollständig spezifizierten** Standardzustand Y* haben, aber unterschiedliche ξ-Werte?

Gefordert wäre:

    Y_A(N*) = Y_B(N*)
    ξ_A(N*) != ξ_B(N*)

mit

    dξ/dN = κ[s(Y)-ξ]

und

    s = -d ln H_std/dN - 3/2.

## 2. Deterministisches Zustandskriterium

Sei die Standardkosmologie als autonomes Anfangswertproblem geschrieben:

    dY/dN = F(Y; θ_std)

mit festen Standardparametern θ_std.

Ist Y ein vollständiger Zustand und F im relevanten Bereich eindeutig lösbar, dann bestimmt Y(N*) die lokale Lösung eindeutig. Rückwärtsintegration bestimmt damit auch die vorangegangene Standardhistorie innerhalb desselben Lösungszweigs.

Für zwei Lösungen mit

    Y_A(N*) = Y_B(N*)

und identischen θ_std folgt daher im Eindeutigkeitsbereich:

    Y_A(N) = Y_B(N)

für die gemeinsame Vergangenheit, und damit

    s_A(N) = s_B(N).

Bei identischer ξ-Anfangsbedingung folgt:

    ξ_A(N*) = ξ_B(N*).

Unter diesen Bedingungen kann Test B nicht bestehen.

## 3. Konsequenz für AVI-B0.1

Der bislang gewählte Treiber s[Y] ist vollständig aus der Standardhistorie abgeleitet. Die Relaxationsgleichung speichert diese Historie zwar mathematisch, erzeugt aber **keinen unabhängigen physikalischen Freiheitsgrad**, wenn Y bereits dynamisch vollständig ist und ξ keine eigene unabhängige Anfangsinformation besitzt.

Das bedeutet:

> Ein Gedächtnisintegral über eine eindeutig durch den vollständigen Gegenwartszustand rekonstruierbare Standardhistorie reicht nicht für den starken Test B.

Dies ist kein experimentelles Scheitern von AVI. Es ist ein Scheitern dieser minimalen Konstruktion als Begründung eines zusätzlichen Zustands.

## 4. Synthetischer Gegenversuch

Man kann formal zwei Funktionen s_A(N) und s_B(N) wählen, die vor N* verschieden sind und am Endpunkt denselben aktuellen Wert besitzen. Dann liefert

    Δξ(N*) =
      κ ∫ exp[-κ(N*-N')]
      [s_A(N')-s_B(N')] dN'

im Allgemeinen Δξ != 0.

Dieser synthetische Erfolg ist jedoch **nicht ausreichend**. Er zeigt nur die Mathematik eines Filters mit Gedächtnis. Er zeigt nicht, dass beide s-Historien Lösungen desselben vollständigen Standard-Anfangswertproblems sind und bei N* denselben vollständigen Y-Zustand besitzen.

Der künstliche Test würde Test B also genau durch das Weglassen relevanter Zustandsinformation erzeugen.

## 5. Wann Historienseparation trotzdem möglich wäre

Der Determinismus-Einwand lässt vier logisch verschiedene Wege offen.

### B1 — Y war nicht vollständig

Wenn Y nur beobachtete oder grob ausgewählte Standardgrößen enthält, können gleiche Y-Werte verschiedene vollständige Mikrozustände verbergen.

Das wäre jedoch kein AVI-Nachweis. Zuerst müsste die fehlende Standardinformation in Y aufgenommen werden.

**Regel:** Unvollständigkeit von Y darf nicht als ξ umetikettiert werden.

### B2 — ξ ist ein echter zusätzlicher Zustand

ξ könnte eine eigene Anfangsbedingung besitzen, die nicht aus Y folgt:

    dξ/dN = G(ξ,Y)
    ξ_i unabhängig.

Dann können bei gleichem Y* verschiedene ξ* existieren.

Das wäre echte Zustandsvergrößerung, verlangt aber eine physikalische Begründung dafür, was ξ ist und warum es existiert. Die bisherige Definition als bloße Kompression der Standardhistorie reicht dafür nicht.

### B3 — Standarddynamik ist effektiv nicht-Markovsch

Falls die korrekte physikalische Beschreibung selbst Gedächtnisterme, nichtlokale Dynamik oder verborgene Freiheitsgrade benötigt, könnte der momentane reduzierte Zustand die Zukunft nicht vollständig bestimmen.

Dann müsste AVI präzise zeigen, welche etablierte oder neu postulierte Physik diesen zusätzlichen Zustand trägt.

### B4 — globale Information ist nicht im lokalen/reduzierten Y enthalten

Topologie, globale Randbedingungen oder andere globale Daten können von lokalen momentanen Größen nicht bestimmt sein.

Das ist methodologisch real und war bereits Motivation für die Topologie-Kontrolle. Aber solche globale Information darf nur ξ heißen, wenn sie eine konkrete Dynamik und messbare Kopplung besitzt. Sonst ist sie lediglich eine separat zu kontrollierende Randbedingung.

## 6. Starkes und schwaches Test B

Zur Vermeidung weiterer Mehrdeutigkeit werden zwei Begriffe getrennt.

### Test B-weak

    Y_red,A(N*) = Y_red,B(N*)
    history_A != history_B
    ξ_A != ξ_B

wobei Y_red ein bewusst reduzierter beobachtbarer Zustandsvektor ist.

Dies kann empirisch interessant sein, beweist aber keinen zusätzlichen fundamentalen Zustand. Unterschiedliche unbeobachtete Standardvariablen können die Trennung erklären.

### Test B-strong

    Y_full,A(N*) = Y_full,B(N*)
    θ_std,A = θ_std,B
    boundary/global controls matched
    ξ_A(N*) != ξ_B(N*)

und daraus eine messbare Observable.

Nur Test B-strong trägt die ursprüngliche starke AVI-Behauptung, dass derselbe vollständig kontrollierte Gegenwartszustand zusätzliche historienabhängige Zustandsinformation benötigt.

## 7. Ergebnis des Gates

Für **AVI-B0.1 in der bisherigen Form** lautet das Ergebnis:

    strong Test B: FAIL

unter den Annahmen:

- Y ist der vollständige Markov-Zustand der Standarddynamik;
- Standardparameter und globale Randbedingungen sind gleich;
- die Standardgleichungen besitzen eine eindeutige Lösung;
- ξ_i ist für beide Historien gleich;
- s ist ausschließlich eine deterministische Funktion der Standardhistorie Y.

Der Grund ist strukturell, nicht numerisch.

Der schwache Test kann weiterhin konstruiert werden, ist aber nicht hinreichend für die starke AVI-Hypothese.

## 8. Was dadurch nicht verworfen ist

Nicht verworfen sind:

- die allgemeine Frage nach zusätzlicher historienabhängiger Zustandsinformation;
- Class-B-Ratenkopplungen als phänomenologischer Suchraum;
- differentielle Observablen O_ij;
- die Systemsignatur S_i;
- globale/topologische Kontrollfragen;
- Modelle, in denen ξ ein tatsächlich zusätzlicher physikalischer Freiheitsgrad ist.

Verworfen wird nur die Behauptung, dass ein deterministischer Filter über eine vollständig rekonstruierbare Standardhistorie **allein** ξ physikalisch unabhängig macht.

## 9. Neue Modellanforderung

Eine nächste AVI-Version darf ξ nicht mehr nur als

    ξ = Filter[standard history]

einführen.

Sie muss stattdessen mindestens eine der folgenden Aussagen physikalisch begründen:

1. ξ besitzt einen unabhängigen Anfangszustand;
2. ξ beschreibt einen zusätzlichen dynamischen Freiheitsgrad;
3. die relevante Dynamik ist fundamental oder effektiv nicht-Markovsch und ξ ist deren Zustandsvariable;
4. ξ kodiert klar definierte globale Information, die nicht Bestandteil des lokalen/reduzierten Standardzustands ist und messbar koppelt.

Erst dann ist strong Test B wieder offen.

## 10. Konsequenz für Datenfits

Es wird **kein** Fit der Präzisionsdaten an die aktuelle AVI-B0.1-Variante durchgeführt.

Ein Fit von κ und λ wäre zwar mathematisch möglich, aber wissenschaftlich verfrüht, weil die zentrale Zustandsbehauptung das Determinismus-Gate nicht bestanden hat.

Dies verhindert, dass experimentelle Präzision einem strukturell redundanten Modell nachträglich Bedeutung verleiht.

## 11. Nächster Forschungszweig

Der nächste sinnvolle Schritt ist kein weiterer Treibervergleich, sondern ein **ξ-Ontologie-Screening**:

- zusätzlicher lokaler dynamischer Freiheitsgrad;
- globaler Zustands-/Randbedingungsparameter;
- effektiver Gedächtniszustand aus nicht-Markov-Dynamik;
- oder Rückstufung von strong Test B zugunsten einer schwächeren, rein operationalen AVI-Version.

Jede Variante muss angeben, was ξ physikalisch repräsentiert, welche Gleichung es trägt, welche Anfangs-/Randbedingungen gelten und wodurch es von bereits bekannter Standardinformation unterscheidbar ist.

## 12. Epistemischer Status

- **[R]** Für ein eindeutig lösbares autonomes Anfangswertproblem bestimmt ein vollständiger Zustand zusammen mit festen Parametern den Lösungszweig.
- **[D]** Daraus folgt innerhalb der definierten AVI-B0.1-Annahmen, dass identisches vollständiges Y* keine zwei verschiedenen ausschließlich aus Y erzeugten ξ-Historien zulässt.
- **[H]** AVI könnte dennoch einen echten zusätzlichen Freiheitsgrad oder globale/nicht-Markovsche Zustandsinformation besitzen.
- **[I]** Philosophische Motivation entscheidet nicht, welche dieser Möglichkeiten physikalisch realisiert ist.
