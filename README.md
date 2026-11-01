# 128-bit 6T SRAM Design and Characterization with March C- MBIST

Design, simulation, and characterization of a 128-bit (16x8) 6T SRAM in SkyWater SKY130 (130 nm) CMOS, with a March C- memory BIST written in Verilog.

## Description
SRAM (Static Random Access Memory) is the main building block of on-chip caches and register files in processors. This project builds a small SRAM from the transistor level up: the bitcell, the peripheral circuits around it, and the test logic that checks it for faults. It covers the same flow used in industry memory design: schematic entry, simulation, stability analysis, PPA (power, performance, area) evaluation, characterization across PVT corners, and design for test (DFT).

## How It Works

### 1. 6T bitcell
Each bit is stored in a cell of six transistors: two cross-coupled inverters (four transistors) hold the value, and two NMOS access transistors connect the cell to the bitlines (BL and BLB) when the wordline (WL) is high.
- **Hold:** WL is low, and the inverters keep the stored value.
- **Read:** BL and BLB are precharged to VDD, WL goes high, and the cell pulls one bitline slightly lower. The pull-down transistor must be stronger than the access transistor (cell ratio > 1) so the read does not flip the cell.
- **Write:** The write driver forces one bitline to 0 V, and the access transistor must overpower the pull-up transistor (pull-up ratio) to flip the cell.

### 2. Stability analysis
- **Read SNM, hold SNM, and write margin** are measured from butterfly curves.
- **Monte Carlo** simulation applies transistor mismatch to estimate yield.
- **TT/FF/SS corners** check behavior across process variation.

### 3. Array and peripheral circuits
The 128 bits are organized as 16 words of 8 bits.
- **Row decoder:** the 4-bit address selects one of 16 wordlines.
- **Wordline driver:** drives the selected wordline.
- **Precharge and equalization:** sets BL and BLB to VDD before each access.
- **Sense amplifier (latch type):** detects the small voltage difference between BL and BLB and amplifies it to a full logic level.
- **Write driver:** pulls one bitline low to write data.
- **Control logic:** generates the timing for precharge, wordline, sense enable, and write.

### 4. Memory BIST (March C-)
The MBIST is a Verilog block that tests the memory without external equipment. It contains an address generator, a data generator, a comparator, and an FSM controller. March C- runs these steps:

`up(w0); up(r0,w1); up(r1,w0); down(r0,w1); down(r1,w0); down(r0)`

It detects stuck-at faults, transition faults, address decoder faults, and many coupling faults. A pass/fail flag is raised if any read does not match the expected value.

### 5. Characterization and automation
Python scripts run ngspice in batch mode across PVT corners, extract access time, power, and margins, and write them into a results table.

## Tools
- ngspice, Xschem
- SkyWater SKY130 PDK (130 nm, 1.8 V devices)
- Verilog, Icarus Verilog, GTKWave
- Python 3 (matplotlib, pandas)

## Folder Structure
```
spice/     netlists and testbenches
verilog/   MBIST controller and testbench
scripts/   Python automation scripts
results/   plots and tables
docs/      notes and report
```

## How to Run
```bash
# SPICE
ngspice spice/<testbench>.sp

# MBIST
iverilog -o mbist_tb verilog/mbist.v verilog/mbist_tb.v
vvp mbist_tb
```

## Future Scope
- Layout in Magic with DRC/LVS and post-layout simulation with parasitic extraction
- Leakage reduction using high-Vt cells, power gating, or a sleep mode
- Read and write assist circuits for low-voltage operation
- Comparison with 8T and 10T bitcells
- Scaling to larger arrays (for example 1 Kb or more) with column muxing
- Built-in self-repair (redundant rows and columns) added to the MBIST
- A simple memory compiler script that generates arrays of different sizes
- Additional test algorithms such as March SS and checkerboard patterns

## References
- Weste and Harris, *CMOS VLSI Design*
- Rabaey, *Digital Integrated Circuits*
- Seevinck et al., SRAM static noise margin analysis
- van de Goor, memory testing and March algorithms

## Author
Shivam kumar
B.Tech in Electronics and Communication Engineering
IIT ISM Dhanbad

## License
MIT
