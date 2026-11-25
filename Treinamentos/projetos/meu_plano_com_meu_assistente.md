# Assistente de Planejamento Inteligente com Notion e IA

## Visão Geral

Este projeto apresenta um assistente de planejamento criado para transformar qualquer objetivo em um plano estruturado, executável e acompanhável ao longo do tempo.

O assistente combina um Planner desenvolvido no Notion com habilidades de Inteligência Artificial para auxiliar desde a definição do objetivo até o acompanhamento do progresso.

O projeto foi desenvolvido como entrega do desafio da trilha de IA aplicada a planejamento.

---

# Problema que o Assistente Resolve

Muitas pessoas conseguem definir objetivos, mas enfrentam dificuldades para:

- Transformar ideias em planos de ação claros;
- Organizar tarefas de forma consistente;
- Adaptar metas à rotina disponível;
- Antecipar obstáculos;
- Monitorar resultados ao longo do tempo.

Este assistente resolve esses problemas utilizando um método estruturado e reutilizável para qualquer tipo de objetivo.

---

# Objetivo Utilizado na Demonstração

Objetivo fictício:

> Lançar uma loja virtual de produtos artesanais em até 90 dias.

Esse objetivo foi utilizado apenas para demonstrar o funcionamento do assistente e das habilidades desenvolvidas.

---

# Ferramentas Utilizadas

## Notion

O Notion foi utilizado para:

- Organização dos objetivos;
- Controle das tarefas;
- Registro de obstáculos;
- Acompanhamento da evolução;
- Relacionamento entre bancos de dados.

### Recursos utilizados

- Databases
- Relations
- Rollups
- Templates
- Notion AI

## ChatGPT

O ChatGPT foi utilizado para:

- Refinamento de objetivos;
- Criação de planos de ação;
- Organização da rotina;
- Identificação de riscos;
- Revisões periódicas de progresso.

---

# Estrutura do Planner

## Base de Dados: Objetivos

Armazena os objetivos principais.

### Propriedades

| Nome | Tipo |
|--------|--------|
| Objetivo | Título |
| Descrição | Texto |
| Data de Início | Data |
| Data Final | Data |
| Prioridade | Select |
| Status | Select |
| Progresso | Número |

---

## Base de Dados: Plano de Ação

Contém todas as tarefas necessárias para atingir o objetivo.

### Propriedades

| Nome | Tipo |
|--------|--------|
| Ação | Título |
| Objetivo Relacionado | Relation |
| Prazo | Data |
| Status | Select |
| Impacto | Select |

---

## Base de Dados: Rotina

Organiza a execução das atividades ao longo da semana.

### Propriedades

| Nome | Tipo |
|--------|--------|
| Atividade | Título |
| Frequência | Select |
| Tempo Estimado | Número |
| Ação Relacionada | Relation |

---

## Base de Dados: Obstáculos

Responsável pelo gerenciamento de riscos.

### Propriedades

| Nome | Tipo |
|--------|--------|
| Obstáculo | Título |
| Probabilidade | Select |
| Impacto | Select |
| Solução Alternativa | Texto |

---

## Base de Dados: Revisões

Registra aprendizados e evolução.

### Propriedades

| Nome | Tipo |
|--------|--------|
| Data | Data |
| Objetivo | Relation |
| Evolução (%) | Número |
| Aprendizados | Texto |
| Próximos Passos | Texto |

---

# Relações Entre as Bases

```text
Objetivos
├── Plano de Ação
├── Rotina
├── Obstáculos
└── Revisões
```

Essa estrutura permite visualizar todas as informações relacionadas a um objetivo em uma única página.

---

# Habilidades Desenvolvidas

## 1. Clarificar Objetivo

### Descrição

Transforma uma ideia inicial em um objetivo específico, mensurável e alcançável.

### O que faz

- Identifica o resultado desejado;
- Define métricas de sucesso;
- Estabelece prazo;
- Registra o objetivo no Planner.

### Exemplo

**Entrada**

```text
Quero abrir uma loja online.
```

**Saída**

```text
Criar uma loja virtual funcional para venda de produtos artesanais em até 90 dias, com pelo menos 20 produtos cadastrados e a primeira venda realizada.
```

---

## 2. Criar Plano de Ação

### Descrição

Transforma objetivos em tarefas práticas organizadas por etapas.

### O que faz

- Divide o objetivo em marcos;
- Identifica dependências;
- Define prioridades;
- Sugere cronograma.

### Exemplo

1. Pesquisa de mercado
2. Escolha da plataforma
3. Cadastro dos produtos
4. Configuração de pagamentos
5. Estratégia de divulgação
6. Lançamento da loja

