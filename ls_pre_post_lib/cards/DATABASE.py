from dataclasses import dataclass, field
from typing import Union, Any, List
from .card import ICard


@dataclass
class ID_line:
    """

    ID1:=ID of the first node.
    -----------------------------------------------------------------
    ID2:=ID of the second node.
    -----------------------------------------------------------------
    ID3:=ID of the third node.
    -----------------------------------------------------------------
    ID4:=ID of the fourth node.
    -----------------------------------------------------------------
    ID5:=ID of the fifth node.
    -----------------------------------------------------------------
    ID6:=ID of the sixth node.
    -----------------------------------------------------------------
    ID7:=ID of the seventh node.
    -----------------------------------------------------------------
    ID8:=ID of the eighth node.

    """
    ID1: int = ""
    ID2: int = ""
    ID3: int = ""
    ID4: int = ""
    ID5: int = ""
    ID6: int = ""
    ID7: int = ""
    ID8: int = ""


@dataclass
class Card_with_id_lines(ICard):
    name: str = "Card_with_id_lines"
    rows_lengths: List[int] = field(default_factory=list)  # variable quantity due to ID_line

    ID_line: List[dict] = field(default_factory=list)


@dataclass
class ASCII_options_main_parameters(ICard):
    """

    """
    name: str = ""
    rows_lengths: List[int] = field(default_factory=lambda: [4])

    DT: Union[int, float] = 0.0
    BINARY: [0, 1, 2, 3] = 0
    LCUR: int = 0
    IOOPT: [1, 2, 3] = 1


@dataclass
class ABSTAT(ASCII_options_main_parameters):
    """
    ABSTAT - Airbag Statistics
    """
    name: str = "DATABASE_ABSTAT"


@dataclass
class ABSTAT_CPM(ASCII_options_main_parameters):
    """
    ABSTAT_CPM - Airbag Statistics CPM
    """
    name: str = "DATABASE_ABSTAT_CPM"


@dataclass
class ATDOUT(ASCII_options_main_parameters):
    """
    ATDOUT - atdout
    """
    name: str = "DATABASE_ATDOUT"


@dataclass
class AVSFLT(ASCII_options_main_parameters):
    """
    AVSFLT - AVS Database
    """
    name: str = "DATABASE_AVSFLT"


@dataclass
class BEARING(ASCII_options_main_parameters):
    """
    BEARING - *ELEMENT_BEARING force output
    """
    name: str = "DATABASE_BEARING"


@dataclass
class BNDOUT(ASCII_options_main_parameters):
    """
    BNDOUT - Boundary Condition forces and energy
    """
    name: str = "DATABASE_BNDOUT"


@dataclass
class CURVOUT(ASCII_options_main_parameters):
    """
    CUTOUT - Output from *DEFINE_CURVE_FUNCTION
    """
    name: str = "DATABASE_CURVOUT"


@dataclass
class DCFAIL(ASCII_options_main_parameters):
    """
    DCFAIL - Failure function data for *MAT_SPOTWELD_DAIMLERCHRYSLER
    """
    name: str = "DATABASE_DCFAIL"


@dataclass
class DISBOUT(ASCII_options_main_parameters):
    """
    DISBOUT - Discrete beam element, type 6,  relative displacements, rotations, and force resultants, all  in the local
    coordinate system, which is also output
    """
    name: str = "DATABASE_DISBOUT"


@dataclass
class DEFGEO(ASCII_options_main_parameters):
    """
    DEFGEO - Deformed Geometry
    """
    name: str = "DATABASE_DEFGEO"


@dataclass
class DEFORC(ASCII_options_main_parameters):
    """
    DEFORC - Discrete Element
    """
    name: str = "DATABASE_DEFORC"


@dataclass
class DEMASSFLOW(ASCII_options_main_parameters):
    """
    DEMASSFLOW - Measure mass flow rate across defined plane and use together with *DEFINE_DE_MASSFLOW_PLANE
    """
    name: str = "DATABASE_DEMASSFLOW"


