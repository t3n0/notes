# DOS

1. Run `pw.x`
   ```
   calculation = 'scf'
   ```

2. Run `pw.x`
   ```
   calculation = 'nscf'
   occupation = 'tetrehedra'
   nbnd = XXXX
   k_points {automatic}
   ```

3. Run `dos.x`

4. Run `projwfc.x`
   
# Bands

1. Run `pw.x`, self-consistent field calculation
   ```
   calculation = 'scf'
   ```

2. Run `pw.x`, compute the fermi energy on a finer kgrid
   ```
   calculation = 'nscf'
   occupation = 'tetrehedra'
   nbnd = XXXX
   k_points {automatic}
   ```

3. Run `px.x`, compute bands on a given k-path
   ```
   calculation = 'bands'
   nbnd = XXXX
   K_POINTS crystal_b
   4
   0.0        0.0        0.0   50      # G
   0.333333   0.666666   0.0   30      # K
   0.5        0.5        0.0   40      # M
   0.0        0.0        0.0   1       # G
   ```

4. Run `bands.x`, writes bands to file `raw_bands` and writes symmetries to file `raw_bands.rap`.
   Optionally, compute the spin projections in a spin-orbit non-collinear system.
   Spins are written to files `raw_bands1`, `raw_bands2`,`raw_bands3`.
   Symmetry files for spin are **not** written explicitly.
   One must **copy** `raw_bands.rap` to `raw_bands.1.rap`, `raw_bands.2.rap`, `raw_bands.3.rap`.
   ```
   filbands = 'raw_bands'
   lsigma(1) = .true.
   lsigma(2) = .true.
   lsigma(3) = .true.
   ```

6. Run `plotband.x`, computes the energy bands with symmetry.
   Reads band structure from `raw_bands` and symmetry from `raw_band.rap`.
   Produces files named `bands.gnu.x.y`:
    - x, k-path identifier
    - y, symmetry identifier
   The code runs interactively, but can also read from a script.
   ```
   raw_bands
   Emin Emax
   bands.gnu
   bands.ps
   Efermi
   Eticks Ezero
   ```

7. (Optional) run `plotband.x`, for the spin projections (see point 4).
   For z projection, reads spin structure from `raw_bands.3` and symmetry from `raw_band.3.rap`.
   Same as above, but now instead of energy we have the spinor projection on a given axis.
   ```
   raw_bands.3
   -0.5 0.5
   spin.gnu
   spin.ps
   0.0
   1.0 0.0
   ```


