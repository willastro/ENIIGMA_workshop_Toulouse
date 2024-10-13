from ENIIGMA.Continuum import Fit
from ENIIGMA.GA import optimize
from ENIIGMA.GA import check_ga
from ENIIGMA.Stats import Pie_chart_plots
from ENIIGMA.Stats import Stats_Module
from ENIIGMA.Stats import Degen_plots
import ENIIGMA
from pyevolve import G1DList, GSimpleGA, Selectors, Crossovers
from pyevolve import Initializators, Mutators, Consts
from pyevolve import Interaction
from pyevolve import Statistics
from pyevolve import DBAdapters
from pyevolve import Scaling



filename = 'Combined_SpcCompanion_NIR.od'
#list_sp = ['COmie', 'CO_CH3OH_4_1_15K_bs', 'H2O_CH3OH_8p', 'CO_CO2_15Kbs', 'CO_CO2_100_70_cde', 'H2O_CO2_6_1_mie', 'H2O_CO2_CH4_10_1_1_a', 'H2O_NH3_Schutte']#, 'H2O_CO2_CO_100_10K']#, 'NH3', 'H2O_NH3_1_05_a']
#list_spmod = ['COmie', 'CO_CH3OH_4_1_15K_bs', 'H2O_CH3OH_8p', 'CO_CO2_15Kbs', 'CO_CO2_100_70_cde', 'H2O_CO2_6_1_mie', 'H2O_NH3_Schutte', 'H2O_HDO_20p_17Kv2']#, 'H2O_CO2_CO_100_10K']#, 'NH3', 'H2O_NH3_1_05_a']
#list_sp_co_heating = ['CO_CO2_1_1_15K', 'CO_CO2_1_1_25K', 'CO_CO2_1_1_60K', 'CO_CO2_1_1_80K', 'CO_CO2_2_1_45K', 'CO_CO2_2_1_50K', 'CO_CO2_2_1_70K', 'CO_CO2_100_8_10K', 'CO_CO2_100_21_10K', 'CO_CO2_100_26_10K', 'CO_CO2_100_70_10K', 'CO_N2_CO2_10K', 'CO_O2_CO2_10K', 'H2O_CO_CO2_10K']
#list_sp_testAV60 = ['CO', 'CO_CH3OH_4_1_15K_bs', 'H2O_CH3OH_8p', 'CO_CO2_15Kbs', 'H2O_CH4_10_06_a_V3', 'H2O_NH3_Schutte']#, 'H2O_CO2_CO_100_10K']#, 'NH3', 'H2O_NH3_1_05_a']
#list_sp_COmie = ['COmie', 'CO_CH3OH_4_1_15K_bs', 'H2O_CH3OH_8p', 'CO_CO2_15Kbs', 'H2O_CH4_10_06_a_V3', 'H2O_NH3_Schutte', 'H2O_CO2_10_1_Ehr']#, 'H2O_CO2_CO_100_10K']#, 'NH3', 'H2O_NH3_1_05_a']
list_sp_hot = ['Mennella2008_binf4_expan', 'COmie', 'CO_CH3OH_4_1_15K_bs', 'H2O_CH3OH_8p', 'CO_CO2_100_70_10K', 'H2O_CH4_10_06_a_V3', 'H2O_NH3_Schutte_v2', 'H2O_CO2_10_1_Ehr', 'CO_CO2_2_1_80K', 'CO2_CH3OH_1_1_10K']#, 'H2O_CO2_CO_100_10K']#, 'NH3', 'H2O_NH3_1_05_a']
#list_sp_hot_HDO = ['COmie', 'CO_CH3OH_4_1_15K_bs', 'H2O_CH3OH_8p', 'CO_CO2_15Kbs', 'H2O_HDO_20p_17Kv2', 'H2O_NH3_Schutte', 'H2O_CO2_10_1_Ehr', 'CO_CO2_2_1_70K']
#list_sp_hot_HDO_gsc = ['COmie', 'CO_CH3OH_4_1_15K_bs', 'H2O_CH3OH_8p', 'CO_CO2_100_70_mie', 'H2O_HDO_20p_17Kv2', 'H2O_NH3_Schutte', 'H2O_CO2_10_1_cde', 'CO_CO2_2_1_70K']

#list_sp_final = ['COmie', 'CO_CH3OH_4_1_15K_bs', 'CO_CO2_100_70_10K', 'H2O_CO2_10_1_Ehr', 'H2O_NH3_Schutte', 'CO_CO2_2_1_70K', 'CO2_CH3OH_1_1_10K']
#list_sp_ref = ['COmie', 'CO_CH3OH_4_1_15K_bs', 'CO_CO2_100_70_10K', 'H2O_CO2_10_1_Ehr', 'H2O_NH3_Schutte', 'CO_CO2_2_1_70K', 'CO2_CH3OH_1_1_10K']

#dir_libice = ENIIGMA.__file__#'/Users/will_rocha_starplan/Downloads/Data_StarPlan_Project/'

libice = '/Users/willrocha/Downloads/Data_StarPlan_Project/IceAge_db_pstar/'#dir_libice[:len(dir_libice)-12]
#exit()
#optimize.ENIIGMA(filename, 2.5, 5.2, list_sp_final, n_points=3500, group_comb=7, skip=True, pathlib = libice, popsize=850, mutp=0.04, gen = 500, ga_min = 0.01, ga_max = 5.5, termination=GSimpleGA.ConvergenceCriteria, fitness='rmse')
#optimize.ENIIGMA(filename, 2.5, 5.2, list_sp_hot, n_points=3500, group_comb=10, skip=True, pathlib = libice, popsize=850, mutp=0.04, gen = 500, ga_min = 0.01, ga_max = 5.5, termination=GSimpleGA.ConvergenceCriteria, fitness='rmse')

#exit()
#Statistic of generations for each combinations
#check_ga.top_five_scaled(savepdf=False)
#check_ga.check(combination=0, option=-4, savepdf=False)

#exit()
#Pie plot
#Pie_chart_plots.pie(sig_level=9.)
#exit()
#Run the statistical module
Stats_Module.stat(f_sig=0.01)

#Check components and create histogram
#Degen_plots.merge_components_cd()
#Degen_plots.hist_plot()	
