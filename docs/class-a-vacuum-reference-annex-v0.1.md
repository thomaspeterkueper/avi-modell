# AVI — Referenzannex Klasse A: dynamische Vakuumenergie und Λ(H,Ḣ)-Reduktionsgate v0.1

**Stand:** 28. November 2026  
**Status:** Referenzannex zum [`dynamischen Closure-Vertrag v0.1`](dynamical-closure-contract-v0.1.md) §7 und Struktur-Gate zu §9/§10 – keine Kanonänderung, kein Datenfit  
**Anlass:** [`EXT-KG-AVI-20261126-001`](../external-tasks/done/EXT-KG-AVI-20261126-001.md), [`EXT-KG-AVI-20261126-002`](../external-tasks/done/EXT-KG-AVI-20261126-002.md)  
**Grundlage:** Research Candidate `RES-20260916-0D488933` in `kueper-knowledge-graph/research/candidates/` (nicht-kanonisch)

## 1. Zweck und Grenze

Der Closure-Vertrag verlangt für Klasse A (`H² = H_std² + ΔH_AVI²`) eine konsistente Energie-/Gravitationsinterpretation von `ΔH_AVI²`, lässt sie aber offen. Dieses Dokument hält fest,

1. welche **externe, etablierte Literatur** einen solchen Hintergrundbeitrag bereits mit definiertem ΛCDM-Nullfall und Bianchi-konsistenter Implementierung beschreibt (Teil A, Referenzannex),
2. ob eine **reine Λ(H,Ḣ)-Closure** überhaupt ein Träger von Test B sein kann (Teil B, Reduktionsgate).

Alles in Teil A ist externe Literatur und **keine AVI-Evidenz**. Teil B ist eine modellinterne mathematische Prüfung. Unverändert bleiben: Definition von Klasse A, `ξ`, `Φ`, Priorisierung von Klasse B (§11) und die Datenfit-Sperre. Der Kandidat erfüllt keinen Reaktivierungstrigger T1–T4 der [Theory Status Consolidation](theory-status-consolidation-v0.1.md).

## Teil A – Referenzannex: etablierter Unterbau für Klasse A

### A.1 Drei Modellfamilien

| Familie | Form des Vakuumbeitrags | Nullfall | Bianchi-Implementierung | Kernquellen |
|---|---|---|---|---|
| Running Vacuum (RVM) | `ρ_vac(H) = (3/8πG_N)(c₀ + νH² + ν̃Ḣ) + O(H⁴)` | `ν = ν̃ = 0` ⇒ ΛCDM | Typ I: Energieaustausch Vakuum–CDM bei festem `G`, `ρ_m ∝ a^{−3(1−ν)}` (ohne Strahlung); Typ II: Materie erhalten, `G(H)` läuft logarithmisch | [Q1], [Q2], [Q6] |
| Vakuum-Metamorphose (Parker–Raval) | Rückwirkung eines ultraleichten Skalarfeldes fixiert nach dem Übergang `R = 6(Ḣ + 2H² + k a⁻²) = m²` | `Ω_* = Ω_m` (Übergang erst bei `z = 0`) ⇒ ΛCDM | Effektivwirkung ist kovariant; kosmologische Standardimplementierung lokal reduziert | [Q7], [Q8], [Q9] |
| Zerfallendes / interagierendes Vakuum Λ(t)CDM | `ρ̇_Λ = −Q`, `ρ̇_m + 3Hρ_m = +Q`, z. B. `Q = 3εHρ_Λ` oder `Q = 3εaHρ_Λ` | `ε = 0` ⇒ ΛCDM | Energieaustausch bei festem `G` | [Q10], [Q11], [Q12] |

### A.2 Publizierte Grenzen und Befunde

