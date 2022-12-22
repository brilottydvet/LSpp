from dataclasses import dataclass, field
from typing import Union, List
from .card import ICard


@dataclass
class ACCURACY(ICard):
    """

    OSU:=Global flag for 2nd order objective stress update:
    EQ.0: Off (default)
    EQ.1: On
    -----------------------------------------------------------------
    INN:=Invariant node numbering for shell and solid elements:
    EQ.1: Off (default for explicit)
    EQ.2: On for shell and thick shell elements(default for implicit)
    EQ.3: On for solid elements
    EQ.4: On for shell, thick shell and solid elements
    EQ.-2:On for shell elements except triangular shells
    EQ.-4:On for both shell and solid elements except triangular
          shells
    -----------------------------------------------------------------
    PIDOSU:=Part set ID for objective stress updates. If this part
            set ID is given only those part IDs listed will use the
            objective stress update; therefore, OSU is ignored.
    -----------------------------------------------------------------
    IACC:=Implicit accuracy flag, turns on some specific accuracy
          considerations in implicit analysis at an extra CPU cost.
    EQ.0: Off (default)
    EQ.1: On
    EQ.2: On (partially also for explicit, for compatibility when
          switching between implicit and explicit)
    -----------------------------------------------------------------
    EXACC:=Explicit accuracy parameter:
    EQ.0.0:	Off(default)
    GT.0.0: On(see Remark 5)

    """
    name: str = "CONTROL_ACCURACY"
    rows_lengths: List[int] = field(default_factory=lambda: [5])

    OSU: [0, 1] = 0
    INN: [1, 2, 3, 4, -2, -4] = 1
    PIDOSU: int = 0
    IACC: [0, 1, 2] = 0
    EXACC: Union[int, float] = 0.0


@dataclass
class ENERGY(ICard):
    """

    HGEN:=Hourglass energy calculation option.
    EQ.1: hourglass energy is not computed (default),
    EQ.2: hourglass energy is computed and included in the energy
          balance.
    -----------------------------------------------------------------
    RWEN:=Stonewall energy dissipation option:
    EQ.1: energy dissipation is not computed,
    EQ.2: energy dissipation is computed and included in the energy
          balance (default).
    -----------------------------------------------------------------
    SLNTEN:=Sliding interface energy dissipation option:
    EQ.1: energy dissipation is not computed,
    EQ.2: energy dissipation is computed and included in the energy
          balance.
    -----------------------------------------------------------------
    RYLEN:=Rayleigh energy dissipation option (damping energy
           dissipation):
    EQ.1: energy dissipation is not computed (default),
    EQ.2: energy dissipation is computed and included in the energy
          balance.
    -----------------------------------------------------------------
    IRGEN:=Initial reference geometry energy option (included in
           internal energy, resulting from
           *INITIAL_FOAM_REFERENCE_GEOMETRY):
    EQ.1: initial reference geometry energy is not computed,
    EQ.2: initial reference geometry energy is computed and included
          in the energy balance as part of the internal energy
          (default).
    -----------------------------------------------------------------
    MATEN:=Detailed material energies option. For a choice of
           material models (currently supported are 3, 4, 15, 19, 24,
           63,81, 82, 98, 104, 105, 106, 107, 123, 124, 188, 224,
           225, 240, and 251 for shell and solid elements), internal
           energy is additionally split into elastic, plastic and
           damage portions:
    EQ.1: detailed material energies are not computed(default).
    EQ.2: detailed material energies are computed and reported as
          mat_energy_elastic, mat_energy_plastic,and mat_energy_
          damage in ASCII file glstatand matsum
    -----------------------------------------------------------------
    DRLEN:=Drilling energy calculation option, for implicit and with
           use of DRCPSID/DRCPRM on *CONTROL_SHELL:
    EQ.1: Drilling energy is not computed(default).
    EQ.2: Drilling energy is computed and included in the energy
          balance.The drilling energies are reported in the ASCII
          file glstat, see* DATABASE_OPTION.
    -----------------------------------------------------------------
    DISEN:=Dissipation energy calculation option, for implicit:
    EQ.1: Dissipated energy is not computed(default).
    EQ.2: Dissipated kinetic and internal energy is computed and
          included in the energy balance.The dissipation energies are
          reported in the ASCII file glstat, see* DATABASE_OPTION.

    """
    name: str = "CONTROL_ENERGY"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    HGEN: [1, 2] = 1
    RWEN: [1, 2] = 2
    SLNTEN: [1, 2] = 1
    RYLEN: [1, 2] = 1
    IRGEN: [1, 2] = 2
    MATEN: [1, 2] = 1
    DRLEN: [1, 2] = 1
    DISEN: [1, 2] = 1

