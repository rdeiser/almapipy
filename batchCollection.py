from almapipy import AlmaCnxn
import subprocess
# Alma Sandbox apikey=l8xx4adda710f8fe4ec89aae0c64a6531cf9

alma = AlmaCnxn('l8xx4adda710f8fe4ec89aae0c64a6531cf9', data_format='json')

# need to create a for loop to take list of collection ids and return the json body.  If the internal_description field is null, add 'LocalOnly'.  If the internal_description field is not null, preappend internal_description with '; LocalOnly'

""" with open('input/lendableJournal.txt', 'r') as f:
    for id in f:
        # Strip any leading/trailing whitespace (like newlines)
        id = id.strip()
        
        collections = alma.electronic.collections.get(id)
        
        print(collections)


# print (collections) """

def update_internal_descriptions():
    with open('input/LendableInternational_Book.txt', 'r') as f:
        for line in f:
            collection_id = line.strip()
            if not collection_id:
                continue  # Skip empty lines
            
            try:
                response = alma.electronic.collections.get(collection_id)
                collection_data = response
                
                # Check if internal_description is null or empty string
                if not collection_data.get('internal_description'):
                    # empty filed data
                    new_description = 'LendableInternational; '
                else:
                    # preapend data
                    new_description = f'LendableInternational; {collection_data["internal_description"]}'
                
                # Update the collection data
                collection_data['internal_description'] = new_description
                
                alma.electronic.collections.put(collection_id, collection_data)
                
                print(f"Successfully updated collection {collection_id}")
                # print( collections)
            except response as e:
                with open("output/LendableInternational_BookerrorFile.txt", "w") as f:
                    f.write("Successfully updated collection {collection_id}\n")
                
if __name__ == "__main__":
    update_internal_descriptions()            
                