| Kanal | Aussage | Quelle | Prüfstand dieses Laufs |
|---|---|---|---|
| BBN | Freeze-out-Bedingung `|δT_f/T_f| < 4,7·10⁻⁴` als Grenze für modifizierte Expansion | [Q4] | **verifiziert** (Gl. 53 der Arbeit) |
| BBN, einfachstes RVM | `−0,0023 ≲ ν ≲ 0,0023` | [Q4] laut Kandidat | **nicht verifiziert** – im Volltext nicht bestätigt; die Arbeit nennt im Modellansatz `ν > 0`. Vor jeder Verwendung am PDF prüfen |
| BBN, RVM mit H⁴-Term | Variante mit `c₂ ≥ 0` erfüllt die BBN-Grenze nicht | [Q4] laut Kandidat | **nicht verifiziert**; Abstract sagt „all models can satisfy the BBN constraints“ – Widerspruch offen |
| `Ġ/G` (Typ II) | `|ν_eff| ≲ (2–5)·10⁻⁴` aus Pulsar-/Sonnensystemgrenzen | [Q1] laut Kandidat | **nicht verifiziert** (Seite in diesem Lauf nicht erreichbar) |
| Fundamentalkonstanten | RVM koppelt Drift von α, α_s, G, m_p/m_e an denselben RG-Fluss, `Ṗ/P ∝ H` | [Q5] laut Kandidat | nicht erneut geprüft |
| Vakuum-Metamorphose ohne Λ (`Ω_* = 1`) | SNe, CMB und BAO untereinander inkonsistent, `Δχ² = 28,5` relativ zu flachem ΛCDM; mit `Ω_* ≠ 1` Konkordanz | [Q9] | **verifiziert** (Rubin et al., Abschnitt 7) |
| Frequentistisch vs. Bayes | `ν = 0,0054 ± 0,0011`, aber Bayes-Faktor `0,0162 < 1` zugunsten ΛCDM | [Q3] laut Kandidat | **nicht verifiziert** (Seite nicht erreichbar) |
| Rekonstruierte Vakuum–CDM-Kopplung | „no meaningful evidence for deviation from the null interacting case, i.e. ΛCDM“ | [Q11] | **verifiziert** (Abstract) |
| DESI-Ära | „geflipptes“ RVM mit Evidenz vergleichbar zu w₀wₐCDM | [Q13] laut Kandidat | **nicht verifiziert**; Existenz der Arbeit in diesem Lauf nicht geprüft |

**Einordnung:** Der etablierte Charakter von Λ(H) als Bianchi-konsistenter Hintergrund mit ΛCDM-Nullfall ist durch die Quellen in A.1 gedeckt. Die Zahlenwerte mit „nicht verifiziert“ sind Sekundärangaben des Kandidaten und dürfen in AVI-Dokumenten erst nach Prüfung am Original verwendet werden.

### A.3 Verbindliche Positionierungsregel für künftige Klasse-A-Formulierungen

Jede künftige Klasse-A-Variante muss vor der Formulierung angeben:

1. Abgrenzung gegen den RVM-Nullfall: Welcher Anteil von `ΔH_AVI²` ist nicht bereits durch `c₀ + νH² + ν̃Ḣ` (Typ I oder II) beschreibbar?
2. Positionierung gegenüber BBN- und `Ġ/G`-Grenzen (nach deren Verifikation, siehe A.2).
3. Welche Bianchi-Implementierung gewählt ist (Energieaustausch oder laufendes `G`) und ob dadurch Klasse-B-Kanäle (Konstantendrift) berührt werden – sonst droht eine unerklärte Klasse C (§7).
4. Das Ergebnis von Teil B: Ohne zusätzlichen, nicht auf `Y` reduzierbaren Anteil ist die Variante kein Test-B-Träger.

## Teil B – Reduktionsgate: Ist eine reine Λ(H,Ḣ)-Closure ein Test-B-Träger?

### B.1 Gate-Frage

Prüfgegenstand sind die Kandidatenaussagen C23/C24: Ein Modell mit `ρ_vac = ρ_vac(H, Ḣ)` besitzt dieselbe Zahl unabhängiger Daten wie ΛCDM und ist durch den momentanen Standardzustand `Y(a*)` vollständig bestimmt; daher ist `Y_A(a*) = Y_B(a*)` bei `ξ_A(a*) ≠ ξ_B(a*)` nicht realisierbar (Closure-Vertrag §9/§10).

