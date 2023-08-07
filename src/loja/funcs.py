def product_image_path(instance, filename:str) -> str:
    '''armazena a ext da file e cria um path de acordo com o nome do produto'''
    ext =  filename.split('.')[-1]
    filename = f"{instance.nome.replace(' ','_')}.{ext}"
    return f"produtos/{filename}"
