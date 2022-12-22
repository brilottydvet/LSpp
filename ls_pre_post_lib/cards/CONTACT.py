from dataclasses import dataclass, field
from typing import Union, List
from .card import ICard


@dataclass
class MPP1(ICard):
    """

    IGNORE:=By setting this variable to 1, the "ignore initial
            penetrations" option is turned on for this contact.
            Alternatively, this option may be turned on by setting
            IGNORE = 1 on Card 4 of *CONTROL_CONTACT or on Optional
            Card C of *CONTACT.  In other words, if IGNORE is set to
            1 in any of three places, initial penetrations are
            tracked.
    -----------------------------------------------------------------
    BCKT:=Bucket sort frequency. This parameter does not apply when
          SOFT = 2 on Optional Card A or to Mortar contacts. For
          these two exceptions, the BSORT option on Optional Card A
          applies instead.
    -----------------------------------------------------------------
    LCBCKT:=Load curve for bucket sort frequency. This parameter does
            not apply when SOFT = 2 on Optional Card A or to Mortar
            contacts.  For the two exceptions, the negative BSORT
            option on Optional Card A applies instead.
    -----------------------------------------------------------------
    NS2TRK:=Number of potential contacts to track for each tracked
            node.  The normal input for this (DEPTH on Optional Card
            A) is ignored..
    -----------------------------------------------------------------
    INITITR:=Number of iterations to perform when trying to eliminate
             initial penetrations.  Note that an input of 0 means 0,
             not the default value (which is 2).  Leaving this field
             blank will set INITITR to 2.
    -----------------------------------------------------------------
    PARMAX:=The parametric extension distance for contact segments.
            The MAXPAR parameter on Optional Card A is not used for
            MPP.  For non-tied contacts, the default is 1.0005. For
            tied contacts the default is 1.035 and, the actual
            extension used is computed as follows: see the manual
    -----------------------------------------------------------------
    UNUSED:=unused.
    -----------------------------------------------------------------
    CPARM8:=Flag for behavior of AUTOMATIC_GENERAL contacts.
            CPARM8вЂ™s value is interpreted as two separate flags:
            OPT1 and OPT2 according to the rule,
    "CPARM8" = "OPT1" + "OPT2".
    When OPT1 and OPT2 are both set, both options are active.
    OPT1.Flag to exclude beam - to - beam contact from the same PID.
    EQ.0: Flag is not set(default).
    EQ.1: Flag is set.
    EQ.2: Flag is set.CPARM8 = 2 additionally permits contact
          treatment of spot weld(type 9) beams in AUTOMATIC_GENERAL
          contacts; spot weld beams are otherwise disregarded
          entirely by AUTOMATIC_GENERAL contacts.
    OPT2.Flag to shift generated beam affecting only shell - edge -
    to - shell - edge treatment.See also SRNDE in Optional Card E.
    EQ.10: Beam generated on exterior shell edge will be shifted into
           the shell by half the shell thickness.Therefore, the shell
           - edge - to - shell - edge contact starts right at the
           shell edge and not at an extension of the shell edge.

    """
    name: str = "_MPP"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    IGNORE: int = 0
    BCKT: int = 200
    LCBCKT: int = ""
    NS2TRK: int = 3
    INITITR: int = 2
    PARMAX: Union[int, float] = 1.0005
    UNUSED1: str = ""
    CPARM8: [0, 1, 2, 10, 11, 12] = 0


@dataclass
class MPP2(MPP1):
    """

    UNUSED:=
    -----------------------------------------------------------------
    CHKSEGS:=If this value is non-zero, then for the node-to-surface
             and surface-to-surface contacts LS-DYNA performs a
             special check at time 0 for elements that are inverted
             (or nearly so), These elements are removed from contact.
             These poorly formed elements have been known to occur on
             the tooling in metalforming problems, which allows these
             problems to run.  It should not normally be needed for
             reasonable meshes.
    -----------------------------------------------------------------
    PENSF:=This option is used together with IGNORE for 3D forging
           problems.  If non-zero, the IGNORE penetration distance is
           multiplied by this value each cycle, effectively pushing
           the tracked node back out to the surface.  This is useful
           for nodes that might get generated below the reference
           surface during 3D remeshing.  Care should be exercised, as
           energy may be generated and stability may be effected for
           values lower than 0.95.  A value in the range of 0.98 to
           0.99 or higher (but < 1.0) is recommended
    -----------------------------------------------------------------
    GRPABLE:=Set to 1 to invoke an alternate MPP communication
             algorithm for various SINGLE_SURFACE (including
             AUTOMATIC_GEN-ERAL), NODES_TO_SURFACE,
             SURFACE_TO_SURFACE, ERODING and SOFT = 2 contacts.  This
             groupable algorithm does not support all contact options,
             including MORTAR. It is still under development.  It can
             be significantly faster and scale better than the normal
             algorithm when there are more than two or three
             applicable contact types defined in the model. It is
             intended for speeding up the contact processing without
             changing the behavior of the contact.  See also
             *CONTROL_MPP_-CONTACT_GROUPABLE.

    """
    name: str = "_MPP"
    rows_lengths: List[int] = field(default_factory=lambda: [8, 4])

    and_: str = "&         "  # necessary for the correct card recording
    # UNUSED2: str = "" existing field in the card, but do not try to use
    CHKSEGS: int = 0
    PENSF: Union[int, float] = 1.0
    GRPABLE: int = 0


