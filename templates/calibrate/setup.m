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

Misc.study = 'ParameterCalibration';
Misc.parameterCalibrationTerms = struct()
possibleMuscsToCal = {'bifemsh_r','med_gas_r','glut_max2_r','rect_fem_r','semimem_r','soleus_r','tib_ant_r','vas_int_r','psoas_r'};

if exist('optimal_fiber_length', 'var') && optimal_fiber_length
	lMo_muscs = {'@lMo_MUSCLES@'};
	lMo_muscs = strsplit(lMo_muscs{1}, ',');
	for m = 1:length(lMo_muscs)
	    if any(strcmp(possibleMuscsToCal, lMo_muscs{m}))
			if isfield(Misc.parameterCalibrationTerms, lMo_muscs{m})
				if isfield(Misc.parameterCalibrationTerms.(lMo_muscs{m}), 'params')
					numParams = length(Misc.parameterCalibrationTerms.(lMo_muscs{m}).params);
				else
					numParams = 0;
				end
			else 
				numParams = 0;
			end
			Misc.parameterCalibrationTerms.(lMo_muscs{m}).params{numParams+1} = 'optimal_fiber_length';
		else
			error('ERROR: muscle %s is not available to calibrate.', lMo_muscs{m})
		end
	end
end
	
if exist('tendon_slack_length', 'var') && tendon_slack_length
	lTs_muscs = {'@lTs_MUSCLES@'};
	lTs_muscs = strsplit(lTs_muscs{1}, ',');
	for m = 1:length(lTs_muscs)
		if any(strcmp(possibleMuscsToCal, lTs_muscs{m}))
			if isfield(Misc.parameterCalibrationTerms, lTs_muscs{m})
				if isfield(Misc.parameterCalibrationTerms.(lTs_muscs{m}), 'params')
					numParams = length(Misc.parameterCalibrationTerms.(lTs_muscs{m}).params);
				else
					numParams = 0;
				end
			else 
				numParams = 0;
			end
			Misc.parameterCalibrationTerms.(lTs_muscs{m}).params{numParams+1} = 'tendon_slack_length'; 
		else
			error('ERROR: muscle %s is not available to calibrate.', lTs_muscs{m})
		end
	end
end
	
if exist('pennation_angle', 'var') && pennation_angle
	alf_muscs = {'@alf_MUSCLES@'};
	alf_muscs = strsplit(alf_muscs{1}, ',');
	for m = 1:length(alf_muscs)
		if any(strcmp(possibleMuscsToCal, alf_muscs{m}))
			if isfield(Misc.parameterCalibrationTerms, alf_muscs{m})
				if isfield(Misc.parameterCalibrationTerms.(alf_muscs{m}), 'params')
					numParams = length(Misc.parameterCalibrationTerms.(alf_muscs{m}).params);
				else
					numParams = 0;
				end
			else 
				numParams = 0;
			end
			Misc.parameterCalibrationTerms.(alf_muscs{m}).params{numParams+1} = 'pennation_angle'; 
		else
			error('ERROR: muscle %s is not available to calibrate.', alf_muscs{m})
		end
	end
end
	
if exist('muscle_strain', 'var') && muscle_strain
	e0_muscs = {'@e0_MUSCLES@'};
	e0_muscs = strsplit(e0_muscs{1}, ',');
	for m = 1:length(e0_muscs)
		if any(strcmp(possibleMuscsToCal, e0_muscs{m}))
			if isfield(Misc.parameterCalibrationTerms, e0_muscs{m})
				if isfield(Misc.parameterCalibrationTerms.(e0_muscs{m}), 'params')
					numParams = length(Misc.parameterCalibrationTerms.(e0_muscs{m}).params);
				else
					numParams = 0;
				end
			else 
				numParams = 0;
			end
			Misc.parameterCalibrationTerms.(e0_muscs{m}).params{numParams+1} = 'muscle_strain'; 
		else
			error('ERROR: muscle %s is not available to calibrate.', e0_muscs{m})
		end
	end
end
	
if exist('emg', 'var') && emg
	emg_muscs = {'@emg_MUSCLES@'};
	emg_muscs = strsplit(emg_muscs{1}, ',');
	for m = 1:length(emg_muscs)
		if any(strcmp(possibleMuscsToCal, emg_muscs{m}))
			if isfield(Misc.parameterCalibrationTerms, emg_muscs{m})
				if isfield(Misc.parameterCalibrationTerms.(emg_muscs{m}), 'costs')
					numCosts = length(Misc.parameterCalibrationTerms.(emg_muscs{m}).params);
				else
					numCosts = 0;
				end
			else 
				numCosts = 0;
			end
			Misc.parameterCalibrationTerms.(emg_muscs{m}).costs{numCosts+1} = 'emg';
		else
			error('ERROR: muscle %s is not available to calibrate.', emg_muscs{m})
		end
	end
end

Misc.parameterCalibrationData.emg = '@EMG_PATH@';
Misc.tendonStiffnessCoeff = 35;
Misc.tendonStiffnessModifiers.soleus_r = 0.5;
Misc.tendonStiffnessModifiers.med_gas_r = 0.5;
tic;
[Time,MExcitation,MActivation,RActivation,TForcetilde,TForce,MuscleNames,MuscleData,OptInfo,DatStore] = ...
SolveMuscleRedundancy_FtildeState(...
    '@MODEL@', ... % model_path
    '@IK_SOLUTION@', ... % IK_path
    '@ID_SOLUTION@', ... % ID_path
    [@INIT_TIME@, @FINAL_TIME@], ... % time
    'results', ... % OutPath
    Misc);
    % TODO '', ... % ID_path
toc
save @STUDYNAME@_@NAME@_calibrate.mat -v7.3