@dataclass
class ELOUT(ASCII_options_main_parameters):
    """

    ELOUT  - Element Output Data

    OPTION1:=OPTION1 applies to either the NODOUT or ELOUT files.
             For the NODOUT file OPTION1 is a real variable that
             defines the time interval between outputs for the high
             frequency file, NODOUTHF. If OPTION1 is zero, no output
             is printed. Nodal points that are to be output at a
             higher frequency are flagged using HFO in the
             DATABASE_HISTORY_NODE_LOCAL input. For the ELOUT file
             OPTION1 is an integer variable that gives the number of
             additional history variables written into the ELOUT file
             for each integration point in the solid elements.
    -----------------------------------------------------------------
    OPTION2:=OPTION2 applies to either the NODOUTHF or ELOUT files.
             For the NODOUTHF OPTION2 defines the binary file flag
             for the high frequency NODOUTHF file. See BINARY above.
             For the ELOUT file OPTION2 is an integer variable that
             gives the number of additional history variables written
             into the ELOUT file for each integration point in the
             shell elements.
    -----------------------------------------------------------------
    OPTION3:=OPTION3 applies to the ELOUT file only. For the ELOUT
             file OPTION3 is an integer variable that gives the
             number of additional history variables written into the
             ELOUT file for each integration point in the thick shell
             elements.
    -----------------------------------------------------------------
    OPTION4:=OPTION4 applies to the ELOUT file only. For the ELOUT
             file OPTION4 is an integer variable that gives the number
             of additional history variables written into the ELOUT
             file for each integration point in the beam elements.

    """
    name: str = "DATABASE_ELOUT"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    OPTION1: int = 0
    OPTION2: int = 0
    OPTION3: int = 0
    OPTION4: int = 0


@dataclass
class ICVOUT(ASCII_options_main_parameters):
    """
    ICVOUT - 
    """
    name: str = "DATABASE_ICVOUT"


@dataclass
class GCEOUT(ASCII_options_main_parameters):
    """
    GCEOUT - Contact Entities
    """
    name: str = "DATABASE_GCEOUT"


@dataclass
class GLSTAT(ASCII_options_main_parameters):
    """
    GLSTAT - Global Statistics
    """
    name: str = "DATABASE_GLSTAT"


@dataclass
class GLSTAT_MASS_PROPERTIES(ASCII_options_main_parameters):
    """
    GLSTAT_MASS_PROPERTIES - This is an option for the glstat file to include mass and inertial properties
    """
    name: str = "DATABASE_GLSTAT_MASS_PROPERTIES"


@dataclass
class JNTFORC(ASCII_options_main_parameters):
    """
    JNTFORC - Joint Forces
    """
    name: str = "DATABASE_JNTFORC"


@dataclass
class MATSUM(ASCII_options_main_parameters):
    """
    MATSUM - Material Energies
    """
    name: str = "DATABASE_MATSUM"


@dataclass
class MOVIE(ASCII_options_main_parameters):
    """
    MOVIE - Movie files
    """
    name: str = "DATABASE_MOVIE"


@dataclass
class MPGS(ASCII_options_main_parameters):
    """
    MPGS - MPGS files
    """
    name: str = "DATABASE_MPGS"


@dataclass
class NCFORC(ASCII_options_main_parameters):
    """
    NCFORC - Nodal Interface Forces
    """
    name: str = "DATABASE_NCFORC"


@dataclass
class NODFOR(ASCII_options_main_parameters):
    """
    NODFOR - Nodal force groups
    """
    name: str = "DATABASE_NODFOR"


