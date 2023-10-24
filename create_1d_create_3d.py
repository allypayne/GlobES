import os
import numpy as np

# Step 1: create a path to the atmospheric files (E-0 to E-5) to extract data
atm_path= '/Users/apayne3/Desktop/GlobES/Checlair_plots/atm_files/'

# Step 2: Create a path to the base configuration file:
# this path already has all of the instrumental/geometric characteristics we want, just need to adjust the remaining parameters from atm
base_cfg= open("/Users/apayne3/Desktop/GlobES/Checlair_plots/comparison_1d_3d/psg_cfg_1dcheclair_e0_official_copy.txt", "r");
basecfg= base_cfg.readlines();
#close the file everytime
base_cfg.close();

############################## CREATE 1D FILE FIRST ############################
#Consider the parameters that vary between each atm file and the base cfg:
# Punit, Atm temp, Surface temp, Albedo, Emissivity

# use file comparisons to see where they differ 
for file in sorted(os.listdir(atm_path)):
    #ignore the DS files
    if '.DS' in file: continue
    # open all of the env files from geronimo
    atm_file= open(atm_path+file, "r");
    atm_lines= atm_file.readlines();
    # close the e_file here and continue to use elines for the rest of the code...
    atm_file.close()

    #Method: use counters to find each needed index

    #consider if need to add 1 to the index values
    print("NEW FILE STARTS HERE. THIS IS:",file)

    # 1: Find location of: NUMBER OF LINES
    loc_num_lines_atm=0
    for line in atm_lines:
        # stores the # of layers in the file as a string
        if r'<ATMOSPHERE-LAYERS>' in line:
            # find the # of layers from the atm file and convert it from a string to integer
            num_layers= int(float(line.split('>')[1]))
            break
        loc_num_lines_atm=loc_num_lines_atm+1
    print(loc_num_lines_atm, num_layers)
    # find location in the template file
    loc_num_lines_base=0
    for line in basecfg:
        if r'<ATMOSPHERE-LAYERS>' in line:
            break
        loc_num_lines_base= loc_num_lines_base+1
    #loc_atm_layers_base= loc_atm_layers_base+1

    # 2: Find location of: Punit
    loc_punit_atm=0
    for line in atm_lines:
        # stores the # of layers in the file as a string
        if r'<ATMOSPHERE-PUNIT>' in line:
            # find the # of layers from the atm file and convert it from a string to integer
            punit= line.split('>')[1]
            break
        loc_punit_atm=loc_punit_atm+1
    print("punit",loc_punit_atm, punit)
    # find location in the template file
    loc_punit_base=0
    for line in basecfg:
        if r'<ATMOSPHERE-PUNIT>' in line:
            break
        loc_punit_base= loc_punit_base+1

    # 3: Find location of: Atm temp
    loc_atmtemp_atm=0
    for line in atm_lines:
        # stores the # of layers in the file as a string
        if r'<ATMOSPHERE-TEMPERATURE>' in line:
            # find the # of layers from the atm file and convert it from a string to integer
            atmtemp= line.split('>')[1]
            break
        loc_atmtemp_atm=loc_atmtemp_atm+1
    print("loc_atmtemp_atm",loc_atmtemp_atm, atmtemp)
    # find location in the template file
    loc_atmtemp_base=0
    for line in basecfg:
        if r'<ATMOSPHERE-TEMPERATURE>' in line:
            break
        loc_atmtemp_base= loc_atmtemp_base+1

    # 4: Find location of: surface temp
    loc_surftemp_atm=0
    for line in atm_lines:
        # stores the # of layers in the file as a string
        if r'<SURFACE-TEMPERATURE>' in line:
            # find the # of layers from the atm file and convert it from a string to integer
            surftemp= line.split('>')[1]
            break
        loc_surftemp_atm=loc_surftemp_atm+1
    print("loc_surftemp_atm",loc_surftemp_atm, surftemp)
    # find location in the template file
    loc_surftemp_base=0
    for line in basecfg:
        if r'<SURFACE-TEMPERATURE>' in line:
            break
        loc_surftemp_base= loc_surftemp_base+1


    # 5: Find location of: albedo
    loc_albedo_atm=0
    for line in atm_lines:
        # stores the # of layers in the file as a string
        if r'<SURFACE-ALBEDO>' in line:
            # find the # of layers from the atm file and convert it from a string to integer
            albedo= line.split('>')[1]
            break
        loc_albedo_atm=loc_albedo_atm+1
    print("loc_albedo_atm",loc_albedo_atm, albedo)
    # find location in the template file
    loc_albedo_base=0
    for line in basecfg:
        if r'<SURFACE-ALBEDO>' in line:
            break
        loc_albedo_base= loc_albedo_base+1
    print("loc_albedo_base", loc_albedo_base)

    # 6: Find location of: emissivity
    loc_emiss_atm=0
    for line in atm_lines:
        # stores the # of layers in the file as a string
        if r'<SURFACE-EMISSIVITY>' in line:
            # find the # of layers from the atm file and convert it from a string to integer
            emissivity= line.split('>')[1]
            break
        loc_emiss_atm=loc_emiss_atm+1
    print("loc_emiss_atm",loc_emiss_atm, emissivity)
    # find location in the template file
    loc_emiss_base=0
    for line in basecfg:
        if r'<SURFACE-EMISSIVITY>' in line:
            break
        loc_emiss_base= loc_emiss_base+1
    print("base file emiss loc", loc_emiss_base)

    # 7: Find location of: molecules needed for config
    list_molecules_loc=0
    for line in atm_lines:
        # find the molecules that we include in the atmosphere from e file
        if r'<ATMOSPHERE-GAS>' in line:
            new_molecules= line.split('>')[1]
            #include break so it stops once it finds it
            break
        list_molecules_loc= list_molecules_loc+1
    print("new_molecules",list_molecules_loc, new_molecules)
    # find location in the template file
    list_molecules_base=0
    for line in basecfg:
        if r'<ATMOSPHERE-LAYERS-MOLECULES>' in line:
            break
        list_molecules_base= list_molecules_base+1
    print("list_molecules_base", list_molecules_base)

    # 8: Find location of: where the atm layers start
    loc_atm_layers_start= 0
    for line in atm_lines:
        if "<ATMOSPHERE-LAYER-1>" in line:
            break
        loc_atm_layers_start= loc_atm_layers_start+1
    print(loc_atm_layers_start,"loc_atm_layers_start", file)
    # find location in the template file
    loc_atm_layers_start_base=0
    for line in basecfg:
        if "<ATMOSPHERE-LAYER-1>" in line:
            break
        loc_atm_layers_start_base= loc_atm_layers_start_base+1
    print(loc_atm_layers_start_base, "layers start base")


    # modifications to the TEMPLATE file here
    #this will be executed 6 times (once for each file)

    # output file name here
    file_name='/Users/apayne3/Desktop/GlobES/Checlair_plots/comparison_1d_3d/psg_cfg_1d_'+file[0:3]+'.txt'
    # open file in write mode to store the new config files
    f = open(file_name, 'w')
    # give each atm a local config file to modify (use the read lines version)
    new_file= basecfg.copy()

    # 1: Modify the number of layers
    new_file[loc_num_lines_base]= "<ATMOSPHERE-LAYERS>"+str(num_layers)+"\n"

    # this step isnt actually necessary for these files
    # # 2: Modify Punit (pressure unit)
    # new_file[loc_punit_base]= "<ATMOSPHERE-PUNIT>"+str(punit)+"\n"

    # 3: Modify atm temp
    new_file[loc_atmtemp_base]= "<ATMOSPHERE-TEMPERATURE>"+str(atmtemp)

    # 4: Modify surface temp
    new_file[loc_surftemp_base]= "<SURFACE-TEMPERATURE>"+str(surftemp)
    print("BADLINE:", new_file[loc_surftemp_base])

    # 5: Modify surface albedo
    new_file[loc_albedo_base]= "<SURFACE-ALBEDO>"+str(albedo)

    # 6: Modify emissivity
    new_file[loc_emiss_base]= "<SURFACE-EMISSIVITY>"+str(emissivity)
    
    # 7: Add the new molecules/ modify list of molecules ("<ATMOSPHERE-LAYERS-MOLECULES>")
    # Give it the full list of molecules (it needs this to find the indexing of the NGAS molecules)
    if "E-0_atm" in file:
        new_file[list_molecules_base]="<ATMOSPHERE-LAYERS-MOLECULES>H2O,CO2,O3,N2O,CO,CH4,O2,NO,SO2,NO2,NH3,HNO3,OH,HF,HCl,HBr,HI,ClO,OCS,H2CO,HOCl,N2,HCN,CH3Cl,H2O2,C2H2,C2H6,PH3" +"\n"
    else:
        new_file[list_molecules_base]="<ATMOSPHERE-LAYERS-MOLECULES>H2O,CO2,O3,N2O,CO,CH4,O2,NO,SO2,NO2,HNO3,OH,HCl,ClO,H2CO,HOCl,N2,CH3Cl,H2O2"+"\n"
    #new_file[list_molecules_base]= '<ATMOSPHERE-LAYERS-MOLECULES>'+str(new_molecules)

    # 8: modify the layers from the base config to the ones specified in the atm files
    print("NUMLAYERS", num_layers)
    for i in range(num_layers):
        new_file[loc_atm_layers_start_base+i]= atm_lines[loc_atm_layers_start+i]
        # this will overwrite the data that exists in the file already until it has overwritten everything there
        #except: new_file.append(atm_lines[i])
        # if there is more data in the new field it will append the rest at the end
    for line in new_file:
        test= f.write(line)
    f.close()

    #Everything looks good!
    #to fix the issue with not all of the atm layers added to the new configs: added a bunch of blank lines to the e0_official_copy at the end

