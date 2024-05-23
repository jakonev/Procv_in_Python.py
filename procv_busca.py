from parametros import procv_busca

def consulta_codigos():

    codigo_buscar = '9'
    consul = procv_busca()
    consul.ler_csv_base()
    cod = consul.procv_base(codigo_buscar)
    return cod

print(consulta_codigos())