@dataclass
class NODOUT(ASCII_options_main_parameters):
    """
    NODOUT - Nodal Displacement/Velocity/Acceleration data

    OPTION1:=OPTION1 applies to either the NODOUT or ELOUT files. For
             the NODOUT file OPTION1 is a real variable that defines
             the time interval between outputs for the high frequency
             file, NODOUTHF. If OPTION1 is zero, no output is
             printed. Nodal points that are to be output at a higher
             frequency are flagged using HFO in the
             DATABASE_HISTORY_NODE_LOCAL input. For the ELOUT file
             OPTION1 is an integer variable that gives the number of
             additional history variables written into the ELOUT file
             for each integration point in the solid elements.
    -----------------------------------------------------------------
    OPTION2:=OPTION2 applies to either the NODOUTHF or ELOUT files.
             For the NODOUTHF OPTION2 defines the binary file flag
             for the high frequency NODOUTHF file. See BINARY above.
             For the ELOUT file OPTION2 is a integer variable that
             gives the number of additional history variables written
             into the ELOUT file for each integration point in the
             shell elements.

    """
    name: str = "DATABASE_NODOUT"
    rows_lengths: List[int] = field(default_factory=lambda: [6])

    OPTION1: Union[int, float] = 0
    OPTION2: Union[int, float] = 0


@dataclass
class PBSTAT(ASCII_options_main_parameters):
    """
    PBSTAT - Particle blast data
    """
    name: str = "DATABASE_PBSTAT"


@dataclass
class PLLYOUT(ASCII_options_main_parameters):
    """
    PLLYOUT - Pulley element data for *ELEMENT_BEAM_PULLEY
    """
    name: str = "DATABASE_PLLYOUT"


@dataclass
class PRTUBE(ASCII_options_main_parameters):
    """
    PRTUBE - Pressure tube data
    """
    name: str = "DATABASE_PRTUBE"


@dataclass
class PYRO(ASCII_options_main_parameters):
    """
    PYRO -
    """
    name: str = "DATABASE_PYRO"


@dataclass
class RBDOUT(ASCII_options_main_parameters):
    """
    RBDOUT - Rigid Body data
    """
    name: str = "DATABASE_RBDOUT"


@dataclass
class RCFORC(ASCII_options_main_parameters):
    """
    RCFORC - Resultant Interface Forces
    """
    name: str = "DATABASE_RCFORC"


@dataclass
class RWFORC(ASCII_options_main_parameters):
    """
    RWFORC - RigidWall Forces
    """
    name: str = "DATABASE_RWFORC"


@dataclass
class SBTOUT(ASCII_options_main_parameters):
    """
    SBTOUT - Seatbelt Output data
    """
    name: str = "DATABASE_SBTOUT"


@dataclass
class SECFORC(ASCII_options_main_parameters):
    """
    SECFORC- Cross Section Forces data
    """
    name: str = "DATABASE_SECFORC"


@dataclass
class SLEOUT(ASCII_options_main_parameters):
    """
    SLEOUT - Sliding Interface Energies
    """
    name: str = "DATABASE_SLEOUT"


@dataclass
class SPCFORC(ASCII_options_main_parameters):
    """
    SPCFORC - SPC Reaction forces
    """
    name: str = "DATABASE_SPCFORC"


@dataclass
class SPHOUT(ASCII_options_main_parameters):
    """
    SPHOUT - SPH Output data
    """
    name: str = "DATABASE_SPHOUT"


@dataclass
class SPHMASSFLOW(ASCII_options_main_parameters):
    """
    SPHMASSFLOW -
    """
    name: str = "DATABASE_SPHMASSFLOW"


@dataclass
class SSSTAT(ASCII_options_main_parameters):
    """
    SSSTAT - Subsystem data
    """
    name: str = "DATABASE_SSSTAT"


@dataclass
class SSSTAT_MASS_PROPERTIES(ASCII_options_main_parameters):
    """
    SSSTAT_MASS_PROPERTIES - This is an option for the ssstat file to include mass and inertial properties for the
    subsystems
    """
    name: str = "DATABASE_SSSTAT_MASS_PROPERTIES"


@dataclass
class SWFORC(ASCII_options_main_parameters):
    """
    SWFORC - Spotweld Nodal Constraint Reaction Forces
    """
    name: str = "DATABASE_SWFORC"


@dataclass
class TPRINT(ASCII_options_main_parameters):
    """
    TPRINT - Structural/Thermal coupled output
    """
    name: str = "DATABASE_TPRINT"


