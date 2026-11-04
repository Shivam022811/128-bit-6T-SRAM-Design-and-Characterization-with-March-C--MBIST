* CMOS inverter VTC, SKY130
.lib /home/shivam/.volare/volare/sky130/versions/c6d73a35f524070e85faff4a6a9eef49553ebc2b/sky130A/libs.tech/ngspice/sky130.lib.spice tt
VDD vdd 0 1.8
VIN in 0 0
XMP out in vdd vdd sky130_fd_pr__pfet_01v8 w=1.26 l=0.15
XMN out in 0 0 sky130_fd_pr__nfet_01v8 w=0.42 l=0.15
.dc VIN 0 1.8 0.01
.control
run
wrdata results/inverter.txt v(out)
.endc
.end