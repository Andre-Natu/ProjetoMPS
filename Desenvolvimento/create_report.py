from business.txt_report_generator import TXTReportGenerator

def create_report_txt(statistics_repository):
    # Criando uma instância do gerador de relatórios em formato de texto
    txt_report_generator = TXTReportGenerator()

    # Dados de exemplo para o relatório
    data = statistics_repository.get_access_num()
    data_dict = {'número de acessos': data}

    # Gerando o relatório em formato de texto
    txt_report_generator.generate_report(data_dict)

    return data_dict