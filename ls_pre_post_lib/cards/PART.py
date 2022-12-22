from dataclasses import dataclass, field
from typing import Union, List
from .card import ICard


@dataclass
class Layer:
    """

    MID:=Material ID of integration point i, see *MAT_? Section
    -----------------------------------------------------------------
    THICK:=Thickness of integration point .
    -----------------------------------------------------------------
    B:=Material angle of integration point i.
    -----------------------------------------------------------------
    TMID:=Thermal ID

    """
    MID1: int = ""
    THICK1: Union[int, float] = ""
    B1: Union[int, float] = ""
    TMID1: Union[int, float] = ""
    MID2: int = ""
    THICK2: Union[int, float] = ""
    B2: Union[int, float] = ""
    TMID2: Union[int, float] = ""


@dataclass
class COMPOSITE(ICard):
    """

    PID:=Part ID.
    -----------------------------------------------------------------
    ELFORM:=Element formulation options, see Remarks 1 and 2 below:
    EQ.1:  Hughes-Liu,
    EQ.2: Belytschko-Tsay,
    EQ.3: BCIZ triangular shell,
    EQ.4: C0 triangular shell,
    EQ.6: S/R Hughes-Liu,
    EQ.7: S/R co-rotational Hughes-Liu,
    EQ.8: Belytschko-Leviathan shell,
    EQ.9: Fully integrated Belytschko-Tsay membrane,
    EQ.10: Belytschko-Wong-Chiang,
    EQ.11: Fast (co-rotational) Hughes-Liu,
    EQ.16: Fully integrated shell element (very fast)
    EQ.-16: Fully integrated shell element modified for higher
            accuracy
    -----------------------------------------------------------------
    SHRF:=Shear correction factor which scales the transverse shear
          stress.  The shell formulations in LS-DYNA, with the
          exception of the BCIZ and DK elements, are based on a first
          order shear deformation theory that yields constant
          transverse shear strains which violates the condition of
          zero traction on the top and bottom surfaces of the shell.
          The shear correction factor is attempt to compensate for
          this error.
    -----------------------------------------------------------------
    NLOC:=Location of reference surface for three dimensional shell
          elements.  If nonzero, the mid-surface of the shell is
          offset by a value equal to  .  Alternatively, the offset
          can be specified by using the OFFSET option in the
          *ELEMENT_SHELL input section.
    EQ. 1.0: top surface,
    EQ. 0.0: mid-surface (default)
    EQ.-1.0: bottom surface..
    -----------------------------------------------------------------
    MAREA:=Non-structural mass per unit area.  This is additional
           mass which comes from materials such as carpeting. This
           mass is not directly included in the time step calculation
    -----------------------------------------------------------------
    HGID:=Hourglass/bulk viscosity identification defined in the
          *HOURGLASS Section:
    EQ.0: default values are used..
    -----------------------------------------------------------------
    ADPOPT:=Indicate if this part is adapted or not. See also
            *CONTROL_ADAPTIVITY.
    EQ.0: no adaptivity (default),
    EQ.1: H-adaptive for 3D shells,
    EQ.2: R-adaptive remeshing for 2D shells.
    -----------------------------------------------------------------
    THSHEL:=Thermal shell formulation:
    EQ.0 Default\nEQ.1 Thick thermal shell
    EQ. 2 Thin thermal shell

    """
    name: str = "PART_COMPOSITE"
    rows_lengths: List[int] = field(default_factory=lambda: [8])  # variable quantity due to Layers ([8] each)

    TITLE: str = ""

    PID: int = 0
    ELFORM: [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 16, -16] = 2
    SHRF: Union[int, float] = ""
    NLOC: [1.0, 0.0, -1.0] = 0.0
    MAREA: Union[int, float] = 0
    HGID: int = 0
    ADPORT: [0, 1, 2] = 0
    THSHEL: [0, 1, 2] = 0

    Layers: List[dict] = field(default_factory=list)