**Annahmen:** flacher FLRW-Hintergrund (Krümmung analog); `Y(a*) ⊇ {a, H, ρ_m, ρ_r}`; Vakuum mit `p_vac = −ρ_vac` (RVM, Λ(t)CDM); Strahlung separat erhalten; Parameter (`c₀, ν, ν̃, ε, m²`) vor dem Vergleich fest. Unabhängige Variable `N = ln a`.

### B.2 RVM Typ I (festes G, Energieaustausch mit CDM)

Aus der Bianchi-Identität folgt bei `p_vac = −ρ_vac` die zweite Friedmann-Gleichung unabhängig von `ρ_vac`:

`Ḣ = −4πG (ρ_m + 4/3 ρ_r)`.

Eingesetzt in `ρ_vac = (3/8πG)(c₀ + νH² + ν̃Ḣ)` und die erste Friedmann-Gleichung:

`(1 − ν) H² = (8πG/3) [ (1 − 3ν̃/2) ρ_m + (1 − 2ν̃) ρ_r ] + c₀`.

`H` ist damit eine **algebraische** Funktion von `(ρ_m, ρ_r)`, ebenso `ρ_vac`. Für `ν̃ = 0` liefert die Erhaltung des Gesamtsystems mit `ρ_r ∝ a⁻⁴`

`dρ_m/dN = −3(1 − ν) ρ_m + 4ν ρ_r`,

ohne Strahlung `ρ_m ∝ a^{−3(1−ν)}` in Übereinstimmung mit der Literatur. Für `ν̃ ≠ 0` ergibt sich analog eine lineare Gleichung erster Ordnung in `ρ_m` mit `a`-abhängigen Koeffizienten. Das Zustandssystem ist `(ρ_m, ρ_r)` mit linearer, also Lipschitz-stetiger rechter Seite. Nach dem Eindeutigkeitssatz (Picard–Lindelöf) legt `(ρ_m, ρ_r)` bei `a*` die gesamte Lösung vorwärts und rückwärts fest.

**Freie Daten:** `ρ_m0, ρ_r0` und die Parameter `c₀, ν, ν̃` – gegenüber ΛCDM (`ρ_m0, ρ_r0, Λ`) kein zusätzliches Anfangsdatum, nur zusätzliche Parameter.

### B.3 RVM Typ II (Materie erhalten, laufendes G)

`ρ_m ∝ a⁻³`, `ρ_r ∝ a⁻⁴` sind fest. Aus `G ρ_vac = (3/8π)(c₀ + νH² + ν̃Ḣ)` und der ersten Friedmann-Gleichung folgt `G` algebraisch aus `(a, H)` (für `ν̃ = 0`: `G = 3[(1−ν)H² − c₀] / [8π(ρ_m + ρ_r)]`). Die Bianchi-Bedingung reduziert sich auf eine **Gleichung erster Ordnung für H(N)**. Einziges zusätzliches Anfangsdatum ist `G(a₀) = G_N` bzw. äquivalent `H₀` – es ersetzt die Rolle von `G_N` in ΛCDM, ist also kein neues Datum.

**Wichtig:** Damit gilt die Reduktion nur, wenn `H(a*)` Bestandteil von `Y` ist (so in §2 des Closure-Vertrags). `G(a*)` folgt dann algebraisch. Ein unabhängig evolvierendes `G` mit eigener Dynamik wäre ein skalar-tensorisches Modell und gehört nicht mehr zu dieser Familie.

### B.4 Vakuum-Metamorphose (lokale Standardimplementierung)

