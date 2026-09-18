# AVI — S_i-Sensitivitätsmatrix v0.1

**Status:** Arbeitsdokument  
**Zweck:** Reale experimentelle Sensitivitätskanäle für die physikalische Systemsignatur `S_i` ordnen, ohne daraus bereits einen AVI-Mechanismus abzuleiten.

## 1. Ausgangspunkt

Für Class-B-AVI ist die elementare Observable ein dimensionsloses differentielles Ratenverhältnis

```text
O_ij = Γ_i / Γ_j
```

mit

```text
O_ij,AVI / O_ij,std = C_i / C_j .
```

Eine universelle gemeinsame Skalierung aller Prozesse ist in solchen lokalen Verhältnissen nicht beobachtbar. Ein testbarer Effekt benötigt daher unterschiedliche physikalische Sensitivitäten.

Für kleine Abweichungen verwenden wir als experimentelles Gerüst

```text
δ ln O_ij = Σ_A (K_i^A - K_j^A) δ ln q_A
```

mit etablierten dimensionslosen Größen `q_A`, etwa `α` oder dimensionslosen Massenverhältnissen. Das ist Standard-Sensitivitätsanalyse und noch keine AVI-Gleichung.

Eine mögliche AVI-Abbildung darf erst danach definiert werden:

```text
(Φ, ξ) -> u_AVI -> S_i -> δ ln O_ij .
```

Dabei kann `u_AVI` eine effektive Antwortstruktur bezeichnen. v0.1 behauptet ausdrücklich **nicht**, dass AVI fundamentale Konstanten zeitlich verändert.

## 2. Reale Sensitivitätsmatrix

| Kanal | Reale Observable / Referenz | Physikalische Sensitivität | Experimenteller Stand | Rolle für AVI |
|---|---|---|---|---|
| Optische Atomuhren: 27Al+, 171Yb, 87Sr | Frequenzverhältnisse `ν_i/ν_j` | unterschiedliche atomare/relativistische Sensitivitäten, insbesondere gegenüber dimensionslosen elektromagnetischen Parametern | Aeppli et al. 2026 berichten Gesamtunsicherheiten der gemessenen Frequenzverhältnisse von höchstens `3.2×10^-18` | stärkster lokaler differentieller Präzisionskanal; Messunsicherheit ist **keine** AVI-Grenze |
| Molekulare Übergänge | Verhältnis molekularer Übergangsfrequenzen zu atomarer Referenz | besonders empfindlich auf dimensionslose Massenverhältnisse wie `μ = m_p/m_e`, abhängig vom Übergang | etablierter unabhängiger Sensitivitätssektor; konkrete Molekül-/Übergangswahl muss für einen numerischen AVI-Test separat festgelegt werden | zweite, qualitativ andere Signaturachse neben atomaren Uhren |
| Nuklear / Oklo | historische Resonanzbedingungen natürlicher Spaltungsreaktoren | nukleare Resonanzen reagieren auf Kombinationen elektromagnetischer und starker/nuklearer Parameter | liefert einen geologischen Langzeitkanal; Umrechnung auf `α` ist modell- und kernphysikabhängig | langer historischer Hebel, aber nicht als modellfreie AVI-Grenze zu behandeln |
| Gravitation / MICROSCOPE | differentielle Beschleunigung von Ti- und Pt-Testmassen | Zusammensetzungsabhängigkeit / Weak Equivalence Principle | `η(Ti,Pt)=[-1.5 ± 2.3(stat) ± 1.5(syst)]×10^-15` (1σ); kein WEP-Verstoß gefunden | harte Konsistenzbedingung für neue sektorabhängige AVI-Kopplungen |
| Kosmologischer/geometrischer Referenzkanal | lokale Rate relativ zu unabhängig bestimmter kosmologischer/geometrischer Größe | keine automatische lokale Prozesssignatur; Referenz muss operational definiert werden | konzeptionell möglich, aber in AVI noch nicht geschlossen | besonders nah an der ursprünglichen lokalen-vs-globalen AVI-Frage; noch kein numerischer Test |

## 3. Was die Zahlen bedeuten — und was nicht

Die `3.2×10^-18` bei den optischen Frequenzverhältnissen ist eine **Messunsicherheit der konkreten Frequenzvergleiche**. Sie darf nicht als Grenze für `ξ`, `Φ` oder eine AVI-Kopplung zitiert werden.

Ebenso ist der MICROSCOPE-Wert eine experimentelle Grenze für eine mögliche Verletzung des Weak Equivalence Principle in der getesteten Ti/Pt-Konfiguration. Er wird erst dann zu einer AVI-Grenze, wenn AVI eine explizite Abbildung von `(Φ,ξ)` auf eine zusammensetzungsabhängige gravitative Kopplung postuliert.