@dataclass
class TRHIST(ASCII_options_main_parameters):
    """
    TRHIST - Trace Particle History data
    """
    name: str = "DATABASE_TRHIST"


@dataclass
class BINARY_D3PLOT(ICard):
    """

    DT:=This field defines the time interval between output states,
        DT, for all options except D3DUMP, RUNRSF, and D3DRLF.
    -----------------------------------------------------------------
    LCDT:=Optional load curve ID specifying the output time interval
          as a function of time. This variable is only available for
          options D3PLOT, D3PART, D3THDT, INTFOR and BLSTFOR.
    -----------------------------------------------------------------
    BEAM:=Discrete element option flag (*DATABASE_вЂЊBINARY_вЂЊD3PLOT
          only):
    EQ.0: Discrete spring and damper elements are added to the d3plot
          database where they are displayed as beam elements.The
          discrete elementsвЂ™ global x, global y, global zand
          resultant forces(moments) and change in length(rotation)
          are written to the database where LS - PrePost(incorrectly)
          labels them as though they were beam quantities, such as
          axial force, S - shear resultant, T - shear resultant, etc.
    EQ.1: No discrete spring, damperand seatbelt elements are added
          to the d3plot database.This option is useful when
          translating old LS - DYNA input decks to KEYWORD input. In
          older input decks there is no requirement that beam and
          spring elements have unique IDs,and beam elements may be
          created for the springand dampers with identical IDs to
          existing beam elements causing a fatal error.However, this
          option comes with some limitationsand, therefore, should be
          used with caution. Contact interfaces which are based on
          part IDs of seatbelt elements will not be properly
          generated if this option is used. DEFORMABLE_TO_RIGID will
          not work if PID refers to discrete, damper, or seatbelt
          elements.
    EQ.2: Discrete spring and damper elements are added to the d3plot
          database where they are displayed as beam elements(similar
          to option 0).In this option the element resultant force is
          written to its first database position allowing beam axial
          forces and spring resultant forces to be plotted at the
          same time.This can be useful during some post - processing
          applications. This flag, set in* DATABASE_BINARY_D3PLOT,
          also affects the display of discrete elements in several
          other databases, such as d3drlfand d3part.
    -----------------------------------------------------------------
    NPLTC:=DT=ENDTIM/NPLTC.  Applies to D3PLOT, D3PART, DEMFOR, and
           INTFOR options only.  This overrides the DT specified in
           the first field. ENDTIM is specified in
           *CONTROL_TERMINATION
    -----------------------------------------------------------------
    PSETID:=Part set ID for D3PART and D3PLOT options only. See
            *SET_вЂЊPART. Parts in PSETID will excluded in the d3plot
            database.  Only parts in PSETID are included in the
            d3part database.

    #################################################################

    IOOPT:=Flag to govern behavior of plot frequency load curve:
    EQ.1: At the time each plot is generated, the load curve value is
          added to the current time to determine the next plot time.
          (this is the default behavior).
    EQ 2: At the time each plot is generated, the next plot time T is
          computed so that T = the current time plus the load curve
          value at time T.
    EQ 3: A plot is generated for each ordinate point in the load
          curve definition. The actual value of the load curve is
          ignored.
    -----------------------------------------------------------------
    RATE:=Time interval T between filter sampling.  See Remark 7
    -----------------------------------------------------------------
    CUTOFF:=Frequency cut-off  in Hz.  See Remark 7
    -----------------------------------------------------------------
    WINDOW:=The width of the window W in units of time for storing
            the single, forward filtering required for the TYPE = 2
            filter option. Increasing the width of the window will
            increase the memory required for the analysis. A window
            that is too narrow will reduce the amplitude of the
            filtered result significantly, and values below 15 are
            not recommended for that reason. In general, the results
            for the TYPE = 2 option are sensitive to the width of the
            window and experimentation is required.  See Remark 7.
    -----------------------------------------------------------------
    TYPE:=Flag for filtering options.  See Remark 7.
    EQ.0: No filtering (default).
    EQ.1: Single pass, forward Butterworth filtering.
    EQ.2: Two pass filtering over the specified time window. Backward
          Butterworth filtering is applied to the forward Butterworth
          results that have been stored.
    This option improves the phase accuracy significantly at the
    expense of memory
    -----------------------------------------------------------------
    PSET:=Part set ID for filtering.  If no set is specified, all
          parts are included.  For each element integration point in
          the d3plot file, 24 words of memory are required in LS-DYNA
          for the single pass filtering, and more for the two pass
          filtering. Specifying PSET is recommended to minimize the
          memory requirements. See Remark 7.

    """
    name: str = "DATABASE_BINARY_D3PLOT"
    rows_lengths: List[int] = field(default_factory=lambda: [5, 6])

    DT: Union[int, float] = 0
    LCDT: int = 0
    BEAM: int = 0
    NPLTC: Any = 0
    PSETID: int = 0

    IOOPT: int = 0
    RATE: Union[int, float] = 0.0
    CUTOFF: Union[int, float] = 0.0
    WINDOW: Union[int, float] = 0.0
    TYPE: int = 0
    PSET: int = 0