Vor dem Übergang: ΛCDM-artig (bzw. mit VEV-Konstante). Nach dem Übergang: `Ḣ = m²/6 − 2H²` (flach) – eine autonome Gleichung erster Ordnung für `H`; `ρ_vac = 3H²/8πG − ρ_m − ρ_r` folgt algebraisch aus `Y`. Die Phase (vor/nach dem Übergang) ist aus `Y(a*)` ablesbar, weil `ρ_vac` vor dem Übergang verschwindet bzw. gleich der VEV-Konstante ist und danach nicht; ausgenommen ist nur der Übergangspunkt selbst. Freie Daten: `ρ_m0, ρ_r0` und die Parameter `m²` bzw. `Ω_*`.

### B.5 Zerfallendes Vakuum Λ(t)CDM

`dρ_Λ/dN = −3ε ρ_Λ` (Modell I) bzw. `−3εa ρ_Λ` (Modell II); `dρ_m/dN = −3ρ_m + 3ε ρ_Λ` (bzw. mit Faktor `a`). Hier ist `ρ_Λ` eine **dynamische Zustandsvariable**, deren Anfangswert `ρ_Λ0` die Rolle von `Λ` in ΛCDM übernimmt. Das lineare System `(ρ_m, ρ_r, ρ_Λ)` ist eindeutig lösbar. Die Reduktion auf `Y` gilt, weil `Y` nach §2 „ρ_Λ bzw. Standard-DE-Parameter“ enthält; unter Flachheit folgt `ρ_Λ(a*)` ohnehin aus `H(a*)` und den übrigen Dichten.

### B.6 Ergebnis

| Rahmen | Reduktion auf `Y(a*)` | Zusätzliches Anfangsdatum ggü. ΛCDM | Test-B-Träger |
|---|---|---|---|
| RVM Typ I, `c₀ + νH² + ν̃Ḣ` | ja, algebraisch + lineare ODE erster Ordnung | nein | **nein – bestanden** |
| RVM Typ II, laufendes `G(H)` | ja, sofern `H ∈ Y` | nein (`G₀` ersetzt `G_N`) | **nein – bestanden** |
| Vakuum-Metamorphose, lokale Form `R = m²` | ja, Phase aus `Y` ablesbar (außer Übergangspunkt) | nein | **nein – bestanden** |
| Λ(t)CDM mit `Q ∝ Hρ_Λ` | ja, sofern `ρ_Λ ∈ Y` bzw. Flachheit | nein (`ρ_Λ0` ersetzt `Λ`) | **nein – bestanden** |
| RVM höherer adiabatischer Ordnung mit Termen in `Ḧ` | nicht gezeigt: ein `Ḧ`-Term macht die Friedmann-Gleichung formal zweiter Ordnung und könnte ein zusätzliches Anfangsdatum einführen; in der Praxis wird perturbativ ordnungsreduziert | offen | **offen** |
| Nichtlokale Parker–Raval-Effektivwirkung ohne Reduktion auf `R = m²` | nicht gezeigt; Gedächtnisstruktur möglich, aber kein ausgearbeitetes Modell | offen | **offen** |

**Gate-Urteil:** `PASS` für C23/C24 in den Standardimplementierungen. Für die drei Rahmen ist die Aussage nicht mehr bloße Inferenz, sondern hier hergeleitet – mit den Annahmen in B.1. **Klasse A in reiner Λ(H,Ḣ)-Form ist kein Test-B-Träger.** Klasse A bleibt als kosmologische Vergleichsvariante zulässig. Ein Test-B-Pfad über Klasse A setzt einen zusätzlichen, ausdrücklich nicht auf `Y(a*)` reduzierbaren Anteil voraus. Die beiden offenen Zeilen sind **offene Verifikationsaufgaben vor jeder Klasse-A-Nutzung**, die sich auf höhere Ordnung oder Nichtlokalität stützt.

Die Herleitung ist AVI-intern und keine Literaturbehauptung. Sie folgt aus den publizierten Gleichungen und dem Eindeutigkeitssatz für gewöhnliche Differentialgleichungen. Ein eigener Literaturbeweis wurde nicht gesucht.

## Quellen

