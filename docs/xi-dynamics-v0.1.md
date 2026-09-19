# AVI — Minimales ξ-Dynamikmodell v0.1

**Stand:** 19. September 2026  
**Status:** Arbeitsmodell / Test-B-Konstruktion  
**Closure-Klasse:** B — Ratenkopplung bei unveränderter Standard-Hintergrundexpansion

## 1. Ziel

Die Kopplungsseite ist durch

    δ ln O_ij(a) = λ ξ(a) ΔS_ij·n

minimal spezifiziert. Dieses Dokument definiert nun die kleinste Dynamik, mit der ξ tatsächlich historische Information tragen kann.

Die Konstruktion ist bewusst phänomenologisch. Sie behauptet keinen mikrophysikalischen Ursprung von ξ.

## 2. Anforderungen

ξ muss:

1. aus einer vorangegangenen kosmologischen Historie eindeutig berechenbar sein;
2. bei gleichem momentanen Standardzustand Y unterschiedliche Werte annehmen können;
3. eine feste Normierung besitzen, damit λ nicht beliebig gegen ξ reskaliert werden kann;
4. einen reproduzierbaren Nullfall besitzen;
5. ohne zukünftige Information kausal berechenbar sein.

## 3. Treiber

Wir führen keine neue frei wählbare Messgröße ein, sondern definieren zunächst einen dimensionslosen historischen Treiber

    s(a) = s[Y(a)]

aus Größen des Standardzustands Y.

Für jede konkrete Modellvariante muss s vor dem Datenvergleich vollständig festgelegt werden. Zulässig sind nur dimensionslose Kombinationen etablierter kosmologischer Größen.

v0.1 lässt die konkrete Wahl von s offen. Damit ist die Dynamik formal geschlossen, aber noch nicht numerisch kalibriert.

## 4. Minimale Gedächtnisdynamik

Als kleinste kausale Dynamik verwenden wir die lineare Relaxationsgleichung in e-fold-Zeit N = ln a:

    dξ/dN = κ [s(N) - ξ(N)]

mit

    κ > 0.

κ ist die dimensionslose Gedächtnis-/Relaxationsrate. Die zugehörige Gedächtnislänge in e-folds ist ungefähr

    L_N = 1/κ.

