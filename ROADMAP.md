# RF Space Systems Lab Roadmap

This repository begins from first principles. It assumes no prior Python, RF, radar, satellite communications, satellite navigation, orbital-mechanics, or professional software-development experience.

The repository will grow incrementally. Only the files and directories required for the current lesson or milestone should be created. Empty curriculum trees should not be added in advance.

---

## Project mission

Build a rigorous, reproducible engineering curriculum and software laboratory covering:

- Engineering Python
- Engineering mathematics
- Signals and systems
- RF fundamentals
- Digital signal processing
- Antennas and propagation
- Radar
- Orbital mechanics
- Satellite communications
- Satellite navigation
- Integrated RF and space systems

The long-term objective is to progress from elementary calculations to verified engineering simulations and portfolio-quality capstone projects.

---

## Core development rule

```text
Learn the concept
        ↓
Complete a hand calculation
        ↓
Implement it clearly in Python
        ↓
Visualize or experiment with it
        ↓
Verify the result
        ↓
Move stable logic into reusable modules
        ↓
Add automated tests
```

Notebooks are used for explanation and experimentation.

Reusable Python modules are introduced only after the relevant programming concepts are understood.

Tests are added when code becomes reusable or when a calculation requires regression protection.

---

## Starting point

The repository initially contains only:

```text
rf-space-systems-lab/
├── README.md
└── ROADMAP.md
```

The next files and directories will be added one step at a time.

---

# Phase 0 — Repository and development foundations

## Goal

Prepare a clean learning environment and understand the minimum Git workflow required to preserve progress.

## Topics

- [ ] Confirm the repository name is `rf-space-systems-lab`
- [ ] Confirm the repository description and topics
- [ ] Install or verify Git
- [ ] Install or verify Python
- [ ] Understand the repository working directory
- [ ] Understand `git status`
- [ ] Understand staging and commits
- [ ] Understand pushing changes to GitHub
- [ ] Create and activate a virtual environment
- [ ] Add a Python-focused `.gitignore`
- [ ] Record the Python version used by the project

## Initial repository structure

```text
rf-space-systems-lab/
├── README.md
├── ROADMAP.md
└── .gitignore
```

## Completion criteria

- The repository can be cloned successfully.
- A local virtual environment can be created and activated.
- `git status` is understood and checked before every commit.
- The virtual environment is not tracked by Git.
- README and roadmap changes are committed with descriptive messages.

## Suggested commits

```text
Define RF and space systems learning roadmap
Add Python development ignore rules
Document local development setup
```

---

# Phase 1 — Engineering Python from scratch

Python will be learned through engineering quantities and RF-related examples rather than through unrelated exercises.

No reusable package is required at the beginning of this phase.

## Module 1.1 — Numbers, units, and scientific notation

### Python concepts

- [ ] Integers
- [ ] Floating-point numbers
- [ ] Arithmetic operators
- [ ] Operator precedence
- [ ] Variable assignment
- [ ] Scientific notation
- [ ] Printing results
- [ ] Basic comments

### Engineering concepts

- [ ] Physical quantities and units
- [ ] SI base and derived units
- [ ] Metric prefixes
- [ ] Frequency in hertz
- [ ] Time and period
- [ ] Distance
- [ ] Power
- [ ] Unit conversion
- [ ] Dimensional consistency

### First lesson

```text
00_engineering_python/
└── 01_numbers_units_scientific_notation/
    ├── README.md
    └── lesson.ipynb
```

### First engineering exercises

- Convert megahertz and gigahertz to hertz.
- Convert kilometres to metres.
- Calculate signal period from frequency.
- Calculate free-space wavelength from frequency.
- Compare wavelengths at different RF bands.
- Identify incorrect unit combinations.

### Completion criteria

- Numerical values and units are kept conceptually separate.
- Scientific notation is used correctly.
- Results are checked manually.
- Every output states its unit.
- The notebook runs from top to bottom without errors.

---

## Module 1.2 — Variables, expressions, and numeric types

### Python concepts

- [ ] Meaningful variable names
- [ ] `int` and `float`
- [ ] Type inspection
- [ ] Assignment and reassignment
- [ ] Formatted strings
- [ ] Floating-point limitations