# Note: all paths are relative to the current folder

'''
## The code below will give the string file needed to call the API and run the files created directly by running this file
#folder_2= '/Users/allypayne/Desktop/NASA_GSFC/IntroPlots/NewPSGFiles_140/'
folder_runatm='/Users/apayne3/Desktop/GlobES/Checlair_plots/comparison_1d_3d/'

for file in sorted(os.listdir(folder_runatm)):
    if '.ipynb' in file: continue
    if "cfg_E" in file:
        if 'DS' not in file:
            file_str= str(file)
            value= 'curl --data-urlencode file@'+folder_runatm+file_str+' https://psg.gsfc.nasa.gov/api.php > ./Checlair_plots/comparison_1d_3d/'+'psg_1d_' +file_str[8:11]+'_out.txt'
            # use this is .append but for strings instead of list objects
            os.system(value)
            # using break only tests the first one
            #break

'''
############################ CREATE 3D FILE HERE ###############################

for file in sorted(os.listdir(atm_path)):
    #ignore the DS files
    if '.DS' in file: continue
    # open all of the env files from geronimo
    atm_file= open(atm_path+file, "r");
    atm_lines= atm_file.readlines();
    # close the e_file here and continue to use elines for the rest of the code...
    atm_file.close()

    # Read in the template file
    template_read= open('Checlair_plots/comparison_1d_3d/3dtemplate.txt', 'r');
    template= template_read.readlines();
    template_read.close()
        
    print(file)
    # output file name here
    file_name='/Users/apayne3/Desktop/GlobES/Checlair_plots/comparison_1d_3d/psg_cfg_3d_'+file[0:3]+'.txt'

    print(file_name)
    # open file in write mode to store the new config files
    f = open(file_name, 'w')
    # give each atm a local config file to modify (use the read lines version)
    new_file= template.copy()

    #the albedo value in each file is = 0.306 so this was modified directly in 3dtemplate

    # 1: Find: NUMBER OF LAYERS in atm file
    for line in atm_lines:
        # stores the # of layers in the file as a string
        if r'<ATMOSPHERE-LAYERS>' in line:
            # find the # of layers from the atm file and convert it from a string to integer
            num_layers= int(float(line.split('>')[1]))
    print("Num layers is:", num_layers)
    # location of #layers
    loc_num_layers_template=0
    for line in new_file:
        if r'<ATMOSPHERE-LAYERS>' in line:
            break
        loc_num_layers_template=loc_num_layers_template+1
    print("loc_num_layers_template", loc_num_layers_template)

    # find location of the gcm parameters
    loc_gcm=0
    for line in new_file:
        if r"<ATMOSPHERE-GCM-PARAMETERS>" in line:
            break
        loc_gcm=loc_gcm+1
    print("loc_gcm", loc_gcm)

    # adjust the # of layers in each config file to agree with the atm files
    new_file[loc_num_layers_template]= "<ATMOSPHERE-LAYERS>" +str(num_layers)
    # Add in the proper GCM KEY line (this line only needs to be varied by the # of layers)
    new_file[loc_gcm]= "<ATMOSPHERE-GCM-PARAMETERS>144,91,"+str(num_layers)+",-180,-90,2.5,2.0,Pressure,Temperature,H2O,CO2,O3,N2O,CO,CH4,O2,N2"
    

    for line in new_file:
        test= f.write(line)
    f.close()


    #### CALL SERVER FOR 3D MODELS

    # This function allows you to call it directly (curl wont work bc files are too big)
    """

    def call_api(config_path: str, psg_url: str = 'http://localhost:3000',
             api_key: str = None, output_type: str = None, app: str = None,
             outfile: str = None) #-> None:
        
        Call the PSG api
    ​
        Build and execute an API query to communicate with PSG.
    ​
        Parameters
        ----------
        config_path : str or pathlib.Path
            The path to the `PSG` config file.
        psg_url : str, default='https://psg.gsfc.nasa.gov'
            The URL of the `PSG` API. Use 'http://localhost:3000' if running locally.
        api_key : str, default=None
            The key for the public API. Needed only if not runnning `PSG` locally.
        output_type : str, default=None
            The type of output to retrieve from `PSG`. Options include 'cfg', 'rad',
            'noi', 'lyr', 'all'.
        app : str, default=None
            The PSG app to call. For example: 'globes'
        outfile : str, default=None
            The path to write the PSG output.
        data = {}
        with open(config_path,'rb') as file:
            dat = file.read()
        data['file'] = dat
        if api_key is not None:
            data['key'] = api_key
        if app is not None:
            data['app'] = app
        if output_type is not None:
            data['type'] = output_type
        data['option'] = '-s'
        
        url = f'{psg_url}/api.php'
        reply = requests.post(url,data=data,timeout=555555555)
        if outfile is not None:
            with open(outfile,'wb') as file:
                file.write(reply.content)
        return reply
    # example

    call_api(config_path=file_name, app='globes', type='set')
    res = call_api(config_path=cfgfile, app='globes', type='rad')

    with open('globes_output'+file[0:3]'.txt' ,'w') as f:
        for line in res:
            f.write(line)
        """