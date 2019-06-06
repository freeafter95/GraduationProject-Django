from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    permission = models.CharField(max_length=1)

# class Literature(models.Model):
#     p_name = models.CharField(max_length=255, primary_key=True)
#     author = models.CharField(max_length=255, null=True)
#     point_word = models.CharField(max_length=255, null=True)
#     open_time = models.DateTimeField()
#     open_book = models.CharField(max_length=255, null=True)
#     insert_time = models.DateTimeField(auto_now=True)

# class Picture(models.Model):
#     pic_path = models.CharField(max_length=255, primary_key=True)
#     pic_attr = models.CharField(max_length=255)
#     pic_num = models.IntegerField()
#     main_elem = models.CharField(max_length=255)
#     insert_time = models.DateTimeField(auto_now=True)


# class Djbasicnatu(models.Model):
#     alloy_grade = models.CharField(max_length=255, null=True)
#     chem_formula = models.CharField(max_length=255, null=True)
#     main_elem  = models.CharField(max_length=255, null=True)
#     second_elem  = models.CharField(max_length=255, null=True)
#     trace_elem  = models.CharField(max_length=255, null=True)
#     literature = models.ForeignKey(Literature)
#     info_source = models.CharField(max_length=255, null=True)
#     structure_Id  = models.CharField(max_length=255, null=True)
#     space_group = models.FloatField(null=True)
#     temperature = models.FloatField(null=True)
#     latt_cons = models.FloatField(null=True)
#     rerong = models.FloatField(null=True)
#     rpzxs = models.FloatField(null=True)
#     volume = models.CharField(max_length=255, null=True)
#     density = models.FloatField(null=True)
#     energy = models.FloatField(null=True)
#     atomic_ener = models.FloatField(null=True)
#     form_ener = models.FloatField(null=True)
#     elastic_cons = models.CharField(max_length=255, null=True)
#     wPoisson_rate = models.FloatField(null=True)
#     elasti_anis = models.FloatField(null=True)
#     wG_Ress = models.IntegerField(null=True)
#     wK_Ress = models.IntegerField(null=True)
#     mater_cate = models.CharField(max_length=255, null=True)
#     brittle_tough = models.CharField(max_length=255, null=True)
#     insert_time = models.DateTimeField(auto_now=True)


# class Process_table(models.Model):
#     alloy_grade = models.CharField(max_length=255, null=True)
#     chem_formula = models.CharField(max_length=255, null=True)
#     main_elem  = models.CharField(max_length=255, null=True)
#     second_elem  = models.CharField(max_length=255, null=True)
#     trace_elem  = models.CharField(max_length=255, null=True)
#     literature = models.ForeignKey(Literature)
#     info_source = models.CharField(max_length=255, null=True)
#     qProcessing_sample  = models.CharField(max_length=255, null=True)
#     qSample_size = models.CharField(max_length=255, null=True)
#     qsyx_com = models.CharField(max_length=255, null=True)
#     qsyjld = models.CharField(max_length=255, null=True)
#     qsyzg = models.CharField(max_length=255, null=True)
#     process_tech = models.CharField(max_length=255, null=True)
#     smelting_vacuum = models.FloatField(null=True)
#     smelting_voltage = models.FloatField(null=True)
#     smelting_current = models.FloatField(null=True)
#     smelting_times = models.FloatField(null=True)
#     ingot_diameter = models.FloatField(null=True)
#     nominal_ability = models.FloatField(null=True)
#     heat_temp = models.FloatField(null=True)
#     bw_time = models.FloatField(null=True)
#     extruder_tonnage = models.FloatField(null=True)
#     jyt_diameter = models.FloatField(null=True)
#     jy_heattemp = models.FloatField(null=True)
#     jy_bwtime = models.FloatField(null=True)
#     yz_jjrtime = models.FloatField(null=True)
#     yz_bwtime = models.FloatField(null=True)
#     dc_maxprorate = models.FloatField(null=True)
#     all_prorate = models.FloatField(null=True)
#     quenching_medium = models.CharField(max_length=255, null=True)
#     quenching_temp = models.FloatField(null=True)
#     annealing_type = models.CharField(max_length=255, null=True)
#     annealing_temp = models.FloatField(null=True)
#     annealing_time  = models.FloatField(max_length=11, null=True)
#     hProcessing_sample = models.CharField(max_length=255, null=True) 
#     hSample_size = models.CharField(max_length=255, null=True)
#     hsyx_com = models.CharField(max_length=255, null=True)
#     hsyjld = models.CharField(max_length=255, null=True)
#     hsyzg = models.CharField(max_length=255, null=True)
#     insert_time = models.DateTimeField(auto_now=True)