### Engineering applications

- Frequency, wavelength, and period tables
- Power and bandwidth values
- Unit-labelled output
- Comparison of calculated and expected results

---

## Module 1.3 — Functions

### Python concepts

- [ ] Function definitions
- [ ] Parameters
- [ ] Return values
- [ ] Local variables
- [ ] Docstrings
- [ ] Type hints

### Engineering applications

Create simple functions for:

- Frequency to period
- Frequency to wavelength
- Hertz to kilohertz, megahertz, and gigahertz
- Watts to milliwatts
- Metres to kilometres

Reusable package files are not required yet. Functions may remain inside the lesson notebook until their purpose is understood.

---

## Module 1.4 — Conditions, validation, and exceptions

### Python concepts

- [ ] Boolean expressions
- [ ] Comparison operators
- [ ] `if`, `elif`, and `else`
- [ ] Input validation
- [ ] Raising `ValueError`
- [ ] Reading error messages

### Engineering applications

- Reject zero or negative frequency.
- Reject negative distance.
- Reject invalid bandwidth.
- Warn when an input falls outside an intended model range.

---

## Module 1.5 — Collections and loops

### Python concepts

- [ ] Lists
- [ ] Tuples
- [ ] Dictionaries
- [ ] `for` loops
- [ ] `while` loops
- [ ] Accumulation
- [ ] Simple tables

### Engineering applications

- Generate wavelength tables for common bands.
- Calculate gains and losses through an RF chain.
- Compare several frequencies or distances.
- Store physical constants and unit labels.

---

## Module 1.6 — NumPy arrays

### Python concepts

- [ ] Creating arrays
- [ ] Array shapes
- [ ] Indexing and slicing
- [ ] Vectorized operations
- [ ] Broadcasting
- [ ] Basic numerical statistics

### Engineering applications

- Calculate wavelength over a frequency range.
- Calculate path loss over a distance range.
- Generate sampled sinusoidal signals.
- Compare loop-based and vectorized calculations.

---

## Module 1.7 — Visualization with Matplotlib

### Python concepts

- [ ] Creating a figure
- [ ] Line plots
- [ ] Markers
- [ ] Axis labels
- [ ] Titles
- [ ] Legends
- [ ] Linear and logarithmic axes
- [ ] Saving figures

### Engineering applications

- Wavelength versus frequency
- Period versus frequency
- Power versus distance
- Sampled sinusoidal signals

Every axis must include the physical quantity and unit.

---

## Module 1.8 — Complex numbers

### Python concepts

- [ ] Python complex values
- [ ] Real and imaginary parts
- [ ] Magnitude
- [ ] Phase
- [ ] Complex conjugate
- [ ] Euler representation

### Engineering applications

- Phasors
- IQ signals
- Complex impedance
- Sinusoidal amplitude and phase

---

## Module 1.9 — Files and structured data

### Python concepts

- [ ] Reading text files
- [ ] Writing text files
- [ ] CSV data
- [ ] Paths
- [ ] Context managers
- [ ] Basic data validation

### Engineering applications

- Save frequency tables.
- Load measurement-like data.
- Export calculated results.
- Preserve experiment parameters.

---

## Module 1.10 — Debugging and testing fundamentals

### Python concepts

- [ ] Reading tracebacks
- [ ] Assertions
- [ ] Small reproducible test cases
- [ ] Floating-point tolerances
- [ ] Introduction to `pytest`
- [ ] Testing expected exceptions

### Engineering applications

Verify:

- Known wavelength values
- Unit conversions
- Invalid-input handling
- Limiting cases
- Results from hand calculations

---

## Module 1.11 — Modules and project packaging

This module introduces reusable software only after variables, functions, validation, files, and testing have been studied.

### Topics

- [ ] Importing modules
- [ ] Creating Python files
- [ ] Package directories
- [ ] `__init__.py`
- [ ] Separating notebook code from reusable code
- [ ] Creating `pyproject.toml`
- [ ] Editable installation
- [ ] Organizing tests

### Repository structure introduced here

