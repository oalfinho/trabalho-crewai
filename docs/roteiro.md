# Roteiro do seminário (6 minutos)

| Slide | Tempo | Sugestão de fala ou ação |
|---|---|---|
| 1. Da anotação ao quiz | 35 s | “Imagina que a prova é amanhã. Como eu transformo uma página de anotações em perguntas para treinar?” Apresente a equipe que divide o trabalho de leitura e elaboração de questões. |
| 2. O que a CrewAI coordena? | 55 s | Explique que o modelo gera texto e a CrewAI organiza o trabalho. Aponte a diferença entre o papel “professor” e a tarefa “escrever duas perguntas”. Dois agentes podem usar o mesmo modelo. |
| 3. O que um agente entrega ao outro? | 45 s | Leia a anotação sobre pilhas. Mostre que “último a entrar, primeiro a sair” é o conceito que o analista precisa preservar no resumo. |
| 4. Onde a colaboração aparece? | 65 s | Abra seminario.py em montar_equipe. Aponte context=[resumir] e a ordem das tarefas. Explique como a anotação entra em kickoff e como o professor recebe o resumo. |
| 5. Qual item sai primeiro? | 60 s | Mostre a lista com A e B. Pergunte qual letra aparece no terminal e dê alguns segundos para a turma responder. Execute a demonstração já instalada conforme o README. |
| 6. Como conferir o resultado? | 65 s | Confira o B com a turma. Compare a anotação, o resumo e o gabarito no terminal. Explique que o ensaio usa respostas fixas e que o modo IA produz novas respostas para outra aula. |
| 7. Para reproduzir | 35 s | Mostre o repositório, o README e as referências. Termine explicando quando vale separar as etapas: por exemplo, quando queremos aproveitar o mesmo resumo para um quiz e depois para flashcards. |

**Pergunta provável:** “Precisava de dois agentes?” Para este quiz curto, um agente também poderia responder. A divisão torna o resumo uma entrega que podemos avaliar e reutilizar.

**Se a demonstração falhar:** abra saida-demo.txt e identifique a saída como registro de uma execução anterior.
