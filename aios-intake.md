# AIS-OS Intake

This is the source-of-truth file for your AIOS. Fill it in by typing, voice-pasting (Wispr Flow / OS dictation), or running `/onboard` for a guided conversation. Whichever mode, this file is what `/onboard` reads to scaffold your Day-1 setup.

**Hard cap: 7 questions.** Each answerable in under 60 seconds. Don't overthink — you can edit and re-run `/onboard` any time.

---

## Q1 — Who are you, what do you sell, who do you sell it to?

Identity, offer, ICP. One paragraph each is fine.

```
QUEM SOU: Larissa, uma das fundadoras da Mexidona (www.mexidona.com.br). Engenheira mecânica
de formação; experiência em multinacional nas áreas de qualidade, industrialização e lean.
Na Mexidona sou responsável por financeiro, compras, planejamento de produção, processos e
melhorias, e puxo os novos projetos. Como sócia, participo das estratégias comerciais e de RH
(há uma gerente comercial). 6 anos no projeto, "de corpo e alma".

O QUE VENDEMOS: refeições desidratadas (sopas, risotos, macarrões etc.), 100% naturais, sem
conservantes, sem glúten, sem glutamato, sem leite. Proposta: alimentação saudável de forma
prática. Empresa com 32 colaboradores, a maioria em produção e expedição, mais um time
administrativo.

PARA QUEM / CANAIS:
- Core: e-commerce próprio (consumidor final)
- Lojistas: atendimento via WhatsApp por uma pessoa dedicada, com CRM usado de forma parcial
- Grandes contas (supermercados) via representantes
- Distribuidoras
- Em estudo: marketplaces, exportação, private label (Marlex e Caçarola)

MOMENTO: este ano a empresa ganhou bastante tração. Pré-lançamento em novembro. Meta de
R$ 22M de faturamento no próximo ano e plano de chegar a R$ 50M em 3 anos, possivelmente
com uma nova unidade.
```

---

## Q2 — Paste 1-2 things you've written recently. Don't edit them.

An email, a LinkedIn post, a DM, a doc — anything that sounds like you when you're not trying. **Paste verbatim.** Do not type these mid-conversation with Claude — chat-shaped samples are worse than no samples (voice contamination).

```
[Amostra 1: mensagem de WhatsApp para o grupo de líderes "Guardiões da Cultura"]
Olá, Guardiões da Cultura! 🧡

Criei este grupo com vocês, Sirlene, Lilian, Raquel, Jonathan e Débora, porque são as pessoas que lideram e que são referência aqui dentro da Mexidona. O jeito como vocês agem, falam e tratam as pessoas já inspira o time todo, e é justamente por isso que quero vocês comigo nessa missão.

A ideia do grupo é a gente cuidar juntos da nossa cultura. Para começar, quero fazer três coisas com vocês:
```

```
[Amostra 2: e-mail curto para contato externo]
Boa tarde, Nathan! Tudo bem?

Obrigada pelo convite. Podemos confirmar a visita conforme a agenda enviada.
Qualquer ajuste, me avisem.

Abraço!
```

---

## Q3 — What are your 2-3 biggest priorities for the next 90 days?

Quarterly priorities. Not yearly aspirations. Things that, if not done by July, would make you say "I wasted Q2."

```
(Período: out/2026 a jan/2027)
1. Cup proteico pronto para produzir até 20/out/2026
2. Agência de marketplace contratada e lojas no ar (agência contratada: Comunidade Marketplace, onboarding 02/10/2026)
3. Pedidos expedidos no prazo ≥ 90%, com a TV de acompanhamento funcionando
```

---

## Q4 — Where does revenue actually land, and where is it tracked?

Multiple answers OK. Stripe? Skool? GoHighLevel? QuickBooks? A spreadsheet?

```
PEDIDOS:
- E-commerce: pedido entra no site e integra com o ERP Tiny
- B2B: pedido chega por mensagem ou e-mail. A equipe administrativa lança manualmente,
  cota frete, agenda a entrega e passa para a expedição

RECEBIMENTO:
- E-commerce: gateway de pagamento Olist
- B2B: Pix, boleto ou transferência direto nas contas bancárias

ACOMPANHAMENTO:
- DRE montada pela assessoria financeira, revisada em reunião mensal
- BI de faturamento por linha de produto, canal de venda e período
- Dashboard separado do e-commerce (ROAS, CAC, taxa de conversão etc.)
```

---

## Q5 — Where do you talk to customers, your team, and the outside world day-to-day?

Email (which one — Gmail / Outlook)? Slack? Teams? DMs (Skool / Discord / iMessage)? Phone?

```
- E-mail: Gmail / Google Workspace
- Equipe: grupos de WhatsApp
- Clientes: WhatsApp Business, Wesales (CRM do atendimento a lojistas), Instagram, TikTok,
  e-mail; disparos de mensagens pelo Martz
- Agenda: Google Agenda
```

---

## Q6 — Where do meeting recordings, notes, and important docs live?

Granola? Otter? Fireflies? Google Drive? Notion? Dropbox? A folder on your desktop you keep meaning to organize?

```
- Reuniões: Granola
- Documentos: Google Drive, Notion, pastas no computador
- Processos: POPs no Notion, mas precisam de revisão. Há procedimentos que ainda não têm POP.
  Ideia futura: um agente que ajude as pessoas a manter os POPs atualizados.
```

---

## Q7 — What's the one task that eats your week, and where do you currently track work?

The single biggest time-suck or recurring drudgery. Plus where tasks/projects live (ClickUp / Asana / Linear / Notion / a notebook).

```
MAIOR DRENO DE TEMPO: responder pessoas, cobrar, pedir e monitorar o andamento das coisas.

ONDE AS TAREFAS FICAM: não há um sistema único. Tentamos o Notion, mas a equipe teve
dificuldade. Hoje uso uma planilha (Google Sheets) para manter simples. Nas reuniões de pulso
semanais, cobro e anoto o andamento nela.
Planilha: https://docs.google.com/spreadsheets/d/1X9GDZwTp52oyEE95FpDpK1XLdEZWfcSXFd8MvGJAWQU/edit?gid=349034216#gid=349034216
```

---

When this file is filled, run `/onboard` (or re-run it) and the wizard will scaffold your Day-1 file set: `context/`, `references/voice.md`, populated `connections.md`, and a filled `CLAUDE.md`.
