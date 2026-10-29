# LLM-Assisted Fuzzing

Projeto acadêmico de fuzzing assistido por modelos de linguagem, utilizando o Fuzz4All, o GCC e o Qwen2.5-Coder 3B executado localmente pelo Ollama.

## Objetivo

Investigar como modelos de linguagem podem auxiliar a geração de programas de teste e a análise de falhas encontradas durante o fuzzing de programas em C.

O projeto está em desenvolvimento. O experimento inicial verificou a geração e compilação de programas. A implementação do módulo de análise e a avaliação experimental ainda precisam ser concluídas.

## Tecnologias

- Python 3.10
- Fuzz4All
- GCC
- Ollama
- Qwen2.5-Coder 3B
- Conda

## 1. Clonar o repositório

```bash
git clone https://github.com/MizaelGbb/fuzz4all.git
cd fuzz4all
```

## 2. Preparar o ambiente Python

Crie e ative o ambiente Conda:

```bash
conda create -n fuzz4all python=3.10
conda activate fuzz4all
```

Instale as dependências seguindo as instruções do repositório original do Fuzz4All.

Antes de utilizar `requirements.txt` ou `pip install -e .`, confira se esses arquivos e instruções estão presentes na versão clonada.

## 3. Instalar e preparar as ferramentas

Verifique se o GCC está disponível:

```bash
gcc --version
```

Instale o Ollama seguindo as instruções oficiais e verifique se ele está funcionando:

```bash
ollama list
```

Baixe o modelo utilizado:

```bash
ollama pull qwen2.5-coder:3b
```

## 4. Executar o experimento inicial

Com o ambiente Conda ativado e o Ollama funcionando, execute:

```bash
python Fuzz4All/fuzz.py \
  --config config/full_run/c_std_qwen_test.yaml \
  main_with_config \
  --folder outputs/qwen_test_03 \
  --batch_size 1 \
  --model_name ollama/qwen2.5-coder:3b
```

Os resultados serão gravados no diretório de saída configurado para a execução.

Utilize outro diretório ao realizar novos experimentos, para preservar os resultados anteriores.

## 5. Estado atual

O teste inicial gerou três programas em C:

- Um programa não compilou devido a código inválido.
- Dois programas foram compilados com sucesso.

Esse resultado é preliminar e não demonstra, por si só, a existência de defeitos no GCC nem permite concluir que o método é eficaz.

## 6. Próximas etapas

1. Reproduzir o experimento em outra máquina.
2. Organizar o registro dos resultados.
3. Implementar um módulo baseado em LLM para analisar as falhas.
4. Realizar experimentos com uma amostra maior.
5. Avaliar a correção das análises.
6. Documentar a metodologia, os resultados e as limitações no artigo científico.

## Observações

O modelo é baixado separadamente e não faz parte do repositório Git.

O ambiente Conda também precisa ser recriado em cada máquina.

A execução de programas gerados por modelos deve ser realizada em um ambiente apropriado para testes.
