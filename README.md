# rgevolve.wet_4.jms

Package providing Renormalization Group Evolution matrices for the
**WET-4** in the **JMS** basis, following the
[wcxf](https://wcxf.github.io/) conventions for Wilson coefficient
bases.

It is a sub-package of the **rgevolve** ecosystem — a set of Python
namespace packages for fast renormalization group evolution of Wilson
coefficients in the SMEFT and the WET using the evolution matrix
formalism. See the [rgevolve organization](https://github.com/rgevolve)
for the full ecosystem and the
[`rgevolve` meta-package](https://github.com/rgevolve/rgevolve) for
installation in lockstep with the core and all companions.

<!-- BEGIN: auto-generated from data.h5 by .github/scripts/generate-readme.py — do not edit by hand -->

## Contents

This distribution bundles RG evolution matrices precomputed at
**4 scales** between **1.3** and
**4.2** GeV:

| scale (GeV) |
| ----------- |
| 1.3 |
| 2 |
| 2.75 |
| 4.2 |

Matrices are organised into **143 sectors** covering a total
of **2545 Wilson coefficients** (counting the real and imaginary
parts of complex coefficients separately):

| sector | # Wilson coefficients |
| ------ | --------------------- |
| `ccde` | 8 |
| `ccdmu` | 8 |
| `ccdtau` | 8 |
| `ccse` | 8 |
| `ccsmu` | 8 |
| `ccstau` | 8 |
| `cddnue` | 4 |
| `cddnumu` | 4 |
| `cddnutau` | 4 |
| `cdenue` | 10 |
| `cdenumu` | 10 |
| `cdenutau` | 10 |
| `cdmunue` | 10 |
| `cdmunumu` | 10 |
| `cdmunutau` | 10 |
| `cdsnue` | 10 |
| `cdsnumu` | 10 |
| `cdsnutau` | 10 |
| `cdtaunue` | 10 |
| `cdtaunumu` | 10 |
| `cdtaunutau` | 10 |
| `csenue` | 10 |
| `csenumu` | 10 |
| `csenutau` | 10 |
| `csmunue` | 10 |
| `csmunumu` | 10 |
| `csmunutau` | 10 |
| `cssnue` | 4 |
| `cssnumu` | 4 |
| `cssnutau` | 4 |
| `cstaunue` | 10 |
| `cstaunumu` | 10 |
| `cstaunutau` | 10 |
| `cu` | 188 |
| `cucu` | 16 |
| `cuemu` | 20 |
| `cuetau` | 20 |
| `cumue` | 20 |
| `cumutau` | 20 |
| `cunuinui` | 12 |
| `cunumunue` | 8 |
| `cunumunutau` | 8 |
| `cunutaunue` | 8 |
| `cutaue` | 20 |
| `cutaumu` | 20 |
| `dF=0` | 341 |
| `etauemu` | 12 |
| `ffnuinui` | 42 |
| `ffnumunue` | 28 |
| `ffnumunutau` | 28 |
| `ffnutaunue` | 28 |
| `mue` | 128 |
| `muemue` | 10 |
| `muemutau` | 12 |
| `muenuenumu` | 4 |
| `muenuenutau` | 4 |
| `muenuinui` | 12 |
| `muenumunue` | 4 |
| `muenumunutau` | 4 |
| `muenutaunue` | 4 |
| `muenutaunumu` | 4 |
| `mutau` | 128 |
| `mutaunuenumu` | 4 |
| `mutaunuenutau` | 4 |
| `mutaunuinui` | 12 |
| `mutaunumunue` | 4 |
| `mutaunumunutau` | 4 |
| `mutaunutaunue` | 4 |
| `mutaunutaunumu` | 4 |
| `nuenutaunuenumu` | 2 |
| `nuinuinujnuj` | 6 |
| `numunuenuinui` | 6 |
| `numunuenumunue` | 2 |
| `numunuenumunutau` | 2 |
| `numunutaunuinui` | 6 |
| `nutaunuenuinui` | 6 |
| `nutaunuenutaunue` | 2 |
| `nutaunuenutaunumu` | 2 |
| `nutaunumunutaunumu` | 2 |
| `sd` | 188 |
| `sdcu` | 40 |
| `sdemu` | 20 |
| `sdetau` | 20 |
| `sdmue` | 20 |
| `sdmutau` | 20 |
| `sdnuinui` | 12 |
| `sdnumunue` | 8 |
| `sdnumunutau` | 8 |
| `sdnutaunue` | 8 |
| `sdsd` | 16 |
| `sdtaue` | 20 |
| `sdtaumu` | 20 |
| `sduc` | 40 |
| `taue` | 128 |
| `tauenuenumu` | 4 |
| `tauenuenutau` | 4 |
| `tauenuinui` | 12 |
| `tauenumunue` | 4 |
| `tauenumunutau` | 4 |
| `tauenutaunue` | 4 |
| `tauenutaunumu` | 4 |
| `tauetaue` | 10 |
| `tauetaumu` | 12 |
| `taumutaumu` | 10 |
| `ucde` | 20 |
| `ucdmu` | 20 |
| `ucdtau` | 20 |
| `ucse` | 20 |
| `ucsmu` | 20 |
| `ucstau` | 20 |
| `uddnue` | 4 |
| `uddnumu` | 4 |
| `uddnutau` | 4 |
| `udenue` | 10 |
| `udenumu` | 10 |
| `udenutau` | 10 |
| `udmunue` | 10 |
| `udmunumu` | 10 |
| `udmunutau` | 10 |
| `udsnue` | 10 |
| `udsnumu` | 10 |
| `udsnutau` | 10 |
| `udtaunue` | 10 |
| `udtaunumu` | 10 |
| `udtaunutau` | 10 |
| `usenue` | 10 |
| `usenumu` | 10 |
| `usenutau` | 10 |
| `usmunue` | 10 |
| `usmunumu` | 10 |
| `usmunutau` | 10 |
| `ussnue` | 4 |
| `ussnumu` | 4 |
| `ussnutau` | 4 |
| `ustaunue` | 10 |
| `ustaunumu` | 10 |
| `ustaunutau` | 10 |
| `uude` | 8 |
| `uudmu` | 8 |
| `uudtau` | 8 |
| `uuse` | 8 |
| `uusmu` | 8 |
| `uustau` | 8 |

<!-- END: auto-generated -->

## Installation

```bash
pip install rgevolve.wet_4.jms
```

To install the core package together with all available EFT/basis
companion packages at once, use the meta-package:

```bash
pip install rgevolve
```

## License

`rgevolve.wet_4.jms` is licensed under the MIT License — see [`LICENSE`](LICENSE).