@dataclass
class CROSS_SECTION_PLANE(ICard):
    """

    TITLE:=Cross section descriptor. It is suggested that unique
           descriptions be used.
    -----------------------------------------------------------------
    CSID:=Optional ID for cross section. If not specified cross
          section ID is taken to be the cross section order in the
          input deck.
    -----------------------------------------------------------------
    PSID:=Part set ID. If zero all parts are included.
    -----------------------------------------------------------------
    XCT:=x-coordinate of tail of any outward drawn normal vector, N,
         originating on wall (tail) and terminating in space (head),
         (see Figure 9.1 in user's manual).
    -----------------------------------------------------------------
    YCT:=y-coordinate of tail of normal vector, N.
    -----------------------------------------------------------------
    ZCT:=z-coordinate of tail of normal vector, N.
    -----------------------------------------------------------------
    XCH:=x-coordinate of head of normal vector, N.
    -----------------------------------------------------------------
    YCH:=y-coordinate of head of normal vector, N.
    -----------------------------------------------------------------
    ZCH:=z-coordinate of head of normal vector, N.
    -----------------------------------------------------------------
    RADIUS:=Optional radius.
    EQ.0.0:	Not used.
    GT.0.0: A circular cut plane will be created that is centered
            at(XCT ,YCT ,ZCT) with radius = RADIUS and has a normal
            vector originating at(XCT ,YCT ,ZCT) and pointing
            towards(XCH ,YCH ,ZCH).
    LT.0.0: The radius will be the absolute value of RADIUS and XCT
            and XCH will be nodes IDs.The node with ID XCT is the
            center of the circular cut plane.The normal vector of the
            plane is the vector pointing from the node with ID XCT to
            the node with ID XCH.YCT, ZCT, YCH,and ZCH are ignored.
    If RADIUS != 0.0, the variables XHEV, YHEV, ZHEV, LENL,and LENM,
    which are specified on Card 1a.2, will be ignored.

    #################################################################

    XHEV:=x-coordinate of head of edge vector, L.
    -----------------------------------------------------------------
    YHEV:=y-coordinate of head of edge vector, L.
    -----------------------------------------------------------------
    ZHEV:=z-coordinate of head of edge vector, L.
    -----------------------------------------------------------------
    LENL:=Length of edge a, in L direction (default is set to
          infinity).
    -----------------------------------------------------------------
    LENM:=Length of edge b, in M direction (default is set to
          infinity).
    -----------------------------------------------------------------
    ID:=Rigid body or accelerometer ID. The force resultants are
        output in the updated local system of the rigid body or
        accelerometer.
    -----------------------------------------------------------------
    ITYPE:=Flag that specifies whether ID above pertains to a rigid
           body, an accelerometer, or a coordinate system:
    EQ. 0: rigid body (default),
    EQ. 1: accelerometer,
    EQ. 2: coordinate ID.

    """
    name: str = "DATABASE_CROSS_SECTION_PLANE_ID"
    rows_lengths: List[int] = field(default_factory=lambda: [2, 8, 6])

    CSID: int = 0
    TITLE: str = ""

    PSID: int = 0
    XCT: Union[int, float] = 0.0
    YCT: Union[int, float] = 0.0
    ZCT: Union[int, float] = 0.0
    XCH: Union[int, float] = 0.0
    YCH: Union[int, float] = 0.0
    ZCH: Union[int, float] = 0.0
    RADIUS: Union[int, float] = 0.0

    XHEV: Union[int, float] = 0.0
    YHEV: Union[int, float] = 0.0
    ZHEV: Union[int, float] = 0.0
    LENL: Union[int, float] = ""
    ID: int = 0
    ITYPE: [0, 1, 2] = 0


