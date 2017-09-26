addpath(genpath('@REL_PATH_TO_TOOL@'));
Misc = struct();
%Misc.Loads_path = 'external_loads.xml';
% TODO Misc.DofNames_Input: solve each leg separately.
% TODO Misc.MuscleNames_Input
Misc.DofNames_Input = {...
                       'hip_flexion_@SIDE@', ...
                       'knee_angle_@SIDE@', ...
                       'ankle_angle_@SIDE@', ...
                       };
%Misc.DofNames_Input = {...
%                       'hip_adduction_@SIDE@', ...
%                       'hip_rotation_@SIDE@', ...
%                       'hip_flexion_@SIDE@', ...
%                       'knee_angle_@SIDE@', ...
%                       'ankle_angle_@SIDE@', ...
%                       };
%Misc.DofNames_Input = {...
%                       'hip_flexion_@SIDE@', ...
%                       'knee_angle_@SIDE@', ...
%                       'ankle_angle_@SIDE@', ...
%                       };
Misc.MuscleNames_Input = {};
%Misc.MuscleNames_Input = {...
%    'soleus_r', ...
%    'med_gas_r', ...
%    'tib_ant_r' ...
%    };
% Misc.Mesh_Frequency = 20;
Misc.costfun = 'Default';
Misc.tendonStiffnessCoeff = 35;
Misc.muscleStrainModifiers.vas_int_r = 1.0/0.6;
Misc.tendonStiffnessModifiers.vas_int_r = 0.8;
Misc.tendonStiffnessModifiers.soleus_r = 0.9;
Misc.tendonStiffnessModifiers.med_gas_r = 0.9;
tic;
[Time,MExcitation,MActivation,RActivation,TForcetilde,TForce,lMtilde,lM,MuscleNames,OptInfo,DatStore] = ...
SolveMuscleRedundancy_FtildeState_actdyn(...
    '@MODEL@', ... % model_path
    '@IK_SOLUTION@', ... % IK_path
    '@ID_SOLUTION@', ... % ID_path
    [@INIT_TIME@, @FINAL_TIME@], ... % time
    'results', ... % OutPath
    Misc);
    % TODO '', ... % ID_path
toc
save @STUDYNAME@_@NAME@_mrs.mat -v7.3

