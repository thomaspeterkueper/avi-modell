# AVI — NV-Spin-Kraft / makroskopischer Resonator: Referenzfall v0.1

**Stand:** 9. Oktober 2026  
**Status:** Experimentelles Standardphysik-Referenzsystem, **keine AVI-Evidenz**  
**Anschluss:** relational-response-selection-gate-v0.1; qft-response-gate-v0.1; theory-status-consolidation-v0.1

## Quellen
- Nayak, Kim, Tian & Twamley (2026), *Spin force from a nitrogen-vacancy ensemble drives a 100-mg levitated resonator*, *Science Advances*, doi:10.1126/sciadv.aeh0566.
- Preprint: https://arxiv.org/abs/2605.17750
- Datensatz und Auswertungscode: https://doi.org/10.5061/dryad.4xgxd25q4
- Institut: https://www.oist.jp/news-center/news/2026/10/8/first-observation-quantum-spins-shifting-centimeter-scale-object-lab

## Reproduzierbarer Befund und Einschränkung
Ensemble optisch polarisierter NV-Zentren in einem Diamanten übt im Magnetfeldgradienten eine Spin-Kraft aus. Ein diamagnetisch schwebender, über einen Stab gekoppelter Resonator (Gesamtmasse 128 mg, zentimetergroße Plattform) zeigt eine angetriebene Schwerpunktschwingung von über 100 nm. Das ist eine klassisch messbare mechanische Antwort auf quantenphysikalisch steuerbare Spins. **Keine makroskopische Orts-Superposition, keine Quantengravitationsmessung und keine AVI-spezifische Abweichung** nachgewiesen.

## Minimalmodell als H0
Spinabhängige Kraft bei bekannter Magnetfeldgradienten-Komponente:
`F_z(t) = ∂_z[m_z(t) B_z]` (Vorzeichen je nach Konvention; bei räumlich nahezu konstantem Moment `F_z ≈ m_z(t)∂_z B_z`).

Mechanische Antwort:
`M z¨ + Γ z˙ + k z = F_spin(t) + F_background(t) + η(t)`.

Für sinusförmigen Antrieb mit Kreisfrequenz ω:
`|z_ω| = |F_ω| / sqrt((k-Mω²)²+(Γω)²)`.

Dabei müssen Kalibration, Geometrie, optische Erwärmung, Lichtdruck, Dämpfung, magnetische Hintergründe und Messrauschen geprüft werden. Alle Effekte fallen vorerst unter Standardphysik.

## Prüfprotokoll
1. Primärarbeit und Supplement lesen: Definitionen der Gesamtmasse, Resonanz, Güte, Spinzustandspräparation, Spin-Kraft und Kontrollversuche prüfen.
2. Aus veröffentlichten Daten die mechanische Transferfunktion, Antwortamplituden sowie Unsicherheitsbereiche reproduzieren. Der Datensatz ist groß (ca. 3,28 GB); zunächst README und abgeleitete Tabellen, danach gezielt Teil-Datensätze.
3. H0 ohne AVI-Zusatz modellieren. Kriterien: Frequenz-, Feldgradient-, Puls- und Abschirmungsabhängigkeit.
4. Dimensionslose Referenzobservable vorab spezifizieren, z. B. `R(ω) = A_spin-on(ω)/A_control(ω)` nur wenn der Kontrollnenner stabil und physikalisch aussagefähig ist; alternativ kalibrierte normierte Übertragungsfunktion.
5. Residuen erst nach vollständiger H0-Analyse definieren und testen. Unzureichend modellierte Messapparatur ist **keine** relationale Zusatzvariable.
6. Ein AVI-spezifischer Ansatz ist nur zulässig, wenn ein unabhängig definierter zusätzlicher Zustandsparameter eine vorab berechenbare, über mehrere Observablen gebundene Abweichung einschließlich Nullkanal, Energieerhaltung und Mikrokausalität liefert.

## Anschluss an Omnizedenz und NOXIA
- *Bestimmung* als ausdrücklich philosophische Deutung von Zustandspräparation + Kopplung + Umgebungs- und Resonanzbedingungen; nicht als experimentelles Resultat.
- *NOXIA* als mögliche numerische Demonstration mikro-zu-makro-Kopplung und Resonanzverstärkung mit expliziten Zuständen und kontrollierten Ressourcen; keine Behauptung fundamentaler Quantenmechanik in der Simulation.

## Ergebnisstatus
**H0 plausibel / noch nicht unabhängig reproduziert.**  
**AVI-Zusatzeffekt: nicht definiert, nicht nachgewiesen.**  
**Nächster wissenschaftlicher Schritt:** Datensatz/Transferfunktion unter H0 reproduzieren, dann entscheiden, ob ein diskriminierender AVI-Test überhaupt formulierbar ist.
