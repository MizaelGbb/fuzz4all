import re
from pathlib import Path

arquivo_log = Path("outputs/qwen_test_20/log_validation.txt")
conteudo = arquivo_log.read_text(encoding="utf-8")

blocos = re.split(r"(?=\[TRACE\] Validating )", conteudo)

aprovados = 0
reprovados = 0

print("\nRESULTADO DOS TESTES\n")

for bloco in blocos:
    resultado = re.search(
        r"\[TRACE\] Validating (.+?) \.\.\.",
        bloco
    )

    if not resultado:
        continue

    arquivo = Path(resultado.group(1)).name

    if " is safe" in bloco:
        print(f"{arquivo}: PASSOU")
        aprovados += 1

    elif "failed validation" in bloco:
        if "stdarg.h" in bloco:
            motivo = "Falta incluir stdarg.h"
        elif "undefined reference" in bloco:
            motivo = "Função não encontrada na ligação"
        elif "as an AI language model" in bloco:
            motivo = "IA não gerou código C"
        elif "error:" in bloco:
            motivo = "Erro de compilação"
        else:
            motivo = "Falha na validação"

        print(f"{arquivo}: FALHOU - {motivo}")
        reprovados += 1

print("\nRESUMO")
print(f"Programas aprovados: {aprovados}")
print(f"Programas reprovados: {reprovados}")
print(f"Total analisado: {aprovados + reprovados}")