@dataclass
class Thermal(ICard):
    """

    K:=Thermal conductivity ( k ) of fluid between the slide
       surfaces. If a gap with a thickness L(gap) exists between the
       slide surfaces, then the conductance due to thermal
       conductivity between the slide surfaces is
    H(cond) = K/L(gap), Note that LS- DYNA calculates L(gap) based on
    deformation.
    -----------------------------------------------------------------
    FRAD:=Radiation factor, f, between the slide surfaces.
    -----------------------------------------------------------------
    H0:=Heat transfer conductance ( H cont ) for closed gaps. Use
        this heat transfer conductance for gaps in the
        range 0 <= L(gap) <= L(min) where L(min) is defined below.
    -----------------------------------------------------------------
    LMIN:=minimum length, use heat transfer conductance defined by
          HTC for gap thickness less than this value.
    -----------------------------------------------------------------
    LMAX:=maximum length, no thermal contact if gap thickness is
          greater than this value.
    -----------------------------------------------------------------
    FTOSA:=fraction of sliding frictional energy distributed to SURFB
           surface. (default: 0.5).Energy partitioned to the SURFB
           surface is (1-f).
    EQ.0: Set to 0.5 (default).The sliding friction energy is
          partitioned 50 % -50 % to the SURFA and SURFB surfaces in
          contact.
    -----------------------------------------------------------------
    BC_FLG:=Thermal boundary condition flag
    EQ.0: thermal boundary conditions are ON when parts are in
          contact
    EQ.1: thermal boundary conditions are OFF when parts are in
          contact
    -----------------------------------------------------------------
    ALGO:=Contact algorithm type.
    EQ.0: two way contact, both surfaces change temperature due to
          contact
    EQ.1: one way contact, surface of SURFB does not change
          temperature due to contact. Surface of SURFA does change
          temperature

    """
    name: str = "_THERMAL"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    K: Union[int, float] = ""
    FRAD: Union[int, float] = ""
    H0: Union[int, float] = ""
    LMIN: Union[int, float] = ""
    LMAX: Union[int, float] = ""
    FTOSA: Union[int, float] = 0.5
    BC_FLG: [0, 1] = ""
    ALGO: [0, 1] = ""


@dataclass
class T_Friction(Thermal):
    """

    LCFST:=Load curve number for static coefficient of friction as a
           function of temperature. The load curve value multiplies
           the coefficient value FS.For Mortar contact the
           temperature defining the scale factor Image is the mean
           temperature Image in the interface, if using a table one
           can prescribe the coefficient as an arbitrary function of
           both, i.e., Image. For this latter option, define a curve
           using Image as abscissa for each value of Image
    -----------------------------------------------------------------
    LCFDT:=Load curve number for dynamic coefficient of friction as a
           function of temperature. The load curve value multiplies
           the coefficient value FD.For Mortar contact the
           temperature defining the scale factor Image is the mean
           temperature Image in the interface, if using a table one
           can prescribe the coefficient as an arbitrary function of
           both, i.e., Image. For this latter option, define a curve
           using Image as abscissa for each value of Image.
    -----------------------------------------------------------------
    FORMULA:=Formula that defines the contact heat conductance as a
             function of temperature and pressure.
    -----------------------------------------------------------------
    a:=Load curve number for the a coefficient used in the formula
    -----------------------------------------------------------------
    b:=Load curve number for the b coefficient used in the formula
    -----------------------------------------------------------------
    c:=Load curve number for the c coefficient used in the formula
    -----------------------------------------------------------------
    d:=Load curve number for the d coefficient used in the formula
    -----------------------------------------------------------------
    LCH:=Load curve number for h. This parameter can refer to a curve
         ID (see *DEFINE_CURVE) or a function ID (see
         *DEFINE_FUNCTION).  When LCH is a curve ID (and a function
         ID) it is interpreted as follows:
    GT.0: the heat transfer coefficient is defined as a function of
          time, t, by a curve consisting of (t,h(t)) data pairs.
    LT.0: the heat transfer coefficient is defined as a function of
          temperature, T, by a curve consisting of (T,h(T)) data
          pairs. When the reference is to a function it is prototyped
          as follows h= h(t,T_avg ,T_slv ,T_msr ,P,g) where:
    t=solution time T_avg =average interface temperature
    T_slv =slave segment temperature
    T_msr =master segment temperature
    P=interface pressure
    g=gap distance between master and slave segment

    """
    name: str = "_THERMAL_FRICTION"
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8])

    LCFST: int = ""
    LCFDT: int = ""
    FORMULA: str = ""
    a: int = ""
    b: int = ""
    c: int = ""
    d: int = ""
    LCH: int = ""


