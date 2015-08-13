import requests
import json
elem = {}
elem["date_of_operation"]= "test"
elem["arrest"]="test"
elem["age_group_of_offender"]="test"
elem["race_of_offender"]="test"
elem["criminal_record"]="test"
elem["repeat_offender"]="datum.repeat_offender"
elem["in_possession_of_weapon"]="datum.in_possession_of_weapon"
elem["marital_status"]='datum.marital_status'
elem["highest_level_of_education"]='datum.highest_level_of_education'
elem["offenders_sector_of_employment"]="datum.offenders_sector_of_employment"
elem["vehicle_towed_impounded"]="datum.vehicle_towed_impounded"
elem["fines"]="datum.fines"
elem["number_of_charges"]="datum.number_of_charges"
elem["dna_taken"]="datum.dna_taken"
elem["method_of_payment_for_ads"]='datum.method_of_payment_for_ads'
elem["website_used_for_posting"]="datum.website_used_for_posting"
        
print requests.get("https://guarded-lake-8332.herokuapp.com/receive_json/"+json.dumps(elem)).text