@dataclass
class IMPLICIT_AUTO(ICard):
    """

    IAUTO:=Automatic time step control flag
    EQ.0: constant time step size
    EQ.1: automatically adjust time step size
    EQ.2: automatically adjust time step size and synchronize with
           thermal mechanical time step.
    EQ.3: same as 1, but accounting for mid step residual values with
           respect to parameters on card 2 and according to the
           Remark for IAUTO.
    LT.0: Curve ID = (-IAUTO) gives time step size as a function of
          time. If specified, DTMIN and DTMAX will still be applied
    -----------------------------------------------------------------
    ITEOPT:=Optimum equilibrium iteration count per time step
    -----------------------------------------------------------------
    ITEWIN:=Allowable iteration window. If iteration count is within
            ITEWIN iterations of ITEOPT, step size will not be
            adjusted.
    -----------------------------------------------------------------
    DTMIN:=Minimum allowable time step size.  Simulation stops with
           error termination if time step falls below DTMIN.
    LT.0: enable automatic key point generation.Minimum allowable
          time step is |DTMIN|.
    -----------------------------------------------------------------
    DTMAX:=Maximum allowable time step size (default = DT*10).
    -----------------------------------------------------------------
    DTEXP:=Time interval to run in explicit mode before returning to
           implicit mode. Applies only when automatic
           implicit-explicit switching is active (IMFLAG= 4 or 5 on
           *CONTROL_IMPLICIT_GENERAL). Also, see KCYCLE.
    EQ.0: defaults to the current implicit time step size.
    LT.0: curve ID = (-DTEXP) gives the time interval as a function
          of time.
    -----------------------------------------------------------------
    KFAIL:=Number of failed attempts to converge implicitly for the
           current time step before automatically switching to
           explicit time integration. Applies only when automatic
           implicit-explicit switching is active. The default is one
           attempt. If IAUTO = 0, any input value is reset to unity
    -----------------------------------------------------------------
    KCYCLE:=Number of explicit cycles to run in explicit mode before
            returning to the implicit mode. The actual time interval
            that is used will be the maximum between DTEXP and
            KCYCLE*(latest estimate of the explicit time step size).

    """
    name: str = "CONTROL_IMPLICIT_AUTO"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    IAUTO: int = 0
    ITEOPT: int = 11
    ITEWIN: int = 5
    DTMIN: Union[int, float] = ""
    DTMAX: Union[int, float] = ""
    DTEXP: Union[int, float] = ""
    KFAIL: int = 1
    KCYCLE: int = ""


@dataclass
class IMPLICIT_GENERAL(ICard):
    """

    IMFLAG:=Implicit/Explicit switching flag
    EQ.0: explicit analysis (default)
    EQ.1: implicit analysis
    EQ.2: explicit followed by one implicit step (springback
          analysis)
    EQ.4: implicit with automatic implicit-explicit switching
    EQ.5: implicit with automatic switching and mandatory implicit
          finish
    EQ.6: explicit with intermittent eigenvalue extraction
    EQ.-n: curve ID=n gives IMFLAG as a function of time.
    -----------------------------------------------------------------
    DT0:=Initial time step size for implicit analysis.  See Remarks 2
         and 5.
    LT.0: eliminate negative principal stresses in geometric(initial
          stress) stiffness.Initial time step is |DT0|.
    -----------------------------------------------------------------
    IMFORM:=Element formulation switching flag
    EQ.1: switch to fully integrated formulation for implicit
          springback
    EQ.2: retain original element formulation (default).
    -----------------------------------------------------------------
    NSBS:=Number of steps in nonlinear springback (default = 1).
    -----------------------------------------------------------------
    IGS:=Geometric (initial stress) stiffness flag
    EQ.2: ignore(default)
    EQ.1: include
    LT.0: include on part set |IGS|.
    -----------------------------------------------------------------
    CNSTN:=Indicator for consistent tangent stiffness:
    EQ.0: do not use (default)
    EQ.1: use.
    -----------------------------------------------------------------
    FORM:=Element formulation when using IMFORM flag.
    EQ.0: type 16
    EQ.1: type 6.
    -----------------------------------------------------------------
    ZERO_V:=Zero out the velocity before switching from explicit to
            implicit.
    EQ.0: The velocities are not zeroed out.
    EQ.1: The velocities are set to zero.

    """
    name: str = "CONTROL_IMPLICIT_GENERAL"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    IMFLAG: int = 0
    DTO: Union[int, float] = ""
    IMFORM: [1, 2] = 2
    NSBS: int = 1
    IGS: [2, 1, 0] = 2
    CNSTN: [0, 1] = 0
    FORM: [0, 1] = 0
    ZERO_V: [0, 1] = 0