@dataclass
class A(ICard):
    """

    SOFT:=Soft constraint option:
    EQ.0: Standard penalty formulation,
    EQ.1: soft constraint penalty formulation,
    EQ.2: pinball segment based contact penalty formulation.
    EQ.4: Constraint approach for FORMING contacts. This formulation
          only applies to one-way forming contacts. You should use
          itIt is used when penetration is large using the penalty
          formulations result in large penetrations. The results,
          however, are sensitive to damping.
    EQ.6: Special contact algorithm to handle sheet blank
          edge(deformable) to gage pin(rigid shell) contact during
          implicit gravity loading.This applies to
          *CONTACT_FORMING_NODES_TO_SURFACE only.See remarks under
          About SOFT = 6
    -----------------------------------------------------------------
    SOFSCL:=Scale factor for constraint forces of soft constraint
            option invoked with SOFT = 1(default=.10). Values greater
            than .5 for single surface contact and 1.0 for a one way
            treatment are inadmissible.
    -----------------------------------------------------------------
    LCIDAB:=Load curve ID defining airbag thickness as a function of
            time for type a13 contact
            (*CONTACT_AIRBAG_SINGLE_SURFACE).
    -----------------------------------------------------------------
    MAXPAR:=Maximum parametric coordinate in segment search (values
            1.025 and 1.20 recommended). Larger values can increase
            cost. If zero, the default is set to 1.025. This factor
            allows an increase in the size of the segments . May be
            useful at sharp corners.
    -----------------------------------------------------------------
    SBOPT:=Segment-based contact options (SOFT=2).
    EQ.0: defaults to 2.
    EQ.1: pinball edge-edge contact (not recommended).
    EQ.2: assume planer segments (default).
    EQ.3: warped segment checking.
    EQ.4: sliding option,
    EQ.5: do options 3 and 4.
    -----------------------------------------------------------------
    DEPTH:=Search depth in automatic contact. Value of 1 is
           sufficiently accurate for most crash applications and is
           much less expensive. LS-DYNA for improved accuracy sets
           this value to 2. If zero, the default is set to 2.
    LT.0: |DEPTH| is the load curve ID defining searching depth
          versus time.
    -----------------------------------------------------------------
    BSORT:=Number of cycles between bucket sorts. Values of 25 and
           100 are recommended for contact types 4 (SINGLE_SURFACE)
           and 13 (AUTOMATIC_SINGLE_SURFACE), respectively.  Values
           of 10-15 are okay for surface-to-surface and
           node-to-surface contact.  If zero, LS-DYNA determines the
           interval.  BSORT applies only to SMP (see BCKT on MPP 1
           for MPP) except in the case of SOFT = 2 or for Mortar
           contact, in which case BSORT applies to both SMP and MPP.
           For Mortar contact the default is the value associated
           with NSBCS on *CONTROL_CONTACT.
    LT.0: |BSORT| is the load curve ID defining bucket sorting
          frequency as a function of time.
    -----------------------------------------------------------------
    FRCFRQ:=Number of cycles between contact force updates for
            penalty contact formulations. This option can provide a
            significant speed-up of the contact treatment. If used,
            values exceeding 3 or 4 are dangerous. Considerable care
            must be exercised when using this option, as this option
            assumes that contact does not change FRCFRG cycles.
    EQ.0: FRCFRG is set to 1 and force calculations are performed
          each cycle-strongly recommended.

    """
    name: str = ""
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    SOFT: [0, 1, 2, 4, 6] = 0
    SOFSCL: Union[int, float] = 0.1
    LCIDAB: int = 0
    MAXPAR: Union[int, float] = 1.025
    SBOPT: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0] = 2.0
    DEPTH: int = 2
    BSORT: int = ""
    FRCFRQ: int = 1


@dataclass
class AB(A):
    """

    PENMAX:=For old types 3, 5, 8, 9, 10 (see Mapping of *CONTACT
            keyword option to contact type in d3hsp at the end of
            General Remarks) and Mortar contact, PENMAX is the
            maximum penetration distance. For contact types a3, a5,
            a10, 13, 15, and 26, the segment thickness multiplied by
            PENMAX defines the maximum penetration allowed (as a
            multiple of the segment thickness).  (See Table 0-2.):):
    EQ.0.0 for old type contacts 3, 5, and 10: Use small penetration
           search and value calculated from thickness and XPENE, see
           *CONTROL_ CONTACT.
    EQ.0.0 for contact types a 3, a 5, a10, 13, and 15: Default is
           0.4, or 40 percent of the segment thickness
    EQ.0.0 for contact type26: Default is 200.0 times the segment
           thickness
    -----------------------------------------------------------------
    THKOPT:=Thickness option for contact types 3, 5, and 10:
    EQ.0: default is taken from control card, *CONTROL_CONTACT,
    EQ.1: thickness offsets are included,
    EQ.2: thickness offsets are not included (old way).
    -----------------------------------------------------------------
    SHLTHK:=Define if and only if THKOPT above equals 1. Shell
            thickness considered in type surface to surface and node
            to surface type contact options, where options 1 and 2
            below activate the new contact algorithms. The thickness
            offsets are always included in single surface and
            constraint method contact types:
    EQ.0: thickness is not considered,
    EQ.1: thickness is considered but rigid bodies are excluded,
    EQ.2: thickness is considered including rigid bodies.
    -----------------------------------------------------------------
    SNLOG:=Disable shooting node logic in thickness offset contact.
           With the shooting node logic enabled, the first cycle that
           a tracked node penetrates a reference segment, that node
           is moved back to the reference surface without applying
           any contact force.
    EQ.0: logic is enabled (default),
    EQ.1: logic is skipped (sometimes recommended for metalforming
          calculations).
    -----------------------------------------------------------------
    ISYM:=Symmetry plane option:
    EQ.0: off,
    EQ.1: do not include faces with normal boundary constraints
          (e.g., segments of brick elements on a symmetry plane).
    This option is important to retain the correct boundary
    conditions in the model with symmetry. For the _ERODING_ contacts
    this option may also be defined on card 4.
    -----------------------------------------------------------------
    I2D3D:=Segment searching option:
    EQ.0: search 2D elements (shells) before 3D elements (solids,
          thick shells) when locating segments.
    EQ.1: search 3D (solids, thick shells) elements before 2D
          elements (shells) when locating segments.
    -----------------------------------------------------------------
    SLDTHK:=Optional solid element thickness. A nonzero positive
            value will activate the contact thickness offsets in the
            contact algorithms where offsets apply. The contact
            treatment with then be equivalent to the case where null
            shell elements are used to cover the brick elements. The
            contact stiffness parameter below, SLDSTF, may also be
            used to override the default value.
    -----------------------------------------------------------------
    SLDSTF:=Optional solid element stiffness. A nonzero positive
            value overrides the bulk modulus taken from the material
            model referenced by the solid element.

    """
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8])

    PENMAX: Union[int, float] = 0.0
    THKOPT: [0, 1, 2] = 0
    SHLTHK: [0, 1, 2] = 0
    SNLOG: [0, 1] = 0
    ISYM: [0, 1] = 0
    I2D3D: [0, 1] = 0
    SLDTHK: Union[int, float] = 0.0
    SLDSTF: Union[int, float] = 0.0


