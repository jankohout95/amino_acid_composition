import pandas as pd

def extract_string(input_string, start_marker, end_marker):
    start_index = input_string.find(start_marker)
    end_index = input_string.find(end_marker, start_index + len(start_marker))
    if start_index != -1 and end_index != -1:
        result = input_string[start_index + len(start_marker):end_index]
        return result
    else:
        return None

def get_percentage_of_aminoacid(aminoAcid: str, dataSequence):
    if len(dataSequence) == 0:
        return None
    else:
        aminoAcidcounter = 0
        for letter in dataSequence:
            if letter == aminoAcid:
                aminoAcidcounter += 1
        return aminoAcidcounter / len(dataSequence)

def convert_to_dataframe(proteins: []):
    data = {
        "name": [],
        "p_percentage": []
    }
    for protein in proteins:
        data["name"].append(protein["name"])
        data["p_percentage"].append(protein["p_percentage"])
    return pd.DataFrame(data)


proteins = []

# Open the file in read mode ('r')
with open('uniprotkb_taxonomy_id_9606_AND_reviewed_2023_11_26.fasta', 'r') as file:
    # Read each line in the file
    protein = {
        "header": "",
        "data": "",
        "p_percentage": None,
        "name": ""
    }
    for line in file:
        # Process the line as needed
        if line[0] == ">":
            protein["header"] = protein["header"].replace("\n", "")
            protein["data"] = protein["data"].replace("\n", "")
            protein["p_percentage"] = get_percentage_of_aminoacid("P", protein["data"])
            protein["name"] = extract_string(protein["header"], "HUMAN", "OS").replace(" ", "")
            proteins.append(protein)
            protein = {
                "header": "",
                "data": "",
                "p_percentage": None,
                "name": ""
            }
            protein["header"] = line
        else:
           protein["data"] += line
        # print(line.strip())  # This will

df = convert_to_dataframe(proteins)

print(df)

# counter = 0
# for protein in proteins:
#     if counter < 10:
#         print(protein)
#     else:
#         break
#     counter += 1