Prüfstand: „verifiziert“ = Titel und Autoren am arXiv-Eintrag bzw. Volltext am 28.11.2026 geprüft; übrige Angaben aus dem Research Candidate übernommen.

- [Q1] J. Solà Peracaula, A. Gómez-Valent, J. de Cruz Pérez, C. Moreno-Pulido, „Running vacuum in the Universe: phenomenological status in light of the latest observations, and its impact on the σ₈ and H₀ tensions“, *Universe* 9, 262 (2023), arXiv:2304.11157 – nicht erneut geprüft.
- [Q2] C. Moreno-Pulido, J. Solà Peracaula, S. Cheraghchi, „Running vacuum in QFT in FLRW spacetime …“, *Eur. Phys. J. C* 83, 637 (2023), arXiv:2301.05205 – nicht erneut geprüft.
- [Q3] Sarath N., T. K. Mathew, „Running vacuum model versus ΛCDM – a Bayesian analysis“, *MNRAS* 510, 5553 (2022), arXiv:2105.03084 – nicht erneut geprüft.
- [Q4] P. Asimakis, S. Basilakos, N. E. Mavromatos, E. N. Saridakis, „Big Bang Nucleosynthesis constraints on higher-order modified gravities“, arXiv:2112.10863 – Autoren und Gl. 53 verifiziert; Zeitschriftenangabe (*Phys. Rev. D* 105, 084010) laut Kandidat, nicht geprüft.
- [Q5] H. Fritzsch, J. Solà, R. C. Nunes, „Running vacuum in the Universe and the time variation of the fundamental constants of Nature“, *Eur. Phys. J. C* 77, 193 (2017), arXiv:1605.06104 – nicht erneut geprüft.
- [Q6] S. Basilakos, N. E. Mavromatos, J. Solà Peracaula, „Scalar Field Theory Description of the Running Vacuum Model: the Vacuumon“, arXiv:1901.06638 – Autoren verifiziert.
- [Q7] L. Parker, A. Raval, *Phys. Rev. D* 60, 123502 (1999); „Vacuum-driven Metamorphosis“, arXiv:gr-qc/9908069 – nicht erneut geprüft.
- [Q8] E. Di Valentino, E. V. Linder, A. Melchiorri, „H₀ Ex Machina: Vacuum Metamorphosis and Beyond H₀“, *Phys. Dark Universe* 30, 100733 (2020), arXiv:2006.16291 – nicht erneut geprüft.
- [Q9] D. Rubin, E. V. Linder, M. Kowalski, G. Aldering, R. Amanullah et al. (Supernova Cosmology Project), „Looking Beyond Lambda with the Union Supernova Compilation“, *ApJ* 695, 391 (2009), arXiv:0807.1108 – Autoren und `Δχ² = 28,5` verifiziert.
- [Q10] Y. Yang, Y. Wang, X. Dai, „Cosmological constraints on two vacuum decay models“, *Eur. Phys. J. C* 85, 224 (2025), arXiv:2502.17792 – nicht erneut geprüft.
- [Q11] N. B. Hogg, M. Bruni, R. Crittenden, M. Martinelli, S. Peirone, „Latest evidence for a late time vacuum–geodesic CDM interaction“, *Phys. Dark Universe* 29, 100583 (2020), arXiv:2002.10449 – Autoren und Kernaussage verifiziert.
- [Q12] Y.-H. Li, J.-F. Zhang, X. Zhang, „Testing models of vacuum energy interacting with cold dark matter“, arXiv:1506.06349 – Autoren verifiziert.
- [Q13] J. de Cruz Pérez, A. Gómez-Valent, J. Solà Peracaula, „Dynamical Dark Energy models in light of the latest observations“, arXiv:2512.20616 (laut Kandidat *Phys. Rev. D* 113, 083521) – nicht geprüft.

Weitere Kandidatenquellen (ΛXCDM-Preprints arXiv:2607.26050, arXiv:2410.20382, arXiv:2608.23633) werden hier nicht verwendet.