@dataclass
class ABC(AB):
    """

    IGAP:=For mortar contact IGAP is used to progressively increase
          contact stiffness for large penetrations,, or use a linear
          relationship between penetration and contact pressure; see
          remarks on mortar contact below.
          For other contacts it is a flag to improve implicit
          convergence behavior at the expense of (1) creating some
          sticking if parts attempt to separate and (2) possibly
          underreporting the contact force magnitude in the output
          files rcforc and ncforc. (IMPLICIT ONLY.).
    LT.0: Like IGAP = 1 except the maximum distance between contact
          surfaces at which stickiness is on is sacled by IGAP/10.
    EQ.1: Apply method to improve convergence (DEFAULT)
    EQ.2: Do not apply method
    GT.2: Set IGAP = 1 for first IGAP-2 converged equilibrium states,
    -----------------------------------------------------------------
    IGNORE:=Ignore initial penetrations for the *CONTACT_AUTOMATIC
            options:
    LT.0: Applies only to the Mortar contact.When less than zero, the
          behavior is the same as for | IGNORE| , but contact between
          segments belonging to the same part is ignored.
    The main purpose of this option is to avoid spurious contact
    detections that otherwise could result for complicated geometries
    in a single surface contact, typically, when eliminating initial
    penetrations by interference.See IGNORE = 3 and IGNORE = 4.
    EQ.0: Take the default value from the fourth card of the
          *CONTROL_CONTACT input.
    EQ.1: Allow initial penetrations to exist by tracking the initial
          penetrations.
    EQ.2: Allow initial penetrations to exist by tracking the initial
          penetrations.However, penetration warning messages are
          printed with the original coordinates, and the recommended
          coordinates of each penetrating node are given.For Mortar
          contact, this is the default (see Remark 14 in the General
          Remarks section).
    EQ.3: Applies only to the Mortar contact.With this option initial
          penetrations are eliminated between time zero and the time
          specified by MPAR1.Intended for small initial penetrations.
          See Remark 14 in the General Remarks section.
    EQ.4: Applies only to the Mortar contact.With this option initial
          penetrations are eliminated between time zero and the time
          specified by MPAR1.In addition, a maximum penetration
          distance can be given as MPAR2, intended for large initial
          penetrations.See Remark 14 in the General Remarks section.
    -----------------------------------------------------------------
    DPRFAC:=Applies to the SOFT=2 and Mortar contacts. Depth of
            penetration reduction factor for SOFT=2 contact.
    EQ.0.0:	Initial penetrations are always ignored.
    GT.0.0: Initial penetrations are penalized over time.
    LT.0.0: |DPRFAC| is the load curve ID defining DPRFAC versus time
    For the mortar conatact MPAR1 corresponds to initial contact
    pressure in interfaces with initial penetrations if IGNORE=2,
    for IGNORE=3,4 it corresponds to the time of closure of initial
    penetrations.
    -----------------------------------------------------------------
    DTSTIF:=Applies to the SOFT=1 and SOFT=2 and Mortar contacts.
            Time step used in stiffness calculation for SOFT=1 and
            SOFT=2 contact.
    EQ.0.0:	Use the initial value that is used for time integration.
    GT.0.0: Use the value specified.
    LT.-0.01 and GT.-1.0: use a moving average of the solution time
                          step. (SOFT=2 only).
    LT.-1.0: |DTSTIF| is the load curve ID defining DTSTIF versus
             time.
    For the mortar contact and IGNORE=4, MPAR2 corresponds a
    penetration depth that must be at least the penetration occurring
    in the contact interface.
    -----------------------------------------------------------------
    EDGEK:=Scale factor for penalty stiffness of edge to edge contact
           when SOFT = 2 and DEPTH = 5, 15, 25, or 35:
    EQ.0.0: Use the default penalty stiffness.
    GT.0.0: Scale the stiffness by EDGEK.
    -----------------------------------------------------------------
    UNUSED:=
    -----------------------------------------------------------------
    FLANGL:=Angle tolerance in radians for feature lines option in
            smooth contact.
    EQ.0.0:	No feature line is considered for surface fitting in
            smooth contact.
    GT.0.0:	Any edge with angle between two contact segments bigger
            than this angle will be treated as feature line during
            surface fitting in smooth contact.
    -----------------------------------------------------------------
    CID_RCF:=Coordinate system ID to output RCFORC force resultants
             in a local system.

    """
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8, 8])

    IGAP: int = 1
    IGNORE: int = 0
    DPRFAC: Union[int, float] = 0.0
    DTSTIF: Union[int, float] = 0.0
    EDGEK: Union[int, float] = 0.0
    UNUSED1: str = ""
    FLANGL: Union[int, float] = 0.0
    CID_RCF: int = ""


