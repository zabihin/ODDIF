from pytrials.client import ClinicalTrials
import pandas as pd

def fetch_studies():
    # Initialize the ClinicalTrials client
    ct = ClinicalTrials()

    # Search for studies involving "Bevacizumab"
    search_results = ct.get_full_studies(search_expr="Bevacizumab", max_studies=100)

    # Extract detailed study information
    studies_data = []
    for study in search_results['FullStudiesResponse']['FullStudies']:
        protocol = study['Study']['ProtocolSection']
        identification = protocol.get('IdentificationModule', {})
        status = protocol.get('StatusModule', {})
        design = protocol.get('DesignModule', {})
        enrollment_info = design.get('EnrollmentInfo', {})
        conditions = protocol.get('ConditionsModule', {})

        study_dict = {
            'NCT ID': identification.get('NCTId'),
            'Title': identification.get('BriefTitle'),
            'Status': status.get('OverallStatus'),
            'Phase': ', '.join(design.get('PhaseList', {}).get('Phase', [])),
            'Study Type': design.get('StudyType'),
            'Enrollment': enrollment_info.get('EnrollmentCount'),
            'Conditions': ', '.join(conditions.get('ConditionList', {}).get('Condition', []))
        }
        studies_data.append(study_dict)

    return studies_data

def main():
    studies_data = fetch_studies()

    # Convert the list of dictionaries into a DataFrame
    studies_df = pd.DataFrame(studies_data)

    # Save the DataFrame to a CSV file
    studies_df.to_csv('studies_data2.csv', index=False, header=True)

    # Display the DataFrame
    print(studies_df)

if __name__ == "__main__":
    main()
