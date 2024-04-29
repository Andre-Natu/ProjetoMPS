from typing import Dict
from business.report_generator import ReportGenerator

class TXTReportGenerator(ReportGenerator):
    def collect_data(self, data: Dict[str, int]) -> Dict[str, str]:
        # Aqui você pode implementar a lógica para coletar os dados relevantes para o relatório em formato de texto
        # Por exemplo, converter os dados para texto simples
        return {key: str(value) for key, value in data.items()}

    def format_data(self, data: Dict[str, str]) -> str:
        # Aqui você pode implementar a lógica para formatar os dados coletados em um formato adequado para um relatório em texto
        # Por exemplo, organizar os dados em linhas ou tabelas
        formatted_data = "\n".join([f"{key}: {value}" for key, value in data.items()])
        return formatted_data

    def generate_file(self, data: str) -> str:
        # Aqui você pode implementar a lógica para gerar o arquivo de relatório em formato de texto
        # Por exemplo, salvar os dados formatados em um arquivo .txt
        filename = "report.txt"
        with open(filename, "w") as file:
            file.write(data)
        return filename
