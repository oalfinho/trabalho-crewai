"""Gere um quiz com uma equipe de dois agentes CrewAI."""
import argparse
import os
from pathlib import Path

os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")

from crewai import Agent, BaseLLM, Crew, LLM, Process, Task

ANOTACAO = (
    "Em uma pilha, o último item inserido sai primeiro. Em Python, "
    "append() insere no fim da lista e pop() retira e devolve o último item."
)
RESUMO = "A pilha segue a ordem LIFO. append() insere no fim e pop() retira o último item."
QUIZ = """1. Inserimos A e depois B. Qual valor pop() devolve?
Gabarito: B, pois foi o último item inserido.

2. Como colocar C no topo de uma pilha representada por uma lista?
Gabarito: pilha.append("C"), pois o topo corresponde ao fim da lista."""


class ModeloDeDemonstracao(BaseLLM):
    """Resposta fixa para ensaiar a execução sem acesso a um provedor."""
    resposta: str

    def call(self, messages, **kwargs):
        return "Final Answer: " + self.resposta


def montar_equipe(modelo_analista, modelo_professor):
    analista = Agent(role="Analista de aula", goal="Extrair conceitos da anotação.",
                     backstory="Você prepara resumos para estudantes.", llm=modelo_analista)
    professor = Agent(role="Professor", goal="Avaliar a compreensão dos conceitos.",
                      backstory="Você cria exercícios curtos com gabarito.", llm=modelo_professor)
    resumir = Task(
        description="Resuma em português os conceitos desta anotação: {anotacao}",
        expected_output="Um parágrafo curto e fiel ao texto.", agent=analista,
    )
    criar_quiz = Task(
        description="Com base no resumo recebido, escreva duas perguntas em português.",
        expected_output="Duas perguntas, cada uma com gabarito e justificativa.",
        agent=professor, context=[resumir],
    )
    return Crew(agents=[analista, professor], tasks=[resumir, criar_quiz],
                process=Process.sequential)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modo = parser.add_mutually_exclusive_group(required=True)
    modo.add_argument("--demo", action="store_true", help="Usar a aula de pilhas e respostas fixas.")
    modo.add_argument("--ia", action="store_true", help="Gerar respostas com a API da OpenAI.")
    parser.add_argument("--arquivo", type=Path, help="Anotação em UTF-8 para o modo IA.")
    args = parser.parse_args()
    texto = ANOTACAO
    if args.demo:
        if args.arquivo:
            parser.error("--arquivo exige --ia. A demonstração usa a aula de pilhas.")
        print("Demonstração com respostas fixas.")
        modelos = [ModeloDeDemonstracao(model="demo", resposta=r) for r in (RESUMO, QUIZ)]
    else:
        if args.arquivo:
            try:
                texto = args.arquivo.read_text(encoding="utf-8-sig").strip()
            except (OSError, UnicodeError) as erro:
                parser.error(str(erro))
            if not texto:
                parser.error("A anotação está vazia.")
        if not os.getenv("OPENAI_API_KEY"):
            parser.error("Defina OPENAI_API_KEY para usar --ia ou execute --demo.")
        modelo = LLM(model=os.getenv("CREWAI_MODELO", "openai/gpt-4o-mini"))
        modelos = [modelo, modelo]
    equipe = montar_equipe(*modelos)
    resultado = equipe.kickoff(inputs={"anotacao": texto})
    print(f"\nANOTAÇÃO\n{texto}\n\nRESUMO\n{resultado.tasks_output[0].raw}")
    print(f"\nQUIZ\n{resultado.raw}")


if __name__ == "__main__":
    main()
