# CrewAI em Python · Da anotação ao quiz

Seminário de Arthur Lemos. Dois agentes transformam uma anotação de aula em um resumo e duas questões comentadas. O projeto mostra como uma equipe compartilha o resultado de uma tarefa com a próxima.

**Para apresentar:** baixe o repositório em **Code → Download ZIP**, extraia e abra [os slides](docs/slides.html) no navegador. Use as setas para avançar e voltar. O [roteiro de fala](docs/roteiro.md) acompanha os sete slides.

## Execução rápida

A instalação inicial requer internet. Ambiente testado com Python 3.12 e CrewAI 1.15.44. Abra o terminal na pasta que contém este README.

**Windows / PowerShell**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe seminario.py --demo
```

**Ubuntu / terminal**

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python seminario.py --demo
```

## Dois modos de execução

O modo `--demo` executa a equipe CrewAI com dois modelos de demonstração que devolvem respostas fixas sobre pilhas. Ele permite inspecionar a ordem das etapas e o resultado intermediário sem contratar uma API. Consulte a [saída de uma execução](docs/saida-demo.txt).

O modo `--ia` envia a anotação ao modelo configurado e gera respostas novas. Exige internet, acesso à API da OpenAI e saldo ou faturamento habilitado. No PowerShell, configure a variável na sessão e execute:

```powershell
$env:OPENAI_API_KEY = Read-Host -MaskInput "Chave da API"   # PowerShell 7.1+
.\.venv\Scripts\python.exe seminario.py --ia
```

No Bash:

```bash
read -rsp 'Chave da API: ' OPENAI_API_KEY
export OPENAI_API_KEY
.venv/bin/python seminario.py --ia
```

Para usar outra aula, acrescente `--arquivo aula.txt` ao comando com `--ia`. Salve o texto em UTF-8. O modelo padrão é `openai/gpt-4o-mini`. A variável opcional `CREWAI_MODELO` permite selecionar outro modelo OpenAI disponível na sua conta.

## Como o programa funciona

1. `main()` lê os argumentos e seleciona o modelo. A anotação padrão trata de pilhas.
2. `montar_equipe()` cria o analista e o professor. Cada `Agent` recebe um papel, um objetivo, uma descrição de experiência e um modelo.
3. A tarefa `resumir` usa o texto fornecido a `kickoff(inputs=...)`. O parâmetro `expected_output` descreve a entrega esperada.
4. A tarefa `criar_quiz` recebe o resumo via `context=[resumir]`. A equipe executa as duas tarefas na ordem especificada por `Process.sequential`.
5. O terminal mostra a anotação, o primeiro resultado em `resultado.tasks_output[0].raw` e o quiz em `resultado.raw`.

## Como avaliar o resultado

Confira se as perguntas podem ser respondidas a partir da anotação. Para a pilha da demonstração, inserir A e depois B deve fazer a primeira remoção devolver B. Um resumo errado pode induzir o professor a repetir o erro. O modo IA exige revisão humana da fidelidade do resumo e do gabarito.

## Referências

- [CrewAI · Agents](https://docs.crewai.com/en/concepts/agents)
- [CrewAI · Tasks e contexto](https://docs.crewai.com/en/concepts/tasks)
- [CrewAI · Crews e execução](https://docs.crewai.com/en/concepts/crews)
- [CrewAI · Modelos personalizados](https://docs.crewai.com/en/learn/custom-llm)
