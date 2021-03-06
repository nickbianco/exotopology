import os

import osimpipeline as osp
import tasks
import helpers

def scale_setup_fcn(pmm, mset, sset, ikts):

    # Manual scale for torso
    # m = pmm.Scale('pelvis', 0.995727, 0.85, 1.085, sset)

    # copied from subject17.
    m = pmm.Measurement('torso_xy', mset)
    m.add_markerpair('LACR', 'LPSI')
    m.add_markerpair('LACR', 'LASI')
    m.add_markerpair('RACR', 'RPSI')
    m.add_markerpair('RACR', 'RASI')
    m.add_bodyscale('torso', 'XY')

    m = pmm.Measurement('torso_z', mset)
    m.add_markerpair('LACR', 'RACR')
    m.add_bodyscale('torso', 'Z')

    m = pmm.Measurement('pelvis_z', mset)
    m.add_markerpair('RHJC', 'LHJC')
    m.add_bodyscale('pelvis', 'Z')

    m = pmm.Measurement('thigh', mset)
    m.add_markerpair('LHJC', 'LLFC')
    m.add_markerpair('LHJC', 'LMFC')
    m.add_markerpair('RHJC', 'RMFC')
    m.add_markerpair('RHJC', 'RLFC')
    m.add_bodyscale_bilateral('femur')

    m = pmm.Measurement('shank', mset)
    m.add_markerpair('LLFC', 'LLMAL')
    m.add_markerpair('LMFC', 'LMMAL')
    m.add_markerpair('RLFC', 'RLMAL')
    m.add_markerpair('RMFC', 'RMMAL')
    m.add_bodyscale_bilateral('tibia', 'XY')

    m = pmm.Measurement('foot', mset)
    m.add_markerpair('LCAL', 'LMT5')
    m.add_markerpair('LCAL', 'LTOE')
    m.add_markerpair('RCAL',' RMT5')
    m.add_markerpair('RCAL', 'RTOE')
    m.add_bodyscale_bilateral('talus')
    m.add_bodyscale_bilateral('calcn')
    m.add_bodyscale_bilateral('toes')

    m = pmm.Measurement('humerus', mset)
    m.add_markerpair('LACR', 'LMEL')
    m.add_markerpair('LACR', 'LLEL')
    m.add_markerpair('RACR', 'RMEL')
    m.add_markerpair('RACR', 'RLEL')
    m.add_bodyscale_bilateral('humerus')

    m = pmm.Measurement('radius_ulna', mset)
    m.add_markerpair('LLEL', 'LFAradius')
    m.add_markerpair('LMEL', 'LFAulna')
    m.add_markerpair('RMEL', 'RFAulna')
    m.add_markerpair('RLEL', 'RFAradius')
    m.add_bodyscale_bilateral('ulna')
    m.add_bodyscale_bilateral('radius')
    m.add_bodyscale_bilateral('hand')

    m = pmm.Measurement('pelvis_Y', mset)
    m.add_markerpair('LPSI', 'LHJC')
    m.add_markerpair('RPSI', 'RHJC')
    m.add_markerpair('LASI', 'LHJC')
    m.add_markerpair('RASI', 'RHJC')
    m.add_bodyscale('pelvis', 'Y')

    m = pmm.Measurement('pelvis_X', mset)
    m.add_markerpair('RASI', 'RPSI')
    m.add_markerpair('LASI', 'LPSI')
    m.add_bodyscale('pelvis', 'X')

    m = pmm.Measurement('shank_width', mset)
    m.add_markerpair('LLMAL', 'LMMAL')
    m.add_markerpair('RLMAL', 'RMMAL')
    m.add_bodyscale_bilateral('tibia', 'Z')

    ikts.add_ikmarkertask_bilateral('ACR', True, 100.0)
    ikts.add_ikmarkertask('CLAV', True, 100.0)
    ikts.add_ikmarkertask_bilateral('LEL', True, 50.0)
    ikts.add_ikmarkertask_bilateral('MEL', True, 50.0)
    ikts.add_ikmarkertask_bilateral('FAradius', True, 50.0)

    ikts.add_ikmarkertask_bilateral('FAulna', True, 50.0)
    ikts.add_ikmarkertask_bilateral('ASI', True, 500.0)
    ikts.add_ikmarkertask_bilateral('PSI', False, 250.0)
    ikts.add_ikmarkertask_bilateral('HJC', True, 1000.0)
    ikts.add_ikmarkertask_bilateral('LFC', True, 1000.0)
    ikts.add_ikmarkertask_bilateral('MFC', True, 200.0)
    ikts.add_ikmarkertask_bilateral('LMAL', True, 500.0)
    ikts.add_ikmarkertask_bilateral('MMAL', True, 500.0)
    ikts.add_ikmarkertask_bilateral('CAL', True, 25.0)
    ikts.add_ikmarkertask_bilateral('TOE', True, 25.0)
    ikts.add_ikmarkertask_bilateral('MT5', True, 25.0)

    ikts.add_ikcoordinatetask('pelvis_list', True, 0.0, 1.0)
    # ikts.add_ikcoordinatetask_bilateral('knee_angle', True, 0.0, 1.0)
    ikts.add_ikcoordinatetask_bilateral('ankle_angle', True, 0.0, 1.0)

    ikts.add_ikmarkertask('C7', False, 0)
    ikts.add_ikmarkertask_bilateral('ASH', False, 10.0)
    ikts.add_ikmarkertask_bilateral('PSH', False, 10.0)

    ikts.add_ikmarkertask_bilateral('FAsuperior', False, 0.0)
    ikts.add_ikmarkertask_bilateral('TH1', False, 0.0)
    ikts.add_ikmarkertask_bilateral('TH2', False, 0.0)
    ikts.add_ikmarkertask_bilateral('TH3', False, 0.0)
    ikts.add_ikmarkertask_bilateral('TB1', False, 0.0)
    ikts.add_ikmarkertask_bilateral('TB2', False, 0.0)
    ikts.add_ikmarkertask_bilateral('TB3', False, 0.0)
    ikts.add_ikmarkertask_bilateral('UA1', False, 0.0)
    ikts.add_ikmarkertask_bilateral('UA2', False, 0.0)
    ikts.add_ikmarkertask_bilateral('UA3', False, 0.0)
    ikts.add_ikmarkertask_bilateral('AJC', False, 0.0)
    ikts.add_ikmarkertask_bilateral('SJC', False, 0.0)
    ikts.add_ikmarkertask_bilateral('EJC', False, 0.0)
    ikts.add_ikmarkertask_bilateral('KJC', False, 0.0)

