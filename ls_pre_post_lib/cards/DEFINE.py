from dataclasses import dataclass, field
from typing import Union, List
from .card import ICard


@dataclass
class Curve_point:
    """

    A1:=Abscissa values. Only pairs have to be defined.
    -----------------------------------------------------------------
    O1:=Ordinate (function) values. Only pairs have to be defined.

    """
    A1: Union[int, float] = ""
    empty_cell: str = ""  # to make distance between a1 and o1 = 20 whitespaces
    O1: Union[int, float] = ""


@dataclass
class COORDINATE_SYSTEM(ICard):
    """

    CID:=Coordinate system ID. A unique number has to be defined.
    -----------------------------------------------------------------
    XO:=x-coordinate of origin.
    -----------------------------------------------------------------
    YO:=y-coordinate of origin.
    -----------------------------------------------------------------
    ZO:=z-coordinate of origin.
    -----------------------------------------------------------------
    XL:=x-coordinate of point on local x-axis.
    -----------------------------------------------------------------
    YL:=y-coordinate of point on local x-axis.
    -----------------------------------------------------------------
    ZL:=z-coordinate of point on local x-axis.
    -----------------------------------------------------------------
    CIDL:=Coordinate system ID applied to the coordinates used to
          define the current system. The coordinates X0, Y0, Z0, XL,
          YL, ZL, XP, YP, and ZP are defined with respect to the
          coordinate system CIDL.

    #################################################################

    XP:=x-coordinate of point in local x-y plane.
    -----------------------------------------------------------------
    YP:=y-coordinate of point in local x-y plane.
    -----------------------------------------------------------------
    ZP:=z-coordinate of point in local x-y plane.

    """
    name: str = "DEFINE_COORDINATE_SYSTEM"
    rows_lengths: List[int] = field(default_factory=lambda: [8, 3])

    CID: int = 0
    XO: Union[int, float] = 0.0
    YO: Union[int, float] = 0.0
    ZO: Union[int, float] = 0.0
    XL: Union[int, float] = 0.0
    YL: Union[int, float] = 0.0
    ZL: Union[int, float] = 0.0
    CIDL: int = 0

    XP: Union[int, float] = 0.0
    YP: Union[int, float] = 0.0
    ZP: Union[int, float] = 0.0


@dataclass
class CURVE(ICard):
    """

    LCID:=Load curve ID. Tables (see *DEFINE_TABLE) and load curves
          may not share common ID's. LS-DYNA3D allows load curve ID's
          and table ID's to be used interchangeably. A unique number
          has to be defined. Note: The magnitude of LCID is
          restricted to 5 significant digits. This limitation will be
          removed in a future release of LS-DYNA3D.
    -----------------------------------------------------------------
    SIDR:=Stress initialization by dynamic relaxation:
    EQ.0: load curve used in transient analysis only or for other
          applications,
    EQ.1: load curve used in stress initialization but not transient
          analysis,
    EQ.2: load curve applies to both initialization and transient
          analysis.
    -----------------------------------------------------------------
    SFA:=Scale factor for abcissa value. This is useful for simple
         modifications.
    EQ.0.0: default set to 1.0.
    -----------------------------------------------------------------
    SFO:=Scale factor for ordinate value (function). This is useful
         for simple modifications.
    EQ.0.0: default set to 1.0.
    -----------------------------------------------------------------
    OFFA:=Offset for abcissa values.
    -----------------------------------------------------------------
    OFFO:=Offset for ordinate values (function).
    -----------------------------------------------------------------
    DATTYP:=Data type.This affects how offsets are applied.
    EQ.-2: for fabric stress vs. strain curves(*MAT_FABRIC) as
           described below.Thickness flag for norminal stress
           calculation.
    EQ.0: general case for time dependent curves,force versus
          displacement curves and stress strain curves.
    EQ.1: for general (x,y) data curves whose abscissa values do not
          increase monotonically.
    EQ.6: for general (r,s) data(coordinates in a 2D parametric space)
          whose values do not increase momotonically. Use for
          definition of trimming polygons for trimmed
          NURBS(*ELEMENT_SHELL_NURBS_PATCH,NL.GT.0).
    EQ.-100: for defining the proxy, О±, from experiments for the
             chemical shrinkage coefficient as a function of
             temperature (see *MAT_ADD_CHEM_SHRINKAGE for details)
    -----------------------------------------------------------------
    LCINT:=The number of discretization intervals to use for this
           curve. If 0 is input, the value of LCINT from
           *CONTROL_SOLUTION will be used.

    """
    name: str = "DEFINE_CURVE"
    rows_lengths: List[int] = field(default_factory=lambda: [8])  # variable quantity due to Curve_points ([2] each)

    LCID: int = 1
    SIDR: [0, 1, 2] = 0
    SFA: Union[int, float] = 1.0
    SFO: Union[int, float] = 1.0
    OFFA: Union[int, float] = 0.0
    OFFO: Union[int, float] = 0.0
    DATTYP: [0, 1, -2, 6, -100] = 0
    LCINT: int = 0

    Curve_points: List[dict] = field(default_factory=list)
