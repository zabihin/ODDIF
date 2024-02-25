import requests
import pandas as pd
import json


def fetch_studies(page_token=None):
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "format": "json",
        "query.intr": "Bevacizumab",
        "query.locn": "United States",
        "pageSize": 100,
    }
    
    if page_token:
        params["pageToken"] = page_token

    response = requests.get(base_url, params=params)
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        # Convert the response to JSON and then dump it into a file
        with open('response.json', 'w', encoding='utf-8') as json_file:
            json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
        return response.json()
    else:
        print(f"Failed to fetch data: HTTP Status Code {response.status_code}")
        return None


def collect_all_studies():
    all_studies, next_page_token = [], None
    while True:
        data = fetch_studies(next_page_token)
        if not data: break
        all_studies.extend(data.get("studies", []))
        next_page_token = data.get("nextPageToken")
        if not next_page_token: break
    return all_studies

def main():
    studies_data = collect_all_studies()
    
    studies_list = []
    for study in studies_data:
        protocol = study.get("protocolSection", {})
        identification = protocol.get("identificationModule", {})
        status = protocol.get("statusModule", {})
        design = protocol.get("designModule", {})
        enrollment_info = design.get("enrollmentInfo", {})
        conditions = protocol.get("conditionsModule", {})

        study_dict = {
            "NCT ID": identification.get("nctId"),
            "Title": identification.get("briefTitle"),
            "Status": status.get("overallStatus"),
            "Phase": design.get("phases"),
            "Study Type": design.get("studyType"),
            "Enrollment": enrollment_info.get("count"),
            "Conditions": conditions.get("conditions"),
        }
        studies_list.append(study_dict)
    
    studies_df = pd.DataFrame(studies_list)
    
    studies_df.to_csv('clinical_data.csv', index=False, sep=';', header=True)


if __name__ == "__main__":
    main()