@dataclass
class ABCD(ABC):
    """

    Q2TRI:=Option to split quadrilateral contact segments into two
           triangles (only available when SOFT=2).
    EQ.0: Off (default).
    EQ.1: On for all SURFA shell segments.
    EQ.2: On for all SURFB shell segments.
    EQ.3: On for all shell segments.
    EQ.4: On for all shell segments of material type 34.
    -----------------------------------------------------------------
    DTPCHK:=Time interval between shell penetration reports (only
            available for segment based contact)
    EQ.0.0:	Off (default).
    GT.0.0: Check and report segment penetrations at time intervals
            equal to DTPCHK.
    LT.0.0:	Check and report segment penetrations at time intervals
            equal to |DTPCHK|. In addition, calculation stops with an
            error at t=0 if any intersections are initially present
    -----------------------------------------------------------------
    SFNBR:=Scale factor for neighbor segment contact (only available
           for segment based contact)
    EQ.0.0:	Off (default).
    GT.0.0: Check neighbor segments for contact
    -----------------------------------------------------------------
    FNLSCL:=Scale factor for nonlinear force scaling
    -----------------------------------------------------------------
    DNLSCL:=Distance for nonlinear force scaling
    -----------------------------------------------------------------
    TCSO:=Option to consider only contact segments (not all attached
          elements) when computing the contact thickness for a node
          or segment (for SURFACE_TO_SURFACE contact and shell
          elements only)
    EQ.0: Off (default).
    EQ.1: Only consider segments in the contact definition
    -----------------------------------------------------------------
    TIEDID:=Incremental displacement update for tied contacts.
    EQ.0:  Off (default).
    EQ.1:  On.
    -----------------------------------------------------------------
    SHLEDG:=Flag for assuming edge shape for shells when measuring
            penetration.This is available for segment - based
            contact(SOFT = 2).
    EQ.0: Default to SHELDG on * CONTROL_CONTACT
    EQ.1: Shell edges are assumed to be square and are flush with the
          nodes.
    EQ.2: Shell edges are assumed to be round with a radius equal to
          half the shell thickness.The edge centers lie on the lines
          between the segment nodes and extend outward by the radius.
          This option is not available for DEPTH values of 23, 33,
          or 35.

    """
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8, 8, 8])

    Q2TRI: [0, 1, 2, 3, 4] = 0
    DTPCHK: Union[int, float] = 0.0
    SFNBR: Union[int, float] = 0.0
    FNLSCL: Union[int, float] = 0.0
    DNLSCL: Union[int, float] = 0.0
    TCSO: [0, 1] = 0
    TIEDID: [0, 1] = 0
    SHLEDG: [0, 1] = 0


@dataclass
class ABCDE(ABCD):
    """

    SHAREC:=Shared constraint flag (only available for segment
            based contact)
    EQ.0: Segments that share constraints not checked for contact.
    EQ.1: Segments that share constraints are checked for contact.
    -----------------------------------------------------------------
    CPARM8:=This variable is similar to CPARM8 in *CONTACT_вЂЊвЂ¦_MPP
            but applies to SMP and not to MPP.  CPARM8 for SMP only
            controls treatment of spot weld beams in
            *CONTACT_AUTOMATIC_GENERAL.
    EQ.0: Spot weld(type 9) beams are not considered in the contact
          even if included in SURFA
    EQ.2: Spot weld(type 9) beams are considered in the contact if
          included in SURFA
    -----------------------------------------------------------------
    IPBACK:=If set to a nonzero value, creates a  backup  penalty
            tied contact for this interface. This option applies to
            constrained tied contacts only. See	Remark 2.
    -----------------------------------------------------------------
    SRNDE:=Segment Rounded Edges:
    EQ.0: free edges have their usual treatement
    EQ.1: free edges are rounded, but without extending them.
    -----------------------------------------------------------------
    FRICSF:=Scale factor for frictional stiffness (available for SOFT
            = 2 only).
    -----------------------------------------------------------------
    ICOR:=If set to a nonzero value, VDC is the coefficient of
          restitution expressed as a percentage. When SOFT = 0 or 1,
          this option applies to AUTOMATIC_NODES_TO_SURFACE,
          AUTOMATIC_SURFACE_TO_SURFACE and AUTOMATIC_SINGLE_SURFACE.
          When SOFT = 2, it applies to all available keywords.
    -----------------------------------------------------------------
    FTORQ:=If set to 1, a torsional force is computed in the beam to
           beam portion of contact type AUTOMATIC_GENERAL, which
           balances the torque produced due to friction. This is
           currently only available in the MPP version.
    -----------------------------------------------------------------
    REGION:=The ID of a *DEFINE_REGION which will delimit the volume
            of space where this contact is active. See Remark 4 below

    """
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8, 8, 8, 8])

    SHAREC: [0, 1] = 0
    CPARM8: [0, 2] = 0
    IPBACK: int = 0
    SRNDE: int = 0
    FRICSF: Union[int, float] = 1
    ICOR: int = 0
    FTORQ: int = 0
    REGION: int = 0