---

## 3. Adaptar à Rotina

### Descrição

Ajusta o plano à disponibilidade de tempo existente.

### O que faz

- Analisa disponibilidade;
- Distribui atividades;
- Evita sobrecarga;
- Sugere frequência adequada.

### Exemplo

Disponibilidade:

```text
1 hora por dia
```

Sugestão:

```text
Segunda a Sexta:
- 1 hora por dia

Sábado:
- 2 horas para atividades estratégicas

Domingo:
- Revisão semanal
```

---

## 4. Antecipar Obstáculos

### Descrição

Identifica possíveis riscos e propõe alternativas.

### O que faz

- Mapeia dificuldades;
- Sugere planos de contingência;
- Reduz riscos de abandono.

### Exemplo

| Obstáculo | Solução |
|------------|---------|
| Falta de tempo | Executar versões reduzidas das tarefas |
| Pouco orçamento | Utilizar ferramentas gratuitas |
| Falta de experiência | Buscar cursos e conteúdos gratuitos |

---

## 5. Revisar Progresso

### Descrição

Analisa os resultados alcançados e sugere ajustes.

### O que faz

- Compara planejado versus realizado;
- Avalia evolução;
- Identifica gargalos;
- Atualiza prioridades.

### Exemplo

```text
Progresso esperado: 70%

Progresso realizado: 50%

Recomendação:
Reduzir o número de tarefas simultâneas e focar na divulgação da loja.
```

---

## 6. Otimizador de Prioridades

### Descrição

Habilidade adicional criada para melhorar a execução.

### O que faz

- Analisa todas as tarefas pendentes;
- Identifica atividades de maior impacto;
- Recomenda foco para a semana.

---

# Instruções Utilizadas nas Habilidades

O assistente deve:

1. Entender claramente o objetivo antes de sugerir ações.
2. Trabalhar com metas específicas e mensuráveis.
3. Criar planos simples e executáveis.
4. Considerar limitações de tempo e recursos.
5. Priorizar ações com maior impacto.
6. Identificar riscos antecipadamente.
7. Sugerir melhorias contínuas através das revisões.

---

# Demonstração Prática

## Etapa 1 - Definição do Objetivo

Objetivo refinado:

```text
Lançar uma loja virtual de produtos artesanais em até 90 dias, com catálogo de 20 produtos e pelo menos uma venda realizada.
```

---

## Etapa 2 - Plano de Ação

Plano criado:

- Realizar pesquisa de mercado;
- Escolher plataforma de e-commerce;
- Produzir fotos dos produtos;
- Criar catálogo;
- Configurar pagamentos;
- Realizar testes;
- Lançar a loja.

---

## Etapa 3 - Organização da Rotina

Planejamento semanal:

| Dia | Atividade |
|------|-----------|
| Segunda | Pesquisa e planejamento |
| Terça | Cadastro de produtos |
| Quarta | Produção de conteúdo |
| Quinta | Configurações da loja |
| Sexta | Divulgação |
| Sábado | Execução estratégica |
| Domingo | Revisão semanal |

---

## Etapa 4 - Obstáculos Identificados

| Obstáculo | Alternativa |
|------------|------------|
| Falta de tempo | Dividir tarefas em blocos de 15 minutos |
| Poucos recursos | Utilizar soluções gratuitas |
| Falta de conhecimento técnico | Buscar treinamentos gratuitos |

---

## Etapa 5 - Revisão

Resultado simulado:

```text
Progresso: 40%

Concluído:
- Loja criada
- Produtos cadastrados

Pendente:
- Estratégia de marketing

Próxima Prioridade:
- Preparar campanha de lançamento
```

---

# Diferenciais do Projeto

- Planejamento reutilizável para qualquer objetivo.
- Integração entre Notion e IA.
- Método baseado em etapas claras.
- Facilidade de manutenção e expansão.
- Possibilidade de adicionar novas habilidades futuramente.

---

# Possíveis Evoluções

- Integração com Google Agenda;
- Integração direta com ChatGPT;
- Revisões automáticas semanais;
- Geração automática de relatórios;
- Painel de métricas em tempo real.

---

# Conclusão

O Assistente de Planejamento Inteligente permite transformar objetivos em planos executáveis de forma organizada, reutilizável e adaptável.

Por meio do Notion e das habilidades de IA, o usuário consegue planejar, executar, acompanhar e revisar qualquer objetivo utilizando um único método estruturado.

---

## Autor

Joaquim Rodrigues de Oliveira Junior