@dataclass
class IMPLICIT_SOLUTION(ICard):
    """

    NSOLVR:=Solution method for implicit analysis:
    EQ.-1: Multistep linear,
    EQ.1: Linear,
    EQ.6: Nonlinear with BFGS updates + arclength,
    EQ.7: Nonlinear with Broyden updates + arclength,
    EQ.8: Nonlinear with DFP updates + arclength,
    -----------------------------------------------------------------
    ILIMIT:=Iteration limit between automatic stiffness reformations.
            Default is set to ILIMIT = 11.
    -----------------------------------------------------------------
    MAXREF:=Stiffness reformation limit per time step.
    LT.0: If  matrix reformations occur, convergence for that time
          step is forced; see Remark 4.
    -----------------------------------------------------------------
    DCTOL:=Displacement relative convergence tolerance (see Remark 5)
    LT.0: -DCTOL references a curve that defines tolerance as a
          function of time.
    -----------------------------------------------------------------
    ECTOL:=Energy relative convergence tolerance (see Remark 5)
    LT.0: -ECTOL references a curve that defines tolerance as a
          function of time.
    -----------------------------------------------------------------
    RCTOL:=Residual (force) relative convergence tolerance
           (see Remark 5)
    LT.0: -RCTOL references a curve that defines tolerance as a
          function of time
    -----------------------------------------------------------------
    LSTOL:=Line search convergence tolerance. Default is set to
           LSTOL = 0.9.
    LT.0: -LSTOL is the line search tolerance, but this option
          activates an alternate strategy where line search acts only
          on the independent degrees of freedom. This is opposed to
          the default strategy, where prescribed motions on nodes and
          rigid bodies are also incorporated, sometimes leading to
          unnecessarily small time steps because of the requirement
          of fulfilling these boundary conditions
    -----------------------------------------------------------------
    ABSTOL:=Absolute convergence tolerance.
    LT.0: Convergence detected when the residual norm is less than.
          Note : To drive convergence based on , set DCTOLand ECTOL
          to 10 - 20

    #################################################################

    DNORM:=Displacement norm for convergence test:
    EQ.1: Increment vs. displacement over current step,
    EQ.2: Increment vs. total displacement (default).
    LT.0: |"DNORM" |; also activates reading of optional Card 2.1
    -----------------------------------------------------------------
    DIVERG:=Divergence flag (force imbalance increase during
            equilibrium iterations):
    EQ.1: Reform stiffness if divergence detected (default),
    EQ.2: Ignore divergence.
    -----------------------------------------------------------------
    ISTIF:=Initial stiffness formation flag:
    EQ.1: Reform stiffness at start of each step (default),
    EQ.n: Reform stiffness at start of every n'th step.
    -----------------------------------------------------------------
    NLPRINT:=Nonlinear solver print flag:
    EQ.0: No nolinear iteration information printed(new v970 default)
    EQ.1: Print iteration information to screen, messag, d3hsp files,
    EQ.2: Print extra norm information (NLNORM = 1).
    EQ.3: Same as 2, but also print information from line search.
    NOTE: during execution, sense switch nlprt can also be used to
          toggle this print flag on and off.
    -----------------------------------------------------------------
    NLNORM:=Nonlinear convergence norm type:
    LT.0: Same as 4, but rotational degrees of freedom are scaled
          appropriately with characteristic length ABS(NLNORM) to
          account for units.
    EQ.1: consider translational and rotational degrees of freedom
    EQ.2: consider translational degrees of freedom only (default)
    EQ.4: consider sum of translational and rotational degrees of
          freedom, i.e., no separate treatment.
    -----------------------------------------------------------------
    D3ITCTL:=Control D3ITER database.  If nonzero, the search
             directions for the nonlinear implicit solution are
             written to the D3ITER database. To reduce the size of
             the D3ITER database the database is reset every n time
             steps where n=D3ITCTL
    -----------------------------------------------------------------
    CPCHK:=Contact penetration check flag
    EQ.0: no contact penetration is performed (default)
    EQ.1: check for contact penetration during the nonlinear solution
          procedure. If such penetration is found modify the line
          search to prevent unnecessary penetration.

    #################################################################

    ARCCTL:=Arc length controlling node ID:
    EQ.0: generalized arc length method (default).
    -----------------------------------------------------------------
    ARCDIR:=Arc length controlling node direction (ignored if
            ARCCTL=0 above):
    EQ.1: global X-translation (default),
    EQ.2: global Y-translation,
    EQ.3: global Z-translation.
    -----------------------------------------------------------------
    ARCLEN:=Arc length size
    LE.0.0: chosen automatically using initial step size
    Default is set to ARCLEN = 0.0.
    -----------------------------------------------------------------
    ARCMTH:=Arc length method:
    EQ.1: Crisfield (default),
    EQ.2: Ramm.
    EQ.3: Modified Crisfield (used with NSOLVR = 12 only)
    -----------------------------------------------------------------
    ARCDMP:=Arc length damping option:
    EQ.1: On, oscillations in static solution are supressed,
    EQ.2: Off (default).
    -----------------------------------------------------------------
    ARCPSI:=Relative influence of load/time parameter in spherical
            arclength constraint, default value is 0 which
            corresponds to a cylindrical arclength constraint.
            Applies to ARCMTH = 3.
    -----------------------------------------------------------------
    ARCALF:=Relative influence of predictor step direction for
            positioning of the arc center, default is 0 which means
            that the center is at the origin. Applies to ARCMTH = 3.
    -----------------------------------------------------------------
    ARCTIM:=Optional time when arc length method is initiated.
            Applies to ARCMTH = 3.

    #################################################################

    LSMTD:=Line search convergence method:
    EQ.1: Energy method using only translational variables,
    EQ.2: Residual method,
    EQ.3: Energy method using both translational and rotational
          variables.
    EQ.4: Energy method using sum of translational and rotational
          degrees of freedom, i.e., no separate treatment (default)
    EQ.5: Same as 4, but account for residual norm growth to be extra
          conservative in step length (applies to NSOLVR=12)
    -----------------------------------------------------------------
    LSDIR:=Line search direction method:
    EQ.1: Search on all variables (traditional approach used in
          versions prior to 971),
    EQ.2: Search only on the independent (unconstrained) variables,
    EQ.3: Use adaptive line search (see AWGT, SRED),
    EQ.4: Use curved line search (see IRAD, SRAD).
    -----------------------------------------------------------------
    IRAD:=Normalized curvature factor for curved line search, where 0
          indicates a straight line search and 1 indicates full
          curved line search.
    -----------------------------------------------------------------
    SRAD:=Radius of influence for determining curve in curved line
          search. For each independent node, all nodes within this
          radius are used for determining the curve. If 0, then all
          nodes connected to the same element as the independent node
          are used.
    -----------------------------------------------------------------
    AWGT:=Adaptive line search weight factor between 0 and 1. A high
          value tends to restrict the motion of oscillating nodes
          during the implicit process.
    -----------------------------------------------------------------
    SRED:=Initial step reduction between 0 and 1 for adaptive line
          search, use large number for conservative start in
          implicit procedure.

    """
    name: str = "CONTROL_IMPLICIT_SOLUTION"
    rows_lengths: List[int] = field(default_factory=lambda: [8, 7, 8, 6])

    NSOLVR: [-1, 1, 6, 7, 8, 9, 12] = 12
    ILIMIT: int = 11
    MAXREF: Union[int, float] = 15
    DCTOL: Union[int, float] = 0.001
    ECTOL: Union[int, float] = 0.01
    RCTOL: Union[int, float] = 1.0e10
    LSTOL: Union[int, float] = 0.9
    ABSTOL: Union[int, float] = 1.0e-10

    DNORM: Union[int, float] = 2
    DIVERG: [1, 2] = 1
    ISTIF: int = 1
    NLPRINT: [0, 1, 2, 3] = 0
    NLNORM: Union[int, float] = 2
    D3ITCTL: Union[int, float] = 0
    CPCHK: [0, 1] = 0

    ARCCTL: int = 0
    ARCDIR: [0, 1, 2, 3] = 0
    ARCLEN: Union[int, float] = 0.0
    ARCMTH: [1, 2, 3] = 1
    ARCDMP: [1, 2] = 2
    ARCPSI: Union[int, float] = 0.0
    ARCALF: Union[int, float] = 0.0
    ARCTIM: Union[int, float] = 0.0

    LSMTD: [1, 2, 3, 4, 5, 6] = 4
    LSDIR: [1, 2, 3, 4] = 2
    IRAD: Union[int, float] = 0.0
    SRAD: Union[int, float] = 0.0
    AWGT: Union[int, float] = 0.0
    SRED: Union[int, float] = 0.0


