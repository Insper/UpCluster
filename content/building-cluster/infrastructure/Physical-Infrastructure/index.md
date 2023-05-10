

# Physical Infrastructure
<br>

![Cluster Perspective](imgs/cluster_rack%20_isometric.png){width=300}

<br>
The cluster structure was made in a rack format containing 24 drawers. Since the project was based on the DevKit Upboards, the design of the cluster started through the concept of a drawer that could hold the board model, giving access for connecting cables (ethernet and USB cable) and airflow through specific cutouts on its acrylic body.


![Drawer and UPBoard Top View](imgs/upboard_drawer_bolt_holes.png)
<figcaption>Screw connectors</figcaption>

<br>

![Drawer cutouts](imgs/upboard_drawer_cutouts.png)
<figcaption>Cutouts for cable connections and air flow</figcaption>

<br>

The drawers are organized in two stacks of 12 units in a symmetrical arrangement where the stacks are opposite each other. Between the drawers it is possible to identify a space destined to contain the cluster network switch and behind this set an area was provided for storing the system cables that is enclosed by a set of two doors.

![Cluster front and back view](imgs/cluster_rack%20_front_and_back.png)
<figcaption>Drawers positions and doors for the cables enclosure</figcaption>

<br>

Above this structure, a specific niche was designed to store the router (*router name*) that is also enclosed by another door at the rear.

![Router niche](imgs/router_niche.png)
<figcaption>Niche for the router</figcaption>

## Materials

The whole rack is made of 3mm thickness acrylic sheet. The choice of material is due to the large amount of leftovers and scraps available for the project. It is worth noting that this material comes from old protections for service areas used during the 2020 COVID-19 pandemic.

![Acrylic Scraps](imgs/acrylic_scraps.png){width=700}
<figcaption>Acrylic scraps from protections for service areas</figcaption>

<br>

After vaccination of a large part of the population and a drop in mortality due to the virus, these acrylic protections were removed and a large amount of this material was found accessible and available for reuse.

## Rack Building Process

The rack building process can be essentially divided into 4 parts:

1. 3D digital modeling the cluster rack in CAD (Autodesk Fusion 360).
2. Cutting the designed parts using a laser cutting process.
3. Bending the drawers walls by molds and heat.
4. Assembling the cutted and bent parts.

Below is the process used in each step.

### 3D Digital Model

The CAD (computer-aided design) software used to design the rack was the Autodesk Fusion 360. Considering that the material avaiable for the project was the 3mm thickness acrylic sheets mentioned before, it was a concern to create a design that contemplated its physical characteristics and properties. 

![Profile Represenation](imgs/sides_profiles.png)
<figcaption>2D projections from the rack parts</figcaption>

<br>

The designing concept were based on 2D profiles of each component with the exception of the frontal piece of the drawer. The thermoplastic properties of acrylic were harnessed to create the L-shaped part. This same part, when is assembled with the rest of the rack, gives to the structure a look similar to a building construction.


![L-shaped Part](imgs/L-shaped_part.png)
<figcaption>Drawer L-shaped part</figcaption>

<br>

![L-shaped Projection](imgs/L-shaped_2d_profile.png)
<figcaption>2D projection from the L-shaped part</figcaption>

### Laser Cutting Parts

The parts manufacturing happened through a laser cutting process. 

A 2D projection from parts profiles were created and organized as a sketch in Fusion 360. 


![2D Rack Projection](imgs/2d_rack_projection.png)
<figcaption>2D projection from the L-shaped part</figcaption>

<br>

The skecth is exported in a DXF file to be imported in a second software called RDWorks. RDWorks is a CAM (computer-aided manufacturing) software. In this software is possible to work on the dxf file organizing the profiles according to the material sheet used in the laser cutting machine, defining what will be cutted and what will be engraved by changing the vectors color and configuring the paremeters for cutting, in this manufacturing process the paremeters are essentially speed and laser power. It is important to mention that we are using leftovers and scraps of acrylic sheets, what means that the size of those materials were not the same between each other and none of them meet the necessary dimension for cutting all the pieces at once.

![RD Works Screen](imgs/rdworks_screen.png)
<figcaption>Paremeters (speed and power) settings in the RDWorks software</figcaption>

<br>

After setting up the paremeter a code file in RD format is saved and sent to the laser cutting machine. 

*images/gif showing the laser cutting machine manufacturing some pieces (maybe a drawer)*

### Manufacturing The Bent Parts

The acrylic is a thermoplastic. Thermoplastic materials has as property the ability to deform when exposed to high temperatures.Using this characteristic of the material, it was possible to idealize an L-shaped piece for front and side part of the drawers.

<br>

![Drawer L-shaped Part](imgs/drawer_isometric_L-shaped_part.png){width=500}
<figcaption>Paremeters (speed and power) settings in the RDWorks software</figcaption>

