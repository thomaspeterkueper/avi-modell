# AVI — Dynamischer Closure-Vertrag v0.1

Stand: 15. September 2026  
Status: Arbeitsdokument / Grundlagenphase

## 1. Zweck

Dieses Dokument definiert, welche mathematischen Beziehungen AVI noch benötigt, bevor aus der konzeptionellen Kette

`X → ℱ → Z_AVI=(Y, ξ) → Q → Φ → C → AVI-Wirkung`

eine quantitativ prüfbare kosmologische Dynamik wird.

Der Closure-Vertrag ist bewusst **keine Wahl einer konkreten AVI-Dynamik**. Er verhindert, dass eine funktionale Form nur deshalb eingeführt wird, weil sie aktuelle Daten besser fitten könnte.

## 2. Standardkosmologischer Unterbau

Als Referenz wird zunächst ein räumlich homogener und isotroper FLRW-Hintergrund verwendet. Der Standardzustand sei schematisch

`Y(a) = {a, H, ρ_m, ρ_r, ρ_Λ bzw. Standard-DE-Parameter, k, ...}`.

Welche Komponenten tatsächlich zu `Y` gehören, muss für jeden Test explizit angegeben werden. Globale Randbedingungen und Topologie werden separat kontrolliert, sofern sie für den betrachteten Test relevant sind.

Im Nullfall muss AVI exakt auf das gewählte Standardmodell zurückfallen. Für Flat-ΛCDM bedeutet das insbesondere

`H_std(a)^2 = H0^2 [Ω_r a^-4 + Ω_m a^-3 + Ω_Λ]`

unter den jeweils verwendeten Konventionen und Erweiterungen.

## 3. Zusätzlicher AVI-Zustand

Arbeitsdefinition:

`Z_AVI(a) = (Y(a), ξ(a))`.

`ξ` bezeichnet die minimale zusätzliche Zustandsinformation, die benötigt würde, falls `Y(a*)` allein den für AVI relevanten Zustand am Zeitpunkt `a*` nicht festlegt.

Damit `ξ` physikalisch mehr ist als eine Umbenennung der Vergangenheit, muss es mindestens geben:

1. eine eindeutige Evolutionsregel für `ξ`;
2. definierte Anfangs- oder Randbedingungen;
3. eine Abbildung von `ξ` auf eine physikalische Größe `Q`, `Φ` oder `C`;
4. einen beobachtbaren Unterschied gegenüber einem Modell ohne `ξ`;
5. einen wohldefinierten Nullfall, in dem dieser Unterschied verschwindet.

## 4. Historienfunktional ℱ

`ℱ` ist zunächst ein Operator auf der bis `a` realisierten kosmologischen Historie:

`ℱ_a : X|_[a_i,a] → ξ(a)`.

Diese Schreibweise legt **nicht** fest, dass `ℱ` ein einfaches Integral ist. Sie hält nur fest, dass die AVI-Hypothese eine mögliche Kompression historischer Information in einen aktuellen Zusatzstatus untersucht.

Eine zulässige spätere Realisierung muss angeben:

- welche Eingangsgrößen aus `X` verwendet werden;
- ob die Entwicklung lokal als Differentialgleichung oder nichtlokal als Funktional formuliert wird;
- welche Dimension und Einheit `ξ` besitzt;
- wie Normalisierung und Anfangswert gewählt werden;
- ob zwei verschiedene Historien tatsächlich denselben `Y(a*)`, aber verschiedenes `ξ(a*)` erreichen können.

## 5. Φ als integrierte Arbeitsgröße

Für die bisherige AVI-Arbeit bleibt `Φ(a)` eine mögliche integrierte Arbeitsgröße. Eine allgemeine Kandidatenform ist

`Φ(a) = ∫[a_i→a] W(a', Y(a'), ξ(a'); θ) da'`.

`W` und die Parameter `θ` sind **nicht festgelegt**. Diese Gleichung ist ein Formvertrag, kein postuliertes Naturgesetz.

Wichtig: `Φ` ist in diesem Arbeitsmodell kein räumlich propagierendes Skalarfeld. Eine spätere Theorieversion müsste ausdrücklich begründen, falls dieser Scope geändert werden sollte.

## 6. Kopplungsgröße C

Damit AVI beobachtbar wird, braucht es eine Kopplungsabbildung

`C(a) = G(Y(a), ξ(a), Φ(a); θ_C)`.

Der Nullfall muss definiert sein, beispielsweise schematisch durch

`C(a) → C_std`

für einen bestimmten Parametergrenzwert oder für verschwindende AVI-Zusatzinformation.