@dataclass
class SOLUTION(ICard):
    """

    SOLN:=Analysis solution procedure:
    EQ.0: Structural analysis only,
    EQ.1: Thermal analysis only,
    EQ.2: Coupled structural thermal analysis.
    -----------------------------------------------------------------
    NLQ:=Define the vector length used in solution.  This value must
         not exceed the vector length of the system which varies
         based on the machine manufacturer.  The default vector
         length is printed at termination in the MESSAG file.
    -----------------------------------------------------------------
    ISNAN:=Flag to check for a NaN in the force and moment arrays
           after the assembly of these arrays is completed.  This
           option can be useful for debugging purposes.  A cost
           overhead of approximately 2% is incurred when this option
           is active.
    EQ.0: No checking,
    EQ.1: Checking is active.
    -----------------------------------------------------------------
    LCINT:=Number of equally spaced points used in curve
           (*DEFINE_CURVE) rediscretization. A minimum number of
           LCINT=100 is always used, i.e., only larger input values
           are possible. Curve rediscretization applies only to
           curves used in material models. Curves defining loads,
           motion, etc. are not rediscretized.
    -----------------------------------------------------------------
    LCACC:=Flag to truncate curves to 6 significant figures for
           single precision and 13 significant figures for double
           precision. The truncation is done after applying the
           offset and scale factors specified in *DEFINE_CURVE.
           Truncation is intended to prevent curve values from
           deviating from the input value, e.g., 0.7 being stored as
           0.69999999. This small deviation was seen to have an
           adverse effect in a particular analysis using *MAT_083. In
           general, curve truncation is not necessary and is unlikely
           to have any effect on results.
    EQ.0: No truncation.
    NE.0: Truncate.
    -----------------------------------------------------------------
    NCDCF:=Global option to evaluate *DEFINE_CURVE_FUNCTION every
           NCDCF:th cycle.
    -----------------------------------------------------------------
    NOCOP:=Avoid copying of material history variables to temporary
           buffers for constitutive evaluations.
    EQ.0: Not active
    EQ.1: Active

    """
    name: str = "CONTROL_SOLUTION"
    rows_lengths: List[int] = field(default_factory=lambda: [7])

    SOLN: [0, 1, 2] = 0
    NLO: Union[int, float] = ""
    ISNAN: [0, 1] = 0
    LCINT: int = 100
    LCACC: [0, 1] = 0
    NCDCF: int = 1
    NOCOP: [0, 1] = 0


