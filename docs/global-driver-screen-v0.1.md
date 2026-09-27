# AVI — Global-Driver Screen v0.1

**Stand:** 27. September 2026
**Status:** kritisches Driver-Gate nach Retention Observable Screen
**Ziel:** prüfen, ob für Test R eine unabhängig definierte globale Größe X existiert, die mehr ist als Zeitkoordinate, Standardkosmologie oder frei gewählte Historienfunktion.

## 1. Ausgangspunkt

Test R benötigt

    ln(O_k/O_k,std) = lambda K_k X

mit einem unabhängig bestimmten X, unabhängigen K_k und einem gemeinsamen lambda.

Das Gate darf X nicht danach auswählen, welches Residuum später am besten korreliert.

## 2. Anforderungen an X

X muss:
1. unabhängig beobachtbar oder aus unabhängig beobachteten Größen berechenbar sein;
2. dimensionslos oder natürlich normiert sein;
3. eine klare physikalische Bedeutung besitzen;
4. nicht bloß a, z oder kosmische Zeit umbenennen;
5. nicht bereits vollständig der lokale QFT/GR-Carrier sein;
6. ohne frei geformten History-Kernel auskommen;
7. vor einem lokalen Datenfit festgelegt werden können;
8. eine plausible gemeinsame Relation zu mehreren lokalen K_k erlauben.

## 3. X1 — Expansionsform epsilon_H = -d ln H / dN

Diese Größe ist dimensionslos und beschreibt die lokale Form der Hintergrundexpansion in e-fold-Zeit N=ln a. Sie steht eng mit dem Verzögerungsparameter q in Beziehung:

    epsilon_H = 1 + q.

### Stärke
- dimensionslos;
- kosmologisch interpretierbar;
- aus einer Expansionshistorie rekonstruierbar;
- der frühere B0.1-Treiber war eine zentrierte Variante davon.

### Problem
epsilon_H ist eine Standard-Hintergrundgröße. Eine lokale Kopplung

    delta ln O_k = lambda K_k epsilon_H

folgt aus keiner etablierten Physik. Sie wäre eine neue, ad hoc gesetzte Relation. Außerdem ist epsilon_H kein Gedächtnis: Es beschreibt den momentanen Verlauf der Expansion, nicht die Entstehungsgeschichte als zusätzliche Information.

### Urteil
**Geeignete Kontrollvariable; kein begründeter AVI-Driver.**

## 4. X2 — Dichteanteile Omega_i(a)

Omega_m, Omega_r, Omega_DE und gegebenenfalls Omega_k sind dimensionslose globale Hintergrundparameter.

### Stärke
- physikalisch klar;
- beobachtbar/re-konstruierbar;
- charakterisieren kosmologische Epochen.

### Problem
Auch sie sind Standardzustandsgrößen. Eine direkte differentielle Kopplung an lokale Frequenzverhältnisse wäre neue Physik ohne derzeitigen Mechanismus. Eine Kombination wie Omega_m-Omega_DE wäre zusätzlich eine willkürliche Feature-Auswahl, solange keine Theorie sie auszeichnet.

### Urteil
**Kosmologische Referenzgrößen; kein AVI-spezifisches X.**

## 5. X3 — globale/topologische Information

Räumliche Topologie ist echte globale Information, die nicht aus einer kleinen lokalen Umgebung vollständig bestimmt werden muss.

### Stärke
- erfüllt die ursprüngliche local/global-Motivation besonders sauber;
- ist nicht bloß eine Zeitkoordinate;
- besitzt standardtheoretische beobachtbare Konsequenzen über Moden/Korrelationen.

### Problem
Topologie ist typischerweise diskret plus geometrische Größen/Orientierungen und kein natürlicher universeller skalarer Driver. Wo sie lokale QFT-Response beeinflusst, gehört dieser Effekt bereits zum QFT+GR-Nullmodell.

### Urteil
**Starker Architekturbeweis; kein verbleibender universeller AVI-Driver.**