@dataclass
class ABCDEF(ABCDE):
    """

    PSTIFF:=Flag to choose the method for calculating the penalty
            stiffness. This	is available for segment based contact
            (see SOFT on optional card A)
    EQ.0: Use the default as defined by PSTIFF on *CONTROL_CONTACT.
    EQ.1: Based on nodal masses
    EQ.2: Based on material density and segment dimensions.
    -----------------------------------------------------------------
    IGNROFF:=Flag to ignore the thickness offset for shells in the
             calculation of the shell contact penetration depth. This
             allows shells to be used for meshing rigid body dies
             without modifying the positions of the nodes to
             compensate for the shell thickness.
    EQ.0: Default
    EQ.1: Ignore the SURFB side thickness.
    EQ.2: Ignore the SURFA side thickness.
    EQ.3: Ignore the thickness of both sides..
    -----------------------------------------------------------------
    unused:=
    -----------------------------------------------------------------
    FSTOL:=Tolerance used with the SMOOTH option for determining
           which segments are considered flat.  The value is in
           degrees and approximately represents half the angle
           between adjacent segments
    -----------------------------------------------------------------
    2DBINR:=Flag to indicate that 2D belts initially inside
            retractors are involved in the contact.  This is only
            available for SURFACE_TO_SURFACE contact of segment-based
            contact (SOFT = 2).
    EQ.0: No 2D belt initially inside a retractor is involved.
    EQ.1: 2D belts initially inside retractors are involved
    -----------------------------------------------------------------
    SSFTYP:=Flag to determine how the SSF option on *PART_вЂЊCONTACT
            behaves when SOFT = 2 on optional card A:
    EQ.0: Use SSF from the tracked segment as determined by the
          SOFT = 2 algorithm (see Remark 2)
    EQ.1: Use the larger of the SSF values.
    -----------------------------------------------------------------
    SWTPR:=Flag to use tapered shell contact segments adjacent to
           segments that are thinned by the SPOTHIN option on
           *CONTROL_CONTACT. This option is only available when
           SOFT=2 on optional card A.
    EQ.0: Use full thickness constant segments.
    EQ.1: Use tapered segments.
    -----------------------------------------------------------------
    TETFAC:=Scale factor for the computed volume of tetrahedral solid
            elements for the mass calculation in SOFT=2 contact. By
            default, half the mass of a solid element is considered
            for the contact segment, which is reasonable for
            hexahedrons. In contrast, for tetrahedrons, a larger
            value than 0.5 would be preferrable, because several tets
            fit into one hex. Therefore, a TETFAC value around 3.0 to
            5.0 should make the contact stiffness more comparable
            with hex meshes.

    """
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8, 8, 8, 8, 8])

    PSTIFF: [0, 1, 2] = 0
    IGNROFF: [0, 1, 2, 3] = 0
    UNUSED2: str = ""
    FSTOL: Union[int, float] = 2.0
    TWODBINR: [0, 1] = 0
    SSFTYP: [0, 1] = 0
    SWTPR: [0, 1] = 0
    TETFAC: int = 0


