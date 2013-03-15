#!/bin/bash

line_number=2

/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt d_num_fire.txt "d_numfire before check of d_i_surface" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt total_ign.txt "total ignition:" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt lightn_ign.txt "lightning igintion:" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt popdens.txt "popd:" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt d_i_sruface.txt "d_i_surface before check of d_i_surface" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt fire_size.txt "mean_fire_size:" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt d_area_burnt_before.txt "d_area_burnt before check of d_i_surface" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt d_area_burnt.txt "d_area_burnt after check of d_i_surface" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt d_fdi.txt "d_fdi:" ${line_number}
/home/users/ychao/script/extract_variable_from_orchidee_output.sh out.txt proc_ba.txt "proc_ba:" ${line_number}