```text
rf-space-systems-lab/
├── README.md
├── ROADMAP.md
├── .gitignore
├── pyproject.toml
├── 00_engineering_python/
├── src/
│   └── rf_space_systems/
│       ├── __init__.py
│       ├── constants.py
│       └── units.py
└── tests/
    └── test_units.py
```

## Phase 1 project — RF calculator

```text
projects/
└── project01_rf_calculator/
```

Initial capabilities:

- Frequency, period, and wavelength conversion
- SI-prefix conversion
- Power conversion between W, mW, dBW, and dBm
- Thermal-noise calculation
- Free-space path-loss calculation
- Input validation
- Automated tests
- Clear documentation of units and assumptions

## Phase 1 completion criteria

- Python fundamentals are understood rather than copied mechanically.
- At least one notebook exists for every completed module.
- Hand calculations are used to verify Python results.
- Reusable functions are moved into `src/` only when appropriate.
- Automated tests cover reusable calculations.
- The RF calculator works from a clean environment.
- Git history contains descriptive, topic-based commits.

## Suggested phase tag

```bash
git tag -a engineering-python-v1 -m "Complete engineering Python foundations"
git push origin engineering-python-v1
```

---

# Phase 2 — Engineering mathematics

## Goal

Develop the mathematical tools required for RF, signal processing, radar, SatCom, SatNav, and orbital mechanics.

## Modules

### 2.1 Algebra and logarithms

- [ ] Rearranging equations
- [ ] Ratios and proportions
- [ ] Powers and roots
- [ ] Base-10 logarithms
- [ ] Natural logarithms
- [ ] Exponential relationships
- [ ] Decibel preparation

### 2.2 Trigonometry

- [ ] Angles and radians
- [ ] Sine, cosine, and tangent
- [ ] Phase
- [ ] Periodic functions
- [ ] Basic geometry
- [ ] Coordinate conversion

### 2.3 Complex numbers and phasors

- [ ] Rectangular and polar forms
- [ ] Euler's formula
- [ ] Phasor arithmetic
- [ ] Complex exponentials
- [ ] Impedance preparation

### 2.4 Calculus

- [ ] Limits
- [ ] Derivatives
- [ ] Integrals
- [ ] Differential equations
- [ ] Physical interpretation of rate and accumulation

### 2.5 Vectors and matrices

- [ ] Vectors
- [ ] Dot products
- [ ] Cross products
- [ ] Matrices
- [ ] Linear systems
- [ ] Coordinate transformations
- [ ] Least-squares preparation

### 2.6 Probability and statistics

- [ ] Random variables
- [ ] Probability distributions
- [ ] Mean and variance
- [ ] Gaussian noise
- [ ] Covariance
- [ ] Estimation fundamentals

### 2.7 Numerical methods

- [ ] Root finding
- [ ] Numerical differentiation
- [ ] Numerical integration
- [ ] Interpolation
- [ ] Numerical stability
- [ ] Error and convergence

## Phase 2 completion criteria

- Mathematical derivations accompany implementations.
- Units are checked during equation manipulation.
- Numerical results are compared with analytical results when possible.
- Matrix and probability concepts are ready for later estimation problems.

---

# Phase 3 — Signals and systems

## Modules

- [ ] Signal classification
- [ ] Continuous- and discrete-time signals
- [ ] Sinusoids and complex exponentials
- [ ] Amplitude, frequency, phase, and energy
- [ ] Time shifting and scaling
- [ ] Linear systems
- [ ] Time invariance
- [ ] Impulse response
- [ ] Convolution
- [ ] Sampling and reconstruction
- [ ] Aliasing
- [ ] Fourier series
- [ ] Fourier transform
- [ ] Frequency response

## Phase project — Signal processing laboratory

```text
projects/
└── project02_signal_processing_lab/
```

Candidate capabilities:

- Signal generation
- Sampling experiments
- Aliasing demonstrations
- Convolution
- Spectrum calculation
- Time- and frequency-domain plots

---

# Phase 4 — RF fundamentals

## Modules