Die Lösung ab N_i lautet

    ξ(N) = exp[-κ(N-N_i)] ξ_i
           + κ ∫_(N_i)^N exp[-κ(N-N')] s(N') dN'.

Damit ist ξ eine komprimierte, kausal gewichtete Information über die realisierte Vergangenheit von s.

## 5. Feste Normierung

Um die Degeneration λ ↔ ξ zu verhindern, wird s für jede Modellvariante mit einer **vorab festgelegten Referenzskala** dimensionslos definiert. Eine nachträgliche Multiplikation

    s -> A s
    ξ -> A ξ
    λ -> λ/A

ist nicht als neue physikalische Lösung zulässig.

Arbeitsregel: Die Definition und Normierung von s gehört zur Modellvariante und wird gemeinsam mit n präregistriert.

κ und λ bleiben unterschiedliche Parameter: κ bestimmt, wie Historie in den aktuellen Zusatzstatus komprimiert wird; λ bestimmt, wie stark dieser Status differentiell an lokale Raten koppelt.

## 6. Anfangsbedingung und Nullfall

Für die erste Testfassung gilt

    ξ(N_i) = 0.

N_i muss physikalisch festgelegt werden, bevor Daten gefittet werden. Es darf nicht pro Datensatz verschoben werden.

Der vollständige beobachtbare AVI-Nullfall ist weiterhin

    λ = 0.

Zusätzlich liefert s(N)=0 bei ξ_i=0 identisch ξ(N)=0.

## 7. Test B ist konstruktiv möglich

Betrachte zwei zulässige Historien A und B, die am Vergleichspunkt denselben Standardzustand besitzen:

    Y_A(N*) = Y_B(N*).

Wenn ihre früheren Treiber verschieden waren,

    s_A(N') != s_B(N')

für einen Teil des Intervalls N_i < N' < N*, dann gilt

    Δξ(N*) =
      κ ∫_(N_i)^(N*) exp[-κ(N*-N')]
      [s_A(N')-s_B(N')] dN'.

Daher kann

    Y_A(N*) = Y_B(N*)
    aber
    ξ_A(N*) != ξ_B(N*)

gelten.

Mit der bereits festgelegten Kopplung folgt

    Δ_B ln O_ij
      = λ Δξ(N*) ΔS_ij·n.

Damit ist Test B erstmals als vollständige mathematische Kette formulierbar:

    unterschiedliche Historie
    -> unterschiedlicher gewichteter Historienzustand ξ
    -> differentielle Kopplung
    -> messbares Ratenverhältnis.

## 8. Wichtige Einschränkung

Die obige Konstruktion zeigt nur, dass Historienseparation **mathematisch möglich** ist. Sie zeigt nicht, dass die reale Kosmologie zwei physikalisch zulässige Lösungen mit vollständig gleichem Y(N*) und verschiedenem vergangenen s besitzt.

Genau diese Existenzfrage muss separat geprüft werden. Werden die vollständigen Standard-Anfangsbedingungen und Bewegungsgleichungen so festgelegt, dass Y(N*) die relevante Historie eindeutig bestimmt, entsteht durch bloßes Umbenennen eines Integrals keine neue Physik.

ξ erhält physikalischen Gehalt nur, wenn seine Dynamik als zusätzlicher Zustand notwendig und empirisch testbar ist.

## 9. Grenzfälle

### κ -> infinity

ξ folgt s praktisch instantan:

    ξ(N) -> s(N).

Dann verschwindet der eigenständige Historiencharakter. Bei gleichem aktuellen Y und damit gleichem s ist ξ ebenfalls gleich. Test B verliert seinen Hebel.

### κ -> 0

Bei ξ_i=0 reagiert ξ über ein endliches Intervall nur sehr schwach. Der beobachtbare Effekt wird entsprechend klein, sofern λ nicht künstlich kompensiert wird.

### endliches κ

Nur der Zwischenbereich trägt ein echtes endliches Gedächtnis vergangener Zustände. Das ist der für Test B relevante Bereich.

## 10. Parameterdisziplin

Die minimale dynamische Modellvariante besitzt damit zwei AVI-Parameter:

- κ: globale Gedächtnisrate;
- λ: globale differentielle Kopplungsamplitude.

n, die Definition von s, seine Normierung, N_i und die Systemsignaturen S_i sind **keine Fitparameter derselben Analyse**. Sie müssen vorab festgelegt oder unabhängig bestimmt werden.

Es werden keine separaten κ- oder λ-Werte für einzelne Experimente eingeführt.

## 11. Erste falsifizierbare Struktur

Für Messpunkt k bei N_k:

    r_k^AVI =
      λ ξ(N_k; κ, s, N_i) ΔS_k·n.

Mit einer Messvektor-Kovarianz C_exp kann eine gemeinsame Likelihood konstruiert werden. Ein Nullresultat begrenzt dann erstmals einen gemeinsamen Bereich im (κ, λ)-Raum einer vollständig spezifizierten Variante.

Die Präzisionsdaten dürfen erst verwendet werden, nachdem s, n, N_i und die S_i feststehen.

## 12. Was noch fehlt

Vor einem echten numerischen Fit fehlt genau eine zentrale Modellentscheidung: die physikalisch begründete Wahl des Treibers s[Y].

Diese Wahl darf nicht danach erfolgen, welche Funktion die vorhandenen Daten am besten reproduziert.

Der nächste Arbeitsschritt ist daher ein **Treiber-Screening** mit wenigen vorab definierten Kandidaten aus dem Standardzustand Y. Jeder Kandidat muss hinsichtlich Dimensionslosigkeit, physikalischer Motivation, Unabhängigkeit, Degenerationen und Fähigkeit zu Test B geprüft werden.

## 13. Epistemischer Status

- **[R]** Lineare Relaxations-/Gedächtnisgleichungen sind mathematisch etablierte dynamische Strukturen.
- **[H]** AVI benötigt einen zusätzlichen historienabhängigen Zustand ξ.
- **[H]** ξ folgt in der Minimalfassung der Relaxationsgleichung dξ/dN = κ(s-ξ).
- **[H]** ξ koppelt über die separat definierte differentielle Class-B-Kopplung an Ratenverhältnisse.
- **[I]** Philosophische Überlegungen zu Werden, Teil und Ganzem können die Forschungsfrage motivieren, bestimmen aber weder s, κ, ξ noch λ.