Oklo besitzt einen langen Zeithebel, aber die Übersetzung von Resonanzdaten in Grenzen für einzelne dimensionslose Kopplungen benötigt Kernmodelle. Deshalb wird hier bewusst keine scheinbar modellfreie einzelne `Δα/α`-Zahl als AVI-Grenze übernommen.

## 4. Minimaler S_i-Raum für v0.1

Als experimentelles Koordinatengerüst kann

```text
S_i = (K_i^α, K_i^μ, K_i^nuc, K_i^grav, ...)
```

verwendet werden.

Die Einträge sind keine frei fitbaren AVI-Koeffizienten. Sie müssen aus unabhängiger Atom-, Molekül-, Kern- oder Gravitationstheorie beziehungsweise Kalibration stammen.

Für zwei Systeme gilt dann schematisch

```text
δ ln O_ij = (S_i - S_j) · u_AVI(Φ, ξ).
```

Diese Gleichung ist ein **Testgerüst**, keine kanonische fundamentale AVI-Dynamik.

Eine nützliche Zerlegung ist

```text
ln C_i = U(Φ,ξ) + S_i · D(Φ,ξ)
ln(C_i/C_j) = (S_i-S_j) · D(Φ,ξ).
```

Damit wird explizit sichtbar: Ein universeller Anteil `U` verschwindet aus lokalen Ratenverhältnissen. Nur ein differentieller Anteil kann dort beobachtet werden.

## 5. Konsequenz für Test B

Test B wird damit operational enger:

```text
Y_A(a*) = Y_B(a*)
ξ_A(a*) != ξ_B(a*)
S_i, S_j vor dem Vergleich festgelegt
=> [C_i/C_j]_A != [C_i/C_j]_B
=> O_ij,A != O_ij,B
```

Die letzte Zeile ist zwingend. Unterschiedliche interne Werte von `ξ`, `Φ` oder `C` ohne messbare differentielle Observable reichen nicht.

Zusätzlich müssen globale Struktur, Randbedingungen und alle Standardparameter, die das jeweilige Experiment beeinflussen, kontrolliert werden.

## 6. Falsifikations- und Modellierungsgrenzen

Ein Class-B-Modell verliert physikalischen Gehalt, wenn

1. für jedes Experiment ein eigener freier Kopplungskoeffizient nachträglich gewählt wird;
2. `S_i` erst aus einer beobachteten Anomalie definiert wird;
3. die erlaubte Kopplung ausschließlich common-mode ist und damit aus allen dimensionslosen lokalen Ratenverhältnissen verschwindet;
4. eine postulierte neue sektorabhängige Kopplung bestehende Uhren-, WEP- oder andere Präzisionsgrenzen verletzt;
5. `ξ` bei vollständig gleichem kontrolliertem Gegenwartszustand nicht historienabhängig verschieden sein kann;
6. unterschiedliche `ξ` keine messbare Observable erzeugen.

## 7. Nächster mathematischer Schritt

Nicht weitere Prozessklassen sammeln, sondern eine minimale Kopplungsfamilie definieren. Sie muss vor einem Datenfit festlegen,

- welche Komponenten von `S_i` AVI überhaupt anspricht,
- wie `D(Φ,ξ)` dimensional und dynamisch definiert ist,
- welche Parameter global geteilt werden,
- welche Observable zuerst vorhergesagt wird,
- und wie der Nullfall exakt auf Standardphysik zurückfällt.

Erst danach dürfen die experimentellen Zahlen dieser Matrix in numerische AVI-Grenzen übersetzt werden.

## 8. Referenzen

- Aeppli et al. (2026), *Optical clock frequency ratios with uncertainty ≤ 3.2 × 10^-18*, NIST/arXiv 2512.21428.
- Beloy et al. (2021), *Frequency Ratio Measurements with 18-Digit Accuracy Using a Network of Optical Clocks*, Nature 591.
- Touboul et al. (2022), *MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle*, Physical Review Letters 129, 121102.
- Davis & Hamdan (2015), *Reappraisal of the limit on the variation in α implied by the Oklo natural fission reactors*, Physical Review C 92, 014319.
- Uzan (2003), *The fundamental constants and their variation: observational and theoretical status*, Reviews of Modern Physics 75, 403.

## Epistemischer Status

- **[R]** Die genannten experimentellen Messkanäle und publizierten Messwerte.
- **[H]** Die Annahme, dass ein AVI-Zustand `(Φ,ξ)` überhaupt lokal differentielle Raten beeinflusst.
- **[H]** Die Abbildung `(Φ,ξ) -> u_AVI`.
- **[I]** Philosophische Motivation durch Teil/Ganzes, Werden oder Omnizedenz; sie ist keine physikalische Evidenz und kein Bestandteil der Gleichungen.
