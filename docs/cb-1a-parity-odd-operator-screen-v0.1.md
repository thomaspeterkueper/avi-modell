# CB-1A — Parity-odd Operator Screen v0.1

**Status:** HOLD — structurally possible, not AVI-specific  
**Datum:** 2026-09-27  
**Parent:** Cosmic Birefringence Observation Gate v0.1

## Forschungsfrage

Kann der aktive AVI-Pfad O1-minimal eine parity-odd Photonenkopplung unabhängig vom beobachteten cosmic-birefringence-Signal motivieren, so dass CB-1 eine AVI-spezifische Vorhersage statt bloßer Anomalieanpassung wird?

## Null- und Vergleichsklasse

Der minimale bekannte Lorentz- und gauge-invariante Mechanismus für isotrope kosmische Doppelbrechung ist eine pseudoskalare/axionartige Kopplung

L_int = -(g/4) χ F_{μν} F_tilde^{μν}.

Für ein zeitlich variierendes homogenes χ führt sie zu einer Rotation der linearen Polarisation. Diese Architektur ist etablierte Vergleichsphysik und darf nicht als AVI-Signatur etikettiert werden.

Weitere Vergleichsklassen:
- axion-like / pseudoscalar dark matter or dark energy;
- early-dark-energy pseudoscalar + photon coupling;
- Lorentz-/CPT-verletzende photon-sector EFTs;
- räumlich fluktuierende pseudoskalare Felder für anisotrope Rotation.

## Symmetrie-Gate

F F_tilde ist P-odd und CP-odd. Damit ein skalarer Lagrangedichteterm entsteht, muss der gekoppelte Koeffizient die passende pseudoskalare/parity-odd Struktur tragen oder die Theorie muss Parität explizit brechen.

Der derzeitige AVI-Zustand ξ bzw. Φ besitzt im Repository **keine unabhängig definierte pseudoskalare Transformationsregel**. Eine solche Eigenschaft allein wegen des Birefringenzsignals nachträglich zu vergeben wäre anomaly fitting.

**Ergebnis S1: FAIL für direkte Identifikation ξ/Φ = χ.**

## Operator-Minimalität

Kandidat O_CB1:
  (c_γ / 4Λ) χ_AVI F F_tilde

ist dimensions-5, gauge-invariant und als EFT strukturell zulässig, sofern χ_AVI ein geeigneter pseudoskalarer Freiheitsgrad ist. Er ist jedoch formal dieselbe Operatorfamilie wie bekannte axionartige Modelle.

**Ergebnis O1: PASS als bekannte EFT-Struktur; FAIL als AVI-spezifischer Operator.**

Ein konstanter Koeffizient vor F F_tilde ist im üblichen lokalen Fall topologisch und erzeugt nicht die gewünschte dynamische kosmische Rotation; relevant ist die Änderung des gekoppelten pseudoskalaren Zustands entlang des Photonenwegs.

## Beziehung zum AVI O1-minimal-Pfad

Das Minimal ξ Degree-of-Freedom Gate hatte bereits ergeben, dass ein zusätzlicher ξ-Zustand zunächst in bekannte zusätzliche-DOF/EFT-Klassen fällt. CB-1A bestätigt dieses Problem im Photonensektor.

Eine zulässige AVI-Verknüpfung müsste daher **vor** jedem Fit mindestens liefern:

1. physikalische Transformationseigenschaft des zusätzlichen Zustands;
2. unabhängige Selektionsregel, warum gerade der parity-odd Photonoperator erlaubt/erforderlich ist;
3. Normierung und Dynamik des Zustands ohne β als Input;
4. Backreaction-/Stabilitätsprüfung;
5. Konsistenz mit nicht-CMB Constraints derselben Kopplung;
6. Standardgrenze c_γ -> 0 oder äquivalente decoupling limit.

## Beobachtungsstatus 2026

Aktuelle ACT-DR6- und gemeinsame ACT+Planck-Analysen berichten isotrope Birefringenzsignale ähnlichen Vorzeichens/Größenordnung, betonen aber verbleibende Systematiken. Diese Resultate sind **Motivation für einen Testkanal, keine Modellselektionsregel**.

## Gate-Entscheidung

**CB-1A = HOLD.**

- PASS: parity-odd Photonenkopplung ist als bekannte EFT-Struktur physikalisch möglich.
- FAIL: keine derzeitige AVI-Struktur selektiert diese Kopplung unabhängig.
- Konsequenz: CB-1B darf noch **kein AVI-β fitten**.
- Freigabebedingung: Das übergeordnete Operator Minimality Gate muss eine AVI-interne Symmetrie-/Selektionsregel liefern, die den Photonoperator unabhängig vom Birefringenzsignal begründet.

## Kill criterion

Falls die einzige Herleitung lautet „AVI besitzt einen zusätzlichen Zustand; wir erklären ihn zum Pseudoskalar und koppeln ihn an F F_tilde“, ist CB-1 als AVI-spezifischer Mechanismus zu verwerfen und nur als externe Constraint-/Vergleichsklasse weiterzuführen.

## Erlaubter nächster Schritt

CB-1B wird in zwei Teile getrennt:

- **CB-1B0:** model-independent transfer kernel von einem generischen pseudoskalaren χ zu β/TB/EB; zulässig als Null-/Vergleichsmodell.
- **CB-1B1:** AVI-spezifisches Forward Model; BLOCKED bis Operator-Minimality-Freigabe.

Damit bleibt die mathematische Infrastruktur entwickelbar, ohne den aktuellen Beobachtungshinweis zur Theorieerzeugung zu verwenden.

## Referenzen

- Lue, Wang & Kamionkowski (1999), parity-violating CMB signatures.
- Liu, Lee & Ng (2006), quintessence/pseudoscalar electromagnetic coupling.
- Murai et al. (2023), isotropic birefringence from early dark energy.
- Murai et al. (2023), constraints on EDE from isotropic cosmic birefringence.
- Nilsson & Le Poncin-Lafitte (2024), generic EFT/spacetime-symmetry-breaking interpretation.
- Diego-Palazuelos et al. (2026), ACT DR6 cosmic birefringence.
- Eskilt (2026), joint ACT + Planck analysis.
