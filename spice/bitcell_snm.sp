* 6T SRAM half-cell for butterfly curve, SKY130
.lib /home/shivam/.volare/volare/sky130/versions/c6d73a35f524070e85faff4a6a9eef49553ebc2b/sky130A/libs.tech/ngspice/sky130.lib.spice tt
VDD vdd 0 1.8
VBL bl 0 1.8
VWL wl 0 1.8
VIN vin 0 0
XMP q vin vdd vdd sky130_fd_pr__pfet_01v8 w=0.42 l=0.15
XMN q vin 0 0 sky130_fd_pr__nfet_01v8 w=0.84 l=0.15
XMA bl wl q 0 sky130_fd_pr__nfet_01v8 w=0.42 l=0.15
.control
dc VIN 0 1.8 0.01
wrdata results/vtc_read.txt v(q)
alter VWL = 0
dc VIN 0 1.8 0.01
wrdata results/vtc_hold.txt v(q)
.endc
.end