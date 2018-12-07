

def look (components):
	results = dict(m00 = f"{components['HH']+components['HV']+components['VH']+components['VV']}",
				   m01 = f"{components['HH']+components['HV']-components['VH']-components['VV']}",
				   m02 = f"{components['PH']+components['PV']-components['MH']-components['MV']}",
				   m03 = f"{components['RH']+components['RV']-components['LH']-components['LV']}",
				   m10 = f"{components['HH']-components['HV']+components['VH']-components['VV']}",
				   m11 = f"{components['HH']-components['HV']-components['VH']+components['VV']}",
				   m12 = f"{components['PH']-components['PV']-components['MH']+components['MV']}",
				   m13 = f"{components['RH']-components['RV']-components['LH']+components['LV']}",
				   m20 = f"{components['HP']-components['HM']+components['VP']-components['VM']}",
				   m21 = f"{components['HP']-components['HM']-components['VP']+components['VM']}",
				   m22 = f"{components['PP']-components['PM']-components['MP']+components['MM']}",
				   m23 = f"{components['RP']-components['RM']-components['LP']+components['LM']}",
				   m30 = f"{components['HR']-components['HL']+components['VR']-components['VL']}",
				   m31 = f"{components['HR']-components['HL']-components['VR']+components['VL']}",
				   m32 = f"{components['PR']-components['PL']-components['ML']+components['ML']}",
				   m33 = f"{components['RR']-components['RL']-components['LR']+components['LL']}",)
	return results