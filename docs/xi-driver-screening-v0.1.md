# AVI — ξ-Treiber-Screening v0.1

**Stand:** 19. September 2026  
**Status:** Arbeitsmodell / Auswahl vor Datenfit  
**Scope:** Class-B-AVI, H = H_std

## 1. Ziel

Das minimale ξ-Modell

    dξ/dN = κ [s(N) - ξ(N)]

benötigt einen dimensionslosen Treiber s[Y]. Dieses Dokument prüft wenige Kandidaten ausschließlich nach physikalischer Definition, Redundanz, Historienfähigkeit und Testbarkeit. Beobachtete Anomalien werden nicht als Auswahlkriterium verwendet.

## 2. Auswahlkriterien

Ein geeigneter Treiber muss:

1. vollständig aus dem Standardzustand Y beziehungsweise einer klar definierten Standard-Referenz ableitbar sein;
2. dimensionslos und normiert sein;
3. ohne AVI-Datenfit definiert werden;
4. nicht bloß eine Umbenennung von ξ oder Φ sein;
5. eine zeitliche Struktur besitzen, die endliches Gedächtnis überhaupt sinnvoll macht;
6. mit dem Nullmodell und den bestehenden kosmologischen Gleichungen kompatibel sein.

Zusätzlich gilt eine harte Test-B-Bedingung: Wenn vollständiges Y(a*) und die Standarddynamik die gesamte relevante Vergangenheit eindeutig festlegen, kann ein aus Y deterministisch erzeugter Treiber keine physikalisch unabhängige Historienseparation erzeugen. Das muss für jede Variante separat geprüft werden.

## 3. Kandidat S1 — normierte Expansionsrate

    s_H(a) = H(a) / H_ref(a) - 1

Als Referenz könnte ein vorab festgelegtes Standardmodell dienen.

**Vorteile:** dimensionslos, direkt kosmologisch, beobachtungsnah.

**Problem:** Wird H_ref als dasselbe Standardmodell gewählt, das Y definiert, ist s_H im Nullmodell identisch null. Wird eine andere Referenz gewählt, misst s_H primär Modellabweichung statt einen eigenständigen historischen Zustand.

**Bewertung:** guter Diagnosekanal, schwacher fundamentaler ξ-Treiber. Für Class B besonders problematisch, weil H_AVI = H_std festgelegt wurde.

**Status:** nicht als Primärtreiber v0.1.

## 4. Kandidat S2 — logarithmische Änderung der Expansionsrate

    s_q(a) = - d ln H / dN

Dieser dimensionslose Ausdruck ist eng mit dem Verzögerungsparameter verknüpft:

    q = -1 - d ln H/dN

also

    s_q = 1 + q.

**Vorteile:** dimensionslos; beschreibt nicht die absolute Expansionsrate, sondern die Form ihrer Entwicklung; unterscheidet Strahlungs-, Materie- und beschleunigte Epochen.

**Problem:** In einem vollständig spezifizierten FLRW-Modell ist s_q aus Y bestimmt. ξ ist damit ein Gedächtnis einer Standardgröße, aber noch kein Beweis für einen zusätzlichen physikalischen Freiheitsgrad.

**Bewertung:** mathematisch sauberster Minimal-Treiber für einen ersten konstruktiven Test. Er entspricht einer Historie der kosmologischen Dynamik statt einer bloßen aktuellen Skala.

**Status:** Primärkandidat.

## 5. Kandidat S3 — Materieanteil

    s_m(a) = Ω_m(a)

oder zentriert

    s_m,c(a) = Ω_m(a) - Ω_m,ref.

**Vorteile:** dimensionslos, physikalisch transparent, verändert sich stark über kosmologische Epochen.

**Problem:** Ω_m ist bereits Bestandteil beziehungsweise direkte Funktion des Standardzustands. Die Integration erzeugt mathematisches Gedächtnis, aber nicht automatisch neue Physik. Außerdem privilegiert der Kandidat Materie ohne bisherige AVI-Begründung gegenüber Strahlung oder dunkler Energie.

**Status:** Kontrollvariante, nicht Primärkandidat.

## 6. Kandidat S4 — Zusammensetzungs-/Epochenkontrast

Eine symmetrischere Möglichkeit ist ein dimensionsloser Kontrast zwischen den Standardkomponenten, zum Beispiel

    s_c(a) = Ω_m(a) - Ω_DE(a)

bei explizit festgelegtem Standard-DE-Modell.

**Vorteile:** markiert den Übergang zwischen Materiedominanz und beschleunigter Epoche und besitzt natürliche Vorzeichenstruktur.

**Problem:** Die konkrete Kombination ist bereits eine Modellentscheidung. Andere Linearkombinationen wären ebenso konstruierbar. Ohne zusätzliche physikalische Begründung droht willkürliche Feature-Auswahl.

**Status:** interessant, aber für v0.1 zurückgestellt.

## 7. Kandidat S5 — Ricci-/Krümmungsskalar normiert

Für FLRW kann eine dimensionslose Krümmungsgröße konstruiert werden, beispielsweise schematisch

    s_R(a) = R(a) / H_ref(a)^2

mit vollständig festgelegter Konvention und Referenz.

**Vorteile:** geometrisch und kovarianter motivierbar als einzelne Dichtekomponenten.

**Problem:** AVI hatte Φ bewusst nicht als räumlich propagierendes Feld definiert, und die frühere Arbeitsrichtung soll nicht wieder unbemerkt zu R(a) zurückkehren. Außerdem ist R im FLRW-Hintergrund aus H und seiner Ableitung bestimmt und liefert daher zunächst keine unabhängige Information.