def add_to_study(study):
    subject = study.add_subject(19, 68.50)

    cond_args = dict()
    cond_args['walk100'] = (1, '_newCOP3')
    cond_args['walk125'] = (1, '_newCOP3')
    cond_args['walk150'] = (1, '_newCOP3')
    cond_args['walk175'] = (1, '_newCOP3')
    cond_args['run200'] = (1, '_newCOP3')
    cond_args['run300'] = (1, '_newCOP3')
    cond_args['run400'] = (1, '_newCOP3')
    cond_args['run500'] = (1, '_newCOP3')
    subject.cond_args = cond_args

    static = subject.add_condition('static')
    static_trial = static.add_trial(1, omit_trial_dir=True)

    # `os.path.basename(__file__)` should be `subject19.py`.
    scale_setup_task = subject.add_task(osp.TaskScaleSetup,
            init_time=0.41667,
            final_time=6.14167,
            mocap_trial=static_trial,
            edit_setup_function=scale_setup_fcn,
            addtl_file_dep=['dodo.py', os.path.basename(__file__)])

    subject.add_task(osp.TaskScale,
            scale_setup_task=scale_setup_task,
            #scale_max_isometric_force=True,
            )

    subject.add_task(tasks.TaskScaleMuscleMaxIsometricForce)
    marker_adjustments = dict()
    # marker_adjustments['RTOE'] = (1, 0.0170717)
    # marker_adjustments['RMT5'] = (1, 0.011679)
    # marker_adjustments['LTOE'] = (1, 0.0170708)
    # marker_adjustments['LMT5'] = (1, 0.0116779)
    subject.add_task(tasks.TaskAdjustScaledModelMarkers, marker_adjustments)
    subject.scaled_model_fpath = os.path.join(subject.results_exp_path,
        '%s_final.osim' % subject.name)

    ## walk1 condition
    walk1 = subject.add_condition('walk1', metadata={'walking_speed': 1.00})

    # GRF gait landmarks
    # walk1_trial_temp = walk1.add_trial(99, omit_trial_dir=True)
    # walk1_trial_temp.add_task(osp.TaskGRFGaitLandmarks)
    # walk1_trial_temp.add_task(tasks.TaskUpdateGroundReactionColumnLabels)
    
    gait_events = dict()
    gait_events['right_strikes'] = [0.503, 2.934, 4.134, 5.361]
    gait_events['left_toeoffs'] = [0.720, 3.148, 4.340] 
    gait_events['left_strikes'] = [1.103, 3.516, 4.744] 
    gait_events['right_toeoffs'] = [1.309, 3.746, 4.959] 
    gait_events['stride_times'] = [1.738-0.503, 4.134-2.934, 5.361-4.134]
    walk1_trial = walk1.add_trial(1,
            gait_events=gait_events,
            omit_trial_dir=True,
            )

    # walk1: main study tasks
    mrs_setup_tasks = helpers.generate_main_tasks(walk1_trial)
    helpers.generate_exotopology_tasks(walk1_trial, mrs_setup_tasks)
    helpers.generate_coupled_controls_tasks(walk1_trial, mrs_setup_tasks)

    ## walk2 condition
    walk2 = subject.add_condition('walk2', metadata={'walking_speed': 1.25})

    # walk2_trial = walk2.add_trial(1, omit_trial_dir=True)
    # walk2_trial.add_task(tasks.TaskUpdateGroundReactionColumnLabels)
    # walk2_trial.add_task(osp.TaskGRFGaitLandmarks, threshold=10)

    # Trial to use
    gait_events = dict()
    gait_events['right_strikes'] = [0.599, 1.653, 2.718, 3.790] #, 4.857]
    gait_events['left_toeoffs'] = [0.782, 1.839, 2.896] #, 3.962]
    gait_events['left_strikes'] = [1.124, 2.183, 3.256] #, 4.331]
    gait_events['right_toeoffs'] = [1.302, 2.368, 3.423] #, 4.504]
    walk2_trial = walk2.add_trial(1,
            gait_events=gait_events,
            omit_trial_dir=True,
            )
    walk2_trial.add_task(tasks.TaskUpdateGroundReactionColumnLabels)

    # walk2: main study tasks
    helpers.generate_sensitivity_tasks(walk2_trial)
    mrs_setup_tasks = helpers.generate_main_tasks(walk2_trial)
    helpers.generate_exotopology_tasks(walk2_trial, mrs_setup_tasks)
    helpers.generate_coupled_controls_tasks(walk2_trial, mrs_setup_tasks)

    ## walk3 condition
    walk3 = subject.add_condition('walk3', metadata={'walking_speed': 1.50})

    # GRF gait landmarks
    # walk3_trial_temp = walk3.add_trial(99, omit_trial_dir=True)
    # walk3_trial_temp.add_task(osp.TaskGRFGaitLandmarks)
    # walk3_trial_temp.add_task(tasks.TaskUpdateGroundReactionColumnLabels)
    
    gait_events = dict()
    gait_events['right_strikes'] = [0.103, 1.081, 2.082, 3.068]
    gait_events['left_toeoffs'] = [0.264, 1.252, 2.243] 
    gait_events['left_strikes'] = [0.597, 1.592, 2.568] 
    gait_events['right_toeoffs'] = [0.774, 1.762, 2.740] 
    walk3_trial = walk3.add_trial(1,
            gait_events=gait_events,
            omit_trial_dir=True,
            )

    # walk3: main study tasks
    mrs_setup_tasks = helpers.generate_main_tasks(walk3_trial)
    helpers.generate_exotopology_tasks(walk3_trial, mrs_setup_tasks)
    helpers.generate_coupled_controls_tasks(walk3_trial, mrs_setup_tasks)

    ## walk4 condition
    walk4 = subject.add_condition('walk4', metadata={'walking_speed': 1.75})

    # GRF gait landmarks
    # walk4_trial_temp = walk4.add_trial(99, omit_trial_dir=True)
    # walk4_trial_temp.add_task(osp.TaskGRFGaitLandmarks)
    # walk4_trial_temp.add_task(tasks.TaskUpdateGroundReactionColumnLabels)
    
    gait_events = dict()
    gait_events['right_strikes'] = [0.123, 1.026, 1.970, 2.886]
    gait_events['left_toeoffs'] = [0.271, 1.189, 2.120] 
    gait_events['left_strikes'] = [0.589, 1.506, 2.439] 
    gait_events['right_toeoffs'] = [0.738, 1.694, 2.591]
    walk4_trial = walk4.add_trial(1,
            gait_events=gait_events,
            omit_trial_dir=True,
            )

    # walk4: main study tasks
    mrs_setup_tasks = helpers.generate_main_tasks(walk4_trial)
    helpers.generate_exotopology_tasks(walk4_trial, mrs_setup_tasks)
    helpers.generate_coupled_controls_tasks(walk4_trial, mrs_setup_tasks)

    # multi-phase parameter calibration (trial does not matter)
    calibrate_setup_task = walk3_trial.add_task(
        tasks.TaskCalibrateParametersMultiPhaseSetup,
        ['walk1','walk2','walk3','walk4'],
        ['cycle01'],
        study.param_dict,
        study.cost_dict,
        passive_precalibrate=True)

    walk3_trial.add_task(
        tasks.TaskCalibrateParametersMultiPhase,
        calibrate_setup_task)

    walk3_trial.add_task(
        tasks.TaskCalibrateParametersMultiPhasePost,
        calibrate_setup_task)