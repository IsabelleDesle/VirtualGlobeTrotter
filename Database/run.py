import ClassVgt as vgt

vgt = vgt.VGT()
vgt.start_docker_services()
vgt.connect_to_elasticSearch()

while True:

    vgt.return_image_path(input_file= "./search_image.json")
    
    exit = input("Enter to search again (or type 'exit' to stop): ")
    if exit.lower() == 'exit':
        break