# class Test_table(models.Model):
#     alloy_grade = models.CharField(max_length=255, null=True)
#     chem_formula = models.CharField(max_length=255, null=True)
#     main_elem  = models.CharField(max_length=255, null=True)
#     second_elem  = models.CharField(max_length=255, null=True)
#     trace_elem  = models.CharField(max_length=255, null=True)
#     literature = models.ForeignKey(Literature)
#     info_source = models.CharField(max_length=255, null=True)
#     hProcess_sample  = models.CharField(max_length=255, null=True)
#     hSample_size = models.CharField(max_length=255, null=True)
#     hsyx_com = models.CharField(max_length=255, null=True)
#     hsyjld = models.CharField(max_length=255, null=True)
#     hsyzg = models.CharField(max_length=255, null=True)
#     xntest_cond = models.CharField(max_length=255, null=True)
#     xndeform_rate = models.CharField(max_length=255, null=True)
#     xntest_temp = models.FloatField(null=True)
#     bulk_modulu = models.FloatField(null=True)
#     shear_modulus = models.FloatField(null=True)
#     young_modulus = models.FloatField(null=True)
#     tensile_strength = models.FloatField(null=True)
#     yield_strength = models.FloatField(null=True) 
#     breaking_strength = models.FloatField(null=True)
#     dhys_rate = models.FloatField(null=True)
#     hPoisson_rate = models.FloatField(null=True)
#     heat_rate = models.FloatField(null=True)
#     bheat_capa = models.FloatField(null=True) 
#     rswell_modu = models.FloatField(null=True) 
#     rfs_rate = models.FloatField(null=True) 
#     conductivity = models.FloatField(null=True) 
#     dielectric_con = models.FloatField(null=True)
#     work_fun = models.FloatField(null=True)
#     coercivity = models.FloatField(null=True)
#     magnetic_rate = models.FloatField(null=True)
#     bhmagnetic_str = models.FloatField(null=True) 
#     curie_temp = models.FloatField(null=True)
#     insert_time = models.DateTimeField(auto_now=True)

# class Radiation_table(models.Model):
#     alloy_grade = models.CharField(max_length=255, null=True)
#     chem_formula = models.CharField(max_length=255, null=True)
#     main_elem  = models.CharField(max_length=255, null=True)
#     second_elem  = models.CharField(max_length=255, null=True)
#     trace_elem  = models.CharField(max_length=255, null=True)
#     literature = models.ForeignKey(Literature)
#     info_source = models.CharField(max_length=255, null=True)
#     hProcess_sample  = models.CharField(max_length=255, null=True)
#     hSample_size = models.CharField(max_length=255, null=True)
#     hsyx_com = models.CharField(max_length=255, null=True)
#     hsyjld = models.CharField(max_length=255, null=True)
#     hsyzg = models.CharField(max_length=255, null=True)
#     Irr_cond = models.CharField(max_length=255, null=True)
#     Ray_type  = models.CharField(max_length=255, null=True)
#     Hirr_symc = models.CharField(max_length=255, null=True)
#     Hirr_sycc = models.CharField(max_length=255, null=True)
#     Hirr_syjld = models.CharField(max_length=255, null=True)
#     Hirr_syzg = models.CharField(max_length=255, null=True)
#     Neu_num = models.FloatField(null=True)
#     Ray_stro = models.FloatField(null=True)
#     Irr_time = models.FloatField(null=True)
#     insert_time = models.DateTimeField(auto_now=True)

# class irrallafter(models.Model):
#     alloy_grade = models.CharField(max_length=255, null=True)
#     chem_formula = models.CharField(max_length=255, null=True)
#     main_elem  = models.CharField(max_length=255, null=True)
#     second_elem  = models.CharField(max_length=255, null=True)
#     trace_elem  = models.CharField(max_length=255, null=True)
#     literature = models.ForeignKey(Literature)
#     info_source = models.CharField(max_length=255, null=True)
#     Irr_cond  = models.CharField(max_length=255, null=True)
#     Ray_type = models.CharField(max_length=255, null=True)
#     Hirr_symc = models.CharField(max_length=255, null=True)
#     Hirr_sycc = models.CharField(max_length=255, null=True)
#     Hirr_syjld = models.CharField(max_length=255, null=True)
#     Hirr_syzg= models.CharField(max_length=255, null=True)
#     Hirrtest_con= models.CharField(max_length=255, null=True)
#     Hfzdefoem_rate = models.CharField(max_length=255, null=True)
#     Neu_num  = models.FloatField(null=True)
#     Ray_stro = models.FloatField(null=True)
#     Irr_time = models.FloatField(null=True)
#     Hirrtest_tem = models.FloatField(null=True)
#     Irrbulk_mod = models.FloatField(null=True)
#     IrrShear_mod = models.FloatField(null=True) 
#     irryoung_mod = models.FloatField(null=True)
#     irryield_stre = models.FloatField(null=True)
#     Irrtensile_stre = models.FloatField(null=True)
#     Irr_dhysl = models.FloatField(null=True)
#     Irr_nybpyl = models.FloatField(null=True) 
#     Irr_nyqfqd = models.FloatField(null=True) 
#     Irr_nybpqd = models.FloatField(null=True) 
#     Irrpossion_rate = models.FloatField(null=True) 
#     Irr_rdl = models.FloatField(null=True)
#     Irr_brr = models.FloatField(null=True)
#     Irr_rpzxs = models.FloatField(null=True)
#     Irr_rfsl = models.FloatField(null=True)
#     Hirr_ddl = models.FloatField(null=True) 
#     Hirr_jdcs = models.FloatField(null=True)
#     Hirr_workfun = models.FloatField(null=True)
#     Hirr_jwl = models.FloatField(null=True)
#     Hirr_cdl = models.FloatField(null=True)
#     Hirr_cgyqd = models.FloatField(null=True)
#     Hirr_jltemp = models.FloatField(null=True) 
#     Irr_injure = models.FloatField(null=True)
#     Irr_lwyn = models.FloatField(null=True)
#     Irr_rslzyn = models.FloatField(null=True)
#     insert_time = models.DateTimeField(auto_now=True)
   
