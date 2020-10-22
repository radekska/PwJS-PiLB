from xml.dom import minidom

def edit_xml(new_data_dict):
    parsed_data = None
    with open('xml_dane/movies.xml', 'r') as file_stream:
        parsed_data = minidom.parse(file_stream)

        for tag_name, value in new_data_dict.items():
            parsed_data.getElementsByTagName(tag_name)[0].childNodes[0].nodeValue = value
            
    with open('xml_dane/new_movies.xml', 'w+') as new_file_stream:
        parsed_data.writexml(new_file_stream)



if __name__ == '__main__':
    new_data_dict = {
        'title' : 'Silicon Valley',
        'type' : 'Commedy',
        'format' : 'HBO / digit',
        'year' : '2014'
    }
    
    edit_xml(new_data_dict)

    