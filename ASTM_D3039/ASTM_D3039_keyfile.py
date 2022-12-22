from ls_pre_post_lib.cards import BOUNDARY, \
                                  CONTROL, \
                                  DATABASE, \
                                  DEFINE, \
                                  PART, \
                                  SET
from ls_pre_post_lib.keyfile import ModelKeyfile
import json


def main() -> None:
    with open(r'D:\Documents\CML\CML_LS-Dyna_scripts\ASTM_D3039_data.json') as file:
        model_data = json.load(file)

    # ---------------------------------------------------------------

    keyfile_path = model_data['keyfile_path']
    keyfile_name = model_data['keyfile_name']

    L = model_data['L']
    b = model_data['b']
    laminate_statement = model_data['laminate_statement']
    n = model_data['n']
    angle = model_data['angle']
    t = model_data['t']
    symmetry = model_data['symmetry']

    lx = model_data['lx']
    ly = model_data['ly']
    lz = model_data['lz']

    A = model_data['A']
    displ = model_data['displ']

    termination_time = model_data['termination_time']
    step = model_data['step']

    # -----------------------------------------------------------------

    ASTM_D3039 = ModelKeyfile(keyfile_name=keyfile_name,
                              keyfile_path=keyfile_path)

    # ---------------------------------------------------------------
    #выгрузка узлов из файла с геометрией
    part = ASTM_D3039.get_partByID(i=1)
    node_list = part.get_node_ids()

    if model_data["problem_statement"] == 0:
        node_list = node_list[-(lx+1)*(ly+1):]

    # there should also be an autofill of cards from the model_data dict.
    ASTM_D3039.add_card(BOUNDARY.PRESCRIBED_MOTION_SET(NSID=2,
                                                       DOF=1,
                                                       VAD=2,
                                                       LCID=1,
                                                       SF=0.0,
                                                       DEATH=0.0))
    ASTM_D3039.add_card(BOUNDARY.SPC_SET(NSID=1,
                                         DOFX=1,
                                         DOFY=1,
                                         DOFZ=1,
                                         DOFRX=1,
                                         DOFRY=1,
                                         DOFRZ=1))
    ASTM_D3039.add_card(BOUNDARY.SPC_SET(NSID=2,
                                         DOFX=0,
                                         DOFY=1,
                                         DOFZ=1,
                                         DOFRX=1,
                                         DOFRY=1,
                                         DOFRZ=1))
    # -----------------------------------------------------------------
    ASTM_D3039.add_card(CONTROL.ACCURACY(INN=2))
    ASTM_D3039.add_card(CONTROL.IMPLICIT_AUTO(IAUTO=1,
                                              DTMIN=step,
                                              DTMAX=0.001))
    ASTM_D3039.add_card(CONTROL.IMPLICIT_GENERAL(IMFLAG=1,
                                                 DTO=step))
    ASTM_D3039.add_card(CONTROL.IMPLICIT_SOLUTION(NLNORM=0))
    ASTM_D3039.add_card(CONTROL.SOLUTION())
    ASTM_D3039.add_card(CONTROL.TERMINATION(ENDTIM=termination_time,
                                            DTMIN=step,
                                            ENDMAS=0.0))
    # -----------------------------------------------------------------
    ASTM_D3039.add_card(DATABASE.ELOUT(DT=step))
    ASTM_D3039.add_card(DATABASE.NODOUT(DT=step))
    ASTM_D3039.add_card(DATABASE.SECFORC(DT=step))
    ASTM_D3039.add_card(DATABASE.BINARY_D3PLOT(DT=step))
    ASTM_D3039.add_card(DATABASE.CROSS_SECTION_PLANE(CSID=1,
                                                     PSID=1,
                                                     XCT=L,
                                                     YCT=b,
                                                     XCH=L + 1,
                                                     YCH=b))
    ASTM_D3039.add_card(DATABASE.EXTENT_BINARY(STRFLG=1,
                                               DCOMP=1,
                                               NINTSLD=0,
                                               INTOUT='ALL',
                                               NODOUT='ALL'))

    id_step = round((lx + 1) / 5) * (ly + 1)
    ids = node_list[round(ly / 2) + id_step:-round(ly / 2) - id_step:id_step]
    ASTM_D3039.add_card(DATABASE.HISTORY_NODE(rows_lengths=[len(ids)],
                                              ID_line=[DATABASE.ID_line(*ids).__dict__]))
    # -----------------------------------------------------------------
    ASTM_D3039.add_card(DEFINE.COORDINATE_SYSTEM(CID=1,
                                                 XL=1.0,
                                                 YP=0.0016667))
    ASTM_D3039.add_card(DEFINE.CURVE(rows_lengths=[8, 3, 3],
                                     SFA=0.0,
                                     SFO=0.0,
                                     Curve_points=[DEFINE.Curve_point(A1=0.0,
                                                                      O1=0.0).__dict__,
                                                   DEFINE.Curve_point(A1=termination_time,
                                                                      O1=displ).__dict__]))
    # -----------------------------------------------------------------
    if laminate_statement == 0:
        if symmetry:
            layer_lines = [PART.Layer(MID1=2,
                                      THICK1=t,
                                      B1=angle,
                                      MID2=2,
                                      THICK2=t,
                                      B2=-angle).__dict__
                           for _ in range(int(n / 2))]
            layer_lines += [PART.Layer(MID1=2,
                                       THICK1=t,
                                       B1=-angle,
                                       MID2=2,
                                       THICK2=t,
                                       B2=angle).__dict__
                            for _ in range(int(n / 2))]
        else:
            layer_lines = [PART.Layer(MID1=2,
                                      THICK1=t,
                                      B1=angle,
                                      MID2=2,
                                      THICK2=t,
                                      B2=-angle).__dict__
                           for _ in range(n)]
    elif laminate_statement == 1:
        layer_lines = [PART.Layer(MID1=2,
                                  THICK1=t,
                                  B1=angle).__dict__
                       for _ in range(n)]

    ASTM_D3039.add_card(PART.COMPOSITE(rows_lengths=[1, 8] + [8] * len(layer_lines),
                                       PID=1,
                                       ELFORM=16,
                                       Layers=layer_lines))
    # -----------------------------------------------------------------
    #узлы для накладок заполнение
    num = (round(A / L * lx) + 1) * (ly + 1)
    fix_nodes = node_list[:num]
    move_nodes = node_list[-num:]

    node_lines_fix = [SET.NodeLine(*nodes).__dict__
                      for nodes in [fix_nodes[i:i + 8]
                                    for i in range(0, len(fix_nodes), 8)]]
    node_lines_move = [SET.NodeLine(*nodes).__dict__
                       for nodes in [move_nodes[i:i + 8]
                                     for i in range(0, len(move_nodes), 8)]]

    ASTM_D3039.add_card(SET.NODE_LIST(rows_lengths=[7] + [8] * len(node_lines_fix),
                                      SID=1,
                                      node_lines=node_lines_fix))
    ASTM_D3039.add_card(SET.NODE_LIST(rows_lengths=[7] + [8] * len(node_lines_move),
                                      SID=2,
                                      node_lines=node_lines_move))

    ASTM_D3039.add_card(SET.PART_LIST(rows_lengths=[6, 8],
                                      SID=1,
                                      part_lines=[SET.PartLine(PID1=1).__dict__]))

    # ---------------------------------------------------------------
    #для удаления парта
    ASTM_D3039.remove_keyword("*PART")
    ASTM_D3039.save(keyfile_path, keyfile_name)


if __name__ == "__main__":
    main()