Noch offen ist, **wo** `C` in die physikalische Dynamik eingreift. Diese Stelle darf nicht implizit bleiben.

## 7. Drei logisch getrennte Closure-Klassen

Für die nächste Modellentscheidung werden drei Klassen unterschieden.

### Klasse A — Expansionskopplung

`C` verändert direkt die Hintergrundexpansion, schematisch

`H^2(a) = H_std^2(a) + ΔH_AVI^2(Y, ξ, Φ)`.

Dann sind `H(z)`, `d_L(z)`, `d_A(z)` und `mu(z)` direkt berechenbare AVI-Observablen. Diese Klasse ist unmittelbar mit SNe/BAO/CMB vergleichbar, verlangt aber eine konsistente Energie-/Gravitationsinterpretation von `ΔH_AVI`.

### Klasse B — Ratenkopplung bei unveränderter Hintergrundexpansion

`H(a)=H_std(a)`, während AVI eine andere physikalische Rate `Γ` koppelt:

`Γ_AVI(a) / Γ_ref(a) = R(C(a))`.

Diese Klasse entspricht stärker der ursprünglichen Frage nach lokalen Raten relativ zu globalen kosmologischen Referenzparametern. Supernova-Distanzen testen sie nicht automatisch; es muss zuerst festgelegt werden, welche messbare Rate betroffen ist.

### Klasse C — gekoppelte Expansion und Rate

Sowohl Hintergrundexpansion als auch lokale/physikalische Rate hängen von `C` ab. Diese Klasse ist am flexibelsten, aber auch am stärksten gefährdet durch Parameterentartung und nachträgliche Anpassung. Sie darf erst betrachtet werden, wenn A und B sauber voneinander verstanden sind.

**Arbeitsregel:** Klasse A, B und C werden nicht vermischt. Eine konkrete AVI-Version muss genau eine Closure-Klasse deklarieren.

## 8. Observable-Pipeline

Falls die gewählte Closure-Klasse `H(z)` verändert, gilt anschließend die übliche geometrische Pipeline. Im räumlich flachen Referenzfall:

`D_C(z) = c ∫[0→z] dz' / H(z')`

`d_L(z) = (1+z) D_C(z)`

`mu(z) = 5 log10[d_L(z)/10 pc]`.

Damit wird die Kette für Distanzdaten vollständig:

`AVI-Dynamik → H(z) → d_L(z) → mu(z) → Likelihood`.

Diese Standardbeziehungen sind keine AVI-Postulate. AVI muss den vorgelagerten dynamischen Teil liefern.

## 9. Test B als Closure-Prüfung

Ein gültiger Test-B-Kandidat muss nach Wahl der Closure zeigen:

`Y_A(a*) = Y_B(a*)`

bei kontrollierten Standard-Randbedingungen, zugleich

`ξ_A(a*) ≠ ξ_B(a*)`,

und schließlich einen durch die deklarierte Closure verursachten Unterschied

`O_A(a*) ≠ O_B(a*)`

für mindestens eine explizite Observable `O`.

`C_A ≠ C_B` allein reicht als Endpunkt nicht, solange `C` nicht auf eine messbare Größe abgebildet ist.

## 10. Falsifizierbarkeitsbedingungen

Eine konkrete AVI-Closure ist wissenschaftlich brauchbar, wenn mindestens folgende Punkte erfüllt sind:

- Nullmodell reproduzierbar;
- Parameter vor dem Datenvergleich definiert;
- Einheiten und Dimensionen konsistent;
- Anfangsbedingungen spezifiziert;
- mindestens eine Observable berechenbar;
- mindestens ein Bereich des Parameterraums durch Daten ausschließbar;
- Test B kann prinzipiell scheitern, etwa wenn `ξ` bei identischem vollständigem `Y` notwendig ebenfalls identisch ist oder keine Observable beeinflusst.

## 11. Unmittelbar nächste Entscheidung

Der nächste Schritt ist **nicht** die Wahl von `W(a)` oder eines Fitparameters. Zuerst muss entschieden werden, welche Closure-Klasse die enge AVI-Hypothese tatsächlich behauptet:

- **A:** AVI verändert kosmische Expansion;
- **B:** AVI verändert eine lokale/physikalische Rate relativ zu einer kosmologischen Referenz, während die Standardexpansion unverändert bleibt;
- **C:** beides.

Nach dem bisherigen Scope ist **Klasse B der konservativste und konzeptionell nächstliegende Ausgangspunkt**. Klasse A bleibt als separat prüfbare kosmologische Variante erhalten. Diese Priorisierung ist eine Arbeitsentscheidung, kein empirisches Ergebnis.