@dataclass
class IMPLICIT_SOLVER(ICard):
    """

    LSOLVR:=Linear equation solver method (see Remarks below).
    EQ.2: Parallel multi-frontal sparse solver (default)
    EQ.22: iterative, CG with diagonal preconditioner
    EQ.23: iterative, CG with SGS preconditioner
    EQ.24: iterative, CG with SSOR preconditioner
    EQ.25: iterative, CG with modified ILDLTD preconditioner
    EQ.26: iterative, CG with modified ILDLTO preconditioner that
           requires extra storage
    EQ.30: Parallel direct/hybrid solver MUMPS
    EQ.90: User Supplied Linear Equation Solver SMP only:
    EQ.6: BCSLIB-EXT, direct, sparse, double precision
    -----------------------------------------------------------------
    LPRINT:=Linear solver print flag controls screen and message file
            output (see Remarks below).
    EQ.0: no printing
    EQ.1: output summary statistics on memory, cpu requirements
    EQ.2: more statistics
    EQ.3: even more statistics and debug checking
    During execution, use the interactive command "<ctrl-c>lprint"
    to toggle this print flag between 0 and 1.
    -----------------------------------------------------------------
    NEGEV:=Negative eigenvalue flag.  Selects procedure when negative
           eigenvalues are detected during stiffness matrix inversion
           (see Remarks below).
    EQ.1: stop, or retry step if auto step control is active
    EQ.2: print warning message, try to continue (default)
    -----------------------------------------------------------------
    ORDER:=Ordering option (see Remarks below)
    EQ.0: Method set automatically by LS-DYNA
    EQ.1: MMD, Multiple Minimum Degree.
    EQ.2: Metis
    EQ.4: LSGpart.
    -----------------------------------------------------------------
    DRCM:=Drilling rotation constraint method for shells (see Remarks
          below).
    EQ.1: add drilling stiffness (old Version 970 method)
    EQ.2: same as 4 below
    EQ.3: add no drilling stiffness
    EQ.4: add drilling stiffness (improved method) (default).
    -----------------------------------------------------------------
    DRCPRM:=Drilling rotation constraint parameter for shells. This
            parameter scales the drilling stiffness.
    For the old method (DRCM = 1) the default value of DRCPRM is 1.0
    for linear analysis, 100.0 for nonlinear implicit analysis, and
    either 1.E-12 or 1.E-8 for eigenvalue analysis depending on the
    shell element type.
    For eigenvalue analysis, the input value for DRCPRM is ignored.
    For the improved method (default, DRCM = 4), the default value of
    DRCPRM is as described above for the old method except default
    DRCPRM is 1.0 for nonlinear implicit analysis.
    -----------------------------------------------------------------
    AUTOSPC:=Automatic Constraint Scan flag
    EQ.1: scan the assembled stiffness matrix looking for
          unconstrained, unattached degrees of freedom.
    Generate additional constraints as necessary to avoid negative eigenvalues.
    EQ.2: do not add constraints.
    -----------------------------------------------------------------
    AUTOTOL:=AUTOSPC tolerance.  The test for singularity is the
             ratio of the smallest singular value and the largest
             singular value.
    If this ratio is less than AUTOTOL, then the triple of columns is
    declared singular and a constraint is generated.
    Default values in single and double precision are 1e-4 and 10e-8,
    respectively.

    #################################################################

    LCPACK:=Matrix assembly package:
    EQ.2: Default.
    EQ.3: Same as 2, but incorporates a non-symmetric linear solver;
          see Remarks below
    -----------------------------------------------------------------
    MTXDMP:=Matrix and right-hand-side dumping. LS-DYNA has the
            option of dumping the globally assembled stiffness matrix
            and right-hand-side vectors files in Harwell-Boeing
            sparse matrix format.
    Such output may be useful for comparing to other linear equation
    solution packages.
    EQ.0: No dumping
    GT.0: Dump all matrices and right-hand-side vectors every MTXDMP
          time steps.
    Output is written as ASCII text and the involved filenames are of
    the following form:	K_xxxx_yyy.mtx.rb
    This file contains the stiffness matrix at step xxxx, iteration
    yyy. M_xxxx_yyy.mtx.rb
    This file contains the mass matrix at step xxxx, iteration yyy.
    Only for eigenvalue analysis.		W_xxxx_yyy.mtx.rb
    This file contains the damping matrix at step xxxx, iteration yyy
    Only for simulations with damping. K_xxxx_yyy_zzz.rhs.rb
    This file contains the right hand side at step xxxx, iteration
    yyy, where yyyis the iteration at which a stiffness matrix is
    formed; and zzz is the cumulative iteration number for the step.
    The values of yyy and zzz donвЂ™t always coincide because the
    stiffness matrix is not necessarily reformed every iteration.
    Node_Data_xxxx_yyy
    This file maps stiffness matrix to nodes and provides nodal
    coordinates.
    LT.0: Like positive values of MTXDMP but dumped data is binary.
    EQ.|9999|: Simulation is terminated after dumping matrices and
    right hand side prior to factorization
    -----------------------------------------------------------------
    IPARM1:=For 22 <= LSOLVR <= 26 only, maximum number of iterations
            Default is 500
    -----------------------------------------------------------------
    RPARM1:=For 22 <= LSOLVR <= 26 only, absolute tolerance for
            convergence.  Default is 10e-10.
    -----------------------------------------------------------------
    RPARM2:=For 22 <= LSOLVR <= 26 only, relative tolerance for
            convergence.  Default is 10e-4.
    -----------------------------------------------------------------
    RPARM5:=For LSOLVR = 30 only, compression tolerance used to
            compute a low - rank factorization with the MUMPS solver.
            Default is 0.0.

    #################################################################

    EMXDMP:=Flag for dumping elemental stiffness and mass matrices:
    EQ.0: No dumping
    GT.0: Dump all elemental matrices every EMXDMP time steps.
    Output is written as ASCII text and the involved filenames are of
    the following form: ElmStfMtx_xxxx_yyy
    This file contains the elemental stiffness matrix at step xxxx,
    iteration yyy. ElmMssMtx_xxxx_yyy
    This file contains the elemental mass matrix at step xxxx,
    iteration yyy.
    LT.0: Like positive values of MTXDMP but dumped data is binary.
    EQ.|9999|: Simulation is terminated after dumping matrices and
               right hand side prior to factorization
    -----------------------------------------------------------------
    RDCMEM:=Starting with LS-DYNA R11, the memory for linear algebra
    has been moved from static memory allocation to dynamic memory
    allocation.
    For implicit applications we have found that some operating
    systems are not вЂњrobustвЂќ when queried about how much dynamic
    memory is free.
    This factor caps the amount of dynamic memory requested for
    linear algebra applications to RDCMEM times the amount that the
    operating system declares available.
    0.85 seems to work well for most systems. If you are using a
    workstation and starting up other applications while running
    LS-DYNA, you may need to use a number like 0.50
    -----------------------------------------------------------------
    ABSMEM:=Absolute upper bound for the dynamic memory allocated for
            factorization. The allocated memory will be bounded above
            by the minвЃЎ(RDCME Г—NWORDS ,ABSMEM ) where NWORDS is
            the number of available words as determined by the
            operating system. If the predicted amount of required
            memory is less than this value, then less memory than
            this bound may be allocated.

    """
    name: str = "CONTROL_IMPLICIT_SOLVER"
    rows_lengths: List[int] = field(default_factory=lambda: [8, 8, 3])

    LSOLVR: [2, 22, 23, 24, 25, 26, 30, 90, 6] = 2
    LPRINT: [0, 1, 2, 3] = 0
    NEGEV: [1, 2] = 2
    ORDER: [0, 1, 2, 4] = 0
    DRCM: [1, 2, 3, 4] = 4
    DRCPRM: Union[int, float] = ""
    AUTOSPC: [1, 2] = 1
    AUTOTOL: Union[int, float] = ""

    LCPACK: [2, 3] = 2
    MTXDMP: Union[int, float] = 0.0
    IPARM1: Union[int, float] = 500
    RPARM1: Union[int, float] = 10e-10
    RPARM2: Union[int, float] = 10e-4
    RPARM3: Union[int, float] = ""  # not used in this card
    RPARM4: Union[int, float] = ""  # not used in this card
    RPARM5: Union[int, float] = 0.0

    EMXDMP: Union[int, float] = 0
    RDCMEM: Union[int, float] = 0.85
    ABSMEM: Union[int, float] = ""


