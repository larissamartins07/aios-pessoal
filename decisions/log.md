# Decisões pessoais (Larissa)

Decisões do AIOS pessoal da Larissa. As da empresa ficam em `decisions/log.md`, no repositório da equipe.

---

## 2026-10-09 - Radar de respostas pendentes no WhatsApp

**Decision:** Criar o Radar (/level-up de 09/10): em cada janela de WhatsApp, uma lista de quem deve resposta à Larissa e do que ela deve aos outros.

**Spec (Method):**
- **Constraint:** a atenção da Larissa. Cobranças e respostas pendentes ficam na memória dela. Análise de 01 a 08/10 (Claude in Chrome): as 10 conversas de trabalho mais ativas somam mais de 1.500 mensagens enviadas por ela, a maior parte decisões, aprovações e dúvidas de processo.
- **EAD:** eliminar o acompanhamento não dá (coisas param). Eliminar a frequência dá: o WhatsApp passa a ser olhado em janelas, com notificações desligadas fora delas (exceto sócias) e a regra "urgente é ligação". Automatizar: ~30% determinístico (quem falou por último, há quantos dias), ~60% IA (entender se a mensagem pede algo e se foi respondida), ~10% manual (decidir o que cobrar e responder). Delegar: não.
- **Processo:** gatilho = início de cada janela (9h, 11h, 14h, 16h, 18h), rodado pela Larissa. Fonte = WhatsApp Web via Claude in Chrome, conversas de trabalho dos últimos 7 dias, incluindo a da Jéssica, sem as pessoais. Transformação = achar pedidos, perguntas, cobranças e aprovações sem resposta, nos dois sentidos. Decisões = "ok"/"👍" conta como resposta; mais de 2 dias = atrasado; pedido que é tarefa de verdade sugere virar linha na planilha (via /marca-passo). Destino = duas listas curtas (te devem / você deve) com quem, o quê, há quanto tempo.
- **Autonomia:** L1 (Sugerido). Só lê e lista; nunca envia mensagem.
- **KPI:** menos custo (tempo da Larissa). Principal: pendências com mais de 2 dias, contadas pelo Radar. Tendência: tempo de tela do WhatsApp no celular, ponto de partida 1h52/dia (sem o WhatsApp Web), meta de cerca de 1h em 4 semanas.

**Why:** responder e cobrar no WhatsApp é o maior consumo de tempo da Larissa, e checar o dia todo é o que fragmenta a agenda dela.

**Alternatives considered:** CRM comercial do VV para a Amanda (maior alavanca de venda; depende do Tiny; fica para o próximo /level-up) e projeção de caixa de 13 semanas (depende de Tiny e banco).

**Owner:** Larissa

## 2026-10-13 - Backup antes da migração para o Team

**Decision:** O backup do GYM 80 ficou na pasta pessoal `LALU/02-saúde/Dieta Larissa/backup-paginas/`. Contexto da migração em `decisions/log.md` (2026-10-13, equipe).

**Owner:** Larissa