@dataclass
class EXTENT_BINARY(ICard):
    """

    NEIPH:=Number of additional integration point history variables
           written to the binary database for solid elements. The
           integration point data is written in the same order that
           it is stored in memory-each material modal has its own
           history variables that are stored. For user defined
           materials it is important to store the history data that
           is needed for plotting before the data which is not of
           interest.
    -----------------------------------------------------------------
    NEIPS:=Number of additional integration point history variables
           written to the binary database for both shell and thick
           shell elements for each integration point, see NEIPH above
    -----------------------------------------------------------------
    MAXINT:=Number of shell integration points written to the LS-DYNA
            database, see also *INTEGRATION_SHELL. If the default
            value of 3 is used then results are output for the
            outermost (top) and innermost (bottom) integration points
            together with results for the neutral axis. If MAXINT is
            set to 3 and the element has 1 integration point then all
            three results will be the same. If a value other than 3
            is used then the results for the first MAXINT integration
            points in the element will be output. NOTE: If the
            element has an even number of integration points and
            MAXINT is not set to 3 then you will not get mid-surface
            results. (See Remarks in user's manual).If MAXINT is set
            to a negative number, MAXINT integration points are
            output for each in plane integration point location and
            no averaging is used. This can greatly increase the size
            of the binary databases d3plot, d3thdt, and d3part
    -----------------------------------------------------------------
    STRFLG:=Flag for output of strain tensors. STRFLG is interpreted
            digit-wise STRFLG = [NML], STRFLG = 100*N + 10*M + L
    L.EQ.1: Write strain tensor data to d3plot, elout, and dynain.
            For shell and thick shell elements two tensors are
            written, one at the innermost and one at the outermost
            integration point.  For solid elements a single strain
            tensor is written
    M.EQ.1:	Write plastic strain data to d3plot.
    N.EQ.1:	Write thermal strain data to d3plot.
    -----------------------------------------------------------------
    SIGFLG:=Flag for including stress tensor in the shell LS-DYNA
            database:
    EQ.1: include (default),
    EQ.2: exclude.
    -----------------------------------------------------------------
    EPSFLG:=Flag for including the effective plastic strains in the
            shell LS-DYNA database:
    EQ.1: include (default),
    EQ.2: exclude.
    -----------------------------------------------------------------
    RLTFLG:=Flag for including stress resultants in the shell LS-DYNA
            database:
    EQ.1: include (default),
    EQ.2: exclude.
    -----------------------------------------------------------------
    ENGFLG:=Flag for including internal energy and thickness in the
            LS-DYNA database:
    EQ.1: include (default),
    EQ.2: exclude.

    #################################################################

    CMPFLG:=Orthotropic and anisotropic material stress output in
            local coordinate system for shells and thick shells.
    EQ.0: global,
    EQ.1: local.
    -----------------------------------------------------------------
    IEVERP:=Every plot state for D3PLOT database is written to a
            separate file. This option will limit the database to 100
            states:
    EQ.0: more than one state can be on each plotfile,
    EQ.1: one state only on each plotfile.
    -----------------------------------------------------------------
    BEAMIP:=Number of beam integration points for output. This option
            does not apply to beams that use a resultant formulation.
    -----------------------------------------------------------------
    DCOMP:=Data compression to eliminate rigid body data:
    EQ.1: off (default), no data compression,
    EQ.2: on.
    EQ.3: off, no rigid body data compression, but nodal velocities
          and accelerations are eliminated from the database.
    EQ.4: on, rigid body data compression active and nodal velocities
          and accelerations are eliminaated from the database.
    EQ.5: on, rigid body data compression active and rigid nodal data
          are eliminated from the database. Only 6 dof rigid body
          motion is written.
    EQ.6: on, rigid body data compression active, rigid nodal data,
          and nodal velocities and accelerations are eliminated from
          the database.  Only 6 dof rigid body motion is written.
    -----------------------------------------------------------------
    SHGE:=Output shell hourglass energy:
    EQ.1: off (default), no hourglass energy written,
    EQ.2: on.
    -----------------------------------------------------------------
    STSSZ:=Output shell element time step, mass or added mass:
    EQ.1: off (default),
    EQ.2: out time step size,
    EQ.3: output mass, added mass, or time step size.
    (See Remark 3 in user's manual).
    -----------------------------------------------------------------
    N3THDT:=Material energy write option for D3THDT database
    EQ.1: off, energy is NOT written to D3THDT database,
    EQ.2: on (default), energy is written to D3THDT database.
    -----------------------------------------------------------------
    IALEMAT:=Output solid part id list containing ale materials
    EQ.1: on (default)
    EQ.0: off

    #################################################################

    NINTSLD:=Number of solid element integration points written to
             the LS-DYNA database. The default value is 1. For solids
             with multiple integration points NINTSLD may be set
             to 8. Currently, no other values for INITSLD are
             allowed. For solids with multiple integration points, an
             average value is output if NINTSLD is set to 1.
    -----------------------------------------------------------------
    PKP_SEN:=Flag to output the peak pressure and surface energy
             computed by each contact interface into the interface
             force database.   To obtain the surface energy, FRCENG,
             must be sent to 1 on the control contact card.  When
             PKP_SEN=1, it is possible to identify the energies
             generated on the upper and lower shell surfaces, which
             is important in metal forming applications.  This data
             is mapped after each H-adaptive remeshing.
    EQ.0: No data is written
    EQ.1: Output the peak pressures and surface energy by contact
          interface.
    -----------------------------------------------------------------
    SCLP:=A scaling parameter used in the computation of the peak
          pressure. This parameter is generally set to unity (the
          default), but it must be greater than 0..
    -----------------------------------------------------------------
    HYDRO:=Either 3 or 5 additional history variables useful to shock
           physics are output as the last history variables. For
           HYDRO = 1, the internal energy per reference volume, the
           reference volume, and the value of the bulk viscosity are
           added to the database, and for HYDRO = 2, the relative
           volume and current density are also added
    -----------------------------------------------------------------
    MSSCL:=Output nodal information related to mass scaling into the
           D3PLOT database.  This option can be activated if and only
           if DT2MS < 0.0, see control card *CONTROL_TIMESTEP.
           This option is available starting with the second release
           of Version 971.
    EQ.0: No data is written
    EQ.1: Output incremental nodal mass
    EQ.2: Output percentage increase in nodal mass.
    -----------------------------------------------------------------
    THERM:=Output of thermal data to d3plot. The use of this option
           (THERM>0) may make the database incompatible with other
           3rd party software.
    EQ.0: (default) output temperature
    EQ.1: output temperature
    EQ.2: output temperature and flux
    EQ.3: output temperature, flux, and shell bottom and top surface
          temperature
    -----------------------------------------------------------------
    INTOUT:=Output stress/strain at all integration points for
            detailed element output in the file ELOUTDET.  DT and
            BINARY of *DATABASE_ELOUT apply to ELOUTDET.  See remarks
            4-10 below.
    EQ.STRESS: when stress output is required
    EQ.STRAIN when strain output is required
    EQ.ALL when both stress and strain output are required
    -----------------------------------------------------------------
    NODOUT:=Output extrapolated stress/strain at connectivity nodes
            points for detailed element output in the file ELOUTDET.
            DT and BINARY of *DATABASE_ELOUT apply to ELOUTDET.
    EQ.STRESS when stress output is required
    EQ.STRAIN when strain output is required
    EQ.ALL when both stress and strain output are required
    EQ.STRESS_GL when nodal averaged stress output is required
    EQ.STRAIN_GL when nodal averaged strain output is required
    EQ.ALL_GL for nodal averaged stress and strain output

    #################################################################

    DTDT:=Output of node point dtemperature/dtime data to d3plot
    EQ.0: (default) no output
    EQ.1: output dT/dt
    -----------------------------------------------------------------
    RESPLT:=Output of translational and rotational residual forces to
            d3plot and d3iter
    EQ.0: No output
    EQ.1: Output residual
    -----------------------------------------------------------------
    NEIPB:=Number of additional integration point history variables
           written to the binary database for beam elements.
    -----------------------------------------------------------------
    QUADSLD:=Output option for quadratic higher order solid elements
             EQ.1: output full connectivity,
    EQ.2: full connectivity and data at all integration points.
    -----------------------------------------------------------------
    CUBSLD:=Output option for cubic higher order solid elements EQ.1:
            output full connectivity,
    EQ.2: full connectivity and data at all integration points.
    -----------------------------------------------------------------
    DELERES:=Output flag for results of deleted elements:
    EQ.0:	no results output(all zero)
    EQ.1 : last available results, e.g., stressesand history
           variables, are written to d3plotand d3part.

    """
    name: str = "DATABASE_EXTENT_BINARY"
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8, 8, 6])

    NEIPH: int = 0
    NEIPS: int = 0
    MAXINT: int = 3
    STRFLG: Union[int, float] = 0
    SIGFLG: [1, 2] = 1
    EPSFLG: [1, 2] = 1
    RLTFLG: [1, 2] = 1
    ENGFLG: [1, 2] = 1

    CMPFLG: [0, 1] = 0
    IEVERP: [0, 1] = 0
    BEAMIP: int = 0
    DCOMP: [1, 2, 3, 4, 5, 6] = 1
    SHGE: [1, 2] = 1
    STSSZ: [1, 2, 3] = 1
    N3THDT: [1, 2] = 2
    IALEMAT: [0, 1] = 1

    NINTSLD: [1, 8] = 1
    PKP_SEN: [0, 1] = 0
    SCLP: Union[int, float] = 1.0
    HYDRO: Union[int, float] = 0
    MSSCL: [0, 1, 2] = 0
    THERM: [0, 1, 2, 3] = 0
    INTOUT: str = ""
    NODOUT: str = ""

    DTDT: [0, 1] = 0
    RESPLT: [0, 1] = 0
    NEIPB: int = 0
    QUADSLD:  [0, 1, 2] = 0
    CUBSLD:  [0, 1, 2] = 0
    DELERES: [0, 1] = 0


@dataclass
class HISTORY_NODE(Card_with_id_lines):
    """

    """
    name: str = "DATABASE_HISTORY_NODE"


@dataclass
class HISTORY_NODE_SET(Card_with_id_lines):
    """

    """
    name: str = "DATABASE_HISTORY_NODE_SET"


@dataclass
class HISTORY_SHELL(Card_with_id_lines):
    """

    """
    name: str = "DATABASE_HISTORY_SHELL"

@dataclass
class HISTORY_SHELL_SET(Card_with_id_lines):
    """

    """
    name: str = "DATABASE_HISTORY_SHELL_SET"


@dataclass
class HISTORY_SOLID(Card_with_id_lines):
    """

    """
    name: str = "DATABASE_HISTORY_SOLID"


@dataclass
class HISTORY_SOLID_SET(Card_with_id_lines):
    """

    """
    name: str = "DATABASE_HISTORY_SOLID_SET"