@dataclass
class TERMINATION(ICard):
    """

    ENDTIM:=Termination time. Mandatory.
    -----------------------------------------------------------------
    ENDCYC:=Termination cycle.
    -----------------------------------------------------------------
    DTMIN:=Reduction (or scale) factor for initial time step size to
           determine minimum time step.
    -----------------------------------------------------------------
    ENDENG:=Percent change in energy ratio for termination of
            calculation. If undefined, this option is inactive.
    -----------------------------------------------------------------
    ENDMAS:=Percent change in the total mass for termination of
            calculation. This option is relevant if and only if mass
            scaling is used to limit the minimum time step size; see
            *CONTROL_TIMESTEP field DT2MS.
    LT.0.0: |ENDMAS| is the load curve ID defining the percent change
            in the total mass as a function of the total mass.
    -----------------------------------------------------------------
    NOSOL:=Flag for a non-solution run, i.e. normal termination
           directly after initialization.
    EQ.0: off (default),
    EQ.1: on.

    """
    name: str = "CONTROL_TERMINATION"
    rows_lengths: List[int] = field(default_factory=lambda: [6])

    ENDTIM: Union[int, float] = 0.0
    ENDCYC: Union[int, float] = 0
    DTMIN: Union[int, float] = 0.0
    ENDENG: Union[int, float] = 0
    ENDMAS: Union[int, float] = 100000000.0
    NOSOL: [0, 1] = 0