- [ ] Electromagnetic-wave concepts
- [ ] Frequency, period, wavelength, and propagation speed
- [ ] Power and energy
- [ ] dB, dBW, and dBm
- [ ] Gain and loss chains
- [ ] Impedance
- [ ] Reflection coefficient
- [ ] Return loss
- [ ] VSWR
- [ ] Transmission-line fundamentals
- [ ] Thermal noise
- [ ] Noise temperature
- [ ] Noise figure
- [ ] Receiver sensitivity
- [ ] Dynamic range
- [ ] Compression and intermodulation fundamentals

## Phase completion criteria

- Decibel calculations are traceable to linear quantities.
- RF-chain calculations state reference planes.
- Noise calculations state temperature and bandwidth.
- Impedance calculations use complex numbers correctly.
- Models include assumptions and validity limits.

## Suggested phase tag

```bash
git tag -a rf-foundations-v1 -m "Complete RF foundations"
git push origin rf-foundations-v1
```

---

# Phase 5 — Digital signal processing

## Modules

- [ ] Discrete sampling
- [ ] Quantization
- [ ] DFT and FFT
- [ ] Spectral resolution
- [ ] Leakage and windowing
- [ ] FIR filters
- [ ] IIR filters
- [ ] Complex baseband
- [ ] IQ representation
- [ ] Digital modulation
- [ ] Correlation
- [ ] Matched filtering
- [ ] Detection and estimation
- [ ] Random processes and noise

## Completion criteria

- Time- and frequency-domain results agree.
- Sampling assumptions are explicit.
- Filter responses are verified.
- FFT scaling and frequency axes are correct.
- Complex baseband conventions are documented.

---

# Phase 6 — Antennas and propagation

## Modules

- [ ] Radiation concepts
- [ ] Gain and directivity
- [ ] Radiation patterns
- [ ] Beamwidth
- [ ] Polarization
- [ ] Effective aperture
- [ ] Friis transmission equation
- [ ] Free-space path loss
- [ ] Atmospheric absorption
- [ ] Rain attenuation
- [ ] Multipath and fading
- [ ] Doppler shift

## Phase project — Antenna and propagation tool

```text
projects/
└── project03_antenna_propagation_tool/
```

Candidate capabilities:

- Antenna-gain calculations
- Effective-aperture calculations
- Radiation-pattern visualization
- Free-space link calculations
- Atmospheric-loss studies
- Doppler studies

---

# Phase 7 — Radar

## Modules

- [ ] Radar system architecture
- [ ] Radar range equation
- [ ] Radar cross section
- [ ] Pulsed radar
- [ ] Continuous-wave radar
- [ ] FMCW radar
- [ ] Range resolution
- [ ] Velocity resolution
- [ ] Ambiguity
- [ ] Pulse compression
- [ ] Matched filtering
- [ ] Coherent integration
- [ ] Range-Doppler processing
- [ ] Detection thresholds
- [ ] Probability of detection
- [ ] Probability of false alarm
- [ ] Tracking fundamentals

## Phase project — Radar simulator

```text
projects/
└── project04_radar_simulator/
```

The project should progress from a scalar range-equation calculator to sampled-signal simulation and range-Doppler processing.

---

# Phase 8 — Orbital mechanics

## Modules

- [ ] Units and astronomical constants
- [ ] Reference frames
- [ ] Coordinate systems
- [ ] Newtonian gravity
- [ ] Two-body motion
- [ ] Keplerian orbital elements
- [ ] State-vector conversion
- [ ] Orbit propagation
- [ ] Ground tracks
- [ ] Ground-station geometry
- [ ] Visibility and elevation
- [ ] Slant range
- [ ] Range rate
- [ ] Orbital Doppler

## Phase project — Satellite pass predictor

```text
projects/
└── project05_orbit_pass_predictor/
```

Candidate capabilities:

- Propagate a satellite state
- Generate a ground track
- Determine rise and set times
- Calculate azimuth and elevation
- Calculate slant range and range rate
- Estimate Doppler shift

---

# Phase 9 — Satellite communications

## Modules

- [ ] Satellite-communications architecture
- [ ] Frequency bands
- [ ] Uplink and downlink
- [ ] Transmit power and EIRP
- [ ] Receive gain and `G/T`
- [ ] Free-space and atmospheric losses
- [ ] Carrier-to-noise density, `C/N0`
- [ ] Energy per bit to noise density, `Eb/N0`
- [ ] Link margins
- [ ] Modulation and coding
- [ ] Multiple access
- [ ] Interference
- [ ] Availability
- [ ] Spectrum and coordination fundamentals

