# Cosmic Birefringence Observation Gate v0.1

**Status:** Forschungsnotiz / Beobachtungskanal, kein Evidenzclaim für AVI  
**Datum:** 2026-09-25

## Anlass

Lonappan, Keating & Arnold (2026) führen einen birefringence-blinden differentiellen Kalibrationstest an acht Planck-NPIPE-Detector-Set-Maps durch. Die rekonstruierte detectorabhängige Kalibrationsstruktur stimmt mit dem Minami-Komatsu-Pfad überein (χ²=8.18 für 7 Freiheitsgrade, PTE=0.32). Die Autoren betonen, dass dies wegen derselben Eingangsdaten keine unabhängige Datenbestätigung einer kosmischen Doppelbrechung ist. Eine bedingte Common-Mode-Rekonstruktion ergibt β = 0.37 ± 0.12 deg.

Primärquelle: Lonappan, Keating & Arnold, *Differential Polarization Calibration: A Consistency Test for Cosmic Birefringence*, ApJL (2026), arXiv:2609.09149.

## Epistemische Einordnung

Der Messwert wird in AVI ausschließlich als **conditional observational anchor** geführt. Er ist weder Nachweis neuer Physik noch Evidenz für AVI. Instrumentelle Winkelkalibration, galaktische Vordergründe und das vollständige QFT+GR/ΛCDM-Nullmodell müssen vor jedem AVI-Residualclaim modelliert werden.

## Neuer AVI-Beobachtungskanal

Ein zusätzlicher AVI-Zustand darf nur dann mit CMB-Polarisation gekoppelt werden, wenn die Kopplung unabhängig vom beobachteten β präregistriert und aus dem aktiven O1-minimal-/Operator-Minimality-Pfad motiviert wird.

Arbeitsform:

β_AVI = ∫[a_rec,1] F(ξ(a), Φ(a), W(a); θ) d ln a

Diese Gleichung ist zunächst **nur eine Testschablone**. F, θ sowie die physikalische Bedeutung von Φ/W in diesem Kanal sind nicht definiert und dürfen nicht durch Fit an β=0.37 deg konstruiert werden.

## Falsifikationsstruktur

1. **Nullmodell zuerst:** instrumentelle Kalibration + Vordergründe + Standardphysik.
2. **Isotropie:** Ein rein globaler AVI-Zustand legt als Minimalhypothese einen führenden Monopolterm β0 nahe. Ein anisotroper Anteil δβ(n) benötigt zusätzliche Freiheitsgrade und darf nicht stillschweigend eingeführt werden.
3. **Anisotropie-Kontrolle:** Bestehende B-Mode-Grenzen auf anisotrope Birefringenz sind als separater Constraint zu behandeln.
4. **Cross-dataset:** Planck, ACT und künftige unabhängige CMB-Polarisationsdaten sind getrennt zu halten; gemeinsame Systematiken dürfen nicht als unabhängige Bestätigung gezählt werden.
5. **No anomaly fitting:** Kein Parameter wird aus dem aktuellen β-Signal definiert.
6. **Kill criterion:** Kann keine unabhängig motivierte parity-odd Photonenkopplung aus dem AVI-Operatorraum abgeleitet werden, bleibt Cosmic Birefringence ein externer Beobachtungskanal ohne AVI-spezifische Vorhersage.

## Einordnung in die AVI-Testmatrix

Neuer Kandidat: **CB-1 — CMB polarization / cosmic birefringence**.

Messgrößen: TB/EB-Paritätskorrelationen, isotroper Rotationswinkel β0, anisotropes Rotationsfeld δβ(n).

Status: **HOLD / theory-gated** bis Operator Minimality Gate eine zulässige Kopplung liefert.

## Nächste Arbeitspakete

- CB-1A: parity-odd Operator-Screening gegen bekannte axion-/Chern-Simons-artige EFT-Klassen.
- CB-1B: Ableitung von β_AVI ohne Verwendung des gemessenen β als Input.
- CB-1C: Nullmodell- und Systematikregister (Kalibration, foreground EB, leakage).
- CB-1D: isotropic-vs-anisotropic discriminator und Falsifikationskriterien.
- CB-1E: Datenmatrix Planck/ACT/künftige unabhängige CMB-Polarisationsexperimente.