<br>

To create the L-shaped piece, it was necessary to build a mold that would allow the acrylic to be deformed accordingly. The mold was also designed in Fusion 360. The digital model of the L-shaped piece were used as counter mold to create the following two bodies.

![Mold](imgs/drawer_mold.png)
<figcaption>Mold bodies modeled from the L-shaped part</figcaption>

<br>

The bodies are exported as STL files and then imported in a software called Autodesk SlicerforFusion360. In this software those bodies are sliced in layers of 3mm thickness that is the same thickness of the mdf wood scraps used for the mold manufacturing. A DXF file with the 2D projections of the layers are exported from the SlicerforFusion360 ready to be prepared in RDWorks and then be cutted in the laser cutting machine.

![Stacked Layers Mold and 2D Layers Projections](imgs/mold_exploded_view.png)
<figcaption>Mold after being sliced in SlicerforFusion360</figcaption>

<br>

![Mold 2D Layers Projections](imgs/2d_mold_projection.png)
<figcaption>Mold 2D projections in RDWorks</figcaption>

<br>

![MDF Mold](imgs/mdf_mold.jpg)
<figcaption>Layers of laser-cut mdf stacked to shape the mold</figcaption>

<br>

After this process, those layers are glued and stashed over each other reproducing the two parts molds designed originally in the Fusion 360. 

For the from part of the drawer getting the L-shaped idealized by the design, it is important to notice the the corresponding piece cutted previously in the laser cutting machine has some marks (three parallel lines located in the middle of the piece) on its surface. Those marks were engraved and they are intended to define the area in which the material will be bent, delimiting where the curvature begins and ends.

![Front Drawer Marks](imgs/drawer_bend_marks.png)
<figcaption>Bending area delimited by the line marks</figcaption>

<br>

![Laser Cutted Front Drawer Part](imgs/laser_cutted_L-shaped_part.jpg)
<figcaption>L-shaped part after laser cutting and with the engraved marks for bending process</figcaption>

<br>

Using a couple of mdf wood scraps and a heat blower, this area between the marks were isolated and heated until the acrylic piece soften. 

![Heating Process](imgs/heating_process.jpg)
<figcaption>Heating up the bending area</figcaption>

<br>

The two parts molds were use to embrace the soften piece giving it the L-shaped aspect until it cools down, resulting in the desired part.

![Molding Process](imgs/molding_process.jpg)
<figcaption>Molding the part after heated</figcaption>

<br>

![Molded Part](imgs/molded_part.jpg)
<figcaption>L-shaped part after the molding process</figcaption>

<br>

After this process, the L-shaped part was assembles with the rest of the drawer pieces.

![Drawer Assembling Process](imgs/assembling_drawer.jpg)
<figcaption>Assembling the drawer parts</figcaption>

<br>

![Drawer Assembling Result](imgs/drawer_fitted_on_rack.jpg)
<figcaption>Drawer fitted into the rack</figcaption>

<br>

### Rack Assembly

With the manufacturing processes done, the rack assembly was performed. It is worth noting that the pieces have specific fittings through cutouts and pins corresponding to each other, but these fittings are not pressure-adjusted what requires the use of adhesion solutions, such as glue. In the case of the acrylic pieces, a solution called S-320 was used. This solution has a glue effect when it reacts with the polymer, fusing the pieces that are in contact.

![Rack Assembling Process](imgs/rack_assembling_process.jpg)
<figcaption>Assembling the rack parts with the S-320 solution</figcaption>

<br>

![Assembled Rack](imgs/assembled_rack.png)
<figcaption>Final result of rack assembly</figcaption>

<br>

For a reference purpose, there is the exploded perspective of the rack. It is possible to check in the image below where each component of the rack are assembled.

![Drawer Assembly](imgs/drawer_assembling.png){width=800}
<figcaption>Drawer exploded perspective</figcaption>

<br>


![Niche Assembly](imgs/niche_assembling.png){width=800}
<figcaption>Router niche exploded perspective</figcaption>

<br>

![Drawer Shelves Assembly](imgs/shelves_assembling.png){width=800}
<figcaption>Drawer shelves exploded perspective</figcaption>

<br>

![Rack Assembly](imgs/rack_assembling.png){width=800}
<figcaption>Rack exploded perspective</figcaption>

<br>

*images with rack exploded perspective*

## Parts Files

In this section is possible to download and work on the same files presented in the previously.

Click [here](https://insper-my.sharepoint.com/:f:/g/personal/leonardonr1_insper_edu_br/Eh0B72-dcSVIvPGwLCOnR-oB-YIDtvz6Izd2h586OY8hQQ?e=SPmWfI)
to get access to the files.
