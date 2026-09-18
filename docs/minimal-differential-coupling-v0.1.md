# AVI — Minimale differentielle Kopplungsfamilie v0.1

**Stand:** 18. September 2026
**Status:** Arbeitsmodell / präregistrierte Modellstruktur
**Closure-Klasse:** B — Ratenkopplung bei unveränderter Standard-Hintergrundexpansion

## 1. Zweck

Dieses Dokument definiert die kleinste AVI-Kopplungsfamilie, mit der die bereits eingeführte Systemsignatur S_i zu einer messbaren differentiellen Observable führt. Die Struktur wird vor einem Fit an Präzisionsdaten festgelegt. Sie ist keine Behauptung, dass ein AVI-Effekt existiert.

## 2. Festgelegter Scope

Für v0.1 gilt:

    H_AVI(a) = H_std(a)

AVI verändert in dieser Modellklasse nicht die FLRW-Hintergrundexpansion. Die lokale messbare Größe ist:

    O_ij(a) = Γ_i(a) / Γ_j(a)

## 3. Minimaler zusätzlicher Zustand

Wir verwenden:

    Z_AVI(a) = (Y(a), ξ(a))

Für diese Kopplungsfassung wird ξ dimensionslos normiert. Die konkrete Evolutionsregel bleibt Teil des Closure-Problems. Φ darf in die Zustandsbildung eingehen, erhält in v0.1 aber keinen zusätzlichen unabhängigen Fitparameter in der lokalen Kopplung.

## 4. Systemsignatur

Jeder Prozess i besitzt eine unabhängig bestimmte physikalische Signatur:

    S_i = (K_i^α, K_i^μ, K_i^nuc, K_i^grav, ...)

Die Komponenten stammen aus Standard-Atom-, Molekül-, Kern- oder Gravitationstheorie beziehungsweise unabhängiger Kalibration. Sie sind keine AVI-Fitparameter.

## 5. Minimale Kopplungsfamilie

Allgemein:

    ln C_i(a) = U(a) + S_i · D(a)

Der universelle Anteil U verschwindet aus lokalen dimensionslosen Ratenverhältnissen:

    ln[C_i/C_j] = (S_i-S_j) · D

Die minimale AVI-Hypothese setzt:

    D(a) = λ ξ(a) n

Dabei ist λ eine einzige dimensionslose globale Kopplungsstärke, n ein vor dem Datenvergleich festgelegter Einheitsvektor im physikalischen Signaturraum und ξ(a) der zusätzliche AVI-Zustand.

Damit:

    ln[C_i/C_j] = λ ξ(a) (S_i-S_j)·n

und im linearen Kleinabweichungsfall:

    δ ln O_ij(a) = λ ξ(a) ΔS_ij·n

mit ΔS_ij = S_i-S_j.

Für festgelegten ξ-Verlauf und präregistrierten Richtungsvektor n besitzt diese Fassung nur eine neue lokale Kopplungsamplitude λ.

## 6. Warum n nicht frei mitgefittet wird

Würde jede Komponente von D unabhängig an Experimente angepasst, könnte nahezu jeder Kanal einen eigenen AVI-Koeffizienten erhalten. Deshalb gilt: n wird physikalisch begründet vor einem AVI-Anomaliefit gewählt; plausible Richtungen werden als getrennte Modellvarianten behandelt und nicht gleichzeitig frei gemischt.

## 7. Nullmodell

AVI verschwindet exakt für λ=0 oder ξ(a)=0. Dann gilt für alle Prozesse:

    C_i/C_j = 1
    O_ij,AVI = O_ij,std

Der unbeobachtbare gemeinsame Anteil U darf nicht verwendet werden, um einen lokalen differentiellen Effekt zu retten.

## 8. Test B

Für zwei zulässige Historien A und B am Vergleichszeitpunkt a*:

    Y_A(a*) = Y_B(a*)
    ξ_A(a*) != ξ_B(a*)

S_i, S_j, n und λ sind für beide Historien identisch. Dann:

    Δ_B ln O_ij
      = λ [ξ_A(a*)-ξ_B(a*)] ΔS_ij·n

Ein positiver Test B benötigt gleichzeitig Δξ != 0, λ != 0 und ΔS_ij·n != 0.

## 9. Direkte experimentelle Schranke

Liefert ein Experiment:

    |δ ln O_ij| < ε_ij

dann folgt innerhalb dieser konkreten AVI-Variante:

    |λ ξ ΔS_ij·n| < ε_ij

Erst hier darf reale experimentelle Präzision in eine AVI-Parametergrenze übersetzt werden. Ohne festgelegte ξ-Dynamik begrenzt ein einzelnes Experiment zunächst nur das Produkt λξ, nicht λ allein.

## 10. Gemeinsamer Fit mehrerer Kanäle

Für Messungen k=1...N mit r_k = δ ln O_k lautet die Vorhersage:

    r_k^AVI = λ ξ(a_k) ΔS_k·n

Die experimentelle Kovarianzmatrix wird übernommen. Es gibt keine kanalweisen AVI-Amplituden. Eine Variante ist ausgeschlossen, wenn kein gemeinsamer Parameterwert die präregistrierte Struktur mit den Messungen vereinbar macht.

## 11. Gravitative Konsistenz

Falls n eine neue zusammensetzungsabhängige gravitative Antwort impliziert, müssen WEP-Grenzen gleichzeitig erfüllt werden. Ein Uhrenfit darf nicht isoliert akzeptiert werden, wenn dieselbe Kopplung einen ausgeschlossenen gravitativen Effekt erzeugt. Die genaue Übersetzung verlangt ein mikrophysikalisches Modell.

## 12. Präregistrierte Modellentscheidungen v0.1

Vor dem ersten numerischen AVI-Fit sind fest:

- Closure-Klasse B;
- H=H_std;
- Observable O_ij=Γ_i/Γ_j;
- S_i stammt unabhängig aus etablierter Physik;
- common-mode ist lokal nicht beobachtbar;
- differentielle Antwort D=λξn;
- genau eine globale lokale Kopplungsamplitude λ je Modellvariante;
- n wird nicht aus derselben Anomalie gefittet;
- keine separate freie Kopplung pro Experiment;
- Nullfall λ=0;
- experimentelle Kovarianzen und Systematiken bleiben Teil des Vergleichs.

## 13. Noch offene Closure-Frage

Die Kopplungsseite ist damit minimal geschlossen, die Zustandsdynamik noch nicht. Als nächstes muss unabhängig definiert werden:

    ℱ_a : X|_[a_i,a] -> ξ(a)

so dass ξ eindeutig berechenbar ist, seine Normierung nicht nachträglich die Bedeutung von λ verschiebt, zwei zulässige Historien denselben vollständig kontrollierten Y(a*) aber verschiedenes ξ(a*) besitzen können und der Nullfall reproduzierbar ist.

Erst danach ist ein numerischer Test B vollständig spezifiziert.

## 14. Epistemischer Status

- [R] Differentielle dimensionslose Ratenverhältnisse und unabhängige physikalische Sensitivitätskoeffizienten sind etablierte experimentelle Werkzeuge.
- [H] AVI besitzt einen zusätzlichen Zustand ξ, der bei gleichem Standardgegenwartszustand historienabhängig verschieden sein kann.
- [H] Die minimale differentielle AVI-Antwort hat die Form D=λξn.
- [I] Omnizedenz kann die Frage nach der Relation von Teil, Ganzem und Werden motivieren. Sie liefert weder ξ, λ noch n und zählt nicht als physikalische Evidenz.