## 6. X4 — integrierte Expansionsgrößen

Man kann dimensionslose Integrale konstruieren, etwa

    I(a) = integral f(H/H0, q, Omega_i, ...) dN.

### Stärke
Sie kodieren tatsächlich Information über einen Abschnitt der Expansionsgeschichte.

### Problem
Ohne unabhängige Theorie ist die Wahl von f, Integrationsgrenze, Normierung und Gewichtung frei. Damit kehrt genau der History-Kernel zurück, den die Determinismus- und Residual-Gates ausgeschlossen haben.

Wenn I vollständig aus Standard-Hintergrundgrößen berechnet wird, ist es außerdem eine abgeleitete Standardgröße, keine zusätzliche Zustandsinformation.

### Urteil
**REJECT als primärer AVI-Driver ohne vorgängige Theorie.**

## 7. X5 — kosmologisches Alter H0 t oder ähnliche globale Clock-Größen

Dimensionslose Altersgrößen erscheinen zunächst attraktiv:

    X_age = H0 t.

### Problem
Sie sind modellabhängige Standardgrößen und koppeln nicht bekannt an lokale dimensionslose Ratenverhältnisse. Wird t als "seit dem Ursprung akkumulierte Zeit" interpretiert, wird zudem genau jene Ontologie vorausgesetzt, die AVI erst testen müsste.

### Urteil
**REJECT als AVI-Driver; nützliche Standarddiagnostik.**

## 8. X6 — Informations-/Entropiegrößen

Globale Entropie, Korrelationsmaße oder Informationsgrößen könnten philosophisch zur Frage des Werdens passen.

### Problem
Es existiert derzeit keine eindeutig definierte, beobachtbare, universelle kosmische Informationsgröße, die die Anforderungen an X erfüllt und eine bekannte differentielle lokale Kopplung besitzt. Unterschiedliche Entropiebegriffe betreffen unterschiedliche Sektoren und coarse grainings.

### Urteil
**Nicht hinreichend definiert; keine zulässige Auswahl.**

## 9. Screening-Ergebnis

Keiner der geprüften Kandidaten erfüllt gleichzeitig:
- unabhängige physikalische Definition,
- echten globalen Informationsgehalt jenseits bloßer Standardzustandsparameter,
- nichtredundante Rolle gegenüber QFT+GR,
- begründete Verbindung zu lokalen dimensionslosen Responsekanälen.

Daher:

    Global-Driver Gate:
      admissible reference variables = YES
      justified AVI-specific X = NO

## 10. Konsequenz für Test R

Test R bleibt eine gültige allgemeine Messarchitektur, besitzt derzeit aber keine AVI-spezifische Testinstanz.

Es wäre methodisch falsch, nun den "besten" X-Kandidaten auszuwählen und lambda gegen Präzisionsdaten zu fitten.

Datenfit bleibt:

    BLOCKED.

## 11. Konsequenz für Class B / O2

Der bisherige O2/Class-B-Pfad hat folgende Bilanz:

- globale Kontextinformation existiert: JA;
- globale Information kann lokale QFT-Response beeinflussen: JA;
- Standard-QFT liefert dafür Carrier: JA;
- bekannte Historienretention existiert: JA;
- Messarchitektur für zusätzliche Relation ist formulierbar: JA;
- unabhängiger AVI-spezifischer globaler Driver: NEIN;
- AVI-spezifische quantitative Vorhersage: NEIN.

Damit ist O2/Class B als **gegenwärtig konstruiertes physikalisches Modell nicht geschlossen**.

Es wird nicht durch zusätzliche freie Parameter gerettet.

## 12. Omnizedenz: die Alternative ohne messbares X

Die philosophische Formulierung "Der Ursprung ist das Ganze im Werden" muss nicht verlangen, dass es einen separaten messbaren Ursprungs- oder Werdensparameter gibt.

Eine logisch konsistente Möglichkeit ist:

    Werden ist konstitutiv für den jeweiligen Zustand,
    aber nicht als zusätzliche Variable neben diesem Zustand gespeichert.