@dataclass
class AUTOMATIC_SURFACE_TO_SURFACE(ICard):
    """

    SURFA:=Segment set ID, node set ID, part set ID, part ID, or
           shell element set ID for specifying the SURFA side of the
           contact interface (see Setting the Contact Interface). See
           *SET_SEGMENT, *SET_NODE_OPTION, *PART, *SET_PART or
           *SET_SHELL_OPTION. For ERODING_SINGLE_SURFACE and
           ERODING_SURFACE_TO_SURFACE contact types, use either a
           part ID or a part set ID. For ERODING_NODES_TO_SURFACE
           contact, use a node set which includes all nodes that may
           be exposed to contact as element erosion occurs.
    EQ.0: Includes all parts in the case of single surface contact
          types
    -----------------------------------------------------------------
    SURFB:=Segment set ID, node set ID, part set ID, part ID, or
           shell element set ID for the SURFB side of the contact
           (see Setting the Contact Interface).
    EQ.0: SURFB side is not applicable for single surface contact types.
    -----------------------------------------------------------------
    SURFATYP:=The ID type of SURFA:
    EQ.0: segment set ID for surface to surface contact,
    EQ.1: shell element set ID for surface to surface contact,
    EQ.2: part set ID,
    EQ.3: part ID,
    EQ.4: node set ID for node to surface contact,
    EQ.5: include all (SURFA field) is ignored,
    EQ.6: part set ID for exempted parts. All non-exempted parts are
          included in the contact.
    EQ.7: Branch ID; see *SET_PART_TREE
    -----------------------------------------------------------------
    SURFBTYP:=ID type of SURFB:
    EQ.0: segment set ID,
    EQ.1: shell element set ID,
    EQ.2: part set ID,
    EQ.3: part ID,
    EQ.5: Include all ( SURFB Field is ignored).
    EQ.6: Part set ID for exempted parts.  All non-exempted parts are
          included in the contact.
    EQ.7: Branch ID; see *SET_PART_TREE
    -----------------------------------------------------------------
    SABOXID:=Include in contact definition only those SURFA
             nodes/segments within box SABOXID (corresponding to
             BOXID in *DEFINE_BOX), or if SABOXID is negative, only
             those SURFA nodes/segments within contact volume
             |SABOXID| (corresponding to CVID in
             *DEFINE_CONTACT_VOLUME). SABOXID can be used only if
             SURFATYP is set to 2, 3, or 6, that is, SURFA is a part
             ID or part set ID. SABOXID is not available for ERODING
             contact types
    -----------------------------------------------------------------
    SBBOXID:=Include in contact definition only those SURFB segments
             within box SBBOXID (corresponding to BOXID in
             *DEFINE_BOX), or if SBBOXID is negative, only those
             SURFB segments within contact volume |SBBOXID |
             (corresponding to CVID in *DEFINE_CONTACT_VOLUME).
             SBBOXID can be used only if SURFBTYP is set to 2, 3, or
             6, that is, SURFB is a part ID or part set ID.  SBBOXID
             is not available for ERODING contact types.
    -----------------------------------------------------------------
    SAPR:=Include the SURFA side in the *DATABASE_NCFORC and the
          *DATABASE_BINARY_INTFOR interface force files, and
          optionally in the dynain file for wear:
    EQ.0: Do not include.
    EQ.1: SURFA side forces included.
    EQ.2: Same as 1 but also allows for SURFA nodes to be written as*
          INITIAL_CONTACT_WEAR to dynain; see NCYC on
          *INTERFACE_SPRINGBACK_LSDYNA.
    -----------------------------------------------------------------
    SBPR:=Include the SURFB side in the *DATABASE_NCFORC and the
          *DATABASE_BINARY_INTFOR interface force files, and
          optionally in the dynain file for wear:
    EQ.0: Do not include.
    EQ.1: SURFB side forces included.
    EQ.2: Same as 1, but also allows for SURFB nodes to be written as
          *INITIAL_CONTACT_WEAR to dynain; see NCYC on
          *INTERFACE_SPRINGBACK_LSDYNA.

    #################################################################

    FS:=Static coefficient of friction if FS > 0 and not equal to 2.
    EQ.-1.0: If the frictional coefficients defined in the *PART
             section are to be used, set FS to a negative number.
    EQ. 2: For contact types SURFACE_TO_SURFACE and
           ONE_WAY_SURFACE_TO_SURFACE, the dynamic coefficient of
           friction points to the table, see DEFINE_TABLE (The table
           ID is give by FD below.), giving the coefficient of
           friction as a function of the relative velocity and
           pressure. This option must be used in combination with the
           thickness offset option. See Figure 6.1.
    Note: For the special contact option
          TIED_SURFACE_TO_SURFACE_FAILURE only, the variables FS is
          the Normal tensile stress at failure.,
    -----------------------------------------------------------------
    FD:=Dynamic coefficient of friction. The frictional coefficient
        is assumed to be dependent on the relative velocity v-rel of
        the surfaces in contact. Give table ID if FS=2 (default=0.0).
    Note: For the special contact option
          TIED_SURFACE_TO_SURFACE_FAILURE only, the variables FD is
          Shear stress at failure
    -----------------------------------------------------------------
    DC:=Exponential decay coefficient. The frictional coefficient is
        assumed to be dependent on the relative velocity v-rel of the
        surfaces in contact. (default=0.0).
    -----------------------------------------------------------------
    VC:=Coefficient for viscous friction. This is necessary to limit
        the friction force to a maximum.
    -----------------------------------------------------------------
    VDC:=Viscous damping coefficient in percent of critical. In order
        to avoid undesirable oscillation in contact, e.g., for sheet
        forming simulation, a contact damping perpendicular to the
        contacting surfaces is applied.
    -----------------------------------------------------------------
    PENCHK:=Small penetration in contact search option.  If the
            tracked node penetrates more than the segment thickness
            times the factor XPENE (see *CONTROL_CONTACT), the
            penetration is ignored, and the tracked node is set free.
            The thickness is taken as the shell thickness if the
            segment belongs to a shell element or it is taken as 1/20
            of its shortest diagonal if the segment belongs to a
            solid element.  This option applies to the
            surface-to-surface contact algorithms.  See Table 0-17
            for contact types and more details.
    -----------------------------------------------------------------
    BT:=Birth time (contact surface becomes active at this time):
    LT.0: Birth time is set to | "BT" | .When negative, birth time is
          followed during the dynamic relaxation phase of the
          calculation. After dynamic relaxation has completed,
          contact is activated regardless of the value of BT.
    EQ.0: Birth time is inactive, meaning contact is always active
    GT.0: If DT = -9999, BT is interpreted as the curve or table ID
          defining multiple pairs of birth - time / death - time;
          see Remark 2 below.Otherwise, if "DT" > 0, birth time
          applies both duringand after dynamic relaxation.
    -----------------------------------------------------------------
    DT:=Death time (contact surface is deactivated at this time):
    LT.0: If DT = -9999, BT is interpreted as the curve or table ID
          defining multiple pairs of birth - time / death - time.
          Otherwise, negative DT indicates that contact is inactive
          during dynamic relaxation.After dynamic relaxation the
          birth and death times are followed and set to | "BT" | and
          | "DT" | , respectively.EQ.0 : DT defaults to 10e20.
    GT.0: DT sets the time at which the contact is deactivated.

    #################################################################

    SFSA:=Scale factor on default SURFA penalty stiffness when
          SOFT = 0 or SOFT = 2; see also *CONTROL_CONTACT.For MORTAR
          frictional contact this is the stiffness scale factor for
          the entire contact, and SFSB does not apply.
    -----------------------------------------------------------------
    SFSB:=Scale factor on default SURFA penalty stiffness when
          SOFT = 0 or SOFT = 2; see also *CONTROL_CONTACT.For MORTAR
          tied contact, this is an additional stiffness scale factor,
          resulting in a total stiffness scale of SFSA*SFSB.
    -----------------------------------------------------------------
    SAST:=Optional thickness for SURFA surface (overrides true
          thickness). This option applies only to contact with shell
          elements. SAST has no bearing on the actual thickness of
          the elements; it only affects the location of the contact
          surface. For the *CONTACT_TIED_.. options, SAST and SBST
          below can be defined as negative values, which will cause
          the determination of whether or not a node is tied to
          depend only on the separation distance relative to the
          absolute value of these thicknesses. More information is
          given under General Remarks on *CONTACT following Optional
          Card C.
    -----------------------------------------------------------------
    SBST:=Optional thickness for SURFA surface (overrides true
          thickness). This option applies only to contact with shell
          elements. True thickness is the element thickness of the
          shell elements. For the TIED options see SAST above.
    -----------------------------------------------------------------
    SFSAT:=Scale factor applied to contact thickness of SURFA surface
           This option applies to contact with shell and beam
           elements
    SFSAT has no bearing on the actual thickness of the elements; it
    only affects the location of the contact surface.
    SFSAT is ignored if SAST is nonzero except in the case of MORTAR
    contact (see Remark 9 in the General Remarks: *Contact section).
    -----------------------------------------------------------------
    SFSBT:=Scale factor applied to contact thickness of SURFA surface
           This option applies only to contact with shell elements.
    SFSAT has no bearing on the actual thickness of the elements; it
    only affects the location of the contact surface.
    SFSAT is ignored if SBST is nonzero except in the case of MORTAR
    contact (see Remark 9 in the General Remarks: *Contact section).
    -----------------------------------------------------------------
    FSF:=Coulomb friction scale factor (default=1.0).The Coulomb
         friction value is scaled as Ој_sc=FSFГ—Ој_c; see Mandatory
         Card 2.
    -----------------------------------------------------------------
    VSF:=Viscous friction scale factor (default=1.0).If this factor
         is defined, then the limiting force becomes:
         F_lim =VSFГ—VCГ—A_cont ; see Mandatory Card 2.

    """
    name: str = "CONTACT_AUTOMATIC_SURFACE_TO_SURFACE"
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8, 8])

    mpp: List[dict] = field(default_factory=lambda: [])

    SURFA: int = ""
    SURFB: int = ""
    SURFATYP: [0, 1, 2, 3, 4, 5, 6, 7] = 0
    SURFBTYP: [0, 1, 2, 3, 4, 5, 6, 7] = 0
    SABOXID: int = ""
    SBBOXID: int = ""
    SAPR: [0, 1, 2] = 0
    SBPR: [0, 1, 2] = 0

    FS: Union[int, float] = 0.0
    FD: Union[int, float] = 0.0
    DC: Union[int, float] = 0.0
    VC: Union[int, float] = 0.0
    VDC: Union[int, float] = 0.0
    PENCHK: int = ""
    BT: Union[int, float] = 0.0
    DT: Union[int, float] = 1.0e20

    SFSA: Union[int, float] = 1.0
    SFSB: Union[int, float] = 1.0
    SAST:  Union[int, float] = ""
    SBST:  Union[int, float] = ""
    SFSAT: Union[int, float] = 1.0
    SFSBT: Union[int, float] = 1.0
    FSF: Union[int, float] = 1.0
    VSF: Union[int, float] = 1.0

    thermal: List[dict] = field(default_factory=lambda: [])
    abcdef: List[dict] = field(default_factory=lambda: [])

    def asdict(self):  # this is strange, but apparently it works when instead __dict__ call class.__dict__
        return {key: value for key, value in self.__dict__.items() if value is not []}

    def __post_init__(self):
        if not self.mpp == []:
            mpp_name = self.mpp[0].pop("name")
            mpp_rows_lengths = self.mpp[0].pop("rows_lengths")
            self.name += mpp_name
            self.rows_lengths = mpp_rows_lengths + self.rows_lengths
        if not self.thermal == []:
            thermal_name = self.thermal[0].pop("name")
            thermal_rows_lengths = self.thermal[0].pop("rows_lengths")
            self.name += thermal_name
            self.rows_lengths += thermal_rows_lengths
        if not self.abcdef == []:
            abcdef_name = self.abcdef[0].pop("name")
            abcdef_rows_length = self.abcdef[0].pop("rows_lengths")
            self.name += abcdef_name
            self.rows_lengths += abcdef_rows_length