## Phase project — SatCom link designer

```text
projects/
└── project06_satcom_link_designer/
```

The project should support transparent uplink, transponder, downlink, noise, and margin calculations with clearly defined reference points.

---

# Phase 10 — Satellite navigation

## Modules

- [ ] GNSS architecture
- [ ] Time systems
- [ ] Coordinate systems
- [ ] Satellite ephemerides
- [ ] PRN codes
- [ ] Correlation
- [ ] Signal acquisition
- [ ] Code tracking
- [ ] Carrier tracking
- [ ] Pseudorange
- [ ] Carrier phase
- [ ] Doppler observables
- [ ] Least-squares positioning
- [ ] Dilution of precision
- [ ] Satellite clock errors
- [ ] Ionospheric and tropospheric errors
- [ ] Multipath
- [ ] Receiver noise

## Phase project — GNSS receiver simulator

```text
projects/
└── project07_gnss_receiver_simulator/
```

The project should progress from pseudorange geometry to noisy position estimation and receiver-processing concepts.

---

# Phase 11 — Integrated RF and space systems

## Goal

Combine the separate subject areas into an end-to-end engineering simulation.

## Final integrated scenario

1. Define a LEO satellite orbit.
2. Propagate the satellite state.
3. Determine ground-station visibility.
4. Calculate azimuth, elevation, and slant range.
5. Calculate range rate and Doppler.
6. Build a SatCom uplink and downlink budget.
7. Generate navigation or ranging observables.
8. Simulate a radar or coherent ranging measurement.
9. Estimate the system state.
10. Compare estimated values with truth data.
11. Quantify error and sensitivity.
12. Document assumptions, limitations, and uncertainty.

## Final deliverables

- [ ] Mathematical model
- [ ] System architecture diagram
- [ ] Reusable Python package
- [ ] Automated test suite
- [ ] Reproducible notebooks
- [ ] Input datasets
- [ ] Generated figures
- [ ] Engineering report
- [ ] Technical references
- [ ] Versioned release

---

# Repository growth policy

Do not create every phase directory immediately.

Create a directory only when:

- Its first lesson is ready to begin.
- Its purpose is documented.
- It contains meaningful content.
- It can be committed with a descriptive message.

The expected early repository growth is:

```text
Step 1
rf-space-systems-lab/
├── README.md
└── ROADMAP.md

Step 2
rf-space-systems-lab/
├── README.md
├── ROADMAP.md
└── .gitignore

Step 3
rf-space-systems-lab/
├── README.md
├── ROADMAP.md
├── .gitignore
└── 00_engineering_python/
    └── 01_numbers_units_scientific_notation/
        ├── README.md
        └── lesson.ipynb

Step 4
Add the next lesson only after the first lesson is complete and committed.

Later
Add pyproject.toml, src/, tests/, projects/, and automation when the associated concepts are introduced.
```

---

# Lesson completion standard

A lesson is complete only when it includes:

- [ ] Learning objectives
- [ ] Required background
- [ ] Theory
- [ ] Definitions of symbols and units
- [ ] At least one hand calculation
- [ ] Python implementation
- [ ] Engineering experiment
- [ ] Visualization when useful
- [ ] Verification
- [ ] Engineering conclusions
- [ ] Assumptions and limitations
- [ ] References
- [ ] A descriptive Git commit

---

# Immediate next milestone

The next repository addition is:

```text
.gitignore
```

After that, create the first lesson:

```text
00_engineering_python/
└── 01_numbers_units_scientific_notation/
    ├── README.md
    └── lesson.ipynb
```

The first lesson should not require NumPy, Matplotlib, packaging, or `pytest`. It should use only basic Python numbers, variables, arithmetic, scientific notation, comments, and printed engineering results.

Recommended commit sequence:

```text
Define from-scratch engineering learning roadmap
Add Python development ignore rules
Add numbers units and scientific notation lesson
```