Dann gilt nicht

    present state + X_becoming,

sondern das Gegenwärtige ist selbst das Resultat des Werdens, ohne dass "Gewordensein" als separater physikalischer Freiheitsgrad operational extrahiert werden muss.

Für Physik hat das eine klare Konsequenz:

> Ein prinzipiell nicht unterscheidbares X darf nicht Bestandteil einer empirischen AVI-Theorie sein.

Das widerspricht der Philosophie nicht. Es trennt vielmehr eine ontologische Aussage über Werden von einer empirischen Behauptung über zusätzliche messbare Zustandsinformation.

## 13. Wichtige Präzisierung

Die Aussage

    "X ist da, kann aber nicht entdeckt werden"

ist physikalisch zu stark, solange "da" eine zusätzliche physikalische Variable bedeuten soll.

Wissenschaftlich sauberer:

    Die Philosophie kann Werden als konstitutiv beschreiben,
    ohne zu behaupten, dass Werden durch eine zusätzliche
    gegenwärtige Observable X repräsentiert wird.

Ob es darüber hinaus ein physikalisches X gibt, bleibt eine empirische Frage. Der aktuelle Screen liefert keinen begründeten Kandidaten.

## 14. Status von AVI nach dem Gate

AVI sollte deshalb vorläufig zweigeteilt werden:

### AVI-P — physikalisches Forschungsprogramm
Offene Frage nach zusätzlichen relationalen/globalen Effekten, strikt gegen QFT+GR getestet. Kein X, xi oder Phi wird derzeit ontologisch vorausgesetzt.

### AVI-F — formale historische Konstruktion
Die bisherigen X/xi/Phi/C-Ansätze bleiben dokumentiert als getestete Modellfamilien einschließlich ihrer gescheiterten Gates.

Diese Trennung verhindert, dass eine philosophische Aussage über Werden durch eine unbegründete physikalische Variable erzwungen wird.

## 15. Entscheidung

    Global-Driver Screen:
      X1 epsilon_H/q ........ reference only
      X2 Omega_i ............ reference only
      X3 topology ........... QFT/GR null-model context
      X4 history integral ... reject without theory
      X5 cosmic age ......... reject as AVI driver
      X6 information ........ undefined

      AVI-specific X ........ NOT FOUND
      data fitting .......... BLOCKED
      O2/Class-B closure .... FAILS CURRENTLY

Dies ist kein Beweis, dass kein AVI-artiger Effekt existieren kann. Es ist das Ergebnis, dass wir ihn mit den bisherigen physikalischen Prinzipien nicht legitim herleiten können.

## 16. Nächster Schritt

Kein weiterer Driver soll erfunden werden.

Als nächstes wird ein **Theory Status Consolidation** erstellt:
- welche AVI-Aussagen die Gates überlebt haben;
- welche falsifiziert/gesperrt/redundant wurden;
- welche nur methodische Referenz sind;
- welche minimalen empirischen Befunde AVI wieder physikalisch aktivieren würden;
- klare Trennung von Omnizedenz-Heuristik und physikalischer Evidenz.

Danach kann entschieden werden, ob AVI als aktive Modelltheorie, als Forschungsprogramm oder als dokumentierte Null-/Grenzstudie weitergeführt wird.

## 17. Epistemischer Status

- **[R]** q, epsilon_H, Omega_i, kosmisches Alter und topologische Daten sind Standardkosmologie bzw. globale Standardinformation.
- **[D]** Aus ihrer Existenz folgt keine differentielle Kopplung an lokale Frequenzverhältnisse.
- **[D]** Frei gewählte Historienintegrale sind ohne vorgängige Theorie kein legitimer AVI-Driver.
- **[I]** Omnizedenz kann Werden als konstitutiv auffassen, ohne eine zusätzliche messbare Variable zu fordern.
- **[H]** Eine bislang unbekannte empirische globale/lokale Relation könnte künftig ein physikalisches AVI-Programm neu motivieren.