**Status:** nicht für v0.1; nur als spätere geometrische Vergleichsvariante.

## 8. Kandidat S6 — kosmische Zusammensetzungsänderung als Geschwindigkeit im Zustandsraum

Allgemeiner könnte man die Änderung eines dimensionslosen Standard-Zustandsvektors Ω=(Ω_r,Ω_m,Ω_DE,...) verwenden:

    s_Ω(a) = || dΩ/dN ||

mit vorab festgelegter Norm.

**Vorteile:** reagiert auf Übergänge zwischen kosmologischen Epochen und bevorzugt keine einzelne Komponente.

**Problem:** Die Wahl der Norm und Koordinaten im Zustandsraum ist nicht eindeutig. Eine ungeeignete Parametrisierung kann den Treiber künstlich verändern.

**Status:** konzeptionell stark, aber noch nicht minimal genug.

## 9. Auswahl für die erste mathematische Testvariante

Für AVI-B0.1 wird als **Testtreiber**, nicht als Naturgesetz, gewählt:

    s(N) = s_q(N) = - d ln H_std / dN.

Begründung:

- dimensionslos ohne zusätzliche willkürliche Einheit;
- vollständig aus dem Standardhintergrund berechenbar;
- besitzt klare kosmologische Zeitstruktur;
- führt keine zusätzliche Materieart oder neue Feldgröße ein;
- passt zur ursprünglichen AVI-Frage nach lokalen Raten relativ zu globaler kosmologischer Entwicklung;
- kann ohne Blick auf eine Uhren- oder andere lokale Anomalie festgelegt werden.

Die Wahl ist ausdrücklich provisorisch. Sie wird verworfen, wenn Test B unter vollständig kontrolliertem Y dadurch nur mathematisch duplizierte, nicht physikalisch unabhängige Information erhält.

## 10. Normierung

Für den Primärkandidaten ist keine dimensionsbehaftete Referenz nötig. Um jedoch einen beliebigen konstanten Offset nicht in ξ zu speichern, verwenden wir für die erste Testkonstruktion eine zentrierte Form

    s(N) = - d ln H_std/dN - s_ref

mit einem einmalig festgelegten s_ref.

Für einen analytischen Materie-Referenzfall bietet sich

    s_ref = 3/2

an, weil H ∝ a^(-3/2) in einer idealisierten Materieepoche.

Damit gilt in diesem Referenzfall s=0. Diese Zentrierung ist eine Konvention der Testvariante und darf später nicht an Daten angepasst werden.

## 11. Erste analytische Plausibilitätsprüfung

Ist s über ein Intervall konstant s=s0 und ξ(N_i)=0, dann

    ξ(N) = s0 [1 - exp(-κ ΔN)].

Damit ist sofort sichtbar:

- κ ΔN << 1: ξ ≈ s0 κ ΔN;
- κ ΔN >> 1: ξ ≈ s0;
- s0=0: kein gespeicherter Zusatzstatus.

Für zwei Historien mit verschiedenen stückweise konstanten s-Werten kann Δξ am gleichen Endpunkt analytisch berechnet werden. Das liefert einen einfachen synthetischen Test B, ohne reale Daten zu fitten.

## 12. Kritischer Punkt: Determinismus

Der Primärkandidat erzeugt nur dann physikalisch relevante Historienseparation, wenn zwei zulässige kosmologische Lösungen am Vergleichspunkt denselben **vollständig definierten** Y besitzen können, obwohl ihre früheren H-Verläufe verschieden waren.

In einem strikt deterministischen Standardmodell mit vollständig spezifizierten Zustandsvariablen und festen Parametern kann das unmöglich oder redundant sein.

Daraus folgt eine wichtige Verschärfung:

> Test B darf nicht dadurch gewonnen werden, dass Y künstlich zu klein definiert wird.

Der nächste Test muss deshalb nicht zuerst reale Uhren fitten, sondern prüfen, ob der aktuelle Y-Begriff dynamisch vollständig ist und ob Historienseparation unter den Standardgleichungen überhaupt zulässig bleibt.

## 13. Entscheidung

Für die nächste Rechenstufe:

    s_B0.1(N) =
      - d ln H_std/dN - 3/2

    dξ/dN =
      κ [s_B0.1(N) - ξ]

    δ ln O_ij =
      λ ξ ΔS_ij·n

Dies ist die erste vollständig ausgeschriebene AVI-B0.1-Testkette.

Sie ist **kein kanonisches Naturgesetz** und keine empirische Evidenz. Ihr Zweck ist, AVI so konkret zu machen, dass die Konstruktion an mathematischer Redundanz oder experimentellen Grenzen scheitern kann.

## 14. Nächster Schritt

Vor einem Datenfit wird ein synthetischer Test-B-Notebook/Testfall benötigt:

1. zwei kontrollierte Historien konstruieren;
2. identischen Endzustand Y* erzwingen, ohne Komponenten von Y wegzulassen;
3. ξ_A und ξ_B berechnen;
4. prüfen, ob Δξ physikalisch zulässig oder nur Folge unvollständiger Zustandsdefinition ist;
5. erst bei Bestehen einen differentiellen O_ij-Test anschließen.

## 15. Epistemischer Status

- **[R]** H, d ln H/dN, q und Ω-Komponenten sind Standardgrößen der FLRW-Kosmologie.
- **[H]** Ein Relaxationszustand ξ könnte historische Information komprimieren.
- **[H]** s_q wird als erster AVI-Testtreiber gewählt.
- **[I]** Die ursprüngliche AVI-Intuition motiviert die Prüfung einer Relation zwischen lokaler Rate und globaler Entwicklung, entscheidet aber nicht über die physikalische Gültigkeit dieses Treibers.
