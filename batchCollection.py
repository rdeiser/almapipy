from almapipy import AlmaCnxn
import subprocess
# Alma Sandbox apikey=l8xx4adda710f8fe4ec89aae0c64a6531cf9

<<<<<<< HEAD
alma = AlmaCnxn('', data_format='json')
=======
alma = AlmaCnxn('', data_format='json')
>>>>>>> 51590f8f991ad8ab928206037b1920bdc8c0e00f

# need to create a for loop to take list of collection ids and return the json body.  If the internal_description field is null, add 'LocalOnly'.  If the internal_description field is not null, preappend internal_description with '; LocalOnly'

""" with open('input/lendableJournal.txt', 'r') as f:
    for id in f:
        # Strip any leading/trailing whitespace (like newlines)
        id = id.strip()
        
        collections = alma.electronic.collections.get(id)
        
        print(collections)


# print (collections) """

def update_internal_descriptions():
    with open('input/PROD/LocalOnly_Final189.txt', 'r') as f:
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
                    # new_description = 'LendableInternational; '
                    new_description = 'LocalOnly; '
                # elif collection_data.get('internal_description').startswith('LendableInternational'):
                # elif collection_data.get('internal_description').startswith('LocalOnly'):
                elif collection_data.get('internal_description').startswith(('LocalOnly', 'LendableInternational')):
                    print(f"Did not update {collection_id}.  Internal Description already set to {collection_data.get('internal_description')}.")
                    continue
                # elif collection_data.get('internal_description').startswith(('LocalOnly', 'LendableInternational')):
                #     new_description = 'LocalOnly; ' + collection_data['internal_description'][len('LendableInternational;'):] 
                else:
                    # new_description = f'LendableInternational; {collection_data["internal_description"]}'
                    new_description = f'LocalOnly;  {collection_data["internal_description"]}'
                
                # Update the collection data
                collection_data['internal_description'] = new_description
                
                updateCollection = alma.electronic.collections.put(collection_id, collection_data)
                
                if updateCollection.status_code == 500:
                    print(f"The following Electronic Collection did not update {collection_id}")
                else:
                    print(f"Successfully updated collection {collection_id}")
                # print( collections)
            except response as e:
                with open("output/LocalOnly_Journal.txterrorFile.txt", "w") as f:
                    f.write("Successfully updated collection {collection_id}\n")
                
if __name__ == "__main__":
    update_internal_descriptions()